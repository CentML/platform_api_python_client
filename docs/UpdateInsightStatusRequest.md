# UpdateInsightStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**InsightStatus**](InsightStatus.md) |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.update_insight_status_request import UpdateInsightStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInsightStatusRequest from a JSON string
update_insight_status_request_instance = UpdateInsightStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInsightStatusRequest.to_json())

# convert the object into a dict
update_insight_status_request_dict = update_insight_status_request_instance.to_dict()
# create an instance of UpdateInsightStatusRequest from a dict
update_insight_status_request_from_dict = UpdateInsightStatusRequest.from_dict(update_insight_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


