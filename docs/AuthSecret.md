# AuthSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from platform_api_client.models.auth_secret import AuthSecret

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSecret from a JSON string
auth_secret_instance = AuthSecret.from_json(json)
# print the JSON string representation of the object
print AuthSecret.to_json()

# convert the object into a dict
auth_secret_dict = auth_secret_instance.to_dict()
# create an instance of AuthSecret from a dict
auth_secret_form_dict = auth_secret.from_dict(auth_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


