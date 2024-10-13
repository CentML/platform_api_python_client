# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.c_serve_recipe_output import CServeRecipeOutput

class TestCServeRecipeOutput(unittest.TestCase):
    """CServeRecipeOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CServeRecipeOutput:
        """Test CServeRecipeOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CServeRecipeOutput`
        """
        model = CServeRecipeOutput()
        if include_optional:
            return CServeRecipeOutput(
                model = '',
                is_embedding_model = True,
                tensor_parallel_size = 56,
                pipeline_parallel_size = 56,
                block_size = 56,
                swap_space = 0.0,
                gpu_mem_util = 0.0,
                max_num_seqs = 56,
                use_prefix_caching = True,
                offloading_num = 56,
                use_flashinfer = True,
                max_model_len = 128.0,
                dtype = 'auto',
                tokenizer = '',
                spec_proposer = '',
                spec_draft_model = '',
                spec_tokens = 56,
                spec_prompt_lookup_min = 1.0,
                spec_prompt_lookup_max = 1.0,
                seed = 56
            )
        else:
            return CServeRecipeOutput(
                model = '',
                is_embedding_model = True,
                tensor_parallel_size = 56,
                pipeline_parallel_size = 56,
                block_size = 56,
                swap_space = 0.0,
                gpu_mem_util = 0.0,
                max_num_seqs = 56,
                use_prefix_caching = True,
                offloading_num = 56,
                use_flashinfer = True,
                max_model_len = 128.0,
                dtype = 'auto',
                tokenizer = '',
                spec_proposer = '',
                spec_draft_model = '',
                spec_tokens = 56,
                spec_prompt_lookup_min = 1.0,
                spec_prompt_lookup_max = 1.0,
                seed = 56,
        )
        """

    def testCServeRecipeOutput(self):
        """Test CServeRecipeOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
