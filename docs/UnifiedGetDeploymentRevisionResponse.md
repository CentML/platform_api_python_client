# UnifiedGetDeploymentRevisionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**revision_number** | **int** |  | 
**deployment_id** | **int** |  | 
**deployment_response** | [**UnifiedGetDeploymentResponse**](UnifiedGetDeploymentResponse.md) |  | 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from platform_api_python_client.models.unified_get_deployment_revision_response import UnifiedGetDeploymentRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetDeploymentRevisionResponse from a JSON string
unified_get_deployment_revision_response_instance = UnifiedGetDeploymentRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetDeploymentRevisionResponse.to_json())

# convert the object into a dict
unified_get_deployment_revision_response_dict = unified_get_deployment_revision_response_instance.to_dict()
# create an instance of UnifiedGetDeploymentRevisionResponse from a dict
unified_get_deployment_revision_response_from_dict = UnifiedGetDeploymentRevisionResponse.from_dict(unified_get_deployment_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


