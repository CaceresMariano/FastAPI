from fastapi import FastAPI

from .api import api_router

fast_proyect = FastAPI()

# Incluimos el router principal
fast_proyect.include_router(api_router)
