# UnifiedWriteDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**endpoint_url** | **str** |  | 
**port** | **int** |  | 

## Example

```python
from platform_api_python_client.models.unified_write_deployment_response import UnifiedWriteDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedWriteDeploymentResponse from a JSON string
unified_write_deployment_response_instance = UnifiedWriteDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedWriteDeploymentResponse.to_json())

# convert the object into a dict
unified_write_deployment_response_dict = unified_write_deployment_response_instance.to_dict()
# create an instance of UnifiedWriteDeploymentResponse from a dict
unified_write_deployment_response_from_dict = UnifiedWriteDeploymentResponse.from_dict(unified_write_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


