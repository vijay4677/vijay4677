from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CI/CD deployment working1 🚀"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.get("/health")
def health():
    return {"status": "ok"}