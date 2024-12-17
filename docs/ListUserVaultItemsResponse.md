# ListUserVaultItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[UserVaultItemOutput]**](UserVaultItemOutput.md) |  | 

## Example

```python
from platform_api_python_client.models.list_user_vault_items_response import ListUserVaultItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserVaultItemsResponse from a JSON string
list_user_vault_items_response_instance = ListUserVaultItemsResponse.from_json(json)
# print the JSON string representation of the object
print(ListUserVaultItemsResponse.to_json())

# convert the object into a dict
list_user_vault_items_response_dict = list_user_vault_items_response_instance.to_dict()
# create an instance of ListUserVaultItemsResponse from a dict
list_user_vault_items_response_from_dict = ListUserVaultItemsResponse.from_dict(list_user_vault_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


