from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.routers import (
    auth,
    dashboard,
    driver,
    expense,
    fuel_log,
    maintenance,
    report,
    trip,
    vehicle,
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TransitOps API",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(vehicle.router)
app.include_router(driver.router)
app.include_router(trip.router)
app.include_router(maintenance.router)
app.include_router(fuel_log.router)
app.include_router(expense.router)
app.include_router(report.router)
app.include_router(dashboard.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to TransitOps API"
    }