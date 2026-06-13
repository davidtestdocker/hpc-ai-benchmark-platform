from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "HPC AI Benchmark Platform"}
