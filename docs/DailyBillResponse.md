# DailyBillResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**credits** | **int** |  | 

## Example

```python
from platform_api_python_client.models.daily_bill_response import DailyBillResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DailyBillResponse from a JSON string
daily_bill_response_instance = DailyBillResponse.from_json(json)
# print the JSON string representation of the object
print(DailyBillResponse.to_json())

# convert the object into a dict
daily_bill_response_dict = daily_bill_response_instance.to_dict()
# create an instance of DailyBillResponse from a dict
daily_bill_response_from_dict = DailyBillResponse.from_dict(daily_bill_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


