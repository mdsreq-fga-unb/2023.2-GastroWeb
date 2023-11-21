from fastapi import FastAPI, APIRouter
from views.recipes import recipes

app = FastAPI()
router = APIRouter()


@app.get("/")
def inicio():
    return {"message" : "ola mundo"}


app.include_router(recipes)

if __name__ == "__main__":
    import os
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, workers=1)


