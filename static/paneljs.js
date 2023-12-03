document.addEventListener('DOMContentLoaded', function () {
    loadAnimation();
    setInterval(updateData, 5000);
});

function loadAnimation() {
    // Vous pouvez ajouter du code JavaScript ici pour personnaliser l'animation
    console.log('Animation loaded.');
}

function updateData() {
    fetch('/get_data')
        .then(response => response.json())
        .then(data => {
            updateSection('avatars', data.avatars);
            updateSection('worlds', data.worlds);
        })
        .catch(error => console.error('Error updating data:', error));
}

function updateSection(sectionId, items) {
    const container = document.getElementById(sectionId + '-container');
    
    // Nouveau code pour créer un conteneur
    const sectionContainer = document.getElementById(sectionId + '-container');
    sectionContainer.innerHTML = '';

    // Vérifier si 'items' est défini et s'il a une longueur supérieure à 0
    if (items && items.length > 0) {
        items.forEach(item => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <img src="${item.thumbnailImageUrl}" alt="${item.name}">
                <h3>${item.name}</h3>
                <p>${item.description}</p>
                <button onclick="showDetails('${item.id}', '${sectionId}')">More Details</button>
            `;
            sectionContainer.appendChild(card);
        });
    } else {
        // Ajoutez un message dans le conteneur si 'items' est indéfini ou vide
        sectionContainer.innerHTML = '<p>No items available</p>';
    }
}
