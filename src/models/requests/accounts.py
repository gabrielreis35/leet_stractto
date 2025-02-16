from pydantic import BaseModel
from typing import List, Optional
from models.requests.pagination import Pagination

class Account(BaseModel):
    id: int
    name: str
    token: str
    
class AccountsRequest(BaseModel):
    accounts: List[Account]
    pagination: Optional[Pagination] = None