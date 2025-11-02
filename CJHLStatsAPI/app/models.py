from pydantic import BaseModel

class PlayerMetadata(BaseModel):
    birthdate: str
    age: int
    draft_eligible: bool
    is_rookie: bool


class PlayerStats(BaseModel):
    name: str
    position: str
    team: str
    GP: int
    G: int
    A: int
    Points: int
    metadata: PlayerMetadata

