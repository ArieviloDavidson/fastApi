# Comando para rodar o servidor com uvicorn:
# uvicorn main:app --reload

# Importando as bibliotecas necessárias FASTAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Importando utilitários
from utils.mainHtml import main_html_content

# Criando a aplicação FastAPI
app = FastAPI()

# Rota principal (No caso vai funcionar como se fosse o site que usa a API)
@app.get("/", response_class=HTMLResponse)
async def root():
    return main_html_content()