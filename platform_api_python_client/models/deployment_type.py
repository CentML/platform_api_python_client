# coding: utf-8

"""
    Platform External API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class DeploymentType(str, Enum):
    """
    DeploymentType
    """

    """
    allowed enum values
    """
    INFERENCE = 'inference'
    TRAINING = 'training'
    COMPUTE = 'compute'
    COMPILATION = 'compilation'
    INFERENCE_V2 = 'inference_v2'
    COMPUTE_V2 = 'compute_v2'
    CSERVE = 'cserve'
    CSERVE_V2 = 'cserve_v2'
    DEPLOYMENT = 'deployment'
    RAG = 'rag'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DeploymentType from a JSON string"""
        return cls(json.loads(json_str))


