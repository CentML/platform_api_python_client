# DeploymentResponse


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
**user_annotations** | **Dict[str, str]** |  | [optional] 
**serving_mode** | [**DynamoServingMode**](DynamoServingMode.md) |  | [optional] 
**worker_pools** | [**DynamoWorkerPools**](DynamoWorkerPools.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 
**concurrency** | **int** |  | [optional] 
**cooldown_period** | **int** |  | [optional] [default to 1800]
**extra_args** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**enable_logging** | **bool** |  | [optional] [default to True]
**enable_node_model_cache** | **bool** |  | [optional] [default to False]
**backend_protocol** | [**BackendProtocol**](BackendProtocol.md) |  | [optional] 
**recipe** | [**CServeV2Recipe**](CServeV2Recipe.md) |  | 
**cserve_version** | **str** |  | [optional] 
**initial_replicas** | **int** |  | [optional] 
**session_affinity** | **bool** | Enable best-effort sticky routing via the &#x60;X-Session-Id&#x60; request header. Requests carrying the same header value land on the same pod, improving KV cache reuse for agentic workloads. Requests without the header are routed at random. Affinity is NOT durable: scaling, rollouts, restarts, or readiness-probe transitions will remap sessions to different pods. Do not use for irreplaceable in-pod state. | [optional] [default to False]
**container_port** | **int** |  | 
**healthcheck** | **str** |  | [optional] 
**command** | **List[str]** |  | [optional] 
**command_args** | **List[str]** |  | [optional] 
**original_command** | **str** |  | [optional] 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**config_file** | [**ConfigFileMount**](ConfigFileMount.md) |  | [optional] 
**metrics** | [**MetricsConfig**](MetricsConfig.md) |  | [optional] 
**exposed_port** | **int** |  | 
**ssh_public_key** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 

## Example

```python
from platform_api_python_client.models.deployment_response import DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentResponse from a JSON string
deployment_response_instance = DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentResponse.to_json())

# convert the object into a dict
deployment_response_dict = deployment_response_instance.to_dict()
# create an instance of DeploymentResponse from a dict
deployment_response_from_dict = DeploymentResponse.from_dict(deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


