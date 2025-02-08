from fastapi import FastAPI

from src.models import Task

app = FastAPI()

# Lista unde stocăm task-urile (temporar, fără DB)
tasks = []

@app.get("/")  # Acest endpoint va răspunde la http://127.0.0.1:8000/
def root():
    return {"message": "Welcome to the To-Do API!"}

@app.get("/healthcheck")  # Acest endpoint verifică dacă serverul merge
def healthcheck():
    return {"status": "OK"}

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added", "task": task}