# CreateBlockVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**backend** | **str** |  | 
**size_gb** | **int** |  | [optional] [default to 100]

## Example

```python
from platform_api_python_client.models.create_block_volume_request import CreateBlockVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlockVolumeRequest from a JSON string
create_block_volume_request_instance = CreateBlockVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBlockVolumeRequest.to_json())

# convert the object into a dict
create_block_volume_request_dict = create_block_volume_request_instance.to_dict()
# create an instance of CreateBlockVolumeRequest from a dict
create_block_volume_request_from_dict = CreateBlockVolumeRequest.from_dict(create_block_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


