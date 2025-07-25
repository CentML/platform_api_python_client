# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.create_c_serve_v3_deployment_request import CreateCServeV3DeploymentRequest

class TestCreateCServeV3DeploymentRequest(unittest.TestCase):
    """CreateCServeV3DeploymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCServeV3DeploymentRequest:
        """Test CreateCServeV3DeploymentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCServeV3DeploymentRequest`
        """
        model = CreateCServeV3DeploymentRequest()
        if include_optional:
            return CreateCServeV3DeploymentRequest(
                name = 'ar1c2v7s6djuy1zmetozkhdomha1b0',
                cluster_id = 56,
                hardware_instance_id = 56,
                recipe = { },
                cserve_version = '',
                hf_token = '',
                endpoint_bearer_token = '',
                endpoint_certificate_authority = '',
                min_replicas = 56,
                max_replicas = 56,
                initial_replicas = 56,
                concurrency = 56,
                env_vars = {
                    'key' : ''
                    }
            )
        else:
            return CreateCServeV3DeploymentRequest(
                name = 'ar1c2v7s6djuy1zmetozkhdomha1b0',
                cluster_id = 56,
                hardware_instance_id = 56,
                recipe = { },
                min_replicas = 56,
                max_replicas = 56,
        )
        """

    def testCreateCServeV3DeploymentRequest(self):
        """Test CreateCServeV3DeploymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
