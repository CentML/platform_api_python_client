# GetObjectVolumeResponse


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
**provider** | [**ObjectStorageProvider**](ObjectStorageProvider.md) |  | 
**bucket** | **str** |  | 
**region** | **str** |  | 
**prefix** | **str** |  | [optional] 
**read_only** | **bool** |  | 
**volume_attributes** | **Dict[str, str]** |  | [optional] 
**mount_options** | **List[str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.get_object_volume_response import GetObjectVolumeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectVolumeResponse from a JSON string
get_object_volume_response_instance = GetObjectVolumeResponse.from_json(json)
# print the JSON string representation of the object
print(GetObjectVolumeResponse.to_json())

# convert the object into a dict
get_object_volume_response_dict = get_object_volume_response_instance.to_dict()
# create an instance of GetObjectVolumeResponse from a dict
get_object_volume_response_from_dict = GetObjectVolumeResponse.from_dict(get_object_volume_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


