# ImagePullSecretCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from platform_api_python_client.models.image_pull_secret_credentials import ImagePullSecretCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePullSecretCredentials from a JSON string
image_pull_secret_credentials_instance = ImagePullSecretCredentials.from_json(json)
# print the JSON string representation of the object
print(ImagePullSecretCredentials.to_json())

# convert the object into a dict
image_pull_secret_credentials_dict = image_pull_secret_credentials_instance.to_dict()
# create an instance of ImagePullSecretCredentials from a dict
image_pull_secret_credentials_from_dict = ImagePullSecretCredentials.from_dict(image_pull_secret_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


