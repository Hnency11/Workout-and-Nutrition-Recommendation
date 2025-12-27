from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recommender import recommender
from models import UserProfile, RecommendationResponse

app = FastAPI(title="Personalized Workout and Nutrition API")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Personalized Workout and Nutrition API"}

@app.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(profile: UserProfile):
    recommendations = recommender.get_recommendations(profile.dict())
    return recommendations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
