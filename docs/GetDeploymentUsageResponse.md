# GetDeploymentUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[DeploymentUsageValue]**](DeploymentUsageValue.md) |  | 

## Example

```python
from platform_api_python_client.models.get_deployment_usage_response import GetDeploymentUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploymentUsageResponse from a JSON string
get_deployment_usage_response_instance = GetDeploymentUsageResponse.from_json(json)
# print the JSON string representation of the object
print(GetDeploymentUsageResponse.to_json())

# convert the object into a dict
get_deployment_usage_response_dict = get_deployment_usage_response_instance.to_dict()
# create an instance of GetDeploymentUsageResponse from a dict
get_deployment_usage_response_from_dict = GetDeploymentUsageResponse.from_dict(get_deployment_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


