async function loadMaintenance() {

    const records = await getMaintenance();

    const table = document.getElementById("maintenanceTable");

    table.innerHTML = "";

    records.forEach(record => {

        table.innerHTML += `

        <tr>

            <td>${record.id}</td>

            <td>${record.vehicle_id}</td>

            <td>${record.maintenance_type}</td>

            <td>₹${record.cost}</td>

            <td>${record.status}</td>

            <td>

                <button onclick="completeMaintenance(${record.id})">

                    Complete

                </button>

            </td>

        </tr>

        `;

    });

}

document
.getElementById("maintenanceForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const maintenance = {

        vehicle_id:
            parseInt(document.getElementById("vehicle_id").value),

        maintenance_type:
            document.getElementById("maintenance_type").value,

        description:
            document.getElementById("description").value,

        cost:
            parseFloat(document.getElementById("cost").value),

        maintenance_date:
            document.getElementById("maintenance_date").value,

        status: "Open"

    };

    await createMaintenance(maintenance);

    this.reset();

    loadMaintenance();

});

async function completeMaintenance(id){

    const response = await fetch(
        `http://127.0.0.1:8000/maintenance/${id}/complete`,
        {
            method: "PATCH"
        }
    );

    if(response.ok){

        loadMaintenance();

    }else{

        alert("Unable to complete maintenance.");

    }

}

loadMaintenance();