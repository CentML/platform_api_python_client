# IstioBase

IstioBase configures the istio-base subchart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_revision** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.istio_base import IstioBase

# TODO update the JSON string below
json = "{}"
# create an instance of IstioBase from a JSON string
istio_base_instance = IstioBase.from_json(json)
# print the JSON string representation of the object
print(IstioBase.to_json())

# convert the object into a dict
istio_base_dict = istio_base_instance.to_dict()
# create an instance of IstioBase from a dict
istio_base_from_dict = IstioBase.from_dict(istio_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


