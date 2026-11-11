# InsightResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**identity** | **str** | Human-readable identifier, e.g. INSIGHT-42 | 
**severity** | [**InsightSeverity**](InsightSeverity.md) |  | 
**status** | [**InsightStatus**](InsightStatus.md) |  | 
**title** | **str** |  | 
**observed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**resource** | [**InsightResource**](InsightResource.md) |  | 
**observed_summary** | **str** |  | 
**recommended_steps** | **str** |  | 
**content** | **str** |  | [optional] 
**reported_by** | **str** | Name of the user that reported it; a service account shows its creator | 
**updated_at** | **datetime** |  | 
**history** | [**List[InsightStatusChangeResponse]**](InsightStatusChangeResponse.md) | Status changes, newest first | 

## Example

```python
from platform_api_python_client.models.insight_response import InsightResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightResponse from a JSON string
insight_response_instance = InsightResponse.from_json(json)
# print the JSON string representation of the object
print(InsightResponse.to_json())

# convert the object into a dict
insight_response_dict = insight_response_instance.to_dict()
# create an instance of InsightResponse from a dict
insight_response_from_dict = InsightResponse.from_dict(insight_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


