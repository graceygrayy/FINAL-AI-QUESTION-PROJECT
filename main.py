from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Connect static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Connect templates folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "questions": []
        }
    )


@app.post("/generate", response_class=HTMLResponse)
async def generate_questions(
    request: Request,
    subject: str = Form(...),
    topic: str = Form(...),
    difficulty: str = Form(...)
):

    # AI generated questions using subject, topic and difficulty
    questions = [
        f"[{difficulty}] What is {topic}?",
        f"[{difficulty}] Explain the importance of {topic} in {subject}.",
        f"[{difficulty}] Give two examples of {topic} in {subject}.",
        f"[{difficulty}] What are the advantages of {topic}?",
        f"[{difficulty}] Describe {topic} and its role in {subject}."
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "questions": questions
        }
    )