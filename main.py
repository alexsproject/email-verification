import uvicorn
from fastapi import FastAPI

from email_verification_task_ForagerAI.api.routers import api_router
from email_verification_task_ForagerAI.core import app_settings

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_settings.HOST,
        port=app_settings.PORT,
        reload=app_settings.RELOAD,
    )
