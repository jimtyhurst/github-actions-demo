from fastapi import FastAPI

DEFAULT_NAME = "World"

app = FastAPI()


def generate_greeting(name=""):
    if name == "":
        name = DEFAULT_NAME
    return f"Hello, {name}!"


@app.get("/greeting")
async def greeting():
    return {"message": generate_greeting()}


@app.get("/greeting/{name}")
async def greeting(name):
    return {"message": generate_greeting(name)}
