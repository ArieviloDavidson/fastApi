# Comando para rodar o servidor com uvicorn:
# uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World in FastAPI!"}