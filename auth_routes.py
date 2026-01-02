from fastapi import APIRouter

# Definindo um prefixo "padrão" para todas as rotas de autenticação
# Tag é só para a documentação automática do Swagger UI
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar() -> dict:
    """
    Rota principal de autenticação do sistema.
    """
    return {"message": "Rota de autenticação principal"}