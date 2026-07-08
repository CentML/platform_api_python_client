# NetworkOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.network_operator import NetworkOperator

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkOperator from a JSON string
network_operator_instance = NetworkOperator.from_json(json)
# print the JSON string representation of the object
print(NetworkOperator.to_json())

# convert the object into a dict
network_operator_dict = network_operator_instance.to_dict()
# create an instance of NetworkOperator from a dict
network_operator_from_dict = NetworkOperator.from_dict(network_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


