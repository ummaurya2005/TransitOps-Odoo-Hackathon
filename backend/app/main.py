from fastapi import FastAPI
from app.routers import vehicle, driver
from app.db.database import Base, engine
from app.routers import vehicle

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TransitOps API",
    version="1.0.0"
)

app.include_router(vehicle.router)
app.include_router(driver.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to TransitOps API"
    }