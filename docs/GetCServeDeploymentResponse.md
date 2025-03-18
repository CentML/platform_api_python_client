# GetCServeDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**is_embedding_model** | **bool** |  | [optional] [default to False]
**tensor_parallel_size** | **int** |  | 
**pipeline_parallel_size** | **int** |  | 
**block_size** | **int** |  | [optional] [default to 32]
**swap_space** | **int** |  | [optional] [default to 0]
**gpu_mem_util** | **float** |  | [optional] [default to 0.95]
**max_num_seqs** | **int** |  | [optional] [default to 256]
**offloading_num** | **int** |  | [optional] [default to 0]
**use_prefix_caching** | **bool** |  | [optional] 
**use_chunked_prefill** | **bool** |  | [optional] 
**chunked_prefill_size** | **int** |  | [optional] 
**eager_execution** | **bool** |  | [optional] 
**num_scheduler_steps** | **int** |  | [optional] 
**use_flashinfer** | **bool** |  | [optional] [default to False]
**max_model_len** | **int** |  | [optional] 
**dtype** | **str** |  | [optional] [default to 'auto']
**tokenizer** | **str** |  | [optional] 
**spec_proposer** | **str** |  | [optional] 
**spec_draft_model** | **str** |  | [optional] 
**spec_tokens** | **int** |  | [optional] 
**spec_prompt_lookup_min** | **int** |  | [optional] 
**spec_prompt_lookup_max** | **int** |  | [optional] 
**seed** | **int** |  | [optional] [default to 0]
**cluster_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**endpoint_url** | **str** |  | 
**image_url** | **str** |  | [optional] 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 
**min_scale** | **int** |  | 
**max_scale** | **int** |  | 
**endpoint_certificate_authority** | **str** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from platform_api_python_client.models.get_c_serve_deployment_response import GetCServeDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCServeDeploymentResponse from a JSON string
get_c_serve_deployment_response_instance = GetCServeDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(GetCServeDeploymentResponse.to_json())

# convert the object into a dict
get_c_serve_deployment_response_dict = get_c_serve_deployment_response_instance.to_dict()
# create an instance of GetCServeDeploymentResponse from a dict
get_c_serve_deployment_response_from_dict = GetCServeDeploymentResponse.from_dict(get_c_serve_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


