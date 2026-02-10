# UserVaultItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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


