# GenerateServiceAccountSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** |  | 

## Example

```python
from platform_api_python_client.models.generate_service_account_secret_response import GenerateServiceAccountSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateServiceAccountSecretResponse from a JSON string
generate_service_account_secret_response_instance = GenerateServiceAccountSecretResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateServiceAccountSecretResponse.to_json())

# convert the object into a dict
generate_service_account_secret_response_dict = generate_service_account_secret_response_instance.to_dict()
# create an instance of GenerateServiceAccountSecretResponse from a dict
generate_service_account_secret_response_from_dict = GenerateServiceAccountSecretResponse.from_dict(generate_service_account_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


