from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CI/CD deployment working1 🚀"}

@app.get("/health")
def get_health():
    return {"status": "ok"}