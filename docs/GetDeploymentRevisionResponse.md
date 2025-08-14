# GetDeploymentRevisionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**revision_number** | **int** |  | 
**deployment_id** | **int** |  | 
**deployment_response** | [**DeploymentResponse**](DeploymentResponse.md) |  | 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from platform_api_python_client.models.get_deployment_revision_response import GetDeploymentRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploymentRevisionResponse from a JSON string
get_deployment_revision_response_instance = GetDeploymentRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(GetDeploymentRevisionResponse.to_json())

# convert the object into a dict
get_deployment_revision_response_dict = get_deployment_revision_response_instance.to_dict()
# create an instance of GetDeploymentRevisionResponse from a dict
get_deployment_revision_response_from_dict = GetDeploymentRevisionResponse.from_dict(get_deployment_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


