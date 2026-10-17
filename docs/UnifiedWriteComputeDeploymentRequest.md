# UnifiedWriteComputeDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cluster_id** | **int** |  | 
**hardware_instance_id** | **int** |  | 
**user_annotations** | **Dict[str, str]** |  | [optional] 
**chart_revision** | **str** |  | [optional] 
**volume_mounts** | [**List[VolumeMount]**](VolumeMount.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**image_url** | **str** |  | 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 
**image_pull_ref** | **int** |  | [optional] 
**image_pull_secret_name** | **str** | Name of a pre-existing image pull Secret in the deployment namespace. Created, refreshed and deleted externally. Mutually exclusive with inline registry credentials and image_pull_ref. Include on updates to retain it; null clears it. | [optional] 
**env_vars_refs** | **object** |  | [optional] 
**ssh_public_key** | **str** |  | 
**enable_logging** | **bool** |  | [optional] [default to False]
**type** | **str** |  | 

## Example

```python
from platform_api_python_client.models.unified_write_compute_deployment_request import UnifiedWriteComputeDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnifiedWriteComputeDeploymentRequest from a JSON string
unified_write_compute_deployment_request_instance = UnifiedWriteComputeDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(UnifiedWriteComputeDeploymentRequest.to_json())

# convert the object into a dict
unified_write_compute_deployment_request_dict = unified_write_compute_deployment_request_instance.to_dict()
# create an instance of UnifiedWriteComputeDeploymentRequest from a dict
unified_write_compute_deployment_request_from_dict = UnifiedWriteComputeDeploymentRequest.from_dict(unified_write_compute_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


