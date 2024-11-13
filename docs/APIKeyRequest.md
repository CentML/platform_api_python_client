# APIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from platform_api_python_client.models.api_key_request import APIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyRequest from a JSON string
api_key_request_instance = APIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(APIKeyRequest.to_json())

# convert the object into a dict
api_key_request_dict = api_key_request_instance.to_dict()
# create an instance of APIKeyRequest from a dict
api_key_request_from_dict = APIKeyRequest.from_dict(api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


