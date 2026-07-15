from fastapi import FastAPI

app = FastAPI(
    title="Smart Money AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "Smart Money AI",
        "status": "Running",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {"status": "ok"}