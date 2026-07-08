# IstioCniSubchartOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cni** | [**IstioCniOverrides**](IstioCniOverrides.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.istio_cni_subchart_overrides import IstioCniSubchartOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of IstioCniSubchartOverrides from a JSON string
istio_cni_subchart_overrides_instance = IstioCniSubchartOverrides.from_json(json)
# print the JSON string representation of the object
print(IstioCniSubchartOverrides.to_json())

# convert the object into a dict
istio_cni_subchart_overrides_dict = istio_cni_subchart_overrides_instance.to_dict()
# create an instance of IstioCniSubchartOverrides from a dict
istio_cni_subchart_overrides_from_dict = IstioCniSubchartOverrides.from_dict(istio_cni_subchart_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


