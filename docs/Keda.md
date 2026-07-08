# Keda


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.keda import Keda

# TODO update the JSON string below
json = "{}"
# create an instance of Keda from a JSON string
keda_instance = Keda.from_json(json)
# print the JSON string representation of the object
print(Keda.to_json())

# convert the object into a dict
keda_dict = keda_instance.to_dict()
# create an instance of Keda from a dict
keda_from_dict = Keda.from_dict(keda_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


