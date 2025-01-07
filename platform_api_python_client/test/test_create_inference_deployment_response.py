# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.create_inference_deployment_response import CreateInferenceDeploymentResponse

class TestCreateInferenceDeploymentResponse(unittest.TestCase):
    """CreateInferenceDeploymentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInferenceDeploymentResponse:
        """Test CreateInferenceDeploymentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInferenceDeploymentResponse`
        """
        model = CreateInferenceDeploymentResponse()
        if include_optional:
            return CreateInferenceDeploymentResponse(
                id = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                endpoint_url = ''
            )
        else:
            return CreateInferenceDeploymentResponse(
                id = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                endpoint_url = '',
        )
        """

    def testCreateInferenceDeploymentResponse(self):
        """Test CreateInferenceDeploymentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
