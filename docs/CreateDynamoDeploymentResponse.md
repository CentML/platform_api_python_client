# CreateDynamoDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**endpoint_url** | **str** |  | 

## Example

```python
from platform_api_python_client.models.create_dynamo_deployment_response import CreateDynamoDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDynamoDeploymentResponse from a JSON string
create_dynamo_deployment_response_instance = CreateDynamoDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(CreateDynamoDeploymentResponse.to_json())

# convert the object into a dict
create_dynamo_deployment_response_dict = create_dynamo_deployment_response_instance.to_dict()
# create an instance of CreateDynamoDeploymentResponse from a dict
create_dynamo_deployment_response_from_dict = CreateDynamoDeploymentResponse.from_dict(create_dynamo_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


