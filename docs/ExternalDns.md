# ExternalDns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.external_dns import ExternalDns

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDns from a JSON string
external_dns_instance = ExternalDns.from_json(json)
# print the JSON string representation of the object
print(ExternalDns.to_json())

# convert the object into a dict
external_dns_dict = external_dns_instance.to_dict()
# create an instance of ExternalDns from a dict
external_dns_from_dict = ExternalDns.from_dict(external_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


