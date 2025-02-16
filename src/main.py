from fastapi import FastAPI, APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
import json
import uvicorn

from services.service import Service

service = Service()
app = FastAPI()
routes = APIRouter(prefix="/api")

@routes.get("/")
def get_home():
    informacoes = {
        "nome": "Gabriel Reis",
        "email": "gabrielreis0406@gmail.com",
        "linkedin": "https://www.linkedin.com/in/gabrielreis35/"
    }
    
    ret = JSONResponse(content=informacoes)
    
    return ret

@routes.get("/{plataforma}", status_code=status.HTTP_200_OK)
def get_plataformas(plataforma: str):
    try:
        data = service.get_platform(platform=plataforma)
        
        ret = JSONResponse(content=data)
    
        return ret
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@routes.get("/{plataforme}/resumo", status_code=status.HTTP_200_OK)
def get_resume_platforms(plataforma: str):
    return "Teste"

@routes.get("/geral", status_code=status.HTTP_200_OK)
def get_general_report():
    return "Teste"


@routes.get("/geral/resumo", status_code=status.HTTP_200_OK)
def get_resume_general_report():
    return "Teste"

app.include_router(routes)


if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="debug")
    server = uvicorn.Server(config)
    server.run()