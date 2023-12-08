from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from views.post_recipes import recipes
from views.auth_user import get_users, post_user
from database.start import create_database
from views.post_recipes import popula_bd
from views.get_recipes import get_recipes
from typing import Annotated



app = FastAPI()
router = APIRouter()

@app.on_event("startup")
async def start():
    await create_database()
    await popula_bd()
    



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

app.include_router(recipes)
app.include_router(get_recipes)
app.include_router(get_users)
app.include_router(post_user)


if __name__ == "__main__":
    import os
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, workers=1)



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#exemplo de função que utiliza a autenticação como requisito
@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}