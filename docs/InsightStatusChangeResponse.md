# InsightStatusChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_status** | [**InsightStatus**](InsightStatus.md) |  | 
**to_status** | [**InsightStatus**](InsightStatus.md) |  | 
**actor_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.insight_status_change_response import InsightStatusChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightStatusChangeResponse from a JSON string
insight_status_change_response_instance = InsightStatusChangeResponse.from_json(json)
# print the JSON string representation of the object
print(InsightStatusChangeResponse.to_json())

# convert the object into a dict
insight_status_change_response_dict = insight_status_change_response_instance.to_dict()
# create an instance of InsightStatusChangeResponse from a dict
insight_status_change_response_from_dict = InsightStatusChangeResponse.from_dict(insight_status_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


