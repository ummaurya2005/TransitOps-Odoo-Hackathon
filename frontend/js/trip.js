async function loadTrips() {

    const trips = await getTrips();

    const table = document.getElementById("tripTable");

    table.innerHTML = "";

    trips.forEach(trip => {

        table.innerHTML += `

        <tr>

        <td>${trip.id}</td>

        <td>${trip.source}</td>

        <td>${trip.destination}</td>

        <td>${trip.vehicle_id}</td>

        <td>${trip.driver_id}</td>

        <td>${trip.status}</td>

        <td>

        <button onclick="dispatch(${trip.id})">

        Dispatch

        </button>

        </td>

       <td>

    <button onclick="completeTripAction(${trip.id})">

    Complete

    </button>

    </td>
        <td>

        <button onclick="cancelTripFrontend(${trip.id})">

        Cancel

        </button>

        </td>

        </tr>

        `;

    });

}

document
.getElementById("tripForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const trip = {

        source:
        document.getElementById("source").value,

        destination:
        document.getElementById("destination").value,

        vehicle_id:
        parseInt(document.getElementById("vehicle_id").value),

        driver_id:
        parseInt(document.getElementById("driver_id").value),

        cargo_weight:
        parseFloat(document.getElementById("cargo_weight").value),

        planned_distance:
        parseFloat(document.getElementById("planned_distance").value),

        trip_date:
        document.getElementById("trip_date").value,

        status:"Draft"

    };

    await createTrip(trip);

    this.reset();

    loadTrips();

});

async function dispatch(id){

    await dispatchTrip(id);

    loadTrips();

}

async function completeTripAction(id){

    await completeTrip(id);

    loadTrips();

}

async function cancelTripFrontend(id){

    await cancelTrip(id);

    loadTrips();

}

loadTrips();