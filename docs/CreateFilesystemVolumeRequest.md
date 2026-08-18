# CreateFilesystemVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**backend** | **str** |  | 
**size_gb** | **int** |  | [optional] [default to 100]
**storage_class** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.create_filesystem_volume_request import CreateFilesystemVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFilesystemVolumeRequest from a JSON string
create_filesystem_volume_request_instance = CreateFilesystemVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFilesystemVolumeRequest.to_json())

# convert the object into a dict
create_filesystem_volume_request_dict = create_filesystem_volume_request_instance.to_dict()
# create an instance of CreateFilesystemVolumeRequest from a dict
create_filesystem_volume_request_from_dict = CreateFilesystemVolumeRequest.from_dict(create_filesystem_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


