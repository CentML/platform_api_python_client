# ListPaymentMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** |  | 

## Example

```python
from platform_api_client.models.list_payment_method_response import ListPaymentMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPaymentMethodResponse from a JSON string
list_payment_method_response_instance = ListPaymentMethodResponse.from_json(json)
# print the JSON string representation of the object
print ListPaymentMethodResponse.to_json()

# convert the object into a dict
list_payment_method_response_dict = list_payment_method_response_instance.to_dict()
# create an instance of ListPaymentMethodResponse from a dict
list_payment_method_response_form_dict = list_payment_method_response.from_dict(list_payment_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


