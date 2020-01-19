from fastapi import FastAPI

from application.core import config
from application.api.router import api_router


app = FastAPI(title=config.PROJECT_TITLE)
app.include_router(api_router, prefix=config.API_V1)