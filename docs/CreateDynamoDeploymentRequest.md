# CreateDynamoDeploymentRequest

Create a Dynamo deployment.  Hardware and scaling live under ``worker_pools``: aggregated mode uses exactly ``worker_pools.worker``; disaggregated mode uses exactly ``worker_pools.prefill`` and ``worker_pools.decode`` (fixed-size until per-role autoscaling ships). The top-level ``hardware_instance_id`` / ``min_replicas`` / ``max_replicas`` / ``concurrency`` / ``cooldown_period`` fields are the deprecated aggregated-only spelling; they stay accepted and may accompany ``worker_pools`` when they agree with it. ``parse_dynamo_topology`` owns every topology rule for both spellings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_surge** | **int** |  | [optional] 
**max_unavailable** | **int** |  | [optional] 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** | Deprecated aggregated-only spelling; set this under worker_pools.worker instead. Accepted alongside worker_pools when the values agree. | [optional] 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** | Kubernetes PriorityClass name on the pod spec. Omit to leave unset. | [optional] 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**worker_pools** | [**DynamoWorkerPools**](DynamoWorkerPools.md) | Hardware and scaling per worker role. Aggregated mode uses exactly &#x60;worker&#x60;; disaggregated mode uses exactly &#x60;prefill&#x60; and &#x60;decode&#x60;. Unused roles are null. | [optional] 
**communications** | [**DynamoCommunicationsInput**](DynamoCommunicationsInput.md) | Platform-managed worker communications. Only disaggregated KV transfer is supported. Omit or set null to preserve the legacy connector configuration. | [optional] 
**weight_transfer** | [**DynamoWeightTransferConfiguration**](DynamoWeightTransferConfiguration.md) | Platform-managed weight loading between the workers of a pool (ModelExpress peer transfer), in either serving mode. An empty object opts in and pins model_revision to a commit; omit or set null to keep the native loader. | [optional] 
**model** | **str** |  | 
**model_revision** | **str** | Hugging Face branch, tag or commit of &#x60;model&#x60;. The API resolves it to a commit SHA and stores that SHA, so resume and rollback load the same weights. An update keeps the stored commit when it omits this field or sends that commit, as long as &#x60;model&#x60; is unchanged and extra_args does not set --revision; send a branch or tag to move to its newest commit. With no stored commit, weight_transfer pins the default branch&#39;s current commit, and otherwise each worker loads the default branch when it starts. | [optional] 
**served_model_name** | **str** |  | [optional] 
**runtime_version** | **str** | Dynamo runtime image tag (for example 1.4.0). Defaults to the platform&#39;s current release; GET /prebuilt-images?type&#x3D;dynamo lists the versions the platform has validated, but any tag may be requested. require_gpu_direct_rdma needs an EFA-capable image. Changing it restarts every component of a running deployment. | [optional] 
**min_replicas** | **int** | Deprecated aggregated-only spelling; set this under worker_pools.worker instead. Accepted alongside worker_pools when the values agree. | [optional] 
**max_replicas** | **int** | Deprecated aggregated-only spelling; set this under worker_pools.worker instead. Accepted alongside worker_pools when the values agree. | [optional] 
**concurrency** | **int** | Deprecated aggregated-only spelling; set this under worker_pools.worker instead. Accepted alongside worker_pools when the values agree. | [optional] 
**cooldown_period** | **int** | Deprecated aggregated-only spelling; set this under worker_pools.worker instead. Accepted alongside worker_pools when the values agree. | [optional] 
**extra_args** | **str** | Extra worker CLI arguments as a single shell-style string, split into argv with POSIX shell quoting (shlex). Backslash is an escape character, so &#x60;\\&#x60; is consumed unless quoted: e.g. &#x60;--regex \\d+&#x60; reaches the worker as &#x60;d+&#x60;. Wrap literal backslashes in single quotes (&#x60;--regex &#39;\\d+&#39;&#x60;). Unbalanced quotes or a trailing backslash are rejected. | [optional] 
**hf_token** | **str** |  | [optional] 
**hf_token_ref** | **int** | Access-token vault item ID for HF_TOKEN. Cannot be combined with hf_token. | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**env_vars_refs** | **object** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**bearer_token_ref** | **int** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**image_pull_ref** | **int** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]
**enable_node_model_cache** | **bool** |  | [optional] [default to False]
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 
**frontend** | [**DynamoFrontendConfig**](DynamoFrontendConfig.md) | Replica bounds and size of the Frontend (HTTP server and router) pods serving the endpoint, which are placed on separate nodes where possible. Two keep the endpoint serving through a node loss. min_replicas and max_replicas must be equal until Frontend autoscaling is supported. Changing any of these restarts every component of a running deployment. | [optional] 

## Example

```python
from platform_api_python_client.models.create_dynamo_deployment_request import CreateDynamoDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDynamoDeploymentRequest from a JSON string
create_dynamo_deployment_request_instance = CreateDynamoDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDynamoDeploymentRequest.to_json())

# convert the object into a dict
create_dynamo_deployment_request_dict = create_dynamo_deployment_request_instance.to_dict()
# create an instance of CreateDynamoDeploymentRequest from a dict
create_dynamo_deployment_request_from_dict = CreateDynamoDeploymentRequest.from_dict(create_dynamo_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


