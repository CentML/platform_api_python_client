# RevisionPodDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision_number** | **int** |  | [optional] 
**revision_status** | [**ServiceStatus**](ServiceStatus.md) |  | 
**pod_details_list** | [**List[PodDetails]**](PodDetails.md) |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.revision_pod_details import RevisionPodDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionPodDetails from a JSON string
revision_pod_details_instance = RevisionPodDetails.from_json(json)
# print the JSON string representation of the object
print(RevisionPodDetails.to_json())

# convert the object into a dict
revision_pod_details_dict = revision_pod_details_instance.to_dict()
# create an instance of RevisionPodDetails from a dict
revision_pod_details_from_dict = RevisionPodDetails.from_dict(revision_pod_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


