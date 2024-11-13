# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_external_client.models.get_deployment_usage_response import GetDeploymentUsageResponse

class TestGetDeploymentUsageResponse(unittest.TestCase):
    """GetDeploymentUsageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDeploymentUsageResponse:
        """Test GetDeploymentUsageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDeploymentUsageResponse`
        """
        model = GetDeploymentUsageResponse()
        if include_optional:
            return GetDeploymentUsageResponse(
                values = [
                    platform_api_external_client.models.deployment_usage_value.DeploymentUsageValue(
                        timestamp = 56, 
                        value = 1.337, )
                    ]
            )
        else:
            return GetDeploymentUsageResponse(
                values = [
                    platform_api_external_client.models.deployment_usage_value.DeploymentUsageValue(
                        timestamp = 56, 
                        value = 1.337, )
                    ],
        )
        """

    def testGetDeploymentUsageResponse(self):
        """Test GetDeploymentUsageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
