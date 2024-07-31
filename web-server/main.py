import pandas as pd
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
#Ayuda a importar archivos CSS y JS
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="./public/static"), name="static")

templates = Jinja2Templates(directory="public/templates")


@app.get('/', response_class=HTMLResponse)
def get_list(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})

#Cargar CSV
@app.post("/upload-csv", response_class=HTMLResponse)
def upload_csv(request: Request, file: UploadFile = File(...)):
    global dataframe

    # Leer el archivo CSV utilizando Pandas
    try:
        dataframe = pd.read_csv(file.file)
    except Exception as e:
        return templates.TemplateResponse("error.html", {"request": request, "message": "Error al leer el archivo CSV."})

    # Convertir el DataFrame a HTML
    table_html = dataframe.to_html(classes="table table-striped", index=False)

    # Renderizar la tabla HTML
    return templates.TemplateResponse("display_csv.html", {
        "request": request,
        "table": table_html,
        "columns": dataframe.columns.tolist()  # Lista de columnas para el formulario de filtrado
    })

#Filtrar CSV
@app.post("/filter-csv", response_class=HTMLResponse)
def filter_csv(request: Request, filterColumn: str = Form(...), filterValue: str = Form(...)):
    global dataframe

    if dataframe is None:
        return templates.TemplateResponse("error.html", {"request": request, "message": "No hay datos cargados."})

    # Aplicar filtro al DataFrame
    filtered_df = dataframe[dataframe[filterColumn].astype(str).str.contains(filterValue, case=False, na=False)]

    # Convertir el DataFrame filtrado a HTML
    table_html = filtered_df.to_html(classes="table table-striped", index=False)

    # Renderizar la tabla HTML
    return templates.TemplateResponse("display_csv.html", {
        "request": request,
        "table": table_html,
        "columns": dataframe.columns.tolist()  # Lista de columnas para el formulario de filtrado
    })

@app.get('/contact', response_class=HTMLResponse)
def get_list(request: Request):
    return templates.TemplateResponse("item.html", {"request":request}, status_code=200)

@app.get("/template/{id}", response_class=HTMLResponse)
def template(request: Request, id:str):
    return templates.TemplateResponse("item.html", {"request": request, "id":id})


def run():
    
    if __name__ == '__main__':
        run()