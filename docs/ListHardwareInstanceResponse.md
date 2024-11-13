# ListHardwareInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HardwareInstanceResponse]**](HardwareInstanceResponse.md) |  | 

## Example

```python
from platform_api_external_client.models.list_hardware_instance_response import ListHardwareInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListHardwareInstanceResponse from a JSON string
list_hardware_instance_response_instance = ListHardwareInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(ListHardwareInstanceResponse.to_json())

# convert the object into a dict
list_hardware_instance_response_dict = list_hardware_instance_response_instance.to_dict()
# create an instance of ListHardwareInstanceResponse from a dict
list_hardware_instance_response_from_dict = ListHardwareInstanceResponse.from_dict(list_hardware_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


