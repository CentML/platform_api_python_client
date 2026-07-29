# VolumeStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**backend** | [**VolumeBackend**](VolumeBackend.md) |  | 
**status** | [**VolumeStatus**](VolumeStatus.md) |  | 
**service_status** | [**ServiceStatus**](ServiceStatus.md) |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.volume_status_response import VolumeStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeStatusResponse from a JSON string
volume_status_response_instance = VolumeStatusResponse.from_json(json)
# print the JSON string representation of the object
print(VolumeStatusResponse.to_json())

# convert the object into a dict
volume_status_response_dict = volume_status_response_instance.to_dict()
# create an instance of VolumeStatusResponse from a dict
volume_status_response_from_dict = VolumeStatusResponse.from_dict(volume_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


