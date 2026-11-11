# InsightListItemResponse


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

## Example

```python
from platform_api_python_client.models.insight_list_item_response import InsightListItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightListItemResponse from a JSON string
insight_list_item_response_instance = InsightListItemResponse.from_json(json)
# print the JSON string representation of the object
print(InsightListItemResponse.to_json())

# convert the object into a dict
insight_list_item_response_dict = insight_list_item_response_instance.to_dict()
# create an instance of InsightListItemResponse from a dict
insight_list_item_response_from_dict = InsightListItemResponse.from_dict(insight_list_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


