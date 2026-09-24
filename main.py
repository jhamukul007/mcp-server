from fastapi import FastAPI
from apis.user_controller import router

app = FastAPI()
app.include_router(router)
