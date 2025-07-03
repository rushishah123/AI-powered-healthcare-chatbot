"""Pydantic models for the Model Context Protocol."""
from datetime import datetime
from typing import List, Union
from typing_extensions import Literal
from pydantic import BaseModel


class Demographics(BaseModel):
    """Patient demographic information."""
    patient_id: str
    name: str
    age: int
    gender: str


class LabResult(BaseModel):
    """Representation of a single lab result."""
    test_name: str
    value: str
    unit: str
    date: datetime


class Medication(BaseModel):
    """Information about a medication."""
    name: str
    dose: str
    frequency: str


class Appointment(BaseModel):
    """Information about an appointment."""
    date: datetime
    provider: str
    reason: str


class ContextBlock(BaseModel):
    """Block of context in the MCP."""
    type: Literal["demographics", "recent_labs", "medications", "appointments"]
    payload: Union[Demographics, List[LabResult], List[Medication], List[Appointment]]


class MCP(BaseModel):
    """Model Context Protocol root object."""
    patient_id: str
    timestamp: datetime
    context_blocks: List[ContextBlock]
