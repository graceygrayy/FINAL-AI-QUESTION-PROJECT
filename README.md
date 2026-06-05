# FINAL-AI-QUESTION-PROJEC
# QuizGenius AI

A web-based AI-powered quiz question generator built with HTML, CSS, and a FastAPI backend.

---

## About the Project

QuizGenius AI is a study tool that helps students generate intelligent study questions instantly.
Users can enter a subject, topic, and difficulty level, and the app will generate 5 relevant study questions automatically.

---

## Features

- AI-powered question generation
- Supports multiple subjects and topics
- Three difficulty levels: Easy, Medium, Hard
- Clean and responsive user interface
- Fast and lightweight backend

---

## Technologies Used

- HTML - Structure and layout of the web pages
- CSS - Styling and responsive design
- FastAPI - Python backend framework for handling requests
- Jinja2 - Template engine for rendering HTML dynamically
- Font Awesome - Icons used throughout the interface
- Uvicorn - ASGI server for running the FastAPI app

---

## How to Run the Project

1. Clone or download the project**

2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows
```

3. Install dependencies**

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
uvicorn main:app --reload
```

---

## How to Use

1. Enter a Subject (e.g. Science, History, Mathematics)
2. Enter a Topic (e.g. Photosynthesis, World War 2, Algebra)
3. Select a Difficulty level (Easy, Medium or Hard)
4. Click Generate Questions
5. View your 5 generated study questions instantly

---

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Jinja2

Install all requirements with:

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

---

## Author

Designed & Developed by **Gracey**

5. Open in your browser**
---

## Project Structure
