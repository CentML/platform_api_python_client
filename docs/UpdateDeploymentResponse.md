# UpdateDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**endpoint_url** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeploymentResponse from a JSON string
update_deployment_response_instance = UpdateDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateDeploymentResponse.to_json())

# convert the object into a dict
update_deployment_response_dict = update_deployment_response_instance.to_dict()
# create an instance of UpdateDeploymentResponse from a dict
update_deployment_response_from_dict = UpdateDeploymentResponse.from_dict(update_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


