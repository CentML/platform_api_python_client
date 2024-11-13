# DeploymentUsageValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**value** | **float** |  | 

## Example

```python
from platform_api_external_client.models.deployment_usage_value import DeploymentUsageValue

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentUsageValue from a JSON string
deployment_usage_value_instance = DeploymentUsageValue.from_json(json)
# print the JSON string representation of the object
print(DeploymentUsageValue.to_json())

# convert the object into a dict
deployment_usage_value_dict = deployment_usage_value_instance.to_dict()
# create an instance of DeploymentUsageValue from a dict
deployment_usage_value_from_dict = DeploymentUsageValue.from_dict(deployment_usage_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


