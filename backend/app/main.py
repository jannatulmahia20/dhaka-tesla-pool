from fastapi import FastAPI

from app.api.routes.auth import router as auth_router


app = FastAPI(
    title="Dhaka Tesla Pool API",
    version="1.0.0",
)


app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Dhaka Tesla Pool API",
    }