function filterProducts(category) {
    const cards = document.querySelectorAll(".product-card");

    cards.forEach(card => {
        if (category === "all") {
            card.style.display = "block";
        } else {
            card.style.display = card.classList.contains(category)
                ? "block"
                : "none";
        }
    });

    document.querySelectorAll(".product-filters button").forEach(btn => {
        btn.classList.remove("active");
    });
}
