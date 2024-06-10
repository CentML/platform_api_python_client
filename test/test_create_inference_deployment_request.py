# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_client.models.create_inference_deployment_request import CreateInferenceDeploymentRequest

class TestCreateInferenceDeploymentRequest(unittest.TestCase):
    """CreateInferenceDeploymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInferenceDeploymentRequest:
        """Test CreateInferenceDeploymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInferenceDeploymentRequest`
        """
        model = CreateInferenceDeploymentRequest()
        if include_optional:
            return CreateInferenceDeploymentRequest(
                name = '',
                image_url = '',
                hardware_instance_id = 56,
                port = 56,
                min_replicas = 56,
                max_replicas = 56,
                timeout = 56,
                healthcheck = '',
                env_vars = {
                    'key' : ''
                    },
                command = [
                    ''
                    ],
                command_args = [
                    ''
                    ],
                endpoint_certificate_authority = ''
            )
        else:
            return CreateInferenceDeploymentRequest(
                name = '',
                image_url = '',
                hardware_instance_id = 56,
                port = 56,
                min_replicas = 56,
                max_replicas = 56,
        )
        """

    def testCreateInferenceDeploymentRequest(self):
        """Test CreateInferenceDeploymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
