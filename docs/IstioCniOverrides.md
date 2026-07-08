# IstioCniOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cni_bin_dir** | **str** |  | [optional] 
**cni_conf_dir** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.istio_cni_overrides import IstioCniOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of IstioCniOverrides from a JSON string
istio_cni_overrides_instance = IstioCniOverrides.from_json(json)
# print the JSON string representation of the object
print(IstioCniOverrides.to_json())

# convert the object into a dict
istio_cni_overrides_dict = istio_cni_overrides_instance.to_dict()
# create an instance of IstioCniOverrides from a dict
istio_cni_overrides_from_dict = IstioCniOverrides.from_dict(istio_cni_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


