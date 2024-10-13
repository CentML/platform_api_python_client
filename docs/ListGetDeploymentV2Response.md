# ListGetDeploymentV2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetDeploymentV2Response]**](GetDeploymentV2Response.md) |  | 

## Example

```python
from platform_api_python_client.models.list_get_deployment_v2_response import ListGetDeploymentV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListGetDeploymentV2Response from a JSON string
list_get_deployment_v2_response_instance = ListGetDeploymentV2Response.from_json(json)
# print the JSON string representation of the object
print(ListGetDeploymentV2Response.to_json())

# convert the object into a dict
list_get_deployment_v2_response_dict = list_get_deployment_v2_response_instance.to_dict()
# create an instance of ListGetDeploymentV2Response from a dict
list_get_deployment_v2_response_from_dict = ListGetDeploymentV2Response.from_dict(list_get_deployment_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


