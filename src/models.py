from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str # obligatoriu
    description: Optional[str] = None # opțional
    status: str = "todo"  # Default: 'todo'