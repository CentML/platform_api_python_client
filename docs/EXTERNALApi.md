# platform_api_client.EXTERNALApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compute_deployment_deployments_compute_post**](EXTERNALApi.md#create_compute_deployment_deployments_compute_post) | **POST** /deployments/compute | Create Compute Deployment
[**create_inference_deployment_deployments_inference_post**](EXTERNALApi.md#create_inference_deployment_deployments_inference_post) | **POST** /deployments/inference | Create Inference Deployment
[**create_payment_payments_post**](EXTERNALApi.md#create_payment_payments_post) | **POST** /payments | Create Payment
[**create_payment_setup_payments_setup_post**](EXTERNALApi.md#create_payment_setup_payments_setup_post) | **POST** /payments/setup | Create Payment Setup
[**create_training_deployment_deployments_training_post**](EXTERNALApi.md#create_training_deployment_deployments_training_post) | **POST** /deployments/training | Create Training Deployment
[**delete_payment_method_payments_methods_payment_method_delete**](EXTERNALApi.md#delete_payment_method_payments_methods_payment_method_delete) | **DELETE** /payments/methods/{payment_method} | Delete Payment Method
[**get_compute_deployment_deployments_compute_deployment_id_get**](EXTERNALApi.md#get_compute_deployment_deployments_compute_deployment_id_get) | **GET** /deployments/compute/{deployment_id} | Get Compute Deployment
[**get_credits_credits_get**](EXTERNALApi.md#get_credits_credits_get) | **GET** /credits | Get Credits
[**get_deployment_status_deployments_status_deployment_id_get**](EXTERNALApi.md#get_deployment_status_deployments_status_deployment_id_get) | **GET** /deployments/status/{deployment_id} | Get Deployment Status
[**get_deployments_deployments_get**](EXTERNALApi.md#get_deployments_deployments_get) | **GET** /deployments | Get Deployments
[**get_hardware_instances_hardware_instances_get**](EXTERNALApi.md#get_hardware_instances_hardware_instances_get) | **GET** /hardware-instances | Get Hardware Instances
[**get_inference_deployment_deployments_inference_deployment_id_get**](EXTERNALApi.md#get_inference_deployment_deployments_inference_deployment_id_get) | **GET** /deployments/inference/{deployment_id} | Get Inference Deployment
[**get_payment_methods_payments_methods_get**](EXTERNALApi.md#get_payment_methods_payments_methods_get) | **GET** /payments/methods | Get Payment Methods
[**get_prebuilt_images_prebuilt_images_get**](EXTERNALApi.md#get_prebuilt_images_prebuilt_images_get) | **GET** /prebuilt-images | Get Prebuilt Images
[**get_training_deployment_deployments_training_deployment_id_get**](EXTERNALApi.md#get_training_deployment_deployments_training_deployment_id_get) | **GET** /deployments/training/{deployment_id} | Get Training Deployment
[**update_deployment_status_deployments_status_deployment_id_put**](EXTERNALApi.md#update_deployment_status_deployments_status_deployment_id_put) | **PUT** /deployments/status/{deployment_id} | Update Deployment Status


# **create_compute_deployment_deployments_compute_post**
> CreateComputeDeploymentResponse create_compute_deployment_deployments_compute_post(create_compute_deployment_request)

Create Compute Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.create_compute_deployment_request import CreateComputeDeploymentRequest
from platform_api_client.models.create_compute_deployment_response import CreateComputeDeploymentResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    create_compute_deployment_request = platform_api_client.CreateComputeDeploymentRequest() # CreateComputeDeploymentRequest | 

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

# **create_inference_deployment_deployments_inference_post**
> CreateInferenceDeploymentResponse create_inference_deployment_deployments_inference_post(create_inference_deployment_request)

Create Inference Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.create_inference_deployment_request import CreateInferenceDeploymentRequest
from platform_api_client.models.create_inference_deployment_response import CreateInferenceDeploymentResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    create_inference_deployment_request = platform_api_client.CreateInferenceDeploymentRequest() # CreateInferenceDeploymentRequest | 

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

# **create_payment_payments_post**
> ClientSecretResponse create_payment_payments_post(create_payment_request)

Create Payment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.client_secret_response import ClientSecretResponse
from platform_api_client.models.create_payment_request import CreatePaymentRequest
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    create_payment_request = platform_api_client.CreatePaymentRequest() # CreatePaymentRequest | 

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
import platform_api_client
from platform_api_client.models.client_secret_response import ClientSecretResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)

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

# **create_training_deployment_deployments_training_post**
> CreateTrainingDeploymentResponse create_training_deployment_deployments_training_post(create_training_deployment_request)

Create Training Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.create_training_deployment_request import CreateTrainingDeploymentRequest
from platform_api_client.models.create_training_deployment_response import CreateTrainingDeploymentResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    create_training_deployment_request = platform_api_client.CreateTrainingDeploymentRequest() # CreateTrainingDeploymentRequest | 

    try:
        # Create Training Deployment
        api_response = api_instance.create_training_deployment_deployments_training_post(create_training_deployment_request)
        print("The response of EXTERNALApi->create_training_deployment_deployments_training_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->create_training_deployment_deployments_training_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_training_deployment_request** | [**CreateTrainingDeploymentRequest**](CreateTrainingDeploymentRequest.md)|  | 

### Return type

[**CreateTrainingDeploymentResponse**](CreateTrainingDeploymentResponse.md)

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

# **delete_payment_method_payments_methods_payment_method_delete**
> object delete_payment_method_payments_methods_payment_method_delete(payment_method)

Delete Payment Method

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
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

# **get_compute_deployment_deployments_compute_deployment_id_get**
> GetComputeDeploymentResponse get_compute_deployment_deployments_compute_deployment_id_get(deployment_id)

Get Compute Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.get_compute_deployment_response import GetComputeDeploymentResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
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
import platform_api_client
from platform_api_client.models.credits_response import CreditsResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)

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

# **get_deployment_status_deployments_status_deployment_id_get**
> DeploymentStatusResponse get_deployment_status_deployments_status_deployment_id_get(deployment_id)

Get Deployment Status

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.deployment_status_response import DeploymentStatusResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
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

# **get_deployments_deployments_get**
> ListGetDeploymentResponse get_deployments_deployments_get(offset=offset, limit=limit, type=type, search_query=search_query)

Get Deployments

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.deployment_type import DeploymentType
from platform_api_client.models.list_get_deployment_response import ListGetDeploymentResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    type = platform_api_client.DeploymentType() # DeploymentType |  (optional)
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
> ListHardwareInstanceResponse get_hardware_instances_hardware_instances_get()

Get Hardware Instances

### Example


```python
import platform_api_client
from platform_api_client.models.list_hardware_instance_response import ListHardwareInstanceResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inference_deployment_deployments_inference_deployment_id_get**
> GetInferenceDeploymentResponse get_inference_deployment_deployments_inference_deployment_id_get(deployment_id)

Get Inference Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.get_inference_deployment_response import GetInferenceDeploymentResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
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

# **get_payment_methods_payments_methods_get**
> ListPaymentMethodResponse get_payment_methods_payments_methods_get()

Get Payment Methods

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.list_payment_method_response import ListPaymentMethodResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)

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


```python
import platform_api_client
from platform_api_client.models.deployment_type import DeploymentType
from platform_api_client.models.list_prebuilt_image_response import ListPrebuiltImageResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    type = platform_api_client.DeploymentType() # DeploymentType |  (optional)

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_training_deployment_deployments_training_deployment_id_get**
> GetTrainingDeploymentResponse get_training_deployment_deployments_training_deployment_id_get(deployment_id)

Get Training Deployment

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.get_training_deployment_response import GetTrainingDeploymentResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 

    try:
        # Get Training Deployment
        api_response = api_instance.get_training_deployment_deployments_training_deployment_id_get(deployment_id)
        print("The response of EXTERNALApi->get_training_deployment_deployments_training_deployment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EXTERNALApi->get_training_deployment_deployments_training_deployment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**|  | 

### Return type

[**GetTrainingDeploymentResponse**](GetTrainingDeploymentResponse.md)

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

# **update_deployment_status_deployments_status_deployment_id_put**
> DeploymentStatusResponse update_deployment_status_deployments_status_deployment_id_put(deployment_id, deployment_status_request)

Update Deployment Status

### Example

* Bearer Authentication (HTTPBearer):

```python
import platform_api_client
from platform_api_client.models.deployment_status_request import DeploymentStatusRequest
from platform_api_client.models.deployment_status_response import DeploymentStatusResponse
from platform_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = platform_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = platform_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with platform_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = platform_api_client.EXTERNALApi(api_client)
    deployment_id = 56 # int | 
    deployment_status_request = platform_api_client.DeploymentStatusRequest() # DeploymentStatusRequest | 

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

