# UpdateAutopayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **int** |  | [optional] 
**amount** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.update_autopay_request import UpdateAutopayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutopayRequest from a JSON string
update_autopay_request_instance = UpdateAutopayRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAutopayRequest.to_json())

# convert the object into a dict
update_autopay_request_dict = update_autopay_request_instance.to_dict()
# create an instance of UpdateAutopayRequest from a dict
update_autopay_request_from_dict = UpdateAutopayRequest.from_dict(update_autopay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


