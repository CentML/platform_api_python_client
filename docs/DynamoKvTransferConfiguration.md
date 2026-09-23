# DynamoKvTransferConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**DynamoKvTransferPolicy**](DynamoKvTransferPolicy.md) | allow_tcp uses platform-managed NIXL/UCX and permits TCP; it does not force TCP or guarantee RDMA. require_gpu_direct_rdma selects EKS EFA device requirements and GPU-buffer transfer over LIBFABRIC without TCP fallback. A compatible EFA chart and runtime image are prerequisites; the API does not validate their capabilities. Device availability is resolved during scheduling. | 

## Example

```python
from platform_api_python_client.models.dynamo_kv_transfer_configuration import DynamoKvTransferConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoKvTransferConfiguration from a JSON string
dynamo_kv_transfer_configuration_instance = DynamoKvTransferConfiguration.from_json(json)
# print the JSON string representation of the object
print(DynamoKvTransferConfiguration.to_json())

# convert the object into a dict
dynamo_kv_transfer_configuration_dict = dynamo_kv_transfer_configuration_instance.to_dict()
# create an instance of DynamoKvTransferConfiguration from a dict
dynamo_kv_transfer_configuration_from_dict = DynamoKvTransferConfiguration.from_dict(dynamo_kv_transfer_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


