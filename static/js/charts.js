// admin-panel/static/js/charts.js

document.addEventListener("DOMContentLoaded", function () {
    // Example: Display leaderboard chart if canvas exists
    const leaderboardCanvas = document.getElementById("leaderboardChart");
    if (leaderboardCanvas) {
        const ctx = leaderboardCanvas.getContext("2d");

        // Dummy data - replace with dynamic data from Flask
        const usernames = JSON.parse(leaderboardCanvas.dataset.usernames);
        const scores = JSON.parse(leaderboardCanvas.dataset.scores);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: usernames,
                datasets: [{
                    label: 'Scores',
                    data: scores,
                    backgroundColor: 'rgba(54, 162, 235, 0.7)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});
