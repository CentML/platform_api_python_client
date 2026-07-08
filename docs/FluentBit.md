# FluentBit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.fluent_bit import FluentBit

# TODO update the JSON string below
json = "{}"
# create an instance of FluentBit from a JSON string
fluent_bit_instance = FluentBit.from_json(json)
# print the JSON string representation of the object
print(FluentBit.to_json())

# convert the object into a dict
fluent_bit_dict = fluent_bit_instance.to_dict()
# create an instance of FluentBit from a dict
fluent_bit_from_dict = FluentBit.from_dict(fluent_bit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


