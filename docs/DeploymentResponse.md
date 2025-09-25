# DeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator_email** | **str** |  | 
**cluster_id** | **int** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**endpoint_url** | **str** |  | 
**image_url** | **str** |  | [optional] 
**type** | [**DeploymentType**](DeploymentType.md) |  | 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | 
**created_at** | **datetime** |  | 
**hardware_instance_id** | **int** |  | 
**revision_number** | **int** |  | 
**recipe** | [**CServeV2Recipe**](CServeV2Recipe.md) |  | 
**cserve_version** | **str** |  | [optional] 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 
**initial_replicas** | **int** |  | [optional] 
**endpoint_certificate_authority** | **str** |  | [optional] 
**endpoint_bearer_token** | **str** |  | [optional] 
**concurrency** | **int** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**container_port** | **int** |  | 
**healthcheck** | **str** |  | [optional] 
**command** | **List[str]** |  | [optional] 
**command_args** | **List[str]** |  | [optional] 
**original_command** | **str** |  | [optional] 
**image_pull_secret_credentials** | [**ImagePullSecretCredentials**](ImagePullSecretCredentials.md) |  | [optional] 

## Example

```python
from platform_api_python_client.models.deployment_response import DeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentResponse from a JSON string
deployment_response_instance = DeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(DeploymentResponse.to_json())

# convert the object into a dict
deployment_response_dict = deployment_response_instance.to_dict()
# create an instance of DeploymentResponse from a dict
deployment_response_from_dict = DeploymentResponse.from_dict(deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


