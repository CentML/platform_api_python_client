# UserVaultItem

Response model for vault reads and writes.  Every row has a primary key, so `id` is always present and clients can always address a secret by it. `key` stays an unconstrained str and `value` stays optional so secrets stored before the SSM migration remain listable and readable: enforcing the write rules here would turn one such row into a 500 for the whole listing. Write validation lives in UpsertUserVaultItemRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**type** | [**UserVaultType**](UserVaultType.md) |  | 
**key** | **str** |  | 
**value** | **str** |  | [optional] 
**visibility** | [**VaultScope**](VaultScope.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.user_vault_item import UserVaultItem

# TODO update the JSON string below
json = "{}"
# create an instance of UserVaultItem from a JSON string
user_vault_item_instance = UserVaultItem.from_json(json)
# print the JSON string representation of the object
print(UserVaultItem.to_json())

# convert the object into a dict
user_vault_item_dict = user_vault_item_instance.to_dict()
# create an instance of UserVaultItem from a dict
user_vault_item_from_dict = UserVaultItem.from_dict(user_vault_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


