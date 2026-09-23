# DynamoCommunicationsInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kv_transfer** | [**DynamoKvTransferConfiguration**](DynamoKvTransferConfiguration.md) |  | 

## Example

```python
from platform_api_python_client.models.dynamo_communications_input import DynamoCommunicationsInput

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoCommunicationsInput from a JSON string
dynamo_communications_input_instance = DynamoCommunicationsInput.from_json(json)
# print the JSON string representation of the object
print(DynamoCommunicationsInput.to_json())

# convert the object into a dict
dynamo_communications_input_dict = dynamo_communications_input_instance.to_dict()
# create an instance of DynamoCommunicationsInput from a dict
dynamo_communications_input_from_dict = DynamoCommunicationsInput.from_dict(dynamo_communications_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


