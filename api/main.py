from fastapi import FastAPI
from monitoring.python.system_snapshot import SystemSnapshot
app = FastAPI()


@app.get("/")
def root():
    return {"message": "HPC AI Benchmark Platform"}

@app.get("/snapshot")
def get_snapshot():
    snapshot = SystemSnapshot()

    return snapshot.generate_snapshot()
