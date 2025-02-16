from pydantic import BaseModel
from typing import List, Optional
from models.requests.pagination import Pagination

class Field(BaseModel):
    text: str
    value: str
    
class FieldsRequest(BaseModel):
    fields: List[Field]
    pagination: Optional[Pagination] = None