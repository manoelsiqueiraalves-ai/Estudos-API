from fastapi import FastAPI

from app2.routes.curso_router import router as curso_router
from app2.routes.usuario_router import router as usuario_router

app = FastAPI()

app.include_router(curso_router, tags=["cursos"])
app.include_router(usuario_router, tags=["usuarios"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)



