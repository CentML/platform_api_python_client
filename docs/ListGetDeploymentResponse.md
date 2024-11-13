# ListGetDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetDeploymentResponse]**](GetDeploymentResponse.md) |  | 

## Example

```python
from platform_api_external_client.models.list_get_deployment_response import ListGetDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListGetDeploymentResponse from a JSON string
list_get_deployment_response_instance = ListGetDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(ListGetDeploymentResponse.to_json())

# convert the object into a dict
list_get_deployment_response_dict = list_get_deployment_response_instance.to_dict()
# create an instance of ListGetDeploymentResponse from a dict
list_get_deployment_response_from_dict = ListGetDeploymentResponse.from_dict(list_get_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


