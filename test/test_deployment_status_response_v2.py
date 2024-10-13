# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.deployment_status_response_v2 import DeploymentStatusResponseV2

class TestDeploymentStatusResponseV2(unittest.TestCase):
    """DeploymentStatusResponseV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentStatusResponseV2:
        """Test DeploymentStatusResponseV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentStatusResponseV2`
        """
        model = DeploymentStatusResponseV2()
        if include_optional:
            return DeploymentStatusResponseV2(
                id = 56,
                type = 'inference',
                status = 'active',
                service_status = 'Healthy',
                error_message = '',
                endpoint_url = ''
            )
        else:
            return DeploymentStatusResponseV2(
                id = 56,
                type = 'inference',
                status = 'active',
                service_status = 'Healthy',
                error_message = '',
                endpoint_url = '',
        )
        """

    def testDeploymentStatusResponseV2(self):
        """Test DeploymentStatusResponseV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
