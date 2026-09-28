import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_flow():
    print("1. Testing GET /api/config...")
    resp = client.get("/api/config")
    assert resp.status_code == 200, f"Config failed: {resp.text}"
    config = resp.json()
    print("   Config:", config)

    print("\n2. Testing POST /api/generate-plan (Validation error case)...")
    bad_resp = client.post("/api/generate-plan", json={
        "name": "Alex",
        "userId": "usr_100",
        "age": 5, # invalid
        "weight": 70,
        "goal": "Muscle Gain",
        "intensity": "Medium"
    })
    assert bad_resp.status_code == 422, f"Expected 422, got: {bad_resp.status_code}"
    print("   Validation guard caught invalid age correctly!")

    print("\n3. Testing POST /api/generate-plan (Valid case in Demo Mode)...")
    gen_resp = client.post("/api/generate-plan", json={
        "name": "Sarah Connor",
        "userId": "user_sarah_01",
        "age": 29,
        "weight": 62.5,
        "goal": "Muscle Gain",
        "intensity": "High"
    })
    assert gen_resp.status_code == 200, f"Generate failed: {gen_resp.text}"
    gen_data = gen_resp.json()
    assert gen_data["success"] is True
    assert gen_data["isDemo"] is True
    assert len(gen_data["originalPlan"]["days"]) == 7
    print(f"   Generated 7-day plan successfully! Day 1 focus: {gen_data['originalPlan']['days'][0]['focus']}")
    print(f"   Nutrition tip: {gen_data['originalPlan']['nutritionTip'][:60]}...")

    print("\n4. Testing POST /api/update-plan (Feedback: 'Add more cardio')...")
    upd_resp = client.post("/api/update-plan", json={
        "userId": "user_sarah_01",
        "feedback": "Add more cardio and make workouts slightly easier"
    })
    assert upd_resp.status_code == 200, f"Update failed: {upd_resp.text}"
    upd_data = upd_resp.json()
    assert upd_data["success"] is True
    assert upd_data["updatedPlan"] is not None
    assert upd_data["originalPlan"] is not None
    assert upd_data["feedback"] == "Add more cardio and make workouts slightly easier"
    print("   Plan updated successfully! Both original and updated plans are preserved.")

    print("\n5. Testing GET /api/users (Admin listing)...")
    users_resp = client.get("/api/users")
    assert users_resp.status_code == 200
    users = users_resp.json()["users"]
    assert len(users) >= 1
    sarah = next(u for u in users if u["id"] == "user_sarah_01")
    assert sarah["status"] == "Updated Plan"
    print(f"   Admin retrieved {len(users)} users. Sarah Connor status: {sarah['status']}")

    print("\n6. Testing GET /api/users/{id}...")
    user_detail_resp = client.get("/api/users/user_sarah_01")
    assert user_detail_resp.status_code == 200
    detail = user_detail_resp.json()
    assert detail["name"] == "Sarah Connor"
    assert detail["feedback"] == "Add more cardio and make workouts slightly easier"
    print(f"   User detail retrieved with feedback and plans!")

    print("\n7. Testing GET / (Static frontend index.html serving)...")
    spa_resp = client.get("/")
    assert spa_resp.status_code == 200
    assert "FITBUDDY" in spa_resp.text or "root" in spa_resp.text
    print("   Frontend SPA served directly by FastAPI!")

    print("\nALL BACKEND & INTEGRATION TESTS PASSED SUCCESSFULLY! [OK]")

if __name__ == "__main__":
    test_flow()
