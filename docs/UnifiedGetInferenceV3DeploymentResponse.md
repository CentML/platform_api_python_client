# UnifiedGetInferenceV3DeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**creator_email** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**revision_number** | **int** |  | 
**endpoint_url** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**pools** | [**CclMainPools**](CclMainPools.md) |  | 
**env** | [**Env**](Env.md) |  | [optional] 
**image** | [**Image**](Image.md) |  | 
**ingress** | [**Ingress**](Ingress.md) |  | 
**port** | **int** |  | 
**healthcheck** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**config_file** | [**ConfigFileMount**](ConfigFileMount.md) |  | [optional] 
**hf_token_ref** | **int** |  | [optional] 
**session_affinity** | **bool** | Enable best-effort sticky routing via the &#x60;X-Session-Id&#x60; request header. Requests carrying the same header value land on the same pod, improving KV cache reuse for agentic workloads. Requests without the header are routed at random. Affinity is NOT durable: scaling, rollouts, restarts, or readiness-probe transitions will remap sessions to different pods. Do not use for irreplaceable in-pod state. | [optional] [default to False]
**metrics** | [**MetricsConfig**](MetricsConfig.md) |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to False]
**enable_node_model_cache** | **bool** |  | [optional] [default to False]

## Example

```python
from platform_api_python_client.models.unified_get_inference_v3_deployment_response import UnifiedGetInferenceV3DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetInferenceV3DeploymentResponse from a JSON string
unified_get_inference_v3_deployment_response_instance = UnifiedGetInferenceV3DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetInferenceV3DeploymentResponse.to_json())

# convert the object into a dict
unified_get_inference_v3_deployment_response_dict = unified_get_inference_v3_deployment_response_instance.to_dict()
# create an instance of UnifiedGetInferenceV3DeploymentResponse from a dict
unified_get_inference_v3_deployment_response_from_dict = UnifiedGetInferenceV3DeploymentResponse.from_dict(unified_get_inference_v3_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


