# DeploymentStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**service_status** | [**ServiceStatus**](ServiceStatus.md) |  | [optional] 
**error_message** | **str** |  | [optional] 
**endpoint_url** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.deployment_status_response import DeploymentStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStatusResponse from a JSON string
deployment_status_response_instance = DeploymentStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentStatusResponse.to_json())

# convert the object into a dict
deployment_status_response_dict = deployment_status_response_instance.to_dict()
# create an instance of DeploymentStatusResponse from a dict
deployment_status_response_from_dict = DeploymentStatusResponse.from_dict(deployment_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


