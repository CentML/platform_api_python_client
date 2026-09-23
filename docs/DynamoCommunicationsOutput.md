# DynamoCommunicationsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kv_transfer** | [**DynamoKvTransferConfiguration**](DynamoKvTransferConfiguration.md) |  | 

## Example

```python
from platform_api_python_client.models.dynamo_communications_output import DynamoCommunicationsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoCommunicationsOutput from a JSON string
dynamo_communications_output_instance = DynamoCommunicationsOutput.from_json(json)
# print the JSON string representation of the object
print(DynamoCommunicationsOutput.to_json())

# convert the object into a dict
dynamo_communications_output_dict = dynamo_communications_output_instance.to_dict()
# create an instance of DynamoCommunicationsOutput from a dict
dynamo_communications_output_from_dict = DynamoCommunicationsOutput.from_dict(dynamo_communications_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


