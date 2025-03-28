# UpdateAutochargePreferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_in_cents** | **int** |  | 
**amount_in_cents** | **int** |  | 

## Example

```python
from platform_api_python_client.models.update_autocharge_preferences_request import UpdateAutochargePreferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutochargePreferencesRequest from a JSON string
update_autocharge_preferences_request_instance = UpdateAutochargePreferencesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAutochargePreferencesRequest.to_json())

# convert the object into a dict
update_autocharge_preferences_request_dict = update_autocharge_preferences_request_instance.to_dict()
# create an instance of UpdateAutochargePreferencesRequest from a dict
update_autocharge_preferences_request_from_dict = UpdateAutochargePreferencesRequest.from_dict(update_autocharge_preferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


