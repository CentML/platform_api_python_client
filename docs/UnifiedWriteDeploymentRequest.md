# UnifiedWriteDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**pools** | [**CclDynamoPools**](CclDynamoPools.md) |  | 
**env** | [**Env**](Env.md) |  | [optional] 
**image** | [**DynamoImage**](DynamoImage.md) |  | 
**ssh_public_key** | **str** |  | 
**enable_logging** | **bool** |  | [optional] [default to True]
**ingress** | [**Ingress**](Ingress.md) |  | 
**port** | **int** |  | 
**healthcheck** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**config_file** | [**ConfigFileMount**](ConfigFileMount.md) |  | [optional] 
**hf_token_ref** | **int** |  | [optional] 
**session_affinity** | **bool** | Enable best-effort sticky routing via the &#x60;X-Session-Id&#x60; request header. Requests carrying the same header value land on the same pod, improving KV cache reuse for agentic workloads. Requests without the header are routed at random. Affinity is NOT durable: scaling, rollouts, restarts, or readiness-probe transitions will remap sessions to different pods. Do not use for irreplaceable in-pod state. | [optional] [default to False]
**metrics** | [**MetricsConfig**](MetricsConfig.md) |  | [optional] 
**enable_node_model_cache** | **bool** |  | [optional] [default to False]
**completions** | **int** |  | [optional] [default to 1]
**parallelism** | **int** |  | [optional] [default to 1]
**backoff_limit** | **int** |  | [optional] [default to 3]
**active_deadline_seconds** | **int** |  | [optional] 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**communications** | [**DynamoCommunicationsInput**](DynamoCommunicationsInput.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**extra_args** | **str** |  | [optional] 

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


