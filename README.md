# FitBuddy — AI Fitness Plan Generator

FitBuddy is a modern, responsive fitness web application that generates personalized 7-day workout programs and actionable nutrition/recovery tips based on user goals, physical attributes, and workout intensity.

It supports **adaptive re-generation** via conversational feedback (e.g., *"Add more cardio"*, *"Make the workouts easier"*), keeping both the original plan and the updated plan intact. FitBuddy also features an **Admin Plan Management Dashboard** backed by **SQLite** for monitoring users, plans, and feedback.

---

## ⚡ Key Highlights & Architecture

- **Low-Credit & High-Efficiency Design**: Built with a single centralized AI service, eliminating redundant API roundtrips and complex dependencies.
- **Built-in Demo Mode**: If no `GEMINI_API_KEY` is present, the app automatically switches to **Demo Mode** with realistic, multi-goal workout plans, allowing immediate testing without an API key or billing costs.
- **Dark Fitness Theme**: Sleek deep-charcoal palette (`#090a0f`), vibrant lime-green accents (`#22c55e`), modern cards, and responsive layout for mobile, tablet, and desktop.
- **Preserved Plan History**: Both the user's original plan and any feedback-adapted plan are preserved and easily toggled.
- **Integrated Admin Dashboard**: Direct `/admin` interface with search and filtering by goal, plus detailed user modal views.
- **Single-Port Production Serving**: FastAPI serves both the REST API and the compiled React SPA from `http://127.0.0.1:8000`.

---

## 🚀 Quick Start

### 1. Requirements
- Python 3.10+
- (Optional) Node.js 18+ (if you wish to run the Vite dev server separately)

### 2. Install Dependencies
```bash
py -3 -m pip install -r backend/requirements.txt
```

### 3. Run the Application
```bash
py -3 run.py
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser.

---

## 🔑 Gemini AI Configuration (Optional)

FitBuddy works right out of the box in **Demo Mode**. To enable live Gemini AI generation:

1. Copy `.env.example` to `.env` in the `backend/` directory:
   ```bash
   cp backend/.env.example backend/.env
   ```
2. Add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```
3. Restart the server. The badge in the navigation bar will automatically change from **Demo Mode** to **AI Powered**.

---

## 🛠️ Tech Stack & Endpoints

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite, Tailwind CSS, Lucide Icons |
| Backend | FastAPI (Python), Uvicorn, Pydantic |
| Database | SQLite (`backend/fitbuddy.db`) |
| AI Service | Gemini 1.5 Flash API with Demo Mode Fallback |

### API Endpoints
- `POST /api/generate-plan`: Validates profile inputs and generates a 7-day schedule with nutrition tips.
- `POST /api/update-plan`: Adapts the plan according to user feedback and preserves original.
- `GET /api/users`: Returns all users and plan statuses for the admin dashboard.
- `GET /api/users/{id}`: Returns complete details and plan history for a specific user ID.
- `GET /api/config`: Reports current server status and AI/Demo operating mode.

---

## 🛡️ Medical Disclaimer
*FitBuddy provides general fitness and wellness guidance and is not a substitute for professional medical advice.*
