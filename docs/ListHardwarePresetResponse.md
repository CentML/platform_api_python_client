# ListHardwarePresetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HardwarePresetResponse]**](HardwarePresetResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.list_hardware_preset_response import ListHardwarePresetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListHardwarePresetResponse from a JSON string
list_hardware_preset_response_instance = ListHardwarePresetResponse.from_json(json)
# print the JSON string representation of the object
print(ListHardwarePresetResponse.to_json())

# convert the object into a dict
list_hardware_preset_response_dict = list_hardware_preset_response_instance.to_dict()
# create an instance of ListHardwarePresetResponse from a dict
list_hardware_preset_response_from_dict = ListHardwarePresetResponse.from_dict(list_hardware_preset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


