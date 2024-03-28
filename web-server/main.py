import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return[1, 2, 3, 4]

@app.get("/contact")
def get_list():
    return { 'name': 'Platzi'} 

@app.get("/contactHTML", response_class=HTMLResponse)
def get_list():
        return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
    #run() -> se comenta para la clase de FastAPI