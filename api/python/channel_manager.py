from backends import backend_provider
from channel import Channel
from common.constants import SOCK_OP_WAIT_TIME
from common.util import background_thread_loop, run_async
from registry_agents import registry_agent_provider


class ChannelManager(object):
    def __init__(self, registry_agent, backend, job, role, channels_roles):
        self.job = job
        self.role = role
        self.channels_roles = channels_roles

        self.channels = {}

        with background_thread_loop() as loop:
            self._loop = loop

        self._registry_agent = registry_agent_provider.get(registry_agent)
        self._backend = backend_provider.get(backend)
        self._backend.set_channel_manager(self)

    def join(self, name):
        '''
        joins a channel
        '''
        if self.join_done(name):
            return True

        coro = self._registry_agent.connect()
        _, status = run_async(coro, self._loop, SOCK_OP_WAIT_TIME)
        if not status:
            return False

        coro = self._registry_agent.register(
            self.job, name, self.role, self._backend.uid(),
            self._backend.endpoint()
        )
        _, status = run_async(coro, self._loop, SOCK_OP_WAIT_TIME)
        if status:
            self.channels[name] = Channel(name, self._backend)
        else:
            return False

        # role_tuples should have at most two entries
        role_tuples = self.channels_roles[name]

        coro = self._registry_agent.get(self.job, name)
        channel_info, status = run_async(coro, self._loop, SOCK_OP_WAIT_TIME)
        if not status:
            return False

        for role, end_id, endpoint in channel_info:
            # the same backend id; skip
            if end_id is self._backend.uid():
                continue

            proceed = False
            for from_role, to_role in role_tuples:
                proceed = self.role is from_role and role is to_role

            if not proceed:
                continue

            # connect to endpoint
            self._backend.connect(end_id, endpoint)

            # notify end_id of the channel handled by the backend
            self._backend.notify(end_id, name)

            # update channel
            self.channels[name].add(end_id)

        coro = self._registry_agent.close()
        _ = run_async(coro, self._loop, SOCK_OP_WAIT_TIME)

        return True

    def leave(self, name):
        '''
        leave a channel
        '''
        if not self.is_joined(name):
            return

        coro = self._registry_agent.reset_channel(
            self.job, name, self.role, self._backend.uid()
        )

        _, status = run_async(coro, self._loop, SOCK_OP_WAIT_TIME)
        if status:
            del self.channels[name]

        return status

    def get(self, name):
        '''
        returns a channel object in the given channel
        '''
        if not self.is_joined(name):
            # didn't join the channel yet
            return None

        return self.channels[name]

    def update(self, name, end_id):
        '''
        add an end ID to a channel with 'name'
        '''
        if not self.is_joined(name):
            # didn't join the channel yet
            return

        channel = self.channels[name]

        channel.add(end_id)

    def is_joined(self, name):
        '''
        check if node joined a channel or not
        '''
        if name in self.channels:
            return True
        else:
            return False


if __name__ == "__main__":
    channels_roles = {'param-channel': (('agg', 'trainer'), ('trainer', 'agg'))}
    cm = ChannelManager('local', 'local', 'test-job', 'agg', channels_roles)
    cm.join('param-channel')
