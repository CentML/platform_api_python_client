# GetDeploymentPodsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pods** | **List[str]** |  | 

## Example

```python
from platform_api_python_client.models.get_deployment_pods_response import GetDeploymentPodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploymentPodsResponse from a JSON string
get_deployment_pods_response_instance = GetDeploymentPodsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDeploymentPodsResponse.to_json())

# convert the object into a dict
get_deployment_pods_response_dict = get_deployment_pods_response_instance.to_dict()
# create an instance of GetDeploymentPodsResponse from a dict
get_deployment_pods_response_from_dict = GetDeploymentPodsResponse.from_dict(get_deployment_pods_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


