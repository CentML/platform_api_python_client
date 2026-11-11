# UnifiedGetDeploymentPodsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pods** | **List[str]** |  | 

## Example

```python
from platform_api_python_client.models.unified_get_deployment_pods_response import UnifiedGetDeploymentPodsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetDeploymentPodsResponse from a JSON string
unified_get_deployment_pods_response_instance = UnifiedGetDeploymentPodsResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetDeploymentPodsResponse.to_json())

# convert the object into a dict
unified_get_deployment_pods_response_dict = unified_get_deployment_pods_response_instance.to_dict()
# create an instance of UnifiedGetDeploymentPodsResponse from a dict
unified_get_deployment_pods_response_from_dict = UnifiedGetDeploymentPodsResponse.from_dict(unified_get_deployment_pods_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


