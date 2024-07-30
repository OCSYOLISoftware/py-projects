import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina </h1>
        <p> parrafo</p>
         <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cambiar Color de Fondo</title>
        <style>
            body {
                background-color: white;
                text-align: center;
                padding-top: 50px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <button onclick="changeBackgroundColor()">Cambiar Color de Fondo</button>

        <script>
            function changeBackgroundColor() {
                // Cambia el color de fondo a un color aleatorio
                const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
                document.body.style.backgroundColor = randomColor;
            }
        </script>
    </body>
    </html>
"""

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()