import store
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
#Ayuda a importar archivos CSS y JS
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./public/static"), name="static")

templates = Jinja2Templates(directory="public/templates")


@app.get('/')
def get_list():
    return [1,2,3]

#Ruta statica
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    html_address = "./public/static/html/index.html"
    return FileResponse(html_address, status_code=200)

@app.get("/template/{id}", response_class=HTMLResponse)
def template(request: Request, id:str):
    return templates.TemplateResponse("item.html", {"request": request, "id":id})


def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()