from fastapi import FastAPI
from api.models.health import HealthResponse
from monitoring.python.system_snapshot import SystemSnapshot
app = FastAPI(
    title="HPC AI Benchmark Platform",
    description="Linux Monitoring and Benchmark API",
    version="1.0.0"
)


@app.get("/", tags=["System"])
def root():
    return {"message": "HPC AI Benchmark Platform"}

@app.get("/snapshot", tags=["Monitoring"])
def get_snapshot():
    snapshot = SystemSnapshot()

    return snapshot.generate_snapshot()


@app.get("/health", tags=["Monitoring"], response_model=HealthResponse)
def health():

    snapshot = SystemSnapshot()
    return snapshot.health_check()
    
