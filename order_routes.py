from fastapi import APIRouter

# Definindo um prefixo "padrão" para todas as rotas de pedidos
# Tag é só para a documentação automática do Swagger UI
order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def list_orders() -> dict:
    """
    Rota para listar todos os pedidos. Todas as rotas de pedidos precisam estar autenticadas.
    """
    return {"message": "List of orders"}