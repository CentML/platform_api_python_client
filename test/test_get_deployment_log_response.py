# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.get_deployment_log_response import GetDeploymentLogResponse

class TestGetDeploymentLogResponse(unittest.TestCase):
    """GetDeploymentLogResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDeploymentLogResponse:
        """Test GetDeploymentLogResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDeploymentLogResponse`
        """
        model = GetDeploymentLogResponse()
        if include_optional:
            return GetDeploymentLogResponse(
                events = [
                    None
                    ],
                next_page_token = ''
            )
        else:
            return GetDeploymentLogResponse(
                events = [
                    None
                    ],
        )
        """

    def testGetDeploymentLogResponse(self):
        """Test GetDeploymentLogResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
