# DynamoWeightTransferConfiguration

ModelExpress peer weight transfer between the workers of one pool, in either serving mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**DynamoWeightTransferPolicy**](DynamoWeightTransferPolicy.md) | The default and only policy, so an empty object opts in. require_gpu_direct_rdma makes a starting worker pull the model&#39;s weights GPU to GPU from a worker of the same pool that already serves the same model_revision commit, over the cluster&#39;s GPU-direct RDMA fabric (currently AWS EFA only), instead of downloading the checkpoint. A pool&#39;s first worker, or one without a reachable peer, falls back to the usual loader. The chart and runtime image prerequisites of require_gpu_direct_rdma KV transfer apply; the API does not validate them. | [optional] 

## Example

```python
from platform_api_python_client.models.dynamo_weight_transfer_configuration import DynamoWeightTransferConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoWeightTransferConfiguration from a JSON string
dynamo_weight_transfer_configuration_instance = DynamoWeightTransferConfiguration.from_json(json)
# print the JSON string representation of the object
print(DynamoWeightTransferConfiguration.to_json())

# convert the object into a dict
dynamo_weight_transfer_configuration_dict = dynamo_weight_transfer_configuration_instance.to_dict()
# create an instance of DynamoWeightTransferConfiguration from a dict
dynamo_weight_transfer_configuration_from_dict = DynamoWeightTransferConfiguration.from_dict(dynamo_weight_transfer_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


