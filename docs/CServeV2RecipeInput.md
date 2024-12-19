# CServeV2RecipeInput

Inputs to start deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**max_model_len** | **int** |  | [optional] 
**is_embedding_model** | **bool** |  | [optional] [default to False]
**tokenizer** | **str** |  | 
**tensor_parallel_size** | **int** |  | 
**pipeline_parallel_size** | **int** |  | 
**gpu_mem_util** | **float** |  | [optional] [default to 0.95]
**block_size** | **int** |  | [optional] [default to 16]
**swap_space** | **int** |  | [optional] [default to 0]
**quantization** | **str** |  | [optional] 
**dtype** | **str** |  | [optional] [default to 'auto']
**cache_dtype** | **str** |  | [optional] [default to 'auto']
**max_num_seqs** | **int** |  | [optional] [default to 256]
**eager_execution** | **bool** |  | [optional] [default to True]
**use_flashinfer** | **bool** |  | [optional] [default to False]
**offloading_num** | **float** |  | [optional] [default to 0]
**spec_draft_model** | **str** |  | [optional] 
**spec_tokens** | **int** |  | [optional] 
**spec_prompt_lookup_max** | **int** |  | [optional] 
**spec_prompt_lookup_min** | **int** |  | [optional] 
**use_prefix_caching** | **bool** |  | [optional] [default to False]
**use_chunked_prefill** | **bool** |  | [optional] [default to False]
**chunked_prefill_size** | **int** |  | [optional] 
**max_seq_len_to_capture** | **int** |  | [optional] [default to 8192]
**distributed_executor_backend** | **str** |  | [optional] [default to 'mp']
**spec_max_batch_size** | **int** |  | [optional] 
**spec_max_seq_len** | **int** |  | [optional] 
**num_scheduler_steps** | **int** |  | [optional] [default to 1]

## Example

```python
from platform_api_python_client.models.c_serve_v2_recipe_input import CServeV2RecipeInput

# TODO update the JSON string below
json = "{}"
# create an instance of CServeV2RecipeInput from a JSON string
c_serve_v2_recipe_input_instance = CServeV2RecipeInput.from_json(json)
# print the JSON string representation of the object
print(CServeV2RecipeInput.to_json())

# convert the object into a dict
c_serve_v2_recipe_input_dict = c_serve_v2_recipe_input_instance.to_dict()
# create an instance of CServeV2RecipeInput from a dict
c_serve_v2_recipe_input_from_dict = CServeV2RecipeInput.from_dict(c_serve_v2_recipe_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


