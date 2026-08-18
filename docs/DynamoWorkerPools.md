# DynamoWorkerPools


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefill** | [**DynamoWorkerPoolConfig**](DynamoWorkerPoolConfig.md) |  | 
**decode** | [**DynamoWorkerPoolConfig**](DynamoWorkerPoolConfig.md) |  | 

## Example

```python
from platform_api_python_client.models.dynamo_worker_pools import DynamoWorkerPools

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoWorkerPools from a JSON string
dynamo_worker_pools_instance = DynamoWorkerPools.from_json(json)
# print the JSON string representation of the object
print(DynamoWorkerPools.to_json())

# convert the object into a dict
dynamo_worker_pools_dict = dynamo_worker_pools_instance.to_dict()
# create an instance of DynamoWorkerPools from a dict
dynamo_worker_pools_from_dict = DynamoWorkerPools.from_dict(dynamo_worker_pools_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


