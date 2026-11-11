# Ingress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 
**bearer_token_ref** | **int** |  | [optional] 
**certificate_authority** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.ingress import Ingress

# TODO update the JSON string below
json = "{}"
# create an instance of Ingress from a JSON string
ingress_instance = Ingress.from_json(json)
# print the JSON string representation of the object
print(Ingress.to_json())

# convert the object into a dict
ingress_dict = ingress_instance.to_dict()
# create an instance of Ingress from a dict
ingress_from_dict = Ingress.from_dict(ingress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


