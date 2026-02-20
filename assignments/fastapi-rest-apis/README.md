# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a small REST API using the FastAPI framework. The API will expose endpoints to create, list, and retrieve simple item records and will use Pydantic models for validation.

## 📝 Tasks

### 🛠️ Setup the project

#### Description
Create a virtual environment, install the required packages, and run the starter app.

#### Requirements
Completed setup should:

- Use a virtual environment (`python -m venv venv`)
- Install dependencies from `requirements.txt`
- Run the server with `uvicorn starter-code:app --reload`

### 🛠️ Implement API endpoints

#### Description
Extend or modify the provided `starter-code.py` to add the following endpoints and behaviors.

#### Requirements
Completed program should:

- Implement `GET /items` to return a list of items.
- Implement `POST /items` to accept an item payload and store it in-memory.
- Implement `GET /items/{item_id}` to return a single item or a 404 if not found.
- Use Pydantic models for request validation and response serialization.

### 🛠️ Add validation and tests (optional)

#### Description
Add validation rules to your Pydantic models and create simple tests for the API endpoints.

#### Requirements
Completed program should:

- Validate required fields and types for items.
- (Optional) Add a few pytest tests using `httpx` or `requests` against `TestClient` from FastAPI.

## 📦 Starter files

- `starter-code.py` — minimal FastAPI app with example endpoints.
- `requirements.txt` — packages needed to run the app.

## 🧾 Submission

Place your completed files in this folder and push to the repo. Include any tests under a `tests/` folder if added.

## ⏰ Due Date

2026-02-27
