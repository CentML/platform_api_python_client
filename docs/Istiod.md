# Istiod

Istiod configures the istiod subchart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pilot** | [**Pilot**](Pilot.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.istiod import Istiod

# TODO update the JSON string below
json = "{}"
# create an instance of Istiod from a JSON string
istiod_instance = Istiod.from_json(json)
# print the JSON string representation of the object
print(Istiod.to_json())

# convert the object into a dict
istiod_dict = istiod_instance.to_dict()
# create an instance of Istiod from a dict
istiod_from_dict = Istiod.from_dict(istiod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


