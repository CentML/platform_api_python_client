# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.c_serve_v2_recipe import CServeV2Recipe

class TestCServeV2Recipe(unittest.TestCase):
    """CServeV2Recipe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CServeV2Recipe:
        """Test CServeV2Recipe
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CServeV2Recipe`
        """
        model = CServeV2Recipe()
        if include_optional:
            return CServeV2Recipe(
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
                num_scheduler_steps = 56
            )
        else:
            return CServeV2Recipe(
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
                num_scheduler_steps = 56,
        )
        """

    def testCServeV2Recipe(self):
        """Test CServeV2Recipe"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
