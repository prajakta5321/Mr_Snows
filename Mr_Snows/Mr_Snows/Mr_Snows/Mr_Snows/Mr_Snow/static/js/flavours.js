function filterFlavours(type) {
    let cards = document.querySelectorAll('.flavour-card');
    let buttons = document.querySelectorAll('.filter-buttons button');

    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    cards.forEach(card => {
        if (type === 'all' || card.classList.contains(type)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}
