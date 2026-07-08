# IngressNginx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**values** | **object** |  | [optional] 

## Example

```python
from platform_api_python_client.models.ingress_nginx import IngressNginx

# TODO update the JSON string below
json = "{}"
# create an instance of IngressNginx from a JSON string
ingress_nginx_instance = IngressNginx.from_json(json)
# print the JSON string representation of the object
print(IngressNginx.to_json())

# convert the object into a dict
ingress_nginx_dict = ingress_nginx_instance.to_dict()
# create an instance of IngressNginx from a dict
ingress_nginx_from_dict = IngressNginx.from_dict(ingress_nginx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


