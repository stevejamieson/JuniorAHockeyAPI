from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class PlayerMetadata(BaseModel):
    birthdate: str
    age: int
    draft_eligible: bool
    is_rookie: bool


class PlayerAnalytics(BaseModel):
    points_per_game: Optional[float] = None
    recent_points: Optional[int] = None  # Last 5 games
    consistency_score: Optional[float] = None  # Std dev or custom metric
    hot_streak: Optional[bool] = None


class PlayerStats(BaseModel):
    name: str
    position: str = Field(..., alias="Pos")
    team: str
    GP: int = Field(..., alias="GamesPlayed")
    G: int = Field(..., alias="Goals")
    A: int = Field(..., alias="Assists")
    Points: int = Field(..., alias="P")
    metadata: PlayerMetadata
    analytics: Optional[PlayerAnalytics] = None
