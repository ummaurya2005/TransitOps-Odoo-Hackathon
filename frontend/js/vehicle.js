async function loadVehicles() {

    const vehicles = await getVehicles();

    const table = document.getElementById("vehicleTable");

    table.innerHTML = "";

    vehicles.forEach(vehicle => {

        table.innerHTML += `

        <tr>

            <td>${vehicle.id}</td>

            <td>${vehicle.registration_number}</td>

            <td>${vehicle.vehicle_name}</td>

            <td>${vehicle.vehicle_type}</td>

            <td>${vehicle.status}</td>

            <td>

                <button onclick="removeVehicle(${vehicle.id})">

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

}

document
.getElementById("vehicleForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const vehicle = {

        registration_number:
            document.getElementById("registration_number").value,

        vehicle_name:
            document.getElementById("vehicle_name").value,

        vehicle_type:
            document.getElementById("vehicle_type").value,

        max_load_capacity:
            parseFloat(document.getElementById("max_load_capacity").value),

        odometer:
            parseFloat(document.getElementById("odometer").value),

        acquisition_cost:
            parseFloat(document.getElementById("acquisition_cost").value),

        acquisition_date:
            document.getElementById("acquisition_date").value,

        status: "Available",

        notes:
            document.getElementById("notes").value

    };

   try {

    await createVehicle(vehicle);

    alert("✅ Vehicle created successfully!");

    this.reset();

    loadVehicles();

} catch (error) {

    alert("❌ Failed to create vehicle.");

}

});

async function removeVehicle(id){

    await deleteVehicle(id);

alert("🗑️ Vehicle deleted successfully!");

loadVehicles();
}

loadVehicles();