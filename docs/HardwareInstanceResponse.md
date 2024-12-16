# HardwareInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**gpu_type** | **str** |  | 
**num_gpu** | **int** |  | 
**cpu** | **int** |  | 
**memory** | **int** |  | 
**cost_per_hr** | **int** |  | 
**cluster_id** | **int** |  | 

## Example

```python
from platform_api_python_client.models.hardware_instance_response import HardwareInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareInstanceResponse from a JSON string
hardware_instance_response_instance = HardwareInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(HardwareInstanceResponse.to_json())

# convert the object into a dict
hardware_instance_response_dict = hardware_instance_response_instance.to_dict()
# create an instance of HardwareInstanceResponse from a dict
hardware_instance_response_from_dict = HardwareInstanceResponse.from_dict(hardware_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


