# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_external_client.models.list_c_serve_recipe_response import ListCServeRecipeResponse

class TestListCServeRecipeResponse(unittest.TestCase):
    """ListCServeRecipeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListCServeRecipeResponse:
        """Test ListCServeRecipeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListCServeRecipeResponse`
        """
        model = ListCServeRecipeResponse()
        if include_optional:
            return ListCServeRecipeResponse(
                results = [
                    platform_api_external_client.models.c_serve_recipe_response.CServeRecipeResponse(
                        model = '', 
                        cluster_id = 56, 
                        fastest = platform_api_external_client.models.c_serve_recipe_perf.CServeRecipePerf(
                            recipe = platform_api_external_client.models.c_serve_recipe.CServeRecipe(
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
                                seed = 56, ), 
                            hardware_instance_id = 56, 
                            output_tp = [
                                [
                                    null
                                    ]
                                ], 
                            mean_ttft = [
                                [
                                    null
                                    ]
                                ], ), 
                        cheapest = platform_api_external_client.models.c_serve_recipe_perf.CServeRecipePerf(
                            recipe = platform_api_external_client.models.c_serve_recipe.CServeRecipe(
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
                                seed = 56, ), 
                            hardware_instance_id = 56, 
                            output_tp = [
                                [
                                    null
                                    ]
                                ], 
                            mean_ttft = [
                                [
                                    null
                                    ]
                                ], ), 
                        best_value = , )
                    ]
            )
        else:
            return ListCServeRecipeResponse(
                results = [
                    platform_api_external_client.models.c_serve_recipe_response.CServeRecipeResponse(
                        model = '', 
                        cluster_id = 56, 
                        fastest = platform_api_external_client.models.c_serve_recipe_perf.CServeRecipePerf(
                            recipe = platform_api_external_client.models.c_serve_recipe.CServeRecipe(
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
                                seed = 56, ), 
                            hardware_instance_id = 56, 
                            output_tp = [
                                [
                                    null
                                    ]
                                ], 
                            mean_ttft = [
                                [
                                    null
                                    ]
                                ], ), 
                        cheapest = platform_api_external_client.models.c_serve_recipe_perf.CServeRecipePerf(
                            recipe = platform_api_external_client.models.c_serve_recipe.CServeRecipe(
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
                                seed = 56, ), 
                            hardware_instance_id = 56, 
                            output_tp = [
                                [
                                    null
                                    ]
                                ], 
                            mean_ttft = [
                                [
                                    null
                                    ]
                                ], ), 
                        best_value = , )
                    ],
        )
        """

    def testListCServeRecipeResponse(self):
        """Test ListCServeRecipeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
