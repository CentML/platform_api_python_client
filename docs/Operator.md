# Operator

Operator configures the KAI operator, which deploys every other KAI component.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_level** | **str** |  | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.operator import Operator

# TODO update the JSON string below
json = "{}"
# create an instance of Operator from a JSON string
operator_instance = Operator.from_json(json)
# print the JSON string representation of the object
print(Operator.to_json())

# convert the object into a dict
operator_dict = operator_instance.to_dict()
# create an instance of Operator from a dict
operator_from_dict = Operator.from_dict(operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


