# GetVolumeResponse


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
**provider** | [**ObjectStorageProvider**](ObjectStorageProvider.md) |  | 
**bucket** | **str** |  | 
**region** | **str** |  | 
**prefix** | **str** |  | [optional] 
**read_only** | **bool** |  | 
**volume_attributes** | **Dict[str, str]** |  | [optional] 
**mount_options** | **List[str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.get_volume_response import GetVolumeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVolumeResponse from a JSON string
get_volume_response_instance = GetVolumeResponse.from_json(json)
# print the JSON string representation of the object
print(GetVolumeResponse.to_json())

# convert the object into a dict
get_volume_response_dict = get_volume_response_instance.to_dict()
# create an instance of GetVolumeResponse from a dict
get_volume_response_from_dict = GetVolumeResponse.from_dict(get_volume_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


