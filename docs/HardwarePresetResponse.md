# HardwarePresetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** |  | 
**accelerator_memory** | **int** |  | [optional] 
**is_mig** | **bool** |  | 

## Example

```python
from platform_api_python_client.models.hardware_preset_response import HardwarePresetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HardwarePresetResponse from a JSON string
hardware_preset_response_instance = HardwarePresetResponse.from_json(json)
# print the JSON string representation of the object
print(HardwarePresetResponse.to_json())

# convert the object into a dict
hardware_preset_response_dict = hardware_preset_response_instance.to_dict()
# create an instance of HardwarePresetResponse from a dict
hardware_preset_response_from_dict = HardwarePresetResponse.from_dict(hardware_preset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


