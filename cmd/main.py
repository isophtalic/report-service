from fastapi import FastAPI
from .api import v1
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(title="Report API")

# Import and register routers
app.include_router(v1.router, prefix="/api/v1/report", tags=["report"])

@app.get("/health")
def health_check():
    return {"status": "running"}


@app.on_event("shutdown")
async def shutdown_event():
    # Cancel tasks, close connections, etc.
    print("Shutting down...")