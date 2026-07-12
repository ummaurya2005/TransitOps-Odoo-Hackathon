async function loadFuelLogs() {

    const logs = await getFuelLogs();

    const table = document.getElementById("fuelTable");

    table.innerHTML = "";

    logs.forEach(log => {

        table.innerHTML += `

        <tr>

            <td>${log.id}</td>

            <td>${log.vehicle_id}</td>

            <td>${log.liters}</td>

            <td>₹${log.cost}</td>

            <td>${log.fuel_date}</td>

        </tr>

        `;

    });

}

document
.getElementById("fuelForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const fuel = {

        vehicle_id:
        parseInt(document.getElementById("vehicle_id").value),

        liters:
        parseFloat(document.getElementById("liters").value),

        cost:
        parseFloat(document.getElementById("cost").value),

        fuel_date:
        document.getElementById("fuel_date").value

    };

    await createFuelLog(fuel);

alert("✅ Fuel log added successfully!");

this.reset();

loadFuelLogs();

});

loadFuelLogs();