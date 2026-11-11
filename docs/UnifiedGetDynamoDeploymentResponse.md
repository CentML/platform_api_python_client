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
**priority** | **str** |  | [optional] 
**pools** | [**CclDynamoPools**](CclDynamoPools.md) |  | 
**env** | [**Env**](Env.md) |  | [optional] 
**image** | [**DynamoImage**](DynamoImage.md) |  | [optional] 
**ingress** | [**Ingress**](Ingress.md) |  | 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**communications** | [**DynamoCommunicationsOutput**](DynamoCommunicationsOutput.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**extra_args** | **str** |  | [optional] 
**hf_token_ref** | **int** |  | [optional] 
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


