# CServeV2RecipeOutput

Inputs to start deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**max_model_len** | **int** |  | 
**is_embedding_model** | **bool** |  | [default to False]
**tokenizer** | **str** |  | 
**tensor_parallel_size** | **int** |  | 
**pipeline_parallel_size** | **int** |  | 
**gpu_mem_util** | **float** |  | [default to 0.95]
**block_size** | **int** |  | [default to 16]
**swap_space** | **int** |  | [default to 0]
**quantization** | **str** |  | 
**dtype** | **str** |  | [default to 'auto']
**cache_dtype** | **str** |  | [default to 'auto']
**max_num_seqs** | **int** |  | [default to 256]
**eager_execution** | **bool** |  | [default to True]
**use_flashinfer** | **bool** |  | [default to False]
**offloading_num** | **float** |  | [default to 0]
**spec_draft_model** | **str** |  | 
**spec_tokens** | **int** |  | 
**spec_prompt_lookup_max** | **int** |  | 
**spec_prompt_lookup_min** | **int** |  | 
**use_prefix_caching** | **bool** |  | [default to False]
**use_chunked_prefill** | **bool** |  | [default to False]
**chunked_prefill_size** | **int** |  | 
**max_seq_len_to_capture** | **int** |  | [default to 8192]
**distributed_executor_backend** | **str** |  | [default to 'mp']
**spec_max_batch_size** | **int** |  | 
**spec_max_seq_len** | **int** |  | 
**num_scheduler_steps** | **int** |  | [default to 1]

## Example

```python
from platform_api_python_client.models.c_serve_v2_recipe_output import CServeV2RecipeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CServeV2RecipeOutput from a JSON string
c_serve_v2_recipe_output_instance = CServeV2RecipeOutput.from_json(json)
# print the JSON string representation of the object
print(CServeV2RecipeOutput.to_json())

# convert the object into a dict
c_serve_v2_recipe_output_dict = c_serve_v2_recipe_output_instance.to_dict()
# create an instance of CServeV2RecipeOutput from a dict
c_serve_v2_recipe_output_from_dict = CServeV2RecipeOutput.from_dict(c_serve_v2_recipe_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


