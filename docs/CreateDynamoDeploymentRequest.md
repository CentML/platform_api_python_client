# CreateDynamoDeploymentRequest

Create a Dynamo deployment.  Hardware and scaling live under ``worker_pools``: aggregated mode uses exactly ``worker_pools.worker``; disaggregated mode uses exactly ``worker_pools.prefill`` and ``worker_pools.decode`` (fixed-size until per-role autoscaling ships). The top-level ``hardware_instance_id`` / ``min_replicas`` / ``max_replicas`` / ``concurrency`` / ``cooldown_period`` fields are the deprecated aggregated-only spelling; they stay accepted and may accompany ``worker_pools`` when they agree with it. ``parse_dynamo_topology`` owns every topology rule for both spellings.

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
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**worker_pools** | [**DynamoWorkerPools**](DynamoWorkerPools.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**runtime_version** | **str** | Dynamo runtime image tag (for example 1.4.0). Defaults to the platform&#39;s current release; GET /prebuilt-images?type&#x3D;dynamo lists the versions the platform has validated, but any tag may be requested. Changing it restarts every component of a running deployment. | [optional] 
**min_replicas** | **int** |  | [optional] 
**max_replicas** | **int** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**cooldown_period** | **int** |  | [optional] 
**extra_args** | **str** |  | [optional] 
**hf_token** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]
**enable_node_model_cache** | **bool** |  | [optional] [default to False]
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 

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


