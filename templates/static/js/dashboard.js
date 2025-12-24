document.addEventListener('DOMContentLoaded', function () {

    const ctx = document.getElementById('graficoEmprestimos');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: MESES,
            datasets: [{
                label: 'Total de Empréstimos',
                data: TOTAIS,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

});
