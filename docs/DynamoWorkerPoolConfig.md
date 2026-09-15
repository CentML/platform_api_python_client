# DynamoWorkerPoolConfig

Hardware and scaling for one Dynamo worker role.  ``min_replicas``/``max_replicas`` are the canonical size. ``replicas`` is the deprecated fixed-size alias (``min == max``) still accepted on disaggregated pools. ``parse_dynamo_topology`` owns the cross-field rules (bounds ordering, autoscaling target, which roles may autoscale).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_instance_id** | **int** |  | 
**replicas** | **int** |  | [optional] 
**min_replicas** | **int** |  | [optional] 
**max_replicas** | **int** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**cooldown_period** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.dynamo_worker_pool_config import DynamoWorkerPoolConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoWorkerPoolConfig from a JSON string
dynamo_worker_pool_config_instance = DynamoWorkerPoolConfig.from_json(json)
# print the JSON string representation of the object
print(DynamoWorkerPoolConfig.to_json())

# convert the object into a dict
dynamo_worker_pool_config_dict = dynamo_worker_pool_config_instance.to_dict()
# create an instance of DynamoWorkerPoolConfig from a dict
dynamo_worker_pool_config_from_dict = DynamoWorkerPoolConfig.from_dict(dynamo_worker_pool_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


