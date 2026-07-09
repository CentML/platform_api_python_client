# CreateObjectVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**backend** | **str** |  | 
**provider** | [**ObjectStorageProvider**](ObjectStorageProvider.md) |  | [optional] 
**bucket** | **str** |  | 
**region** | **str** |  | 
**prefix** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] [default to False]
**volume_attributes** | **Dict[str, str]** |  | [optional] 
**mount_options** | **List[str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_object_volume_request import CreateObjectVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectVolumeRequest from a JSON string
create_object_volume_request_instance = CreateObjectVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateObjectVolumeRequest.to_json())

# convert the object into a dict
create_object_volume_request_dict = create_object_volume_request_instance.to_dict()
# create an instance of CreateObjectVolumeRequest from a dict
create_object_volume_request_from_dict = CreateObjectVolumeRequest.from_dict(create_object_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


