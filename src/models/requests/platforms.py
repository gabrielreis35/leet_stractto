from pydantic import BaseModel
from typing import List

class Platform(BaseModel):
    text: str
    value: str
    
class PlatformsRequest(BaseModel):
    platforms: List[Platform]