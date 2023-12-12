from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from views.post_recipes import recipes
from views.auth_user import post_user
from database.start import create_database
from views.post_recipes import popula_bd
from views.get_recipes import get_recipes
from views.update_recipes import update_recipes
from views.delete_recipes import delete_recipes
from typing import Annotated



app = FastAPI()
router = APIRouter()


@app.on_event("startup")
async def start():
    await create_database()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


""" @app.get("/")
def inicio():
    return {"message" : "ola mundo"}
 """

app.include_router(post_user)
app.include_router(recipes)
app.include_router(get_recipes)
app.include_router(update_recipes)
app.include_router(delete_recipes)


if __name__ == "__main__":
    import os
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, workers=1)
