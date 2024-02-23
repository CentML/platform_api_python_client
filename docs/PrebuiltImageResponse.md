# PrebuiltImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** |  | 
**label** | **str** |  | 
**tags** | **List[str]** |  | 
**type** | [**DeploymentType**](DeploymentType.md) |  | 

## Example

```python
from platform_api_client.models.prebuilt_image_response import PrebuiltImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrebuiltImageResponse from a JSON string
prebuilt_image_response_instance = PrebuiltImageResponse.from_json(json)
# print the JSON string representation of the object
print PrebuiltImageResponse.to_json()

# convert the object into a dict
prebuilt_image_response_dict = prebuilt_image_response_instance.to_dict()
# create an instance of PrebuiltImageResponse from a dict
prebuilt_image_response_form_dict = prebuilt_image_response.from_dict(prebuilt_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


