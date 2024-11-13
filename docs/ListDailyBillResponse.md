# ListDailyBillResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DailyBillResponse]**](DailyBillResponse.md) |  | 

## Example

```python
from platform_api_external_client.models.list_daily_bill_response import ListDailyBillResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDailyBillResponse from a JSON string
list_daily_bill_response_instance = ListDailyBillResponse.from_json(json)
# print the JSON string representation of the object
print(ListDailyBillResponse.to_json())

# convert the object into a dict
list_daily_bill_response_dict = list_daily_bill_response_instance.to_dict()
# create an instance of ListDailyBillResponse from a dict
list_daily_bill_response_from_dict = ListDailyBillResponse.from_dict(list_daily_bill_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


