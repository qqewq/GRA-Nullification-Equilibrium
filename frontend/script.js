document.getElementById('runBtn').addEventListener('click', runSimulation);

async function runSimulation() {
    const dim = parseInt(document.getElementById('dim').value) || 3;
    const steps = parseInt(document.getElementById('steps').value) || 10;

    // Generate random initial vectors
    const pi = Array.from({length: dim}, () => (Math.random()*2 - 1));
    const w = Array.from({length: dim}, () => (Math.random()*2 - 1));
    const s = Array.from({length: dim}, () => (Math.random()*2 - 1));

    const payload = { pi, w, s, steps };

    try {
        const response = await fetch('http://localhost:8000/simulate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        if (!response.ok) throw new Error('Server error');
        const data = await response.json();

        // Update output
        document.getElementById('finalPhi').textContent = data.phi_history[data.phi_history.length-1].toFixed(4);
        document.getElementById('finalPi').textContent = JSON.stringify(data.final_pi.slice(0, 5)) + (data.final_pi.length > 5 ? '...' : '');

        // Plot foam history
        const ctx1 = document.getElementById('foamChart').getContext('2d');
        if (window.foamChartInstance) window.foamChartInstance.destroy();
        window.foamChartInstance = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: data.phi_history.map((_, i) => i),
                datasets: [{
                    label: 'Foam Φ',
                    data: data.phi_history,
                    borderColor: '#e74c3c',
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: { display: true, text: 'Эволюция пены' }
                }
            }
        });

        // Plot first component of pi over time
        const piComp = data.pi_history.map(p => p[0] || 0);
        const ctx2 = document.getElementById('piChart').getContext('2d');
        if (window.piChartInstance) window.piChartInstance.destroy();
        window.piChartInstance = new Chart(ctx2, {
            type: 'line',
            data: {
                labels: data.phi_history.map((_, i) => i),
                datasets: [{
                    label: 'π₁ (первая компонента)',
                    data: piComp,
                    borderColor: '#2ecc71',
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: { display: true, text: 'Эволюция π₁' }
                }
            }
        });

    } catch (error) {
        alert('Ошибка: ' + error.message);
    }
}
