# GetAutochargePreferencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_in_cents** | **int** |  | 
**amount_in_cents** | **int** |  | 

## Example

```python
from platform_api_python_client.models.get_autocharge_preferences_response import GetAutochargePreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAutochargePreferencesResponse from a JSON string
get_autocharge_preferences_response_instance = GetAutochargePreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAutochargePreferencesResponse.to_json())

# convert the object into a dict
get_autocharge_preferences_response_dict = get_autocharge_preferences_response_instance.to_dict()
# create an instance of GetAutochargePreferencesResponse from a dict
get_autocharge_preferences_response_from_dict = GetAutochargePreferencesResponse.from_dict(get_autocharge_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


