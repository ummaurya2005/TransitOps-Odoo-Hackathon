# 🚚 TransitOps - Fleet Management System

## 📌 Overview

TransitOps is a Fleet Management System developed for the Odoo Hackathon. It helps organizations efficiently manage vehicles, drivers, trips, maintenance, fuel consumption, expenses, and operational reports through a simple web interface.

The project is built using **FastAPI** for the backend and **HTML, CSS, and JavaScript** for the frontend with **SQLite** as the database.

---

# ✨ Features

## 🚚 Vehicle Management

- Add new vehicles
- Update vehicle details
- Delete vehicles
- View all vehicles
- Vehicle status management
- Vehicle capacity tracking

---

## 👨 Driver Management

- Add drivers
- Update driver details
- Delete drivers
- License management
- Safety score tracking
- Driver availability

---

## 🛣 Trip Management

- Create trips
- Dispatch trips
- Complete trips
- Cancel trips
- Vehicle allocation
- Driver allocation
- Cargo weight validation

---

## 🔧 Maintenance Management

- Schedule maintenance
- Track maintenance records
- Maintenance completion
- Vehicle service history

---

## ⛽ Fuel Log Management

- Record fuel usage
- Track fuel expenses
- Fuel history

---

## 💰 Expense Management

- Toll expenses
- Repair expenses
- Miscellaneous expenses
- Expense history

---

## 📊 Dashboard

Displays:

- Total Vehicles
- Available Vehicles
- Vehicles On Trip
- Total Drivers
- Active Trips
- Maintenance Records
- Fuel Cost
- Expense Cost
- Fleet Utilization

---

## 📈 Reports

- Vehicle Report
- Driver Report
- Trip Report
- Fuel Report
- Expense Report
- Operational Cost Report

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

## Database

- SQLite

---

# 📁 Project Structure

```
TransitOps/

│

├── app/

│   ├── db/

│   │   └── database.py

│   │

│   ├── models/

│   │   ├── vehicle.py

│   │   ├── driver.py

│   │   ├── trip.py

│   │   ├── maintenance.py

│   │   ├── fuel_log.py

│   │   ├── expense.py

│   │   └── user.py

│   │

│   ├── schemas/

│   │

│   ├── services/

│   │

│   ├── routers/

│   │

│   └── main.py

│

├── frontend/

│   ├── index.html

│   ├── dashboard.html

│   ├── vehicles.html

│   ├── drivers.html

│   ├── trips.html

│   ├── maintenance.html

│   ├── fuel.html

│   ├── expenses.html

│   ├── reports.html

│

│   ├── css/

│

│   ├── js/

│

│   └── assets/

│

└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/transitops.git

cd transitops
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend

Using VS Code Live Server

or

```bash
cd frontend

python -m http.server 5500
```

Frontend URL

```
http://127.0.0.1:5500
```

---

# 🗄 Database

Database Used

- SQLite

Tables

- Vehicles
- Drivers
- Trips
- Maintenance
- Fuel Logs
- Expenses
- Users

---

# 🔗 API Endpoints

## Vehicles

```
GET     /vehicles/

POST    /vehicles/

PUT     /vehicles/{id}

DELETE  /vehicles/{id}
```

---

## Drivers

```
GET     /drivers/

POST    /drivers/

PUT     /drivers/{id}

DELETE  /drivers/{id}
```

---

## Trips

```
GET     /trips/

POST    /trips/

PATCH   /trips/{id}/dispatch

PATCH   /trips/{id}/complete

PATCH   /trips/{id}/cancel

DELETE  /trips/{id}
```

---

## Maintenance

```
GET     /maintenance/

POST    /maintenance/

PATCH   /maintenance/{id}/complete

DELETE  /maintenance/{id}
```

---

## Fuel

```
GET     /fuel-logs/

POST    /fuel-logs/

DELETE  /fuel-logs/{id}
```

---

## Expenses

```
GET     /expenses/

POST    /expenses/

DELETE  /expenses/{id}
```

---

## Dashboard

```
GET

/dashboard/
```

---

## Reports

```
GET

/reports/vehicles

/reports/drivers

/reports/trips

/reports/fuel

/reports/expenses

/reports/operational-cost
```

---

# 📷 Screenshots

Add screenshots here.

- Landing Page
- Dashboard
- Vehicle Management
- Driver Management
- Trip Management
- Maintenance
- Fuel Logs
- Expenses
- Reports
- Swagger UI

---

# 👨‍💻 Team Members

| Name | Role |
|------|------|
| Uttam Maurya | Backend Developer |
| Aman | Frontend |
| Team Member | UI Development |
| Team Member | Documentation |

---

# 🚀 Future Enhancements

- JWT Authentication
- Role-Based Access Control
- GPS Tracking
- Live Vehicle Location
- Email Notifications
- Predictive Maintenance using AI
- Analytics Dashboard
- Export Reports (PDF & Excel)
- Dark Mode
- Mobile Responsive UI

---

# 🏆 Hackathon

Developed for the **Odoo Hackathon**.

---

# 📄 License

This project is developed for educational and hackathon purposes.

---

# ⭐ Thank You

Thank you for exploring TransitOps!

If you like this project, please consider giving it a ⭐ on GitHub.