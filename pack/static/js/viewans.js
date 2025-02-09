
document.addEventListener('DOMContentLoaded', () => {
    const headers = document.querySelectorAll('.responses-table th');
    headers.forEach((header, index) => {
        if (index > 2) { 
            header.addEventListener('click', () => {
                const rows = document.querySelectorAll('.responses-table tr');
                rows.forEach(row => {
                    const cell = row.querySelectorAll('td')[index];
                    if (cell) {
                        cell.style.display = cell.style.display === 'none' ? '' : 'none';
                    }
                });
            });
        }
    });
});