# GetFilesystemVolumeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**backend** | **str** |  | 
**access_mode** | [**VolumeAccessMode**](VolumeAccessMode.md) |  | 
**status** | [**VolumeStatus**](VolumeStatus.md) |  | 
**pvc_name** | **str** |  | 
**created_at** | **datetime** |  | 
**size_gb** | **int** |  | 
**storage_class** | **str** |  | 

## Example

```python
from platform_api_python_client.models.get_filesystem_volume_response import GetFilesystemVolumeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFilesystemVolumeResponse from a JSON string
get_filesystem_volume_response_instance = GetFilesystemVolumeResponse.from_json(json)
# print the JSON string representation of the object
print(GetFilesystemVolumeResponse.to_json())

# convert the object into a dict
get_filesystem_volume_response_dict = get_filesystem_volume_response_instance.to_dict()
# create an instance of GetFilesystemVolumeResponse from a dict
get_filesystem_volume_response_from_dict = GetFilesystemVolumeResponse.from_dict(get_filesystem_volume_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


