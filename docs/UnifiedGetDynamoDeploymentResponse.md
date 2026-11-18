# UnifiedGetDynamoDeploymentResponse


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
**priority** | **str** | Kubernetes PriorityClass name on the pod spec. Omit to leave unset. | [optional] 
**pools** | [**CclDynamoPools**](CclDynamoPools.md) |  | 
**env** | [**Env**](Env.md) |  | [optional] 
**image** | [**DynamoImage**](DynamoImage.md) |  | [optional] 
**ingress** | [**Ingress**](Ingress.md) |  | 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**communications** | [**DynamoCommunicationsInput**](DynamoCommunicationsInput.md) | Platform-managed worker communications. Only disaggregated KV transfer is supported. Omit or set null to preserve the legacy connector configuration. | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**extra_args** | **str** | Extra worker CLI arguments as a single shell-style string, split into argv with POSIX shell quoting (shlex). Backslash is an escape character, so &#x60;\\&#x60; is consumed unless quoted: e.g. &#x60;--regex \\d+&#x60; reaches the worker as &#x60;d+&#x60;. Wrap literal backslashes in single quotes (&#x60;--regex &#39;\\d+&#39;&#x60;). Unbalanced quotes or a trailing backslash are rejected. | [optional] 
**hf_token_ref** | **int** | Access-token vault item ID for HF_TOKEN. | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]
**enable_node_model_cache** | **bool** |  | [optional] [default to False]

## Example

```python
from platform_api_python_client.models.unified_get_dynamo_deployment_response import UnifiedGetDynamoDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedGetDynamoDeploymentResponse from a JSON string
unified_get_dynamo_deployment_response_instance = UnifiedGetDynamoDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(UnifiedGetDynamoDeploymentResponse.to_json())

# convert the object into a dict
unified_get_dynamo_deployment_response_dict = unified_get_dynamo_deployment_response_instance.to_dict()
# create an instance of UnifiedGetDynamoDeploymentResponse from a dict
unified_get_dynamo_deployment_response_from_dict = UnifiedGetDynamoDeploymentResponse.from_dict(unified_get_dynamo_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


