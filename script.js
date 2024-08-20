document.addEventListener("DOMContentLoaded", () => {
    const animeList = document.getElementById("animeList");
    const searchInput = document.getElementById("searchInput");
    const backButton = document.getElementById("backButton");

    let animes = [];

    // Carregar dados dos animes a partir do JSON gerado por Python
    fetch('animes.json')
        .then(response => response.json())
        .then(data => {
            animes = data;
            displayAnimes(animes);
        });

    const displayAnimes = (animes) => {
        animeList.innerHTML = "";
        animes.forEach(anime => {
            const animeCard = document.createElement("div");
            animeCard.classList.add("anime-card");
            animeCard.innerHTML = `
                <img src="${anime.image}" alt="${anime.name}">
                <h2>${anime.name}</h2>
                <p>${anime.description}</p>
            `;
            animeCard.addEventListener("click", () => {
                displayCharacters(anime);
            });
            animeList.appendChild(animeCard);
        });
    };

    const displayCharacters = (anime) => {
        animeList.innerHTML = "";
        backButton.style.display = "block";
        anime.characters.forEach(character => {
            const characterCard = document.createElement("div");
            characterCard.classList.add("anime-card");
            characterCard.innerHTML = `
                <img src="${character.image}" alt="${character.name}">
                <h2>${character.name}</h2>
                <p>${character.description}</p>
            `;
            animeList.appendChild(characterCard);
        });
    };

    backButton.addEventListener("click", () => {
        backButton.style.display = "none";
        displayAnimes(animes);
    });

    searchInput.addEventListener("input", (event) => {
        const searchTerm = event.target.value.toLowerCase();
        const filteredAnimes = animes.filter(anime =>
            anime.name.toLowerCase().includes(searchTerm)
        );
        displayAnimes(filteredAnimes);
    });
});
