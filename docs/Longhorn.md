# Longhorn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.longhorn import Longhorn

# TODO update the JSON string below
json = "{}"
# create an instance of Longhorn from a JSON string
longhorn_instance = Longhorn.from_json(json)
# print the JSON string representation of the object
print(Longhorn.to_json())

# convert the object into a dict
longhorn_dict = longhorn_instance.to_dict()
# create an instance of Longhorn from a dict
longhorn_from_dict = Longhorn.from_dict(longhorn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


