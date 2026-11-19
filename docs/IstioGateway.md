# IstioGateway

IstioGateway configures the istio-gateway subchart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from platform_api_python_client.models.istio_gateway import IstioGateway

# TODO update the JSON string below
json = "{}"
# create an instance of IstioGateway from a JSON string
istio_gateway_instance = IstioGateway.from_json(json)
# print the JSON string representation of the object
print(IstioGateway.to_json())

# convert the object into a dict
istio_gateway_dict = istio_gateway_instance.to_dict()
# create an instance of IstioGateway from a dict
istio_gateway_from_dict = IstioGateway.from_dict(istio_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


