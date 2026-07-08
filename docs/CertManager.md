# CertManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.cert_manager import CertManager

# TODO update the JSON string below
json = "{}"
# create an instance of CertManager from a JSON string
cert_manager_instance = CertManager.from_json(json)
# print the JSON string representation of the object
print(CertManager.to_json())

# convert the object into a dict
cert_manager_dict = cert_manager_instance.to_dict()
# create an instance of CertManager from a dict
cert_manager_from_dict = CertManager.from_dict(cert_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


