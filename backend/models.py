from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    difficulty: int  # 1-5
    duration: int    # minutes
    intensity: int   # 1-5
    goal: int        # 0: Weight Loss, 1: Muscle Gain, 2: Flexibility

class Recommendation(BaseModel):
    name: str
    description: str
    difficulty: Optional[int] = None
    duration: Optional[int] = None
    intensity: Optional[int] = None
    calories: Optional[int] = None
    protein: Optional[int] = None
    carbs: Optional[int] = None
    fats: Optional[int] = None

class RecommendationResponse(BaseModel):
    workouts: List[Recommendation]
    nutrition: List[Recommendation]
