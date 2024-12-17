# UserVaultItemOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**UserVaultType**](UserVaultType.md) |  | 
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from platform_api_python_client.models.user_vault_item_output import UserVaultItemOutput

# TODO update the JSON string below
json = "{}"
# create an instance of UserVaultItemOutput from a JSON string
user_vault_item_output_instance = UserVaultItemOutput.from_json(json)
# print the JSON string representation of the object
print(UserVaultItemOutput.to_json())

# convert the object into a dict
user_vault_item_output_dict = user_vault_item_output_instance.to_dict()
# create an instance of UserVaultItemOutput from a dict
user_vault_item_output_from_dict = UserVaultItemOutput.from_dict(user_vault_item_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


