const counters = document.querySelectorAll('.counter');

counters.forEach(counter => {
    let count = 0;
    const target = parseInt(counter.innerText);

    const update = () => {
        const increment = target / 100;

        if (count < target) {
            count += increment;
            counter.innerText = Math.ceil(count) + "+";
            setTimeout(update, 20);
        } else {
            counter.innerText = target + "+";
        }
    };

    update();
});


function filterCards(category) {
    let items = document.querySelectorAll('.filter-item');
    let buttons = document.querySelectorAll('.filter-btn');

    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    items.forEach(item => {
        if (category === 'all' || item.classList.contains(category)) {
            item.style.display = "block";
        } else {
            item.style.display = "none";
        }
    });
}


// SIP Calculator
let chart;

function calculateSIP() {
    let P = document.getElementById("amount").value;
    let rate = document.getElementById("rate").value;
    let years = document.getElementById("years").value;

    document.getElementById("amountValue").innerText = P;
    document.getElementById("rateValue").innerText = rate;
    document.getElementById("yearsValue").innerText = years;

    let r = rate / 12 / 100;
    let n = years * 12;

    let maturity = P * ((Math.pow(1 + r, n) - 1) / r) * (1 + r);
    let invested = P * n;
    let returns = maturity - invested;

    document.getElementById("invested").innerText = Math.round(invested);
    document.getElementById("returns").innerText = Math.round(returns);
    document.getElementById("total").innerText = Math.round(maturity);

    updateChart(invested, returns);
}

function updateChart(invested, returns) {
    const ctx = document.getElementById('sipChart');

    if (chart) chart.destroy();

    chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Invested', 'Returns'],
            datasets: [{
                data: [invested, returns],
                backgroundColor: ['#3a86ff', '#fca311']
            }]
        }
    });
}

document.querySelectorAll("input").forEach(input => {
    input.addEventListener("input", calculateSIP);
});

calculateSIP();



