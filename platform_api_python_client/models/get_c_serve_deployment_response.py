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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from platform_api_python_client.models.deployment_status import DeploymentStatus
from platform_api_python_client.models.deployment_type import DeploymentType
from typing import Optional, Set
from typing_extensions import Self

class GetCServeDeploymentResponse(BaseModel):
    """
    GetCServeDeploymentResponse
    """ # noqa: E501
    model: StrictStr
    is_embedding_model: StrictBool
    tensor_parallel_size: StrictInt
    pipeline_parallel_size: StrictInt
    block_size: StrictInt
    swap_space: Annotated[int, Field(strict=True, ge=0)]
    gpu_mem_util: Union[Annotated[float, Field(le=1.0, strict=True, ge=0.0)], Annotated[int, Field(le=1, strict=True, ge=0)]]
    max_num_seqs: StrictInt
    use_prefix_caching: Optional[StrictBool]
    offloading_num: StrictInt
    use_flashinfer: StrictBool
    max_model_len: Optional[Annotated[int, Field(strict=True, ge=128)]]
    dtype: StrictStr
    tokenizer: Optional[StrictStr]
    spec_proposer: Optional[StrictStr]
    spec_draft_model: Optional[StrictStr]
    spec_tokens: Optional[StrictInt]
    spec_prompt_lookup_min: Optional[Annotated[int, Field(strict=True, ge=1)]]
    spec_prompt_lookup_max: Optional[Annotated[int, Field(strict=True, ge=1)]]
    seed: StrictInt
    cluster_id: StrictInt
    id: StrictInt
    name: StrictStr
    endpoint_url: StrictStr
    image_url: Optional[StrictStr]
    type: DeploymentType
    status: DeploymentStatus
    created_at: datetime
    hardware_instance_id: StrictInt
    min_scale: StrictInt
    max_scale: StrictInt
    endpoint_certificate_authority: Optional[StrictStr]
    concurrency: Optional[StrictInt]
    __properties: ClassVar[List[str]] = ["model", "is_embedding_model", "tensor_parallel_size", "pipeline_parallel_size", "block_size", "swap_space", "gpu_mem_util", "max_num_seqs", "use_prefix_caching", "offloading_num", "use_flashinfer", "max_model_len", "dtype", "tokenizer", "spec_proposer", "spec_draft_model", "spec_tokens", "spec_prompt_lookup_min", "spec_prompt_lookup_max", "seed", "cluster_id", "id", "name", "endpoint_url", "image_url", "type", "status", "created_at", "hardware_instance_id", "min_scale", "max_scale", "endpoint_certificate_authority", "concurrency"]

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
        """Create an instance of GetCServeDeploymentResponse from a JSON string"""
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
        # set to None if use_prefix_caching (nullable) is None
        # and model_fields_set contains the field
        if self.use_prefix_caching is None and "use_prefix_caching" in self.model_fields_set:
            _dict['use_prefix_caching'] = None

        # set to None if max_model_len (nullable) is None
        # and model_fields_set contains the field
        if self.max_model_len is None and "max_model_len" in self.model_fields_set:
            _dict['max_model_len'] = None

        # set to None if tokenizer (nullable) is None
        # and model_fields_set contains the field
        if self.tokenizer is None and "tokenizer" in self.model_fields_set:
            _dict['tokenizer'] = None

        # set to None if spec_proposer (nullable) is None
        # and model_fields_set contains the field
        if self.spec_proposer is None and "spec_proposer" in self.model_fields_set:
            _dict['spec_proposer'] = None

        # set to None if spec_draft_model (nullable) is None
        # and model_fields_set contains the field
        if self.spec_draft_model is None and "spec_draft_model" in self.model_fields_set:
            _dict['spec_draft_model'] = None

        # set to None if spec_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.spec_tokens is None and "spec_tokens" in self.model_fields_set:
            _dict['spec_tokens'] = None

        # set to None if spec_prompt_lookup_min (nullable) is None
        # and model_fields_set contains the field
        if self.spec_prompt_lookup_min is None and "spec_prompt_lookup_min" in self.model_fields_set:
            _dict['spec_prompt_lookup_min'] = None

        # set to None if spec_prompt_lookup_max (nullable) is None
        # and model_fields_set contains the field
        if self.spec_prompt_lookup_max is None and "spec_prompt_lookup_max" in self.model_fields_set:
            _dict['spec_prompt_lookup_max'] = None

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['image_url'] = None

        # set to None if endpoint_certificate_authority (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_certificate_authority is None and "endpoint_certificate_authority" in self.model_fields_set:
            _dict['endpoint_certificate_authority'] = None

        # set to None if concurrency (nullable) is None
        # and model_fields_set contains the field
        if self.concurrency is None and "concurrency" in self.model_fields_set:
            _dict['concurrency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetCServeDeploymentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "model": obj.get("model"),
            "is_embedding_model": obj.get("is_embedding_model") if obj.get("is_embedding_model") is not None else False,
            "tensor_parallel_size": obj.get("tensor_parallel_size"),
            "pipeline_parallel_size": obj.get("pipeline_parallel_size"),
            "block_size": obj.get("block_size") if obj.get("block_size") is not None else 32,
            "swap_space": obj.get("swap_space") if obj.get("swap_space") is not None else 0,
            "gpu_mem_util": obj.get("gpu_mem_util") if obj.get("gpu_mem_util") is not None else 0.95,
            "max_num_seqs": obj.get("max_num_seqs") if obj.get("max_num_seqs") is not None else 256,
            "use_prefix_caching": obj.get("use_prefix_caching"),
            "offloading_num": obj.get("offloading_num") if obj.get("offloading_num") is not None else 0,
            "use_flashinfer": obj.get("use_flashinfer") if obj.get("use_flashinfer") is not None else False,
            "max_model_len": obj.get("max_model_len"),
            "dtype": obj.get("dtype") if obj.get("dtype") is not None else 'auto',
            "tokenizer": obj.get("tokenizer"),
            "spec_proposer": obj.get("spec_proposer"),
            "spec_draft_model": obj.get("spec_draft_model"),
            "spec_tokens": obj.get("spec_tokens"),
            "spec_prompt_lookup_min": obj.get("spec_prompt_lookup_min"),
            "spec_prompt_lookup_max": obj.get("spec_prompt_lookup_max"),
            "seed": obj.get("seed") if obj.get("seed") is not None else 0,
            "cluster_id": obj.get("cluster_id"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "endpoint_url": obj.get("endpoint_url"),
            "image_url": obj.get("image_url"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "hardware_instance_id": obj.get("hardware_instance_id"),
            "min_scale": obj.get("min_scale"),
            "max_scale": obj.get("max_scale"),
            "endpoint_certificate_authority": obj.get("endpoint_certificate_authority"),
            "concurrency": obj.get("concurrency")
        })
        return _obj


