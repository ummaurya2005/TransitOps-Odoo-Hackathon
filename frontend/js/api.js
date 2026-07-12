const BASE_URL = "http://127.0.0.1:8000";

// ==========================
// VEHICLES
// ==========================

async function getVehicles() {
    const response = await fetch(`${BASE_URL}/vehicles`);
    return await response.json();
}

async function createVehicle(vehicle) {
    const response = await fetch(`${BASE_URL}/vehicles`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(vehicle)
    });

    return await response.json();
}

async function updateVehicle(id, vehicle) {
    const response = await fetch(`${BASE_URL}/vehicles/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(vehicle)
    });

    return await response.json();
}

async function deleteVehicle(id) {
    const response = await fetch(`${BASE_URL}/vehicles/${id}`, {
        method: "DELETE"
    });

    return await response.json();
}

// ==========================
// DRIVERS
// ==========================

async function getDrivers() {
    const response = await fetch(`${BASE_URL}/drivers`);
    return await response.json();
}

async function createDriver(driver) {
    const response = await fetch(`${BASE_URL}/drivers`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(driver)
    });

    return await response.json();
}

async function deleteDriver(id) {
    const response = await fetch(`${BASE_URL}/drivers/${id}`, {
        method: "DELETE"
    });

    return await response.json();
}

// ==========================
// TRIPS
// ==========================

async function getTrips() {
    const response = await fetch(`${BASE_URL}/trips`);
    return await response.json();
}

async function createTrip(trip) {
    const response = await fetch(`${BASE_URL}/trips`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(trip)
    });

    return await response.json();
}

async function dispatchTrip(id) {
    const response = await fetch(`${BASE_URL}/trips/${id}/dispatch`, {
        method: "PATCH"
    });

    return await response.json();
}

async function completeTrip(id) {
    const response = await fetch(`${BASE_URL}/trips/${id}/complete`, {
        method: "PATCH"
    });

    return await response.json();
}

async function cancelTrip(id) {
    const response = await fetch(`${BASE_URL}/trips/${id}/cancel`, {
        method: "PATCH"
    });

    return await response.json();
}

// ==========================
// MAINTENANCE
// ==========================

async function getMaintenance() {
    const response = await fetch(`${BASE_URL}/maintenance`);
    return await response.json();
}

async function createMaintenance(data) {
    const response = await fetch(`${BASE_URL}/maintenance`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    return await response.json();
}

// ==========================
// FUEL LOGS
// ==========================

async function getFuelLogs() {
    const response = await fetch(`${BASE_URL}/fuel-logs`);
    return await response.json();
}

async function createFuelLog(data) {
    const response = await fetch(`${BASE_URL}/fuel-logs`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    return await response.json();
}

// ==========================
// EXPENSES
// ==========================

async function getExpenses() {
    const response = await fetch(`${BASE_URL}/expenses`);
    return await response.json();
}

async function createExpense(data) {
    const response = await fetch(`${BASE_URL}/expenses`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    return await response.json();
}

// ==========================
// DASHBOARD
// ==========================

async function getDashboard() {
    const response = await fetch(`${BASE_URL}/dashboard`);
    return await response.json();
}

// ==========================
// REPORTS
// ==========================

async function getVehicleReport() {
    const response = await fetch(`${BASE_URL}/reports/vehicles`);
    return await response.json();
}

async function getDriverReport() {
    const response = await fetch(`${BASE_URL}/reports/drivers`);
    return await response.json();
}

async function getTripReport() {
    const response = await fetch(`${BASE_URL}/reports/trips`);
    return await response.json();
}

async function getFuelReport() {
    const response = await fetch(`${BASE_URL}/reports/fuel`);
    return await response.json();
}

async function getExpenseReport() {
    const response = await fetch(`${BASE_URL}/reports/expenses`);
    return await response.json();
}

async function getOperationalCost() {
    const response = await fetch(`${BASE_URL}/reports/operational-cost`);
    return await response.json();
}