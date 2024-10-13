# platform_api_python_client.EXTERNALApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_feedback_request_support_feedback_post**](EXTERNALApi.md#add_feedback_request_support_feedback_post) | **POST** /support/feedback | Add Feedback Request
[**create_api_key_credentials_api_key_post**](EXTERNALApi.md#create_api_key_credentials_api_key_post) | **POST** /credentials/api-key | Create Api Key
[**create_compute_deployment_deployments_v2_compute_post**](EXTERNALApi.md#create_compute_deployment_deployments_v2_compute_post) | **POST** /deployments/v2/compute | Create Compute Deployment
[**create_cserve_deployment_deployments_v2_cserve_post**](EXTERNALApi.md#create_cserve_deployment_deployments_v2_cserve_post) | **POST** /deployments/v2/cserve | Create Cserve Deployment
[**create_hardware_request_support_hardware_request_post**](EXTERNALApi.md#create_hardware_request_support_hardware_request_post) | **POST** /support/hardware-request | Create Hardware Request
[**create_inference_deployment_deployments_v2_inference_post**](EXTERNALApi.md#create_inference_deployment_deployments_v2_inference_post) | **POST** /deployments/v2/inference | Create Inference Deployment
[**create_payment_payments_post**](EXTERNALApi.md#create_payment_payments_post) | **POST** /payments | Create Payment
[**create_payment_setup_payments_setup_post**](EXTERNALApi.md#create_payment_setup_payments_setup_post) | **POST** /payments/setup | Create Payment Setup
[**delete_api_key_credentials_api_key_id_delete**](EXTERNALApi.md#delete_api_key_credentials_api_key_id_delete) | **DELETE** /credentials/api-key/{id} | Delete Api Key
[**delete_payment_method_payments_methods_payment_method_delete**](EXTERNALApi.md#delete_payment_method_payments_methods_payment_method_delete) | **DELETE** /payments/methods/{payment_method} | Delete Payment Method
[**get_api_keys_credentials_api_key_get**](EXTERNALApi.md#get_api_keys_credentials_api_key_get) | **GET** /credentials/api-key | Get Api Keys
[**get_clusters_clusters_get**](EXTERNALApi.md#get_clusters_clusters_get) | **GET** /clusters | Get Clusters
[**get_compute_deployment_deployments_v2_compute_deployment_id_get**](EXTERNALApi.md#get_compute_deployment_deployments_v2_compute_deployment_id_get) | **GET** /deployments/v2/compute/{deployment_id} | Get Compute Deployment
[**get_credits_credits_get**](EXTERNALApi.md#get_credits_credits_get) | **GET** /credits | Get Credits
[**get_cserve_deployment_deployments_v2_cserve_deployment_id_get**](EXTERNALApi.md#get_cserve_deployment_deployments_v2_cserve_deployment_id_get) | **GET** /deployments/v2/cserve/{deployment_id} | Get Cserve Deployment
[**get_cserve_recipe_deployments_v2_cserve_recipes_get**](EXTERNALApi.md#get_cserve_recipe_deployments_v2_cserve_recipes_get) | **GET** /deployments/v2/cserve/recipes | Get Cserve Recipe
[**get_deployment_logs_deployments_logs_deployment_id_get**](EXTERNALApi.md#get_deployment_logs_deployments_logs_deployment_id_get) | **GET** /deployments/logs/{deployment_id} | Get Deployment Logs
[**get_deployment_status_deployments_v2_status_deployment_id_get**](EXTERNALApi.md#get_deployment_status_deployments_v2_status_deployment_id_get) | **GET** /deployments/v2/status/{deployment_id} | Get Deployment Status
[**get_deployments_deployments_v2_get**](EXTERNALApi.md#get_deployments_deployments_v2_get) | **GET** /deployments/v2 | Get Deployments
[**get_hardware_instances_hardware_instances_get**](EXTERNALApi.md#get_hardware_instances_hardware_instances_get) | **GET** /hardware-instances | Get Hardware Instances
[**get_hardware_instances_hardware_instances_v2_get**](EXTERNALApi.md#get_hardware_instances_hardware_instances_v2_get) | **GET** /hardware-instances/v2 | Get Hardware Instances
[**get_inference_deployment_deployments_v2_inference_deployment_id_get**](EXTERNALApi.md#get_inference_deployment_deployments_v2_inference_deployment_id_get) | **GET** /deployments/v2/inference/{deployment_id} | Get Inference Deployment
[**get_payment_methods_payments_methods_get**](EXTERNALApi.md#get_payment_methods_payments_methods_get) | **GET** /payments/methods | Get Payment Methods
[**get_prebuilt_images_prebuilt_images_get**](EXTERNALApi.md#get_prebuilt_images_prebuilt_images_get) | **GET** /prebuilt-images | Get Prebuilt Images
[**get_usage_daily_bills_get**](EXTERNALApi.md#get_usage_daily_bills_get) | **GET** /daily_bills | Get Usage
[**get_usage_deployments_usage_deployment_id_get**](EXTERNALApi.md#get_usage_deployments_usage_deployment_id_get) | **GET** /deployments/usage/{deployment_id} | Get Usage
[**update_deployment_status_deployments_v2_status_deployment_id_put**](EXTERNALApi.md#update_deployment_status_deployments_v2_status_deployment_id_put) | **PUT** /deployments/v2/status/{deployment_id} | Update Deployment Status


# **add_feedback_request_support_feedback_post**
> object add_feedback_request_support_feedback_post(feedback_request)

Add Feedback Request

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.feedback_request import FeedbackRequest
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
    feedback_request = platform_api_python_client.FeedbackRequest() # FeedbackRequest | 

    try:
        # Add Feedback Request
        api_response = api_instance.add_feedback_request_support_feedback_post(feedback_request)
        print("The response of EXTERNALApi->add_feedback_request_support_feedback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->add_feedback_request_support_feedback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_request** | [**FeedbackRequest**](FeedbackRequest.md)|  | 

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

# **create_compute_deployment_deployments_v2_compute_post**
> CreateComputeDeploymentResponse create_compute_deployment_deployments_v2_compute_post(create_compute_deployment_v2_request)

Create Compute Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_compute_deployment_response import CreateComputeDeploymentResponse
from platform_api_python_client.models.create_compute_deployment_v2_request import CreateComputeDeploymentV2Request
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
    create_compute_deployment_v2_request = platform_api_python_client.CreateComputeDeploymentV2Request() # CreateComputeDeploymentV2Request | 

    try:
        # Create Compute Deployment
        api_response = api_instance.create_compute_deployment_deployments_v2_compute_post(create_compute_deployment_v2_request)
        print("The response of EXTERNALApi->create_compute_deployment_deployments_v2_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_compute_deployment_deployments_v2_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_compute_deployment_v2_request** | [**CreateComputeDeploymentV2Request**](CreateComputeDeploymentV2Request.md)|  | 

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

# **create_cserve_deployment_deployments_v2_cserve_post**
> CreateCServeDeploymentResponse create_cserve_deployment_deployments_v2_cserve_post(create_c_serve_deployment_request)

Create Cserve Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_c_serve_deployment_request import CreateCServeDeploymentRequest
from platform_api_python_client.models.create_c_serve_deployment_response import CreateCServeDeploymentResponse
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
    create_c_serve_deployment_request = platform_api_python_client.CreateCServeDeploymentRequest() # CreateCServeDeploymentRequest | 

    try:
        # Create Cserve Deployment
        api_response = api_instance.create_cserve_deployment_deployments_v2_cserve_post(create_c_serve_deployment_request)
        print("The response of EXTERNALApi->create_cserve_deployment_deployments_v2_cserve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_cserve_deployment_deployments_v2_cserve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_c_serve_deployment_request** | [**CreateCServeDeploymentRequest**](CreateCServeDeploymentRequest.md)|  | 

### Return type

[**CreateCServeDeploymentResponse**](CreateCServeDeploymentResponse.md)

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

# **create_hardware_request_support_hardware_request_post**
> object create_hardware_request_support_hardware_request_post(add_hardware_request)

Create Hardware Request

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.add_hardware_request import AddHardwareRequest
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
    add_hardware_request = platform_api_python_client.AddHardwareRequest() # AddHardwareRequest | 

    try:
        # Create Hardware Request
        api_response = api_instance.create_hardware_request_support_hardware_request_post(add_hardware_request)
        print("The response of EXTERNALApi->create_hardware_request_support_hardware_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_hardware_request_support_hardware_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_hardware_request** | [**AddHardwareRequest**](AddHardwareRequest.md)|  | 

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

# **create_inference_deployment_deployments_v2_inference_post**
> CreateInferenceDeploymentResponse create_inference_deployment_deployments_v2_inference_post(create_inference_deployment_v2_request)

Create Inference Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.create_inference_deployment_response import CreateInferenceDeploymentResponse
from platform_api_python_client.models.create_inference_deployment_v2_request import CreateInferenceDeploymentV2Request
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
    create_inference_deployment_v2_request = platform_api_python_client.CreateInferenceDeploymentV2Request() # CreateInferenceDeploymentV2Request | 

    try:
        # Create Inference Deployment
        api_response = api_instance.create_inference_deployment_deployments_v2_inference_post(create_inference_deployment_v2_request)
        print("The response of EXTERNALApi->create_inference_deployment_deployments_v2_inference_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_inference_deployment_deployments_v2_inference_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_inference_deployment_v2_request** | [**CreateInferenceDeploymentV2Request**](CreateInferenceDeploymentV2Request.md)|  | 

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

# **create_payment_payments_post**
> ClientSecretResponse create_payment_payments_post(create_payment_request)

Create Payment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.client_secret_response import ClientSecretResponse
from platform_api_python_client.models.create_payment_request import CreatePaymentRequest
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
    create_payment_request = platform_api_python_client.CreatePaymentRequest() # CreatePaymentRequest | 

    try:
        # Create Payment
        api_response = api_instance.create_payment_payments_post(create_payment_request)
        print("The response of EXTERNALApi->create_payment_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_payment_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_request** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | 

### Return type

[**ClientSecretResponse**](ClientSecretResponse.md)

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

# **create_payment_setup_payments_setup_post**
> ClientSecretResponse create_payment_setup_payments_setup_post()

Create Payment Setup

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.client_secret_response import ClientSecretResponse
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
        # Create Payment Setup
        api_response = api_instance.create_payment_setup_payments_setup_post()
        print("The response of EXTERNALApi->create_payment_setup_payments_setup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_payment_setup_payments_setup_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClientSecretResponse**](ClientSecretResponse.md)

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

# **delete_payment_method_payments_methods_payment_method_delete**
> object delete_payment_method_payments_methods_payment_method_delete(payment_method)

Delete Payment Method

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
    payment_method = 'payment_method_example' # str | 

    try:
        # Delete Payment Method
        api_response = api_instance.delete_payment_method_payments_methods_payment_method_delete(payment_method)
        print("The response of EXTERNALApi->delete_payment_method_payments_methods_payment_method_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->delete_payment_method_payments_methods_payment_method_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method** | **str**|  | 

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

# **get_compute_deployment_deployments_v2_compute_deployment_id_get**
> GetComputeV2DeploymentResponse get_compute_deployment_deployments_v2_compute_deployment_id_get(deployment_id)

Get Compute Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_compute_v2_deployment_response import GetComputeV2DeploymentResponse
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
        api_response = api_instance.get_compute_deployment_deployments_v2_compute_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_compute_deployment_deployments_v2_compute_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_compute_deployment_deployments_v2_compute_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetComputeV2DeploymentResponse**](GetComputeV2DeploymentResponse.md)

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

# **get_cserve_deployment_deployments_v2_cserve_deployment_id_get**
> GetCServeDeploymentResponse get_cserve_deployment_deployments_v2_cserve_deployment_id_get(deployment_id)

Get Cserve Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_c_serve_deployment_response import GetCServeDeploymentResponse
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
        # Get Cserve Deployment
        api_response = api_instance.get_cserve_deployment_deployments_v2_cserve_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_cserve_deployment_deployments_v2_cserve_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_cserve_deployment_deployments_v2_cserve_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetCServeDeploymentResponse**](GetCServeDeploymentResponse.md)

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

# **get_cserve_recipe_deployments_v2_cserve_recipes_get**
> ListCServeRecipeResponse get_cserve_recipe_deployments_v2_cserve_recipes_get(model=model, cluster_id=cluster_id)

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
    cluster_id = 56 # int |  (optional)

    try:
        # Get Cserve Recipe
        api_response = api_instance.get_cserve_recipe_deployments_v2_cserve_recipes_get(model=model, cluster_id=cluster_id)
        print("The response of EXTERNALApi->get_cserve_recipe_deployments_v2_cserve_recipes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_cserve_recipe_deployments_v2_cserve_recipes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**|  | [optional] 
 **cluster_id** | **int**|  | [optional] 

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

# **get_deployment_logs_deployments_logs_deployment_id_get**
> GetDeploymentLogResponse get_deployment_logs_deployments_logs_deployment_id_get(deployment_id, start_time, end_time, next_page_token=next_page_token)

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

    try:
        # Get Deployment Logs
        api_response = api_instance.get_deployment_logs_deployments_logs_deployment_id_get(deployment_id, start_time, end_time, next_page_token=next_page_token)
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

# **get_deployment_status_deployments_v2_status_deployment_id_get**
> DeploymentStatusResponseV2 get_deployment_status_deployments_v2_status_deployment_id_get(deployment_id)

Get Deployment Status

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_status_response_v2 import DeploymentStatusResponseV2
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
        api_response = api_instance.get_deployment_status_deployments_v2_status_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_deployment_status_deployments_v2_status_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployment_status_deployments_v2_status_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**DeploymentStatusResponseV2**](DeploymentStatusResponseV2.md)

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

# **get_deployments_deployments_v2_get**
> ListGetDeploymentV2Response get_deployments_deployments_v2_get(offset=offset, limit=limit, type=type, search_query=search_query)

Get Deployments

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_type import DeploymentType
from platform_api_python_client.models.list_get_deployment_v2_response import ListGetDeploymentV2Response
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
        api_response = api_instance.get_deployments_deployments_v2_get(offset=offset, limit=limit, type=type, search_query=search_query)
        print("The response of EXTERNALApi->get_deployments_deployments_v2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_deployments_deployments_v2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **type** | [**DeploymentType**](.md)|  | [optional] 
 **search_query** | **str**|  | [optional] 

### Return type

[**ListGetDeploymentV2Response**](ListGetDeploymentV2Response.md)

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
> ListHardwareInstanceResponse get_hardware_instances_hardware_instances_get()

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

    try:
        # Get Hardware Instances
        api_response = api_instance.get_hardware_instances_hardware_instances_get()
        print("The response of EXTERNALApi->get_hardware_instances_hardware_instances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_hardware_instances_hardware_instances_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_instances_hardware_instances_v2_get**
> ListHardwareInstanceResponse get_hardware_instances_hardware_instances_v2_get(cluster_id)

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
    cluster_id = 56 # int | 

    try:
        # Get Hardware Instances
        api_response = api_instance.get_hardware_instances_hardware_instances_v2_get(cluster_id)
        print("The response of EXTERNALApi->get_hardware_instances_hardware_instances_v2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_hardware_instances_hardware_instances_v2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

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

# **get_inference_deployment_deployments_v2_inference_deployment_id_get**
> GetInferenceV2DeploymentResponse get_inference_deployment_deployments_v2_inference_deployment_id_get(deployment_id)

Get Inference Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.get_inference_v2_deployment_response import GetInferenceV2DeploymentResponse
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
        api_response = api_instance.get_inference_deployment_deployments_v2_inference_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_inference_deployment_deployments_v2_inference_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_inference_deployment_deployments_v2_inference_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetInferenceV2DeploymentResponse**](GetInferenceV2DeploymentResponse.md)

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

# **get_payment_methods_payments_methods_get**
> ListPaymentMethodResponse get_payment_methods_payments_methods_get()

Get Payment Methods

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.list_payment_method_response import ListPaymentMethodResponse
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
        # Get Payment Methods
        api_response = api_instance.get_payment_methods_payments_methods_get()
        print("The response of EXTERNALApi->get_payment_methods_payments_methods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_payment_methods_payments_methods_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListPaymentMethodResponse**](ListPaymentMethodResponse.md)

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
> GetDeploymentUsageResponse get_usage_deployments_usage_deployment_id_get(deployment_id, metric, duration, end_time=end_time)

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
    duration = 56 # int | 
    end_time = 56 # int |  (optional)

    try:
        # Get Usage
        api_response = api_instance.get_usage_deployments_usage_deployment_id_get(deployment_id, metric, duration, end_time=end_time)
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
 **duration** | **int**|  | 
 **end_time** | **int**|  | [optional] 

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

# **update_deployment_status_deployments_v2_status_deployment_id_put**
> DeploymentStatusResponseV2 update_deployment_status_deployments_v2_status_deployment_id_put(deployment_id, deployment_status_request)

Update Deployment Status

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_python_client
from platform_api_python_client.models.deployment_status_request import DeploymentStatusRequest
from platform_api_python_client.models.deployment_status_response_v2 import DeploymentStatusResponseV2
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
        api_response = api_instance.update_deployment_status_deployments_v2_status_deployment_id_put(deployment_id, deployment_status_request)
        print("The response of EXTERNALApi->update_deployment_status_deployments_v2_status_deployment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->update_deployment_status_deployments_v2_status_deployment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 
 **deployment_status_request** | [**DeploymentStatusRequest**](DeploymentStatusRequest.md)|  | 

### Return type

[**DeploymentStatusResponseV2**](DeploymentStatusResponseV2.md)

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

