# Personalized Workout and Nutrition Recommendation System

A beginner-friendly system that provides personalized fitness and nutrition advice based on user profiles using simple machine learning concepts.

## 🚀 Features

- **Personalized Recommendations**: Tailored workout plans and nutrition advice.
- **Modern UI**: A sleek, responsive frontend built with React and Vite.
- **FastAPI Backend**: Performent API for handling recommendation logic.
- **Machine Learning**: Utilizes pandas and scikit-learn for intelligent recommendation

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.8+
- Node.js & npm

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the API server:
   ```bash
   python main.py
   ```
   The backend will be running at `http://localhost:8000`.

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at the URL provided by Vite (usually `http://localhost:5173`).

## 📡 API Endpoints

- `GET /`: Welcome message.
- `POST /recommend`: Get personalized recommendations.
  - **Body**: `UserProfile` object (age, weight, height, goal, etc.)


