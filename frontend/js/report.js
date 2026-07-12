async function loadReports() {

    // Vehicle Report
    const vehicles = await getVehicleReport();

    document.getElementById("vehicleCount").innerText =
        vehicles.length;

    let vehicleTable = document.getElementById("vehicleReport");

    vehicleTable.innerHTML = "";

    vehicles.forEach(vehicle => {

        vehicleTable.innerHTML += `

        <tr>

        <td>${vehicle.id}</td>

        <td>${vehicle.registration_number}</td>

        <td>${vehicle.vehicle_name}</td>

        <td>${vehicle.status}</td>

        </tr>

        `;

    });

    // Driver Report
    const drivers = await getDriverReport();

    document.getElementById("driverCount").innerText =
        drivers.length;

    // Trip Report
    const trips = await getTripReport();

    document.getElementById("tripCount").innerText =
        trips.length;

    // Fuel Report
    const fuel = await getFuelReport();

    document.getElementById("fuelCount").innerText =
        fuel.length;

    // Expense Report
    const expense = await getExpenseReport();

    document.getElementById("expenseCount").innerText =
        expense.length;

    // Operational Cost
    const cost = await getOperationalCost();

    document.getElementById("totalCost").innerText =
        "₹" + cost.total_cost;

}

loadReports();