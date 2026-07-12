async function loadDrivers() {

    const drivers = await getDrivers();

    const table = document.getElementById("driverTable");

    table.innerHTML = "";

    drivers.forEach(driver => {

        table.innerHTML += `

        <tr>

            <td>${driver.id}</td>

            <td>${driver.name}</td>

            <td>${driver.license_number}</td>

            <td>${driver.license_category}</td>

            <td>${driver.status}</td>

            <td>

                <button onclick="removeDriver(${driver.id})">

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

}

document
.getElementById("driverForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const driver = {

        name:
            document.getElementById("name").value,

        license_number:
            document.getElementById("license_number").value,

        license_category:
            document.getElementById("license_category").value,

        license_expiry_date:
            document.getElementById("license_expiry_date").value,

        contact_number:
            document.getElementById("contact_number").value,

        safety_score:
            parseFloat(document.getElementById("safety_score").value),

        status:"Available"

    };

    try {

    await createDriver(driver);

    alert("✅ Driver created successfully!");

    this.reset();

    loadDrivers();

} catch (error) {

    alert("❌ Failed to create driver.");

}

});

async function removeDriver(id){

    await deleteDriver(id);

    loadDrivers();

}

loadDrivers();