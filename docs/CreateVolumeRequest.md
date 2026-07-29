# CreateVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**backend** | **str** |  | 
**size_gb** | **int** |  | [optional] [default to 100]
**storage_class** | **str** |  | [optional] 
**provider** | [**ObjectStorageProvider**](ObjectStorageProvider.md) |  | [optional] 
**bucket** | **str** |  | 
**region** | **str** |  | 
**prefix** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] [default to False]
**volume_attributes** | **Dict[str, str]** |  | [optional] 
**mount_options** | **List[str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_volume_request import CreateVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVolumeRequest from a JSON string
create_volume_request_instance = CreateVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVolumeRequest.to_json())

# convert the object into a dict
create_volume_request_dict = create_volume_request_instance.to_dict()
# create an instance of CreateVolumeRequest from a dict
create_volume_request_from_dict = CreateVolumeRequest.from_dict(create_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


