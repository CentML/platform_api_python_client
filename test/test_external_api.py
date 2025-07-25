# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from platform_api_python_client.api.external_api import EXTERNALApi


class TestEXTERNALApi(unittest.TestCase):
    """EXTERNALApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EXTERNALApi()

    def tearDown(self) -> None:
        pass

    def test_create_api_key_credentials_api_key_post(self) -> None:
        """Test case for create_api_key_credentials_api_key_post

        Create Api Key
        """
        pass

    def test_create_checkout_payments_checkout_post(self) -> None:
        """Test case for create_checkout_payments_checkout_post

        Create Checkout
        """
        pass

    def test_create_compute_deployment_deployments_compute_post(self) -> None:
        """Test case for create_compute_deployment_deployments_compute_post

        Create Compute Deployment
        """
        pass

    def test_create_cserve_v2_deployment_deployments_cserve_v2_post(self) -> None:
        """Test case for create_cserve_v2_deployment_deployments_cserve_v2_post

        Create Cserve V2 Deployment
        """
        pass

    def test_create_cserve_v3_deployment_deployments_cserve_v3_post(self) -> None:
        """Test case for create_cserve_v3_deployment_deployments_cserve_v3_post

        Create Cserve V3 Deployment
        """
        pass

    def test_create_inference_deployment_deployments_inference_post(self) -> None:
        """Test case for create_inference_deployment_deployments_inference_post

        Create Inference Deployment
        """
        pass

    def test_create_inference_v3_deployment_deployments_inference_v3_post(self) -> None:
        """Test case for create_inference_v3_deployment_deployments_inference_v3_post

        Create Inference V3 Deployment
        """
        pass

    def test_create_new_organization_organizations_post(self) -> None:
        """Test case for create_new_organization_organizations_post

        Create New Organization
        """
        pass

    def test_create_rag_deployment_deployments_rag_post(self) -> None:
        """Test case for create_rag_deployment_deployments_rag_post

        Create Rag Deployment
        """
        pass

    def test_create_setup_payments_setup_checkout_post(self) -> None:
        """Test case for create_setup_payments_setup_checkout_post

        Create Setup
        """
        pass

    def test_delete_api_key_credentials_api_key_id_delete(self) -> None:
        """Test case for delete_api_key_credentials_api_key_id_delete

        Delete Api Key
        """
        pass

    def test_delete_autocharge_preferences_autocharge_preferences_delete(self) -> None:
        """Test case for delete_autocharge_preferences_autocharge_preferences_delete

        Delete Autocharge Preferences
        """
        pass

    def test_delete_payment_method_payments_methods_delete(self) -> None:
        """Test case for delete_payment_method_payments_methods_delete

        Delete Payment Method
        """
        pass

    def test_delete_user_vault_item_endpoint_user_vault_delete(self) -> None:
        """Test case for delete_user_vault_item_endpoint_user_vault_delete

        Delete User Vault Item Endpoint
        """
        pass

    def test_download_url_file_url_download_post(self) -> None:
        """Test case for download_url_file_url_download_post

        Download Url
        """
        pass

    def test_get_all_user_vault_items_endpoint_user_vault_get(self) -> None:
        """Test case for get_all_user_vault_items_endpoint_user_vault_get

        Get All User Vault Items Endpoint
        """
        pass

    def test_get_api_keys_credentials_api_key_get(self) -> None:
        """Test case for get_api_keys_credentials_api_key_get

        Get Api Keys
        """
        pass

    def test_get_autocharge_preferences_autocharge_preferences_get(self) -> None:
        """Test case for get_autocharge_preferences_autocharge_preferences_get

        Get Autocharge Preferences
        """
        pass

    def test_get_clusters_clusters_get(self) -> None:
        """Test case for get_clusters_clusters_get

        Get Clusters
        """
        pass

    def test_get_compute_deployment_deployments_compute_deployment_id_get(self) -> None:
        """Test case for get_compute_deployment_deployments_compute_deployment_id_get

        Get Compute Deployment
        """
        pass

    def test_get_credits_credits_get(self) -> None:
        """Test case for get_credits_credits_get

        Get Credits
        """
        pass

    def test_get_cserve_recipe_deployments_cserve_recipes_get(self) -> None:
        """Test case for get_cserve_recipe_deployments_cserve_recipes_get

        Get Cserve Recipe
        """
        pass

    def test_get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get(self) -> None:
        """Test case for get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get

        Get Cserve V2 Deployment
        """
        pass

    def test_get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get(self) -> None:
        """Test case for get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get

        Get Cserve V3 Deployment
        """
        pass

    def test_get_deployment_logs_deployments_logs_deployment_id_get(self) -> None:
        """Test case for get_deployment_logs_deployments_logs_deployment_id_get

        Get Deployment Logs
        """
        pass

    def test_get_deployment_status_deployments_status_deployment_id_get(self) -> None:
        """Test case for get_deployment_status_deployments_status_deployment_id_get

        Get Deployment Status
        """
        pass

    def test_get_deployments_deployments_get(self) -> None:
        """Test case for get_deployments_deployments_get

        Get Deployments
        """
        pass

    def test_get_hardware_instances_hardware_instances_get(self) -> None:
        """Test case for get_hardware_instances_hardware_instances_get

        Get Hardware Instances
        """
        pass

    def test_get_inference_deployment_deployments_inference_deployment_id_get(self) -> None:
        """Test case for get_inference_deployment_deployments_inference_deployment_id_get

        Get Inference Deployment
        """
        pass

    def test_get_inference_v3_deployment_deployments_inference_v3_deployment_id_get(self) -> None:
        """Test case for get_inference_v3_deployment_deployments_inference_v3_deployment_id_get

        Get Inference V3 Deployment
        """
        pass

    def test_get_payment_method_payments_methods_get(self) -> None:
        """Test case for get_payment_method_payments_methods_get

        Get Payment Method
        """
        pass

    def test_get_payments_payments_get(self) -> None:
        """Test case for get_payments_payments_get

        Get Payments
        """
        pass

    def test_get_prebuilt_images_prebuilt_images_get(self) -> None:
        """Test case for get_prebuilt_images_prebuilt_images_get

        Get Prebuilt Images
        """
        pass

    def test_get_rag_deployment_deployments_rag_deployment_id_get(self) -> None:
        """Test case for get_rag_deployment_deployments_rag_deployment_id_get

        Get Rag Deployment
        """
        pass

    def test_get_usage_daily_bills_get(self) -> None:
        """Test case for get_usage_daily_bills_get

        Get Usage
        """
        pass

    def test_get_usage_deployments_usage_deployment_id_get(self) -> None:
        """Test case for get_usage_deployments_usage_deployment_id_get

        Get Usage
        """
        pass

    def test_setup_stripe_customer_payments_setup_post(self) -> None:
        """Test case for setup_stripe_customer_payments_setup_post

        Setup Stripe Customer
        """
        pass

    def test_update_autocharge_preferences_autocharge_preferences_put(self) -> None:
        """Test case for update_autocharge_preferences_autocharge_preferences_put

        Update Autocharge Preferences
        """
        pass

    def test_update_compute_deployment_deployments_compute_put(self) -> None:
        """Test case for update_compute_deployment_deployments_compute_put

        Update Compute Deployment
        """
        pass

    def test_update_cserve_v2_deployment_deployments_cserve_v2_put(self) -> None:
        """Test case for update_cserve_v2_deployment_deployments_cserve_v2_put

        Update Cserve V2 Deployment
        """
        pass

    def test_update_cserve_v3_deployment_deployments_cserve_v3_put(self) -> None:
        """Test case for update_cserve_v3_deployment_deployments_cserve_v3_put

        Update Cserve V3 Deployment
        """
        pass

    def test_update_deployment_status_deployments_status_deployment_id_put(self) -> None:
        """Test case for update_deployment_status_deployments_status_deployment_id_put

        Update Deployment Status
        """
        pass

    def test_update_inference_deployment_deployments_inference_put(self) -> None:
        """Test case for update_inference_deployment_deployments_inference_put

        Update Inference Deployment
        """
        pass

    def test_update_inference_v3_deployment_deployments_inference_v3_put(self) -> None:
        """Test case for update_inference_v3_deployment_deployments_inference_v3_put

        Update Inference V3 Deployment
        """
        pass

    def test_update_rag_deployment_deployments_rag_put(self) -> None:
        """Test case for update_rag_deployment_deployments_rag_put

        Update Rag Deployment
        """
        pass

    def test_update_user_vault_item_endpoint_user_vault_put(self) -> None:
        """Test case for update_user_vault_item_endpoint_user_vault_put

        Update User Vault Item Endpoint
        """
        pass

    def test_upload_url_file_url_upload_post(self) -> None:
        """Test case for upload_url_file_url_upload_post

        Upload Url
        """
        pass


if __name__ == '__main__':
    unittest.main()
