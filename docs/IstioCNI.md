# IstioCNI

IstioCNI configures the istio-cni subchart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cni** | [**CNI**](CNI.md) |  | [optional] 
**tolerations** | [**List[Toleration]**](Toleration.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.istio_cni import IstioCNI

# TODO update the JSON string below
json = "{}"
# create an instance of IstioCNI from a JSON string
istio_cni_instance = IstioCNI.from_json(json)
# print the JSON string representation of the object
print(IstioCNI.to_json())

# convert the object into a dict
istio_cni_dict = istio_cni_instance.to_dict()
# create an instance of IstioCNI from a dict
istio_cni_from_dict = IstioCNI.from_dict(istio_cni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


