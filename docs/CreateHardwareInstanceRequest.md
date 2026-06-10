# CreateHardwareInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | 
**name** | **str** |  | 
**gpu_type** | **str** |  | 
**num_gpu** | **int** |  | 
**cpu** | **int** |  | 
**memory** | **int** |  | 
**accelerator_resource_key** | **str** |  | 
**node_affinity_labels** | **Dict[str, str]** |  | 
**accelerator_memory** | **int** |  | 

## Example

```python
from platform_api_python_client.models.create_hardware_instance_request import CreateHardwareInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHardwareInstanceRequest from a JSON string
create_hardware_instance_request_instance = CreateHardwareInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHardwareInstanceRequest.to_json())

# convert the object into a dict
create_hardware_instance_request_dict = create_hardware_instance_request_instance.to_dict()
# create an instance of CreateHardwareInstanceRequest from a dict
create_hardware_instance_request_from_dict = CreateHardwareInstanceRequest.from_dict(create_hardware_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


