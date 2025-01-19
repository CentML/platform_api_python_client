# CreateSetupCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_url** | **str** |  | 

## Example

```python
from platform_api_python_client.models.create_setup_checkout_request import CreateSetupCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSetupCheckoutRequest from a JSON string
create_setup_checkout_request_instance = CreateSetupCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSetupCheckoutRequest.to_json())

# convert the object into a dict
create_setup_checkout_request_dict = create_setup_checkout_request_instance.to_dict()
# create an instance of CreateSetupCheckoutRequest from a dict
create_setup_checkout_request_from_dict = CreateSetupCheckoutRequest.from_dict(create_setup_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


