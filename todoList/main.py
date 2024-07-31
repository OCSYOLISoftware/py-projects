from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="templates")

tasks = []

#Inicio
@app.get('/', response_class=HTMLResponse)
async def get_tasks(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "task": tasks})

#Agregar tarea
@app.post("/add-task", response_class=HTMLResponse)
async def add_task(request: Request, task_name: str = Form(...)):
    global tasks
    tasks.append({"name": task_name, "completed": False})
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


#Cambio de estado de tareas
@app.post("/toggle-task", response_class=HTMLResponse)
async def toggle_task(request: Request, task_index: int = Form(...)):
    global tasks
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


#Eliminar tarea
@app.post("/delete-task", response_class=HTMLResponse)
async def delete_task(request: Request, task_index: int = Form(...)):
    global tasks
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

