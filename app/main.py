from fastapi import FastAPI

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
 