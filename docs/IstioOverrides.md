# IstioOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**istio_cni** | [**IstioCniSubchartOverrides**](IstioCniSubchartOverrides.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.istio_overrides import IstioOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of IstioOverrides from a JSON string
istio_overrides_instance = IstioOverrides.from_json(json)
# print the JSON string representation of the object
print(IstioOverrides.to_json())

# convert the object into a dict
istio_overrides_dict = istio_overrides_instance.to_dict()
# create an instance of IstioOverrides from a dict
istio_overrides_from_dict = IstioOverrides.from_dict(istio_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


