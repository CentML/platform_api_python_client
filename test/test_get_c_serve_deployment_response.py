# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.get_c_serve_deployment_response import GetCServeDeploymentResponse

class TestGetCServeDeploymentResponse(unittest.TestCase):
    """GetCServeDeploymentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCServeDeploymentResponse:
        """Test GetCServeDeploymentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCServeDeploymentResponse`
        """
        model = GetCServeDeploymentResponse()
        if include_optional:
            return GetCServeDeploymentResponse(
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
                cluster_id = 56,
                id = 56,
                name = '',
                endpoint_url = '',
                image_url = '',
                type = 'inference',
                status = 'active',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                hardware_instance_id = 56,
                min_scale = 56,
                max_scale = 56,
                endpoint_certificate_authority = '',
                concurrency = 56
            )
        else:
            return GetCServeDeploymentResponse(
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
                cluster_id = 56,
                id = 56,
                name = '',
                endpoint_url = '',
                image_url = '',
                type = 'inference',
                status = 'active',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                hardware_instance_id = 56,
                min_scale = 56,
                max_scale = 56,
                endpoint_certificate_authority = '',
                concurrency = 56,
        )
        """

    def testGetCServeDeploymentResponse(self):
        """Test GetCServeDeploymentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
