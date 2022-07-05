from fastapi import FastAPI

app = FastAPI()

posts = []

@app.get('/')
def read_root():
    return {"welcome": "Welcome to mi REST API"}