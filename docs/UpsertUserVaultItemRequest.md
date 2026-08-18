# UpsertUserVaultItemRequest

Write model for PUT /user_vault, where the key and value rules are enforced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | [**UserVaultType**](UserVaultType.md) |  | 
**key** | **str** |  | 
**value** | **str** |  | 
**visibility** | [**VaultScope**](VaultScope.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.upsert_user_vault_item_request import UpsertUserVaultItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertUserVaultItemRequest from a JSON string
upsert_user_vault_item_request_instance = UpsertUserVaultItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertUserVaultItemRequest.to_json())

# convert the object into a dict
upsert_user_vault_item_request_dict = upsert_user_vault_item_request_instance.to_dict()
# create an instance of UpsertUserVaultItemRequest from a dict
upsert_user_vault_item_request_from_dict = UpsertUserVaultItemRequest.from_dict(upsert_user_vault_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


