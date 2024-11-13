# GetPaymentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | 
**payments** | **List[object]** |  | 

## Example

```python
from platform_api_external_client.models.get_payments_response import GetPaymentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentsResponse from a JSON string
get_payments_response_instance = GetPaymentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentsResponse.to_json())

# convert the object into a dict
get_payments_response_dict = get_payments_response_instance.to_dict()
# create an instance of GetPaymentsResponse from a dict
get_payments_response_from_dict = GetPaymentsResponse.from_dict(get_payments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

