# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.list_daily_bill_response import ListDailyBillResponse

class TestListDailyBillResponse(unittest.TestCase):
    """ListDailyBillResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListDailyBillResponse:
        """Test ListDailyBillResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDailyBillResponse`
        """
        model = ListDailyBillResponse()
        if include_optional:
            return ListDailyBillResponse(
                results = [
                    platform_api_python_client.models.daily_bill_response.DailyBillResponse(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        credits = 56, )
                    ]
            )
        else:
            return ListDailyBillResponse(
                results = [
                    platform_api_python_client.models.daily_bill_response.DailyBillResponse(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        credits = 56, )
                    ],
        )
        """

    def testListDailyBillResponse(self):
        """Test ListDailyBillResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()