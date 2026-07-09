# ListVolumesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetVolumeResponse]**](GetVolumeResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.list_volumes_response import ListVolumesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListVolumesResponse from a JSON string
list_volumes_response_instance = ListVolumesResponse.from_json(json)
# print the JSON string representation of the object
print(ListVolumesResponse.to_json())

# convert the object into a dict
list_volumes_response_dict = list_volumes_response_instance.to_dict()
# create an instance of ListVolumesResponse from a dict
list_volumes_response_from_dict = ListVolumesResponse.from_dict(list_volumes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


