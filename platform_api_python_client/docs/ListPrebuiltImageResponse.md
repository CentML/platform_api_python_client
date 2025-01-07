# ListPrebuiltImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PrebuiltImageResponse]**](PrebuiltImageResponse.md) |  | 

## Example

```python
from platform_api_python_client.models.list_prebuilt_image_response import ListPrebuiltImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPrebuiltImageResponse from a JSON string
list_prebuilt_image_response_instance = ListPrebuiltImageResponse.from_json(json)
# print the JSON string representation of the object
print(ListPrebuiltImageResponse.to_json())

# convert the object into a dict
list_prebuilt_image_response_dict = list_prebuilt_image_response_instance.to_dict()
# create an instance of ListPrebuiltImageResponse from a dict
list_prebuilt_image_response_from_dict = ListPrebuiltImageResponse.from_dict(list_prebuilt_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


