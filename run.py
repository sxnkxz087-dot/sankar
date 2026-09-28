import os
import sys
import uvicorn

if __name__ == "__main__":
    print("==========================================================")
    print("       FITBUDDY — AI Fitness Plan Generator              ")
    print("==========================================================")
    print("Starting FitBuddy server on http://127.0.0.1:8000 ...")
    print("Open your browser and navigate to: http://127.0.0.1:8000")
    print("==========================================================")
    
    # Add backend directory to sys.path
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    sys.path.insert(0, backend_dir)
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, app_dir=backend_dir)
