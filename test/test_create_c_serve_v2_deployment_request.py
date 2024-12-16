# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.create_c_serve_v2_deployment_request import CreateCServeV2DeploymentRequest

class TestCreateCServeV2DeploymentRequest(unittest.TestCase):
    """CreateCServeV2DeploymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCServeV2DeploymentRequest:
        """Test CreateCServeV2DeploymentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCServeV2DeploymentRequest`
        """
        model = CreateCServeV2DeploymentRequest()
        if include_optional:
            return CreateCServeV2DeploymentRequest(
                name = '',
                cluster_id = 56,
                hardware_instance_id = 56,
                recipe = platform_api_python_client.models.c_serve_v2_recipe.CServeV2Recipe(
                    model = '', 
                    max_model_len = 56, 
                    is_embedding_model = True, 
                    tokenizer = '', 
                    tensor_parallel_size = 56, 
                    pipeline_parallel_size = 56, 
                    gpu_mem_util = 1.337, 
                    block_size = 56, 
                    swap_space = 56, 
                    quantization = '', 
                    dtype = 'auto', 
                    cache_dtype = 'auto', 
                    max_num_seqs = 56, 
                    eager_execution = True, 
                    use_flashinfer = True, 
                    offloading_num = 1.337, 
                    spec_draft_model = '', 
                    spec_tokens = 56, 
                    spec_prompt_lookup_max = 56, 
                    spec_prompt_lookup_min = 56, 
                    use_prefix_caching = True, 
                    use_chunked_prefill = True, 
                    chunked_prefill_size = 56, 
                    max_seq_len_to_capture = 56, 
                    distributed_executor_backend = 'ray', 
                    spec_max_batch_size = 56, 
                    spec_max_seq_len = 56, 
                    num_scheduler_steps = 56, ),
                hf_token = '',
                endpoint_certificate_authority = '',
                min_scale = 56,
                max_scale = 56,
                concurrency = 56,
                env_vars = {
                    'key' : ''
                    }
            )
        else:
            return CreateCServeV2DeploymentRequest(
                name = '',
                cluster_id = 56,
                hardware_instance_id = 56,
                recipe = platform_api_python_client.models.c_serve_v2_recipe.CServeV2Recipe(
                    model = '', 
                    max_model_len = 56, 
                    is_embedding_model = True, 
                    tokenizer = '', 
                    tensor_parallel_size = 56, 
                    pipeline_parallel_size = 56, 
                    gpu_mem_util = 1.337, 
                    block_size = 56, 
                    swap_space = 56, 
                    quantization = '', 
                    dtype = 'auto', 
                    cache_dtype = 'auto', 
                    max_num_seqs = 56, 
                    eager_execution = True, 
                    use_flashinfer = True, 
                    offloading_num = 1.337, 
                    spec_draft_model = '', 
                    spec_tokens = 56, 
                    spec_prompt_lookup_max = 56, 
                    spec_prompt_lookup_min = 56, 
                    use_prefix_caching = True, 
                    use_chunked_prefill = True, 
                    chunked_prefill_size = 56, 
                    max_seq_len_to_capture = 56, 
                    distributed_executor_backend = 'ray', 
                    spec_max_batch_size = 56, 
                    spec_max_seq_len = 56, 
                    num_scheduler_steps = 56, ),
                min_scale = 56,
                max_scale = 56,
        )
        """

    def testCreateCServeV2DeploymentRequest(self):
        """Test CreateCServeV2DeploymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()