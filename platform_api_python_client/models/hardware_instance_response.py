# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class HardwareInstanceResponse(BaseModel):
    """
    HardwareInstanceResponse
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    gpu_type: StrictStr
    num_gpu: StrictInt
    cpu: StrictInt
    memory: StrictInt
    cost_per_hr: StrictInt
    cluster_id: StrictInt
    provider: Optional[StrictStr] = None
    num_accelerators: Optional[StrictInt] = None
    accelerator_memory: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "name", "gpu_type", "num_gpu", "cpu", "memory", "cost_per_hr", "cluster_id", "provider", "num_accelerators", "accelerator_memory"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HardwareInstanceResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if provider (nullable) is None
        # and model_fields_set contains the field
        if self.provider is None and "provider" in self.model_fields_set:
            _dict['provider'] = None

        # set to None if num_accelerators (nullable) is None
        # and model_fields_set contains the field
        if self.num_accelerators is None and "num_accelerators" in self.model_fields_set:
            _dict['num_accelerators'] = None

        # set to None if accelerator_memory (nullable) is None
        # and model_fields_set contains the field
        if self.accelerator_memory is None and "accelerator_memory" in self.model_fields_set:
            _dict['accelerator_memory'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HardwareInstanceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "gpu_type": obj.get("gpu_type"),
            "num_gpu": obj.get("num_gpu"),
            "cpu": obj.get("cpu"),
            "memory": obj.get("memory"),
            "cost_per_hr": obj.get("cost_per_hr"),
            "cluster_id": obj.get("cluster_id"),
            "provider": obj.get("provider"),
            "num_accelerators": obj.get("num_accelerators"),
            "accelerator_memory": obj.get("accelerator_memory")
        })
        return _obj


