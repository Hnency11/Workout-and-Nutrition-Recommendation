import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

# Mock dataset for Workout Recommendations
# Features: Difficulty (1-5), Duration (15-60 min), Intensity (1-5), Goal (0: Weight Loss, 1: Muscle Gain, 2: Flexibility)
workouts_df = pd.DataFrame([
    {"name": "HIIT Sprint", "difficulty": 4, "duration": 20, "intensity": 5, "goal": 0, "description": "High intensity interval training involving quick sprints."},
    {"name": "Power Lifting", "difficulty": 5, "duration": 60, "intensity": 5, "goal": 1, "description": "Heavy lifting focus on compound movements."},
    {"name": "Yoga Flow", "difficulty": 2, "duration": 45, "intensity": 2, "goal": 2, "description": "Flowing sequences to improve flexibility and mindfulness."},
    {"name": "Steady Jog", "difficulty": 2, "duration": 30, "intensity": 3, "goal": 0, "description": "Modarate pace jogging for cardiovascular health."},
    {"name": "Bodyweight Strength", "difficulty": 3, "duration": 40, "intensity": 4, "goal": 1, "description": "Strengthening exercises using only your body weight."},
    {"name": "Pilates", "difficulty": 3, "duration": 50, "intensity": 3, "goal": 2, "description": "Core focused exercises for stability and posture."},
    {"name": "Swimming Laps", "difficulty": 3, "duration": 45, "intensity": 4, "goal": 0, "description": "Full body cardio workout in the pool."},
    {"name": "Hypertrophy Training", "difficulty": 4, "duration": 55, "intensity": 4, "goal": 1, "description": "Volume-based training for muscle size."},
    {"name": "Stretching Routine", "difficulty": 1, "duration": 15, "intensity": 1, "goal": 2, "description": "Short and easy stretching to improve mobility."},
    {"name": "Circuit Training", "difficulty": 4, "duration": 35, "intensity": 4, "goal": 0, "description": "Continuous movement through various exercise stations."}
])

# Mock dataset for Nutrition Recommendations
# Features: Calories, Protein (g), Carbs (g), Fats (g), Goal (0: Weight Loss, 1: Muscle Gain, 2: Maintenance)
nutrition_df = pd.DataFrame([
    {"name": "Grilled Chicken Salad", "calories": 350, "protein": 35, "carbs": 10, "fats": 12, "goal": 0, "description": "Lean protein with fresh greens."},
    {"name": "Steak and Sweet Potato", "calories": 700, "protein": 50, "carbs": 60, "fats": 25, "goal": 1, "description": "High calorie, high protein meal for muscle growth."},
    {"name": "Quinoa Bowl", "calories": 450, "protein": 15, "carbs": 65, "fats": 15, "goal": 2, "description": "Balanced meal with complex carbs and plant protein."},
    {"name": "Salmon and Asparagus", "calories": 400, "protein": 30, "carbs": 5, "fats": 20, "goal": 0, "description": "Fresh salmon high in omega-3s for weight loss."},
    {"name": "Pasta Carbonara (High Protein)", "calories": 800, "protein": 45, "carbs": 80, "fats": 30, "goal": 1, "description": "Rich pasta dish for high energy demands."},
    {"name": "Greek Yogurt Parfait", "calories": 300, "protein": 20, "carbs": 30, "fats": 5, "goal": 2, "description": "Simple and healthy snack or light breakfast."},
    {"name": "Tofu Stir-fry", "calories": 380, "protein": 25, "carbs": 35, "fats": 14, "goal": 0, "description": "Vegan friendly stir-fry for weight management."},
    {"name": "Oatmeal with Peanuts", "calories": 550, "protein": 22, "carbs": 70, "fats": 18, "goal": 1, "description": "Hearty breakfast for muscle building."},
    {"name": "Avocado Toast", "calories": 320, "protein": 8, "carbs": 25, "fats": 18, "goal": 2, "description": "Healthy fats and simple carbs for maintenance."},
    {"name": "Turkey Wrap", "calories": 420, "protein": 28, "carbs": 40, "fats": 12, "goal": 0, "description": "Quick lean lunch for weight loss goals."}
])

class Recommender:
    def __init__(self):
        self.workout_scaler = StandardScaler()
        self.nutrition_scaler = StandardScaler()
        self.workout_model = NearestNeighbors(n_neighbors=2, algorithm='auto')
        self.nutrition_model = NearestNeighbors(n_neighbors=2, algorithm='auto')
        self._prepare_data()

    def _prepare_data(self):
        # Prepare Workout features
        workout_features = workouts_df[['difficulty', 'duration', 'intensity', 'goal']]
        workout_features_scaled = self.workout_scaler.fit_transform(workout_features)
        self.workout_model.fit(workout_features_scaled)

        # Prepare Nutrition features
        nutrition_features = nutrition_df[['calories', 'protein', 'carbs', 'fats', 'goal']]
        nutrition_features_scaled = self.nutrition_scaler.fit_transform(nutrition_features)
        self.nutrition_model.fit(nutrition_features_scaled)

    def get_recommendations(self, user_profile):
        """
        user_profile: {
            'difficulty': int (1-5),
            'duration': int (min),
            'intensity': int (1-5),
            'goal': int (0, 1, 2)
        }
        """
        # Workout Recommendation
        user_workout_feat = np.array([[user_profile['difficulty'], user_profile['duration'], user_profile['intensity'], user_profile['goal']]])
        user_workout_feat_scaled = self.workout_scaler.transform(user_workout_feat)
        distances, indices = self.workout_model.kneighbors(user_workout_feat_scaled)
        
        recommended_workouts = workouts_df.iloc[indices[0]].to_dict('records')

        # Nutrition Recommendation
        if user_profile['goal'] == 0: target_nutri = [350, 30, 15, 12, 0]
        elif user_profile['goal'] == 1: target_nutri = [750, 45, 70, 25, 1]
        else: target_nutri = [400, 20, 40, 15, 2]

        user_nutri_feat_scaled = self.nutrition_scaler.transform(np.array([target_nutri]))
        distances_nutri, indices_nutri = self.nutrition_model.kneighbors(user_nutri_feat_scaled)
        
        recommended_meals = nutrition_df.iloc[indices_nutri[0]].to_dict('records')

        return {
            "workouts": recommended_workouts,
            "nutrition": recommended_meals
        }

recommender = Recommender()
