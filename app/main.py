from dotenv import load_dotenv
load_dotenv(".env")

from fastapi import FastAPI
from app.api.api_router import router
from app.core.core import core_loop

app = FastAPI()

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello, Webgenie Task Generator!"}

if __name__ == "__main__":
    core_loop()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=18000)