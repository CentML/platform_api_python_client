# GetBlockVolumeResponse


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

## Example

```python
from platform_api_python_client.models.get_block_volume_response import GetBlockVolumeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockVolumeResponse from a JSON string
get_block_volume_response_instance = GetBlockVolumeResponse.from_json(json)
# print the JSON string representation of the object
print(GetBlockVolumeResponse.to_json())

# convert the object into a dict
get_block_volume_response_dict = get_block_volume_response_instance.to_dict()
# create an instance of GetBlockVolumeResponse from a dict
get_block_volume_response_from_dict = GetBlockVolumeResponse.from_dict(get_block_volume_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


