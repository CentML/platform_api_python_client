# UnifiedWriteDynamoDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_surge** | **int** |  | [optional] 
**max_unavailable** | **int** |  | [optional] 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | [optional] 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**worker_pools** | [**DynamoWorkerPools**](DynamoWorkerPools.md) |  | [optional] 
**communications** | [**DynamoCommunicationsInput**](DynamoCommunicationsInput.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**runtime_version** | **str** | Dynamo runtime image tag (for example 1.4.0). Defaults to the platform&#39;s current release; GET /prebuilt-images?type&#x3D;dynamo lists the versions the platform has validated, but any tag may be requested. require_gpu_direct_rdma needs an EFA-capable image. Changing it restarts every component of a running deployment. | [optional] 
**min_replicas** | **int** |  | [optional] 
**max_replicas** | **int** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**cooldown_period** | **int** |  | [optional] 
**extra_args** | **str** |  | [optional] 
**hf_token** | **str** |  | [optional] 
**hf_token_ref** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**env_vars_refs** | **object** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**bearer_token_ref** | **int** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**image_pull_ref** | **int** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]
**enable_node_model_cache** | **bool** |  | [optional] [default to False]
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from platform_api_python_client.models.unified_write_dynamo_deployment_request import UnifiedWriteDynamoDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedWriteDynamoDeploymentRequest from a JSON string
unified_write_dynamo_deployment_request_instance = UnifiedWriteDynamoDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(UnifiedWriteDynamoDeploymentRequest.to_json())

# convert the object into a dict
unified_write_dynamo_deployment_request_dict = unified_write_dynamo_deployment_request_instance.to_dict()
# create an instance of UnifiedWriteDynamoDeploymentRequest from a dict
unified_write_dynamo_deployment_request_from_dict = UnifiedWriteDynamoDeploymentRequest.from_dict(unified_write_dynamo_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


