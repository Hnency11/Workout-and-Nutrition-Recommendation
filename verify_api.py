import requests
import json

def test_recommendation():
    url = "http://localhost:8000/recommend"
    payload = {
        "difficulty": 4,
        "duration": 45,
        "intensity": 5,
        "goal": 1
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("Successfully received recommendations!")
            print(f"Workouts: {[w['name'] for w in data['workouts']]}")
            print(f"Meals: {[m['name'] for m in data['nutrition']]}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_recommendation()
