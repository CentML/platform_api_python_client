# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.models.c_serve_v2_recipe_input import CServeV2RecipeInput

class TestCServeV2RecipeInput(unittest.TestCase):
    """CServeV2RecipeInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CServeV2RecipeInput:
        """Test CServeV2RecipeInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CServeV2RecipeInput`
        """
        model = CServeV2RecipeInput()
        if include_optional:
            return CServeV2RecipeInput(
                model = '',
                is_embedding_model = True
            )
        else:
            return CServeV2RecipeInput(
                model = '',
        )
        """

    def testCServeV2RecipeInput(self):
        """Test CServeV2RecipeInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
