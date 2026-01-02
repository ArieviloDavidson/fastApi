# Comando para rodar o servidor com uvicorn:
# uvicorn main:app --reload

# Detalhamento teórico sobre padrão REST e FastAPI:
# Get -> Obter informações (Ler)
# Post -> Criar informações (Criar)
# Put/Patch -> Atualizar informações (Atualizar)
# Delete -> Deletar informações (Deletar)

# Endpoint -> Rota da API
# Exemplo de endpoint: /users, /products, /items/{item_id}

# Importando as bibliotecas necessárias FASTAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Importando utilitários
from utils.mainHtml import main_html_content

# Criando a aplicação FastAPI
app = FastAPI()

# Preciso importar as rotas depois do aplicativo para evitar erros de importação circular
from auth_routes import auth_router
from order_routes import order_router

# Incluindo as rotas na aplicação
app.include_router(auth_router)
app.include_router(order_router)

# ROTAS DA APLICAÇÃO

# Rota principal (No caso vai funcionar como se fosse o site que usa a API)
@app.get("/", response_class=HTMLResponse, tags=["home"])
async def home() -> str:
    """
    Home return HTML content.
    """
    return main_html_content()