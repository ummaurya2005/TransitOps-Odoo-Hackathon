document.addEventListener("DOMContentLoaded", async () => {

    try {

        const data = await getDashboard();

        document.getElementById("totalVehicles").innerText =
            data.total_vehicles;

        document.getElementById("availableVehicles").innerText =
            data.available_vehicles;

        document.getElementById("onTrip").innerText =
            data.vehicles_on_trip;

        document.getElementById("drivers").innerText =
            data.total_drivers;

        document.getElementById("activeTrips").innerText =
            data.active_trips;

        document.getElementById("maintenance").innerText =
            data.maintenance_records;

        document.getElementById("fuelCost").innerText =
            "₹" + data.fuel_cost;

        document.getElementById("expenseCost").innerText =
            "₹" + data.expense_cost;

        document.getElementById("utilization").innerText =
            data.fleet_utilization + "%";

        const ctx = document.createElement("canvas");
        document.querySelector(".main").appendChild(ctx);

        new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["Available", "On Trip", "In Shop"],
                datasets: [{
                    label: "Vehicles",
                    data: [
                        data.available_vehicles,
                        data.vehicles_on_trip,
                        data.vehicles_in_shop
                    ]
                }]
            }
        });

    } catch (error) {

        console.error(error);

        alert("Unable to load dashboard.");

    }

});