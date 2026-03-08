from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "CI/CD deployment working1 🚀"}