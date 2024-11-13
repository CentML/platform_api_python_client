# UserSupportEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**subject** | **str** |  | 

## Example

```python
from platform_api_external_client.models.user_support_email_request import UserSupportEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSupportEmailRequest from a JSON string
user_support_email_request_instance = UserSupportEmailRequest.from_json(json)
# print the JSON string representation of the object
print(UserSupportEmailRequest.to_json())

# convert the object into a dict
user_support_email_request_dict = user_support_email_request_instance.to_dict()
# create an instance of UserSupportEmailRequest from a dict
user_support_email_request_from_dict = UserSupportEmailRequest.from_dict(user_support_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


