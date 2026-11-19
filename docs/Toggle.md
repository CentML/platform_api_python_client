# Toggle

Toggle is a subchart's enable flag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from platform_api_python_client.models.toggle import Toggle

# TODO update the JSON string below
json = "{}"
# create an instance of Toggle from a JSON string
toggle_instance = Toggle.from_json(json)
# print the JSON string representation of the object
print(Toggle.to_json())

# convert the object into a dict
toggle_dict = toggle_instance.to_dict()
# create an instance of Toggle from a dict
toggle_from_dict = Toggle.from_dict(toggle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


