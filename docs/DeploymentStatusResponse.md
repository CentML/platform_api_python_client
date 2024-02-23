# DeploymentStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**service_status** | [**EndpointReadyState**](EndpointReadyState.md) |  | 
**error_message** | **str** |  | 

## Example

```python
from platform_api_client.models.deployment_status_response import DeploymentStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatusResponse from a JSON string
deployment_status_response_instance = DeploymentStatusResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentStatusResponse.to_json()

# convert the object into a dict
deployment_status_response_dict = deployment_status_response_instance.to_dict()
# create an instance of DeploymentStatusResponse from a dict
deployment_status_response_form_dict = deployment_status_response.from_dict(deployment_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


