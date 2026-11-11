# DynamoImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_version** | **str** | Dynamo runtime image tag (for example 1.4.0). Defaults to the platform&#39;s current release; GET /prebuilt-images?type&#x3D;dynamo lists the versions the platform has validated, but any tag may be requested. require_gpu_direct_rdma needs an EFA-capable image. Changing it restarts every component of a running deployment. | [optional] 
**pull_ref** | **int** |  | [optional] 

## Example

```python
from platform_api_python_client.models.dynamo_image import DynamoImage

# TODO update the JSON string below
json = "{}"
# create an instance of DynamoImage from a JSON string
dynamo_image_instance = DynamoImage.from_json(json)
# print the JSON string representation of the object
print(DynamoImage.to_json())

# convert the object into a dict
dynamo_image_dict = dynamo_image_instance.to_dict()
# create an instance of DynamoImage from a dict
dynamo_image_from_dict = DynamoImage.from_dict(dynamo_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


