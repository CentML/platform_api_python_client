# FinalStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.final_stack import FinalStack

# TODO update the JSON string below
json = "{}"
# create an instance of FinalStack from a JSON string
final_stack_instance = FinalStack.from_json(json)
# print the JSON string representation of the object
print(FinalStack.to_json())

# convert the object into a dict
final_stack_dict = final_stack_instance.to_dict()
# create an instance of FinalStack from a dict
final_stack_from_dict = FinalStack.from_dict(final_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


