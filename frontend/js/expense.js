async function loadExpenses() {

    const expenses = await getExpenses();

    const table = document.getElementById("expenseTable");

    table.innerHTML = "";

    expenses.forEach(expense => {

        table.innerHTML += `

        <tr>

            <td>${expense.id}</td>

            <td>${expense.vehicle_id}</td>

            <td>${expense.expense_type}</td>

            <td>₹${expense.amount}</td>

            <td>${expense.expense_date}</td>

        </tr>

        `;

    });

}

document
.getElementById("expenseForm")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const expense = {

        vehicle_id:
        parseInt(document.getElementById("vehicle_id").value),

        expense_type:
        document.getElementById("expense_type").value,

        amount:
        parseFloat(document.getElementById("amount").value),

        description:
        document.getElementById("description").value,

        expense_date:
        document.getElementById("expense_date").value

    };

    await createExpense(expense);

    this.reset();

    loadExpenses();

});

loadExpenses();