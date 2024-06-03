from fastapi import FastAPI
from .external_apis import router as external_apis_router

app = FastAPI(
    title="Interactive Story API",
    description="API for generating and managing interactive stories.",
    version="1.0.0"
)

# Incluir routers de outros arquivos
app.include_router(external_apis_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
