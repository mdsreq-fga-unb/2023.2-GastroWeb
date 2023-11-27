from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from views.recipes import recipes
from database.start import create_database



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


@app.get("/")
def inicio():
    return {"message" : "ola mundo"}


app.include_router(recipes)

if __name__ == "__main__":
    import os
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, workers=1)


