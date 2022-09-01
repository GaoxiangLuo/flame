# Copyright 2022 Cisco Systems, Inc. and its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmeta.proto\x12\x08grpcMeta\"X\n\x08MetaInfo\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63h_name\x18\x02 \x01(\t\x12\n\n\x02me\x18\x03 \x01(\t\x12\r\n\x05other\x18\x04 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x05 \x01(\t\"r\n\x0cMetaResponse\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.grpcMeta.MetaResponse.Status\x12\x11\n\tendpoints\x18\x02 \x03(\t\" \n\x06Status\x12\t\n\x05\x45RROR\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x32\x88\x01\n\tMetaRoute\x12@\n\x10RegisterMetaInfo\x12\x12.grpcMeta.MetaInfo\x1a\x16.grpcMeta.MetaResponse\"\x00\x12\x39\n\tHeartBeat\x12\x12.grpcMeta.MetaInfo\x1a\x16.grpcMeta.MetaResponse\"\x00\x42,Z*github.com/cisco-open/flame/pkg/proto/metab\x06proto3')



_METAINFO = DESCRIPTOR.message_types_by_name['MetaInfo']
_METARESPONSE = DESCRIPTOR.message_types_by_name['MetaResponse']
_METARESPONSE_STATUS = _METARESPONSE.enum_types_by_name['Status']
MetaInfo = _reflection.GeneratedProtocolMessageType('MetaInfo', (_message.Message,), {
  'DESCRIPTOR' : _METAINFO,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:grpcMeta.MetaInfo)
  })
_sym_db.RegisterMessage(MetaInfo)

MetaResponse = _reflection.GeneratedProtocolMessageType('MetaResponse', (_message.Message,), {
  'DESCRIPTOR' : _METARESPONSE,
  '__module__' : 'meta_pb2'
  # @@protoc_insertion_point(class_scope:grpcMeta.MetaResponse)
  })
_sym_db.RegisterMessage(MetaResponse)

_METAROUTE = DESCRIPTOR.services_by_name['MetaRoute']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z*github.com/cisco-open/flame/pkg/proto/meta'
  _METAINFO._serialized_start=24
  _METAINFO._serialized_end=112
  _METARESPONSE._serialized_start=114
  _METARESPONSE._serialized_end=228
  _METARESPONSE_STATUS._serialized_start=196
  _METARESPONSE_STATUS._serialized_end=228
  _METAROUTE._serialized_start=231
  _METAROUTE._serialized_end=367
# @@protoc_insertion_point(module_scope)
