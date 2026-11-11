# ListInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[InsightListItemResponse]**](InsightListItemResponse.md) | Newest first. A page shorter than the requested limit is the last one; pass the last id as before_id for the next page. | 

## Example

```python
from platform_api_python_client.models.list_insights_response import ListInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInsightsResponse from a JSON string
list_insights_response_instance = ListInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(ListInsightsResponse.to_json())

# convert the object into a dict
list_insights_response_dict = list_insights_response_instance.to_dict()
# create an instance of ListInsightsResponse from a dict
list_insights_response_from_dict = ListInsightsResponse.from_dict(list_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


