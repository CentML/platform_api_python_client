# CreateUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**extension** | **str** |  | 

## Example

```python
from platform_api_python_client.models.create_url_request import CreateUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUrlRequest from a JSON string
create_url_request_instance = CreateUrlRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUrlRequest.to_json())

# convert the object into a dict
create_url_request_dict = create_url_request_instance.to_dict()
# create an instance of CreateUrlRequest from a dict
create_url_request_from_dict = CreateUrlRequest.from_dict(create_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


