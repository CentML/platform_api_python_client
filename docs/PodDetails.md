# PodDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**revision_number** | **int** |  | [optional] 
**status** | [**PodStatus**](PodStatus.md) |  | 
**error_message** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.pod_details import PodDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PodDetails from a JSON string
pod_details_instance = PodDetails.from_json(json)
# print the JSON string representation of the object
print(PodDetails.to_json())

# convert the object into a dict
pod_details_dict = pod_details_instance.to_dict()
# create an instance of PodDetails from a dict
pod_details_from_dict = PodDetails.from_dict(pod_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


