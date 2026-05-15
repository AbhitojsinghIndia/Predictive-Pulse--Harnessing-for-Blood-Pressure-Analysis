const form = document.getElementById("predictionForm");

const button = document.getElementById("predictBtn");

const btnText = document.getElementById("btnText");

const loader = document.querySelector(".loader");

if(form){

    form.addEventListener("submit", () => {

        btnText.style.display = "none";

        loader.style.display = "block";

        button.style.opacity = "0.8";

    });

}

const resultBox = document.querySelector(".result-box");

if(resultBox){

    resultBox.style.opacity = "0";

    resultBox.style.transform = "translateY(20px)";

    setTimeout(() => {

        resultBox.style.opacity = "1";

        resultBox.style.transform = "translateY(0)";

        resultBox.style.transition = "1s";

    }, 300);

}

// Dynamic Chart

const ctx = document.getElementById('bpChart');

if(ctx){

    const chartLabels = JSON.parse(
        document.getElementById("chart-labels").textContent
    );

    const chartValues = JSON.parse(
        document.getElementById("chart-values").textContent
    );

    new Chart(ctx, {

        type: 'bar',

        data: {

            labels: chartLabels,

            datasets: [{

                label: 'Patient Count',

                data: chartValues,

                borderWidth: 1

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: 'white'

                    }

                }

            },

            scales: {

                y: {

                    ticks: {

                        color: 'white'

                    }

                },

                x: {

                    ticks: {

                        color: 'white'

                    }

                }

            }

        }

    });

}