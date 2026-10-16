# UnifiedWriteDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**image_url** | **str** |  | 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**image_pull_ref** | **int** |  | [optional] 
**env_vars_refs** | **object** |  | [optional] 
**ssh_public_key** | **str** |  | 
**enable_logging** | **bool** |  | [optional] [default to True]
**type** | **str** |  | 
**max_surge** | **int** |  | [optional] 
**max_unavailable** | **int** |  | [optional] 
**hf_token_ref** | **int** |  | [optional] 
**port** | **int** |  | 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 
**concurrency** | **int** |  | [optional] 
**cooldown_period** | **int** |  | [optional] 
**healthcheck** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**command** | **str** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**bearer_token_ref** | **int** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**hf_token** | **str** |  | [optional] 
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 
**enable_node_model_cache** | **bool** |  | [optional] [default to False]
**session_affinity** | **bool** | Enable best-effort sticky routing via the &#x60;X-Session-Id&#x60; request header. Requests carrying the same header value land on the same pod, improving KV cache reuse for agentic workloads. Requests without the header are routed at random. Affinity is NOT durable: scaling, rollouts, restarts, or readiness-probe transitions will remap sessions to different pods. Do not use for irreplaceable in-pod state. | [optional] [default to False]
**config_file** | [**ConfigFileMount**](ConfigFileMount.md) |  | [optional] 
**metrics** | [**MetricsConfig**](MetricsConfig.md) |  | [optional] 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**worker_pools** | [**DynamoWorkerPools**](DynamoWorkerPools.md) |  | [optional] 
**communications** | [**DynamoCommunicationsInput**](DynamoCommunicationsInput.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**runtime_version** | **str** | Dynamo runtime image tag (for example 1.4.0). Defaults to the platform&#39;s current release; GET /prebuilt-images?type&#x3D;dynamo lists the versions the platform has validated, but any tag may be requested. require_gpu_direct_rdma needs an EFA-capable image. Changing it restarts every component of a running deployment. | [optional] 
**extra_args** | **str** |  | [optional] 
**completions** | **int** |  | [optional] [default to 1]
**parallelism** | **int** |  | [optional] [default to 1]
**backoff_limit** | **int** |  | [optional] [default to 3]
**active_deadline_seconds** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.unified_write_deployment_request import UnifiedWriteDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedWriteDeploymentRequest from a JSON string
unified_write_deployment_request_instance = UnifiedWriteDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(UnifiedWriteDeploymentRequest.to_json())

# convert the object into a dict
unified_write_deployment_request_dict = unified_write_deployment_request_instance.to_dict()
# create an instance of UnifiedWriteDeploymentRequest from a dict
unified_write_deployment_request_from_dict = UnifiedWriteDeploymentRequest.from_dict(unified_write_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


