# DeploymentUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **Dict[str, str]** |  | 
**values** | [**List[DeploymentUsageValue]**](DeploymentUsageValue.md) |  | 

## Example

```python
from platform_api_python_client.models.deployment_usage import DeploymentUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentUsage from a JSON string
deployment_usage_instance = DeploymentUsage.from_json(json)
# print the JSON string representation of the object
print(DeploymentUsage.to_json())

# convert the object into a dict
deployment_usage_dict = deployment_usage_instance.to_dict()
# create an instance of DeploymentUsage from a dict
deployment_usage_from_dict = DeploymentUsage.from_dict(deployment_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


