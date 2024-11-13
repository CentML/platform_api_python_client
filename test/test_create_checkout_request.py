# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_external_client.models.create_checkout_request import CreateCheckoutRequest

class TestCreateCheckoutRequest(unittest.TestCase):
    """CreateCheckoutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCheckoutRequest:
        """Test CreateCheckoutRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCheckoutRequest`
        """
        model = CreateCheckoutRequest()
        if include_optional:
            return CreateCheckoutRequest(
                amount_credits = 56,
                success_url = ''
            )
        else:
            return CreateCheckoutRequest(
                amount_credits = 56,
                success_url = '',
        )
        """

    def testCreateCheckoutRequest(self):
        """Test CreateCheckoutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()