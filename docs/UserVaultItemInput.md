# UserVaultItemInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**UserVaultType**](UserVaultType.md) |  | 
**key** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.user_vault_item_input import UserVaultItemInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserVaultItemInput from a JSON string
user_vault_item_input_instance = UserVaultItemInput.from_json(json)
# print the JSON string representation of the object
print(UserVaultItemInput.to_json())

# convert the object into a dict
user_vault_item_input_dict = user_vault_item_input_instance.to_dict()
# create an instance of UserVaultItemInput from a dict
user_vault_item_input_from_dict = UserVaultItemInput.from_dict(user_vault_item_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


