from fastapi import FastAPI
from app.routers import vehicle, driver
from app.db.database import Base, engine
from app.routers import vehicle
from app.routers import maintenance
from app.routers import fuel_log
from app.routers import expense
# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TransitOps API",
    version="1.0.0"
)

app.include_router(vehicle.router)
app.include_router(driver.router)
app.include_router(maintenance.router)
app.include_router(fuel_log.router)
app.include_router(expense.router)
@app.get("/")
def root():
    return {
        "message": "Welcome to TransitOps API"
    }