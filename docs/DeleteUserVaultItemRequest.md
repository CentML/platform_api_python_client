# DeleteUserVaultItemRequest

Body for the legacy delete, deliberately permissive.  Kept separate from UserVaultItem so that model can require `id`. Here `id` stays optional because resolving by (type, key, visibility) is the only way to delete a row for which the client was never handed an id, and `value` is accepted and ignored because old clients send back a whole vault item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | [**UserVaultType**](UserVaultType.md) |  | 
**key** | **str** |  | 
**value** | **str** |  | [optional] 
**visibility** | [**VaultScope**](VaultScope.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.delete_user_vault_item_request import DeleteUserVaultItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserVaultItemRequest from a JSON string
delete_user_vault_item_request_instance = DeleteUserVaultItemRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteUserVaultItemRequest.to_json())

# convert the object into a dict
delete_user_vault_item_request_dict = delete_user_vault_item_request_instance.to_dict()
# create an instance of DeleteUserVaultItemRequest from a dict
delete_user_vault_item_request_from_dict = DeleteUserVaultItemRequest.from_dict(delete_user_vault_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


