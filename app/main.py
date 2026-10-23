from fastapi import FastAPI
from app.routes import files
app = FastAPI()

@app.get("/")
def landing_page():
    return {
        "message": "Hi Santhosh"
    }

@app.get("/health")
def health():
    return {
        "status": "your app is healthy"
    }
 
app.include_router(files.router)