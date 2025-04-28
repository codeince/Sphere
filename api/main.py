from sphere import *
from sphere import __main__
from uuid import uuid1

from fastapi import FastAPI
from fastapi.applications import HTMLResponse as html

client_spheres: dict[str, list[dict[str, str]]] = {} # token: history

app = FastAPI()
sphere = Sphere(__main__.lang_build, __main__.answers)

@app.post("/api/generate_answer")
def generate_answer(question: str, token: str = None):
    result = {}
    if client_spheres.get(token) is None:
        token = uuid1().hex
        client_spheres[token] = []
        result.update(dict(token=token))
    history: list = client_spheres.get(token)

    sphere.load_history(history)
    answer = sphere.ask(question)
    history = sphere.to_list()

    client_spheres[token] = history
    result.update(dict(answer=answer))

    return result

@app.get("/api/get_history")
@app.get("/api/history/{token}")
def get_history(token: str):
    if type(client_spheres.get(token)) is list:
        return dict(status="success", history=client_spheres.get(token))
    else:
        return dict(status="error", message="This history doesn't exist")
    
@app.get('/')
def get_homepage():
    return html(open('index.html', 'r', encoding='utf-8').read())

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)