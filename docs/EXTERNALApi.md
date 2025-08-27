# platform_api_python_client.EXTERNALApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key_credentials_api_key_post**](EXTERNALApi.md#create_api_key_credentials_api_key_post) | **POST** /credentials/api-key | Create Api Key
[**create_compute_deployment_deployments_compute_post**](EXTERNALApi.md#create_compute_deployment_deployments_compute_post) | **POST** /deployments/compute | Create Compute Deployment
[**create_cserve_v2_deployment_deployments_cserve_v2_post**](EXTERNALApi.md#create_cserve_v2_deployment_deployments_cserve_v2_post) | **POST** /deployments/cserve_v2 | Create Cserve V2 Deployment
[**create_cserve_v3_deployment_deployments_cserve_v3_post**](EXTERNALApi.md#create_cserve_v3_deployment_deployments_cserve_v3_post) | **POST** /deployments/cserve_v3 | Create Cserve V3 Deployment
[**create_inference_deployment_deployments_inference_post**](EXTERNALApi.md#create_inference_deployment_deployments_inference_post) | **POST** /deployments/inference | Create Inference Deployment
[**create_inference_v3_deployment_deployments_inference_v3_post**](EXTERNALApi.md#create_inference_v3_deployment_deployments_inference_v3_post) | **POST** /deployments/inference_v3 | Create Inference V3 Deployment
[**create_new_organization_organizations_post**](EXTERNALApi.md#create_new_organization_organizations_post) | **POST** /organizations | Create New Organization
[**create_rag_deployment_deployments_rag_post**](EXTERNALApi.md#create_rag_deployment_deployments_rag_post) | **POST** /deployments/rag | Create Rag Deployment
[**delete_api_key_credentials_api_key_id_delete**](EXTERNALApi.md#delete_api_key_credentials_api_key_id_delete) | **DELETE** /credentials/api-key/{id} | Delete Api Key
[**delete_user_vault_item_endpoint_user_vault_delete**](EXTERNALApi.md#delete_user_vault_item_endpoint_user_vault_delete) | **DELETE** /user_vault | Delete User Vault Item Endpoint
[**download_url_file_url_download_post**](EXTERNALApi.md#download_url_file_url_download_post) | **POST** /file_url/download | Download Url
[**get_all_user_vault_items_endpoint_user_vault_get**](EXTERNALApi.md#get_all_user_vault_items_endpoint_user_vault_get) | **GET** /user_vault | Get All User Vault Items Endpoint
[**get_api_keys_credentials_api_key_get**](EXTERNALApi.md#get_api_keys_credentials_api_key_get) | **GET** /credentials/api-key | Get Api Keys
[**get_clusters_clusters_get**](EXTERNALApi.md#get_clusters_clusters_get) | **GET** /clusters | Get Clusters
[**get_compute_deployment_deployments_compute_deployment_id_get**](EXTERNALApi.md#get_compute_deployment_deployments_compute_deployment_id_get) | **GET** /deployments/compute/{deployment_id} | Get Compute Deployment
[**get_credits_credits_get**](EXTERNALApi.md#get_credits_credits_get) | **GET** /credits | Get Credits
[**get_cserve_recipe_deployments_cserve_recipes_get**](EXTERNALApi.md#get_cserve_recipe_deployments_cserve_recipes_get) | **GET** /deployments/cserve/recipes | Get Cserve Recipe
[**get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get**](EXTERNALApi.md#get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get) | **GET** /deployments/cserve_v2/{deployment_id} | Get Cserve V2 Deployment
[**get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get**](EXTERNALApi.md#get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get) | **GET** /deployments/cserve_v3/{deployment_id} | Get Cserve V3 Deployment
[**get_deployment_logs_deployments_logs_deployment_id_get**](EXTERNALApi.md#get_deployment_logs_deployments_logs_deployment_id_get) | **GET** /deployments/logs/{deployment_id} | Get Deployment Logs
[**get_deployment_logs_v3_deployments_logs_v3_deployment_id_revision_number_get**](EXTERNALApi.md#get_deployment_logs_v3_deployments_logs_v3_deployment_id_revision_number_get) | **GET** /deployments/logs_v3/{deployment_id}/{revision_number} | Get Deployment Logs V3
[**get_deployment_revision_deployments_revisions_deployment_id_revision_number_get**](EXTERNALApi.md#get_deployment_revision_deployments_revisions_deployment_id_revision_number_get) | **GET** /deployments/revisions/{deployment_id}/{revision_number} | Get Deployment Revision
[**get_deployment_revisions_deployments_revisions_deployment_id_get**](EXTERNALApi.md#get_deployment_revisions_deployments_revisions_deployment_id_get) | **GET** /deployments/revisions/{deployment_id} | Get Deployment Revisions
[**get_deployment_status_deployments_status_deployment_id_get**](EXTERNALApi.md#get_deployment_status_deployments_status_deployment_id_get) | **GET** /deployments/status/{deployment_id} | Get Deployment Status
[**get_deployment_status_v3_deployments_status_v3_deployment_id_get**](EXTERNALApi.md#get_deployment_status_v3_deployments_status_v3_deployment_id_get) | **GET** /deployments/status_v3/{deployment_id} | Get Deployment Status V3
[**get_deployments_deployments_get**](EXTERNALApi.md#get_deployments_deployments_get) | **GET** /deployments | Get Deployments
[**get_hardware_instances_hardware_instances_get**](EXTERNALApi.md#get_hardware_instances_hardware_instances_get) | **GET** /hardware-instances | Get Hardware Instances
[**get_inference_deployment_deployments_inference_deployment_id_get**](EXTERNALApi.md#get_inference_deployment_deployments_inference_deployment_id_get) | **GET** /deployments/inference/{deployment_id} | Get Inference Deployment
[**get_inference_v3_deployment_deployments_inference_v3_deployment_id_get**](EXTERNALApi.md#get_inference_v3_deployment_deployments_inference_v3_deployment_id_get) | **GET** /deployments/inference_v3/{deployment_id} | Get Inference V3 Deployment
[**get_prebuilt_images_prebuilt_images_get**](EXTERNALApi.md#get_prebuilt_images_prebuilt_images_get) | **GET** /prebuilt-images | Get Prebuilt Images
[**get_rag_deployment_deployments_rag_deployment_id_get**](EXTERNALApi.md#get_rag_deployment_deployments_rag_deployment_id_get) | **GET** /deployments/rag/{deployment_id} | Get Rag Deployment
[**get_usage_daily_bills_get**](EXTERNALApi.md#get_usage_daily_bills_get) | **GET** /daily_bills | Get Usage
[**get_usage_deployments_usage_deployment_id_get**](EXTERNALApi.md#get_usage_deployments_usage_deployment_id_get) | **GET** /deployments/usage/{deployment_id} | Get Usage
[**rollout_existing_revision_deployments_revisions_deployment_id_revision_number_put**](EXTERNALApi.md#rollout_existing_revision_deployments_revisions_deployment_id_revision_number_put) | **PUT** /deployments/revisions/{deployment_id}/{revision_number} | Rollout Existing Revision
[**setup_stripe_customer_payments_setup_post**](EXTERNALApi.md#setup_stripe_customer_payments_setup_post) | **POST** /payments/setup | Setup Stripe Customer
[**update_compute_deployment_deployments_compute_put**](EXTERNALApi.md#update_compute_deployment_deployments_compute_put) | **PUT** /deployments/compute | Update Compute Deployment
[**update_cserve_v2_deployment_deployments_cserve_v2_put**](EXTERNALApi.md#update_cserve_v2_deployment_deployments_cserve_v2_put) | **PUT** /deployments/cserve_v2 | Update Cserve V2 Deployment
[**update_cserve_v3_deployment_deployments_cserve_v3_put**](EXTERNALApi.md#update_cserve_v3_deployment_deployments_cserve_v3_put) | **PUT** /deployments/cserve_v3 | Update Cserve V3 Deployment
[**update_deployment_status_deployments_status_deployment_id_put**](EXTERNALApi.md#update_deployment_status_deployments_status_deployment_id_put) | **PUT** /deployments/status/{deployment_id} | Update Deployment Status
[**update_deployment_status_v3_deployments_status_v3_deployment_id_put**](EXTERNALApi.md#update_deployment_status_v3_deployments_status_v3_deployment_id_put) | **PUT** /deployments/status_v3/{deployment_id} | Update Deployment Status V3
[**update_inference_deployment_deployments_inference_put**](EXTERNALApi.md#update_inference_deployment_deployments_inference_put) | **PUT** /deployments/inference | Update Inference Deployment
[**update_inference_v3_deployment_deployments_inference_v3_put**](EXTERNALApi.md#update_inference_v3_deployment_deployments_inference_v3_put) | **PUT** /deployments/inference_v3 | Update Inference V3 Deployment
[**update_rag_deployment_deployments_rag_put**](EXTERNALApi.md#update_rag_deployment_deployments_rag_put) | **PUT** /deployments/rag | Update Rag Deployment
[**update_user_vault_item_endpoint_user_vault_put**](EXTERNALApi.md#update_user_vault_item_endpoint_user_vault_put) | **PUT** /user_vault | Update User Vault Item Endpoint
[**upload_url_file_url_upload_post**](EXTERNALApi.md#upload_url_file_url_upload_post) | **POST** /file_url/upload | Upload Url


# **create_api_key_credentials_api_key_post**
> APIKeyResponse create_api_key_credentials_api_key_post(api_key_request)

Create Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.api_key_request import APIKeyRequest
from platform_api_python_client.models.api_key_response import APIKeyResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    api_key_request = platform_api_python_client.APIKeyRequest() # APIKeyRequest | 

    try:
        # Create Api Key
        api_response = api_instance.create_api_key_credentials_api_key_post(api_key_request)
        print("The response of EXTERNALApi->create_api_key_credentials_api_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_api_key_credentials_api_key_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_request** | [**APIKeyRequest**](APIKeyRequest.md)|  | 

### Return type

[**APIKeyResponse**](APIKeyResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_compute_deployment_deployments_compute_post**
> CreateComputeDeploymentResponse create_compute_deployment_deployments_compute_post(create_compute_deployment_request)

Create Compute Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_compute_deployment_request import CreateComputeDeploymentRequest
from platform_api_python_client.models.create_compute_deployment_response import CreateComputeDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_compute_deployment_request = platform_api_python_client.CreateComputeDeploymentRequest() # CreateComputeDeploymentRequest | 

    try:
        # Create Compute Deployment
        api_response = api_instance.create_compute_deployment_deployments_compute_post(create_compute_deployment_request)
        print("The response of EXTERNALApi->create_compute_deployment_deployments_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_compute_deployment_deployments_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_compute_deployment_request** | [**CreateComputeDeploymentRequest**](CreateComputeDeploymentRequest.md)|  | 

### Return type

[**CreateComputeDeploymentResponse**](CreateComputeDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cserve_v2_deployment_deployments_cserve_v2_post**
> CreateCServeV2DeploymentResponse create_cserve_v2_deployment_deployments_cserve_v2_post(create_c_serve_v2_deployment_request)

Create Cserve V2 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_c_serve_v2_deployment_request import CreateCServeV2DeploymentRequest
from platform_api_python_client.models.create_c_serve_v2_deployment_response import CreateCServeV2DeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_c_serve_v2_deployment_request = platform_api_python_client.CreateCServeV2DeploymentRequest() # CreateCServeV2DeploymentRequest | 

    try:
        # Create Cserve V2 Deployment
        api_response = api_instance.create_cserve_v2_deployment_deployments_cserve_v2_post(create_c_serve_v2_deployment_request)
        print("The response of EXTERNALApi->create_cserve_v2_deployment_deployments_cserve_v2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_cserve_v2_deployment_deployments_cserve_v2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_c_serve_v2_deployment_request** | [**CreateCServeV2DeploymentRequest**](CreateCServeV2DeploymentRequest.md)|  | 

### Return type

[**CreateCServeV2DeploymentResponse**](CreateCServeV2DeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cserve_v3_deployment_deployments_cserve_v3_post**
> CreateCServeV3DeploymentResponse create_cserve_v3_deployment_deployments_cserve_v3_post(create_c_serve_v3_deployment_request)

Create Cserve V3 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_c_serve_v3_deployment_request import CreateCServeV3DeploymentRequest
from platform_api_python_client.models.create_c_serve_v3_deployment_response import CreateCServeV3DeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_c_serve_v3_deployment_request = platform_api_python_client.CreateCServeV3DeploymentRequest() # CreateCServeV3DeploymentRequest | 

    try:
        # Create Cserve V3 Deployment
        api_response = api_instance.create_cserve_v3_deployment_deployments_cserve_v3_post(create_c_serve_v3_deployment_request)
        print("The response of EXTERNALApi->create_cserve_v3_deployment_deployments_cserve_v3_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_cserve_v3_deployment_deployments_cserve_v3_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_c_serve_v3_deployment_request** | [**CreateCServeV3DeploymentRequest**](CreateCServeV3DeploymentRequest.md)|  | 

### Return type

[**CreateCServeV3DeploymentResponse**](CreateCServeV3DeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inference_deployment_deployments_inference_post**
> CreateInferenceDeploymentResponse create_inference_deployment_deployments_inference_post(create_inference_deployment_request)

Create Inference Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_inference_deployment_request import CreateInferenceDeploymentRequest
from platform_api_python_client.models.create_inference_deployment_response import CreateInferenceDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_inference_deployment_request = platform_api_python_client.CreateInferenceDeploymentRequest() # CreateInferenceDeploymentRequest | 

    try:
        # Create Inference Deployment
        api_response = api_instance.create_inference_deployment_deployments_inference_post(create_inference_deployment_request)
        print("The response of EXTERNALApi->create_inference_deployment_deployments_inference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_inference_deployment_deployments_inference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inference_deployment_request** | [**CreateInferenceDeploymentRequest**](CreateInferenceDeploymentRequest.md)|  | 

### Return type

[**CreateInferenceDeploymentResponse**](CreateInferenceDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inference_v3_deployment_deployments_inference_v3_post**
> CreateInferenceDeploymentResponse create_inference_v3_deployment_deployments_inference_v3_post(create_inference_v3_deployment_request)

Create Inference V3 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_inference_deployment_response import CreateInferenceDeploymentResponse
from platform_api_python_client.models.create_inference_v3_deployment_request import CreateInferenceV3DeploymentRequest
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_inference_v3_deployment_request = platform_api_python_client.CreateInferenceV3DeploymentRequest() # CreateInferenceV3DeploymentRequest | 

    try:
        # Create Inference V3 Deployment
        api_response = api_instance.create_inference_v3_deployment_deployments_inference_v3_post(create_inference_v3_deployment_request)
        print("The response of EXTERNALApi->create_inference_v3_deployment_deployments_inference_v3_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_inference_v3_deployment_deployments_inference_v3_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inference_v3_deployment_request** | [**CreateInferenceV3DeploymentRequest**](CreateInferenceV3DeploymentRequest.md)|  | 

### Return type

[**CreateInferenceDeploymentResponse**](CreateInferenceDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_organization_organizations_post**
> CreateOrganizationResponse create_new_organization_organizations_post(create_organization_request)

Create New Organization

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_organization_request import CreateOrganizationRequest
from platform_api_python_client.models.create_organization_response import CreateOrganizationResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_organization_request = platform_api_python_client.CreateOrganizationRequest() # CreateOrganizationRequest | 

    try:
        # Create New Organization
        api_response = api_instance.create_new_organization_organizations_post(create_organization_request)
        print("The response of EXTERNALApi->create_new_organization_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_new_organization_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_request** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | 

### Return type

[**CreateOrganizationResponse**](CreateOrganizationResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rag_deployment_deployments_rag_post**
> CreateRagDeploymentResponse create_rag_deployment_deployments_rag_post(create_rag_deployment_request)

Create Rag Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_rag_deployment_request import CreateRagDeploymentRequest
from platform_api_python_client.models.create_rag_deployment_response import CreateRagDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_rag_deployment_request = platform_api_python_client.CreateRagDeploymentRequest() # CreateRagDeploymentRequest | 

    try:
        # Create Rag Deployment
        api_response = api_instance.create_rag_deployment_deployments_rag_post(create_rag_deployment_request)
        print("The response of EXTERNALApi->create_rag_deployment_deployments_rag_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_rag_deployment_deployments_rag_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rag_deployment_request** | [**CreateRagDeploymentRequest**](CreateRagDeploymentRequest.md)|  | 

### Return type

[**CreateRagDeploymentResponse**](CreateRagDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key_credentials_api_key_id_delete**
> object delete_api_key_credentials_api_key_id_delete(id)

Delete Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Api Key
        api_response = api_instance.delete_api_key_credentials_api_key_id_delete(id)
        print("The response of EXTERNALApi->delete_api_key_credentials_api_key_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->delete_api_key_credentials_api_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_vault_item_endpoint_user_vault_delete**
> object delete_user_vault_item_endpoint_user_vault_delete(user_vault_item)

Delete User Vault Item Endpoint

Delete an item of a specific type for the user.

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.user_vault_item import UserVaultItem
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    user_vault_item = platform_api_python_client.UserVaultItem() # UserVaultItem | 

    try:
        # Delete User Vault Item Endpoint
        api_response = api_instance.delete_user_vault_item_endpoint_user_vault_delete(user_vault_item)
        print("The response of EXTERNALApi->delete_user_vault_item_endpoint_user_vault_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->delete_user_vault_item_endpoint_user_vault_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_vault_item** | [**UserVaultItem**](UserVaultItem.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_url_file_url_download_post**
> CreateUrlResponse download_url_file_url_download_post(create_url_request)

Download Url

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_url_request import CreateUrlRequest
from platform_api_python_client.models.create_url_response import CreateUrlResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_url_request = platform_api_python_client.CreateUrlRequest() # CreateUrlRequest | 

    try:
        # Download Url
        api_response = api_instance.download_url_file_url_download_post(create_url_request)
        print("The response of EXTERNALApi->download_url_file_url_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->download_url_file_url_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_url_request** | [**CreateUrlRequest**](CreateUrlRequest.md)|  | 

### Return type

[**CreateUrlResponse**](CreateUrlResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_vault_items_endpoint_user_vault_get**
> ListUserVaultItemsResponse get_all_user_vault_items_endpoint_user_vault_get(type=type, search_query=search_query)

Get All User Vault Items Endpoint

Retrieve all items of a specific type for the user.

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_user_vault_items_response import ListUserVaultItemsResponse
from platform_api_python_client.models.user_vault_type import UserVaultType
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    type = platform_api_python_client.UserVaultType() # UserVaultType |  (optional)
    search_query = 'search_query_example' # str |  (optional)

    try:
        # Get All User Vault Items Endpoint
        api_response = api_instance.get_all_user_vault_items_endpoint_user_vault_get(type=type, search_query=search_query)
        print("The response of EXTERNALApi->get_all_user_vault_items_endpoint_user_vault_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_all_user_vault_items_endpoint_user_vault_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**UserVaultType**](.md)|  | [optional] 
 **search_query** | **str**|  | [optional] 

### Return type

[**ListUserVaultItemsResponse**](ListUserVaultItemsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys_credentials_api_key_get**
> ListAPIKeyResponse get_api_keys_credentials_api_key_get()

Get Api Keys

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_api_key_response import ListAPIKeyResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)

    try:
        # Get Api Keys
        api_response = api_instance.get_api_keys_credentials_api_key_get()
        print("The response of EXTERNALApi->get_api_keys_credentials_api_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_api_keys_credentials_api_key_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAPIKeyResponse**](ListAPIKeyResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_clusters_get**
> ListGetClusterResponse get_clusters_clusters_get()

Get Clusters

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_get_cluster_response import ListGetClusterResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)

    try:
        # Get Clusters
        api_response = api_instance.get_clusters_clusters_get()
        print("The response of EXTERNALApi->get_clusters_clusters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_clusters_clusters_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListGetClusterResponse**](ListGetClusterResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compute_deployment_deployments_compute_deployment_id_get**
> GetComputeDeploymentResponse get_compute_deployment_deployments_compute_deployment_id_get(deployment_id)

Get Compute Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_compute_deployment_response import GetComputeDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Compute Deployment
        api_response = api_instance.get_compute_deployment_deployments_compute_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_compute_deployment_deployments_compute_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_compute_deployment_deployments_compute_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetComputeDeploymentResponse**](GetComputeDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credits_credits_get**
> CreditsResponse get_credits_credits_get()

Get Credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.credits_response import CreditsResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)

    try:
        # Get Credits
        api_response = api_instance.get_credits_credits_get()
        print("The response of EXTERNALApi->get_credits_credits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_credits_credits_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreditsResponse**](CreditsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cserve_recipe_deployments_cserve_recipes_get**
> ListCServeRecipeResponse get_cserve_recipe_deployments_cserve_recipes_get(model=model, hf_token=hf_token)

Get Cserve Recipe

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_c_serve_recipe_response import ListCServeRecipeResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    model = 'model_example' # str |  (optional)
    hf_token = 'hf_token_example' # str |  (optional)

    try:
        # Get Cserve Recipe
        api_response = api_instance.get_cserve_recipe_deployments_cserve_recipes_get(model=model, hf_token=hf_token)
        print("The response of EXTERNALApi->get_cserve_recipe_deployments_cserve_recipes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_cserve_recipe_deployments_cserve_recipes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | [optional] 
 **hf_token** | **str**|  | [optional] 

### Return type

[**ListCServeRecipeResponse**](ListCServeRecipeResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get**
> GetCServeV2DeploymentResponse get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get(deployment_id)

Get Cserve V2 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_c_serve_v2_deployment_response import GetCServeV2DeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Cserve V2 Deployment
        api_response = api_instance.get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_cserve_v2_deployment_deployments_cserve_v2_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetCServeV2DeploymentResponse**](GetCServeV2DeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get**
> GetCServeV3DeploymentResponse get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get(deployment_id)

Get Cserve V3 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_c_serve_v3_deployment_response import GetCServeV3DeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Cserve V3 Deployment
        api_response = api_instance.get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_cserve_v3_deployment_deployments_cserve_v3_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetCServeV3DeploymentResponse**](GetCServeV3DeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_logs_deployments_logs_deployment_id_get**
> GetDeploymentLogResponse get_deployment_logs_deployments_logs_deployment_id_get(deployment_id, start_time, end_time, next_page_token=next_page_token, start_from_head=start_from_head, line_count=line_count)

Get Deployment Logs

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_deployment_log_response import GetDeploymentLogResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    start_time = 56 # int | 
    end_time = 56 # int | 
    next_page_token = 'next_page_token_example' # str |  (optional)
    start_from_head = True # bool |  (optional) (default to True)
    line_count = 56 # int |  (optional)

    try:
        # Get Deployment Logs
        api_response = api_instance.get_deployment_logs_deployments_logs_deployment_id_get(deployment_id, start_time, end_time, next_page_token=next_page_token, start_from_head=start_from_head, line_count=line_count)
        print("The response of EXTERNALApi->get_deployment_logs_deployments_logs_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployment_logs_deployments_logs_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **next_page_token** | **str**|  | [optional] 
 **start_from_head** | **bool**|  | [optional] [default to True]
 **line_count** | **int**|  | [optional] 

### Return type

[**GetDeploymentLogResponse**](GetDeploymentLogResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_logs_v3_deployments_logs_v3_deployment_id_revision_number_get**
> GetDeploymentLogResponse get_deployment_logs_v3_deployments_logs_v3_deployment_id_revision_number_get(deployment_id, revision_number, start_time, end_time, next_page_token=next_page_token, start_from_head=start_from_head, line_count=line_count)

Get Deployment Logs V3

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_deployment_log_response import GetDeploymentLogResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    revision_number = 56 # int | 
    start_time = 56 # int | 
    end_time = 56 # int | 
    next_page_token = 'next_page_token_example' # str |  (optional)
    start_from_head = True # bool |  (optional) (default to True)
    line_count = 56 # int |  (optional)

    try:
        # Get Deployment Logs V3
        api_response = api_instance.get_deployment_logs_v3_deployments_logs_v3_deployment_id_revision_number_get(deployment_id, revision_number, start_time, end_time, next_page_token=next_page_token, start_from_head=start_from_head, line_count=line_count)
        print("The response of EXTERNALApi->get_deployment_logs_v3_deployments_logs_v3_deployment_id_revision_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployment_logs_v3_deployments_logs_v3_deployment_id_revision_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **revision_number** | **int**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **next_page_token** | **str**|  | [optional] 
 **start_from_head** | **bool**|  | [optional] [default to True]
 **line_count** | **int**|  | [optional] 

### Return type

[**GetDeploymentLogResponse**](GetDeploymentLogResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_revision_deployments_revisions_deployment_id_revision_number_get**
> GetDeploymentRevisionResponse get_deployment_revision_deployments_revisions_deployment_id_revision_number_get(deployment_id, revision_number)

Get Deployment Revision

Get a specific revision for a deployment.

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_deployment_revision_response import GetDeploymentRevisionResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    revision_number = 56 # int | 

    try:
        # Get Deployment Revision
        api_response = api_instance.get_deployment_revision_deployments_revisions_deployment_id_revision_number_get(deployment_id, revision_number)
        print("The response of EXTERNALApi->get_deployment_revision_deployments_revisions_deployment_id_revision_number_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployment_revision_deployments_revisions_deployment_id_revision_number_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **revision_number** | **int**|  | 

### Return type

[**GetDeploymentRevisionResponse**](GetDeploymentRevisionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_revisions_deployments_revisions_deployment_id_get**
> ListDeploymentRevisionsResponse get_deployment_revisions_deployments_revisions_deployment_id_get(deployment_id)

Get Deployment Revisions

List all revisions for a deployment.

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_deployment_revisions_response import ListDeploymentRevisionsResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Deployment Revisions
        api_response = api_instance.get_deployment_revisions_deployments_revisions_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_deployment_revisions_deployments_revisions_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployment_revisions_deployments_revisions_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**ListDeploymentRevisionsResponse**](ListDeploymentRevisionsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_status_deployments_status_deployment_id_get**
> DeploymentStatusResponse get_deployment_status_deployments_status_deployment_id_get(deployment_id)

Get Deployment Status

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_status_response import DeploymentStatusResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Deployment Status
        api_response = api_instance.get_deployment_status_deployments_status_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_deployment_status_deployments_status_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployment_status_deployments_status_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**DeploymentStatusResponse**](DeploymentStatusResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_status_v3_deployments_status_v3_deployment_id_get**
> DeploymentStatusV3Response get_deployment_status_v3_deployments_status_v3_deployment_id_get(deployment_id)

Get Deployment Status V3

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_status_v3_response import DeploymentStatusV3Response
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Deployment Status V3
        api_response = api_instance.get_deployment_status_v3_deployments_status_v3_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_deployment_status_v3_deployments_status_v3_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployment_status_v3_deployments_status_v3_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**DeploymentStatusV3Response**](DeploymentStatusV3Response.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_deployments_get**
> ListGetDeploymentResponse get_deployments_deployments_get(offset=offset, limit=limit, type=type, search_query=search_query)

Get Deployments

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_type import DeploymentType
from platform_api_python_client.models.list_get_deployment_response import ListGetDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    type = platform_api_python_client.DeploymentType() # DeploymentType |  (optional)
    search_query = 'search_query_example' # str |  (optional)

    try:
        # Get Deployments
        api_response = api_instance.get_deployments_deployments_get(offset=offset, limit=limit, type=type, search_query=search_query)
        print("The response of EXTERNALApi->get_deployments_deployments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployments_deployments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **type** | [**DeploymentType**](.md)|  | [optional] 
 **search_query** | **str**|  | [optional] 

### Return type

[**ListGetDeploymentResponse**](ListGetDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_instances_hardware_instances_get**
> ListHardwareInstanceResponse get_hardware_instances_hardware_instances_get(cluster_id=cluster_id)

Get Hardware Instances

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_hardware_instance_response import ListHardwareInstanceResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    cluster_id = 56 # int |  (optional)

    try:
        # Get Hardware Instances
        api_response = api_instance.get_hardware_instances_hardware_instances_get(cluster_id=cluster_id)
        print("The response of EXTERNALApi->get_hardware_instances_hardware_instances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_hardware_instances_hardware_instances_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | [optional] 

### Return type

[**ListHardwareInstanceResponse**](ListHardwareInstanceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inference_deployment_deployments_inference_deployment_id_get**
> GetInferenceDeploymentResponse get_inference_deployment_deployments_inference_deployment_id_get(deployment_id)

Get Inference Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_inference_deployment_response import GetInferenceDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Inference Deployment
        api_response = api_instance.get_inference_deployment_deployments_inference_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_inference_deployment_deployments_inference_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_inference_deployment_deployments_inference_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetInferenceDeploymentResponse**](GetInferenceDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inference_v3_deployment_deployments_inference_v3_deployment_id_get**
> GetInferenceV3DeploymentResponse get_inference_v3_deployment_deployments_inference_v3_deployment_id_get(deployment_id)

Get Inference V3 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_inference_v3_deployment_response import GetInferenceV3DeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Inference V3 Deployment
        api_response = api_instance.get_inference_v3_deployment_deployments_inference_v3_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_inference_v3_deployment_deployments_inference_v3_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_inference_v3_deployment_deployments_inference_v3_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetInferenceV3DeploymentResponse**](GetInferenceV3DeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prebuilt_images_prebuilt_images_get**
> ListPrebuiltImageResponse get_prebuilt_images_prebuilt_images_get(type=type)

Get Prebuilt Images

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_type import DeploymentType
from platform_api_python_client.models.list_prebuilt_image_response import ListPrebuiltImageResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    type = platform_api_python_client.DeploymentType() # DeploymentType |  (optional)

    try:
        # Get Prebuilt Images
        api_response = api_instance.get_prebuilt_images_prebuilt_images_get(type=type)
        print("The response of EXTERNALApi->get_prebuilt_images_prebuilt_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_prebuilt_images_prebuilt_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**DeploymentType**](.md)|  | [optional] 

### Return type

[**ListPrebuiltImageResponse**](ListPrebuiltImageResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rag_deployment_deployments_rag_deployment_id_get**
> GetRagDeploymentResponse get_rag_deployment_deployments_rag_deployment_id_get(deployment_id)

Get Rag Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_rag_deployment_response import GetRagDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Rag Deployment
        api_response = api_instance.get_rag_deployment_deployments_rag_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_rag_deployment_deployments_rag_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_rag_deployment_deployments_rag_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetRagDeploymentResponse**](GetRagDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_daily_bills_get**
> ListDailyBillResponse get_usage_daily_bills_get(start_date, end_date)

Get Usage

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_daily_bill_response import ListDailyBillResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    start_date = '2013-10-20' # date | 
    end_date = '2013-10-20' # date | 

    try:
        # Get Usage
        api_response = api_instance.get_usage_daily_bills_get(start_date, end_date)
        print("The response of EXTERNALApi->get_usage_daily_bills_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_usage_daily_bills_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | 
 **end_date** | **date**|  | 

### Return type

[**ListDailyBillResponse**](ListDailyBillResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_deployments_usage_deployment_id_get**
> GetDeploymentUsageResponse get_usage_deployments_usage_deployment_id_get(deployment_id, metric, start_time_in_seconds, end_time_in_seconds, step=step)

Get Usage

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_deployment_usage_response import GetDeploymentUsageResponse
from platform_api_python_client.models.metric import Metric
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    metric = platform_api_python_client.Metric() # Metric | 
    start_time_in_seconds = 56 # int | 
    end_time_in_seconds = 56 # int | 
    step = 15 # int |  (optional) (default to 15)

    try:
        # Get Usage
        api_response = api_instance.get_usage_deployments_usage_deployment_id_get(deployment_id, metric, start_time_in_seconds, end_time_in_seconds, step=step)
        print("The response of EXTERNALApi->get_usage_deployments_usage_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_usage_deployments_usage_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **metric** | [**Metric**](.md)|  | 
 **start_time_in_seconds** | **int**|  | 
 **end_time_in_seconds** | **int**|  | 
 **step** | **int**|  | [optional] [default to 15]

### Return type

[**GetDeploymentUsageResponse**](GetDeploymentUsageResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollout_existing_revision_deployments_revisions_deployment_id_revision_number_put**
> UpdateDeploymentResponse rollout_existing_revision_deployments_revisions_deployment_id_revision_number_put(deployment_id, revision_number, rollout_strategy_params=rollout_strategy_params)

Rollout Existing Revision

Change the selected revision for a deployment and apply the changes.

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.rollout_strategy_params import RolloutStrategyParams
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    revision_number = 56 # int | 
    rollout_strategy_params = platform_api_python_client.RolloutStrategyParams() # RolloutStrategyParams |  (optional)

    try:
        # Rollout Existing Revision
        api_response = api_instance.rollout_existing_revision_deployments_revisions_deployment_id_revision_number_put(deployment_id, revision_number, rollout_strategy_params=rollout_strategy_params)
        print("The response of EXTERNALApi->rollout_existing_revision_deployments_revisions_deployment_id_revision_number_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->rollout_existing_revision_deployments_revisions_deployment_id_revision_number_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **revision_number** | **int**|  | 
 **rollout_strategy_params** | [**RolloutStrategyParams**](RolloutStrategyParams.md)|  | [optional] 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setup_stripe_customer_payments_setup_post**
> object setup_stripe_customer_payments_setup_post()

Setup Stripe Customer

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)

    try:
        # Setup Stripe Customer
        api_response = api_instance.setup_stripe_customer_payments_setup_post()
        print("The response of EXTERNALApi->setup_stripe_customer_payments_setup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->setup_stripe_customer_payments_setup_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compute_deployment_deployments_compute_put**
> UpdateDeploymentResponse update_compute_deployment_deployments_compute_put(deployment_id, create_compute_deployment_request)

Update Compute Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_compute_deployment_request import CreateComputeDeploymentRequest
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    create_compute_deployment_request = platform_api_python_client.CreateComputeDeploymentRequest() # CreateComputeDeploymentRequest | 

    try:
        # Update Compute Deployment
        api_response = api_instance.update_compute_deployment_deployments_compute_put(deployment_id, create_compute_deployment_request)
        print("The response of EXTERNALApi->update_compute_deployment_deployments_compute_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_compute_deployment_deployments_compute_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **create_compute_deployment_request** | [**CreateComputeDeploymentRequest**](CreateComputeDeploymentRequest.md)|  | 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cserve_v2_deployment_deployments_cserve_v2_put**
> UpdateDeploymentResponse update_cserve_v2_deployment_deployments_cserve_v2_put(deployment_id, create_c_serve_v2_deployment_request)

Update Cserve V2 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_c_serve_v2_deployment_request import CreateCServeV2DeploymentRequest
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    create_c_serve_v2_deployment_request = platform_api_python_client.CreateCServeV2DeploymentRequest() # CreateCServeV2DeploymentRequest | 

    try:
        # Update Cserve V2 Deployment
        api_response = api_instance.update_cserve_v2_deployment_deployments_cserve_v2_put(deployment_id, create_c_serve_v2_deployment_request)
        print("The response of EXTERNALApi->update_cserve_v2_deployment_deployments_cserve_v2_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_cserve_v2_deployment_deployments_cserve_v2_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **create_c_serve_v2_deployment_request** | [**CreateCServeV2DeploymentRequest**](CreateCServeV2DeploymentRequest.md)|  | 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cserve_v3_deployment_deployments_cserve_v3_put**
> UpdateDeploymentResponse update_cserve_v3_deployment_deployments_cserve_v3_put(deployment_id, create_c_serve_v3_deployment_request)

Update Cserve V3 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_c_serve_v3_deployment_request import CreateCServeV3DeploymentRequest
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    create_c_serve_v3_deployment_request = platform_api_python_client.CreateCServeV3DeploymentRequest() # CreateCServeV3DeploymentRequest | 

    try:
        # Update Cserve V3 Deployment
        api_response = api_instance.update_cserve_v3_deployment_deployments_cserve_v3_put(deployment_id, create_c_serve_v3_deployment_request)
        print("The response of EXTERNALApi->update_cserve_v3_deployment_deployments_cserve_v3_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_cserve_v3_deployment_deployments_cserve_v3_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **create_c_serve_v3_deployment_request** | [**CreateCServeV3DeploymentRequest**](CreateCServeV3DeploymentRequest.md)|  | 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment_status_deployments_status_deployment_id_put**
> DeploymentStatusResponse update_deployment_status_deployments_status_deployment_id_put(deployment_id, deployment_status_request)

Update Deployment Status

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_status_request import DeploymentStatusRequest
from platform_api_python_client.models.deployment_status_response import DeploymentStatusResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    deployment_status_request = platform_api_python_client.DeploymentStatusRequest() # DeploymentStatusRequest | 

    try:
        # Update Deployment Status
        api_response = api_instance.update_deployment_status_deployments_status_deployment_id_put(deployment_id, deployment_status_request)
        print("The response of EXTERNALApi->update_deployment_status_deployments_status_deployment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_deployment_status_deployments_status_deployment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **deployment_status_request** | [**DeploymentStatusRequest**](DeploymentStatusRequest.md)|  | 

### Return type

[**DeploymentStatusResponse**](DeploymentStatusResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment_status_v3_deployments_status_v3_deployment_id_put**
> DeploymentStatusV3Response update_deployment_status_v3_deployments_status_v3_deployment_id_put(deployment_id, update_deployment_status_v3_request)

Update Deployment Status V3

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_status_v3_response import DeploymentStatusV3Response
from platform_api_python_client.models.update_deployment_status_v3_request import UpdateDeploymentStatusV3Request
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    update_deployment_status_v3_request = platform_api_python_client.UpdateDeploymentStatusV3Request() # UpdateDeploymentStatusV3Request | 

    try:
        # Update Deployment Status V3
        api_response = api_instance.update_deployment_status_v3_deployments_status_v3_deployment_id_put(deployment_id, update_deployment_status_v3_request)
        print("The response of EXTERNALApi->update_deployment_status_v3_deployments_status_v3_deployment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_deployment_status_v3_deployments_status_v3_deployment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **update_deployment_status_v3_request** | [**UpdateDeploymentStatusV3Request**](UpdateDeploymentStatusV3Request.md)|  | 

### Return type

[**DeploymentStatusV3Response**](DeploymentStatusV3Response.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inference_deployment_deployments_inference_put**
> UpdateDeploymentResponse update_inference_deployment_deployments_inference_put(deployment_id, create_inference_deployment_request)

Update Inference Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_inference_deployment_request import CreateInferenceDeploymentRequest
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    create_inference_deployment_request = platform_api_python_client.CreateInferenceDeploymentRequest() # CreateInferenceDeploymentRequest | 

    try:
        # Update Inference Deployment
        api_response = api_instance.update_inference_deployment_deployments_inference_put(deployment_id, create_inference_deployment_request)
        print("The response of EXTERNALApi->update_inference_deployment_deployments_inference_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_inference_deployment_deployments_inference_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **create_inference_deployment_request** | [**CreateInferenceDeploymentRequest**](CreateInferenceDeploymentRequest.md)|  | 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inference_v3_deployment_deployments_inference_v3_put**
> UpdateDeploymentResponse update_inference_v3_deployment_deployments_inference_v3_put(deployment_id, create_inference_v3_deployment_request)

Update Inference V3 Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_inference_v3_deployment_request import CreateInferenceV3DeploymentRequest
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    create_inference_v3_deployment_request = platform_api_python_client.CreateInferenceV3DeploymentRequest() # CreateInferenceV3DeploymentRequest | 

    try:
        # Update Inference V3 Deployment
        api_response = api_instance.update_inference_v3_deployment_deployments_inference_v3_put(deployment_id, create_inference_v3_deployment_request)
        print("The response of EXTERNALApi->update_inference_v3_deployment_deployments_inference_v3_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_inference_v3_deployment_deployments_inference_v3_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **create_inference_v3_deployment_request** | [**CreateInferenceV3DeploymentRequest**](CreateInferenceV3DeploymentRequest.md)|  | 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rag_deployment_deployments_rag_put**
> UpdateDeploymentResponse update_rag_deployment_deployments_rag_put(deployment_id, create_rag_deployment_request)

Update Rag Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_rag_deployment_request import CreateRagDeploymentRequest
from platform_api_python_client.models.update_deployment_response import UpdateDeploymentResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    create_rag_deployment_request = platform_api_python_client.CreateRagDeploymentRequest() # CreateRagDeploymentRequest | 

    try:
        # Update Rag Deployment
        api_response = api_instance.update_rag_deployment_deployments_rag_put(deployment_id, create_rag_deployment_request)
        print("The response of EXTERNALApi->update_rag_deployment_deployments_rag_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_rag_deployment_deployments_rag_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **create_rag_deployment_request** | [**CreateRagDeploymentRequest**](CreateRagDeploymentRequest.md)|  | 

### Return type

[**UpdateDeploymentResponse**](UpdateDeploymentResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_vault_item_endpoint_user_vault_put**
> object update_user_vault_item_endpoint_user_vault_put(user_vault_item)

Update User Vault Item Endpoint

Update or add multiple items of a specific type for the user.

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.user_vault_item import UserVaultItem
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    user_vault_item = platform_api_python_client.UserVaultItem() # UserVaultItem | 

    try:
        # Update User Vault Item Endpoint
        api_response = api_instance.update_user_vault_item_endpoint_user_vault_put(user_vault_item)
        print("The response of EXTERNALApi->update_user_vault_item_endpoint_user_vault_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_user_vault_item_endpoint_user_vault_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_vault_item** | [**UserVaultItem**](UserVaultItem.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_url_file_url_upload_post**
> CreateUrlResponse upload_url_file_url_upload_post(create_url_request)

Upload Url

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_url_request import CreateUrlRequest
from platform_api_python_client.models.create_url_response import CreateUrlResponse
from platform_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_python_client.EXTERNALApi(api_client)
    create_url_request = platform_api_python_client.CreateUrlRequest() # CreateUrlRequest | 

    try:
        # Upload Url
        api_response = api_instance.upload_url_file_url_upload_post(create_url_request)
        print("The response of EXTERNALApi->upload_url_file_url_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->upload_url_file_url_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_url_request** | [**CreateUrlRequest**](CreateUrlRequest.md)|  | 

### Return type

[**CreateUrlResponse**](CreateUrlResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

