# ConfigFileMount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**mount_path** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from platform_api_python_client.models.config_file_mount import ConfigFileMount

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFileMount from a JSON string
config_file_mount_instance = ConfigFileMount.from_json(json)
# print the JSON string representation of the object
print(ConfigFileMount.to_json())

# convert the object into a dict
config_file_mount_dict = config_file_mount_instance.to_dict()
# create an instance of ConfigFileMount from a dict
config_file_mount_from_dict = ConfigFileMount.from_dict(config_file_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


