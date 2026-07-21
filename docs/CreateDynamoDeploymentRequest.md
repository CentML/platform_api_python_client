# CreateDynamoDeploymentRequest

Create a NVIDIA Dynamo (DynamoGraphDeployment) inference deployment.  Aggregated + KV-router pattern with a vLLM backend. The Frontend pod enables KV-aware routing across worker replicas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_surge** | **int** |  | [optional] 
**max_unavailable** | **int** |  | [optional] 
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**image_url** | **str** |  | 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**model** | **str** |  | 
**served_model_name** | **str** |  | [optional] 
**container_port** | **int** | Internal Dynamo Frontend listener port for the non-root runtime. The public endpoint remains on HTTPS; port 8788 is unavailable when backend_protocol is GRPC. | [optional] [default to 8000]
**initial_replicas** | **int** |  | [optional] [default to 1]
**gpus_per_worker** | **int** |  | [optional] [default to 1]
**extra_args** | **str** |  | [optional] 
**hf_token** | **str** |  | [optional] 
**hf_token_secret_name** | **str** |  | [optional] 
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


