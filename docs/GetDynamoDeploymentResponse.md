# GetDynamoDeploymentResponse

Dynamo deployment read model.  ``worker_pools`` is the authoritative hardware/scaling view for both serving modes. The inherited ``hardware_instance_id`` is the single-hardware projection (worker for aggregated, decode for disaggregated) and the top-level scaling fields mirror ``worker_pools.worker``; both remain for consumers that predate ``worker_pools``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_email** | **str** |  | 
**cluster_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**endpoint_url** | **str** |  | 
**image_url** | **str** |  | [optional] 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 
**revision_number** | **int** |  | 
**chart_revision** | **str** |  | [optional] 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**priority** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**worker_pools** | [**DynamoWorkerPools**](DynamoWorkerPools.md) |  | [optional] 
**communications** | [**DynamoCommunicationsOutput**](DynamoCommunicationsOutput.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**runtime_version** | **str** |  | [optional] 
**min_replicas** | **int** | Deprecated aggregated-only spelling; set this under worker_pools.worker instead. Accepted alongside worker_pools when the values agree. | 
**max_replicas** | **int** | Deprecated aggregated-only spelling; set this under worker_pools.worker instead. Accepted alongside worker_pools when the values agree. | 
**concurrency** | **int** |  | [optional] 
**cooldown_period** | **int** |  | [optional] 
**extra_args** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]
**enable_node_model_cache** | **bool** |  | [optional] [default to False]
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.get_dynamo_deployment_response import GetDynamoDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDynamoDeploymentResponse from a JSON string
get_dynamo_deployment_response_instance = GetDynamoDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetDynamoDeploymentResponse.to_json())

# convert the object into a dict
get_dynamo_deployment_response_dict = get_dynamo_deployment_response_instance.to_dict()
# create an instance of GetDynamoDeploymentResponse from a dict
get_dynamo_deployment_response_from_dict = GetDynamoDeploymentResponse.from_dict(get_dynamo_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


