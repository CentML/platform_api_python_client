# Istio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | [**IstioOverrides**](IstioOverrides.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.istio import Istio

# TODO update the JSON string below
json = "{}"
# create an instance of Istio from a JSON string
istio_instance = Istio.from_json(json)
# print the JSON string representation of the object
print(Istio.to_json())

# convert the object into a dict
istio_dict = istio_instance.to_dict()
# create an instance of Istio from a dict
istio_from_dict = Istio.from_dict(istio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


