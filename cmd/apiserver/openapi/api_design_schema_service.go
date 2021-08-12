/*
 * Fledge REST API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

import (
	"context"
	"errors"
	"net/http"

	"go.uber.org/zap"

	"wwwin-github.cisco.com/eti/fledge/pkg/objects"
	"wwwin-github.cisco.com/eti/fledge/pkg/util"
)

// DesignSchemaApiService is a service that implents the logic for the DesignSchemaApiServicer
// This service should implement the business logic for every endpoint for the DesignSchemaApi API.
// Include any external packages or services that will be required by this service.
type DesignSchemaApiService struct {
}

// NewDesignSchemaApiService creates a default api service
func NewDesignSchemaApiService() DesignSchemaApiServicer {
	return &DesignSchemaApiService{}
}

// GetDesignSchema - Get a design schema owned by user
func (s *DesignSchemaApiService) GetDesignSchema(ctx context.Context, user string, designId string, getType string, schemaId string) (objects.ImplResponse, error) {
	//TODO input validation
	zap.S().Debugf("Get design schema details for user: %s | designId: %s | type: %s | schemaId: %s", user, designId, getType, schemaId)

	//create controller request
	uriMap := map[string]string{
		"user":     user,
		"designId": designId,
		"type":     getType,
		"schemaId": schemaId,
	}
	url := CreateURI(util.GetDesignSchemaEndPoint, uriMap)

	//send get request
	responseBody, err := util.HTTPGet(url)

	//response to the user
	if err != nil {
		return objects.Response(http.StatusInternalServerError, nil), errors.New("get design schema details request failed")
	}
	var resp []objects.DesignSchema
	err = util.ByteToStruct(responseBody, &resp)
	return objects.Response(http.StatusOK, resp), err
}

// UpdateDesignSchema - Update a design schema
func (s *DesignSchemaApiService) UpdateDesignSchema(ctx context.Context, user string, designId string, designSchema objects.DesignSchema) (objects.ImplResponse, error) {
	//TODO input validation
	zap.S().Debugf("Update/insert design schema request recieved for designId: %v", designId)

	//create controller request
	uriMap := map[string]string{
		"user":     user,
		"designId": designId,
	}
	url := CreateURI(util.UpdateDesignSchemaEndPoint, uriMap)

	//send get request
	_, _, err := util.HTTPPost(url, designSchema, "application/json")

	//response to the user
	if err != nil {
		return objects.Response(http.StatusInternalServerError, nil), errors.New("error while updating/inserting design schema")
	}
	return objects.Response(http.StatusOK, nil), err
}
