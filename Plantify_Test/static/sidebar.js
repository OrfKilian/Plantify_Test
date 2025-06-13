document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/items')
        .then(response => response.json())
        .then(data => {

            const list = document.getElementById('sidebar-list');
            list.innerHTML = '';

            data.forEach(item => {
                const li = document.createElement('li');
                const link = document.createElement('a');
                link.href = `/pflanze/${item.name.toLowerCase().replace(/\s+/g, '-')}`;

                // Einheitliches, neutrales Icon (🪴)
                link.innerHTML = `🪴 <span class="sidebar-text">${item.name}</span>`;

                li.appendChild(link);
                list.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Fehler beim Laden der Sidebar:', error);
        });
});
