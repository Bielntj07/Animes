import json

animes_data = [
    {
        "id": 1,
        "name": "Naruto",
        "description": "A história de um jovem ninja em sua jornada para se tornar Hokage...",
        "image": "assets/imagens/naruto.jpg",
        "characters": [
            {"id": 1, "name": "Naruto Uzumaki", "description": "O protagonista da série que busca reconhecimento e poder...", "image": "assets/imagens/naruto-uzumaki.jpg"},
            {"id": 2, "name": "Sasuke Uchiha", "description": "O rival de Naruto, buscando vingança e poder...", "image": "assets/imagens/sasuke-uchiha.jpg"},
            {"id": 3, "name": "Sakura Haruno", "description": "A ninja médica do time 7, com habilidades excepcionais...", "image": "assets/imagens/sakura-haruno.jpg"},
            {"id": 4, "name": "Kakashi Hatake", "description": "O lendário ninja copiador, conhecido por suas técnicas únicas...", "image": "assets/imagens/kakashi-hatake.jpg"},
            {"id": 5, "name": "Itachi Uchiha", "description": "O irmão de Sasuke, com um passado complexo e trágico...", "image": "assets/imagens/itachi-uchiha.jpg"},
            {"id": 6, "name": "Jiraiya", "description": "O Sannin Eterno, mentor de Naruto e mestre em técnicas poderosas...", "image": "assets/imagens/jiraiya.jpg"},
            {"id": 7, "name": "Orochimaru", "description": "O Sannin que busca a imortalidade e possui habilidades terríveis...", "image": "assets/imagens/orochimaru.jpg"},
            {"id": 8, "name": "Tsunade", "description": "A Sannin Médica e uma das ninjas mais fortes, conhecida por suas habilidades de cura...", "image": "assets/imagens/tsunade.jpg"},
            {"id": 9, "name": "Minato Namikaze", "description": "O Quarto Hokage, pai de Naruto, conhecido por sua velocidade e habilidades...", "image": "assets/imagens/minato-namikaze.jpg"},
            {"id": 10, "name": "Kushina Uzumaki", "description": "A mãe de Naruto, com um passado significativo e habilidades poderosas...", "image": "assets/imagens/kushina-uzumaki.jpg"},
            {"id": 11, "name": "Hiruzen Sarutobi", "description": "O Terceiro Hokage, conhecido por sua sabedoria e liderança...", "image": "assets/imagens/hiruzen-sarutobi.jpg"},
            {"id": 12, "name": "Danzo Shimura", "description": "O líder dos Anbu, com métodos questionáveis e ambições ocultas...", "image": "assets/imagens/danzo-shimura.jpg"},
            {"id": 13, "name": "Kurenai Yuhi", "description": "A jounin especialista em genjutsu, com habilidades mentais excepcionais...", "image": "assets/imagens/kurenai-yuhi.jpg"},
            {"id": 14, "name": "Asuma Sarutobi", "description": "O jounin especialista em taijutsu, conhecido por seu espírito e habilidades...", "image": "assets/imagens/asuma-sarutobi.jpg"},
            {"id": 15, "name": "Shikamaru Nara", "description": "O estrategista do time 10, conhecido por sua inteligência e habilidades táticas...", "image": "assets/imagens/shikamaru-nara.jpg"},
            {"id": 16, "name": "Ino Yamanaka", "description": "A especialista em jutsu mental, com habilidades em controle da mente...", "image": "assets/imagens/ino-yamanaka.jpg"},
            {"id": 17, "name": "Choji Akimichi", "description": "O membro do time 10 com habilidades de expansão, conhecido por sua força...", "image": "assets/imagens/choji-akimichi.jpg"},
            {"id": 18, "name": "Neji Hyuga", "description": "O prodígio do clã Hyuga, com habilidades impressionantes de taijutsu e visão...", "image": "assets/imagens/neji-hyuga.jpg"},
            {"id": 19, "name": "Hinata Hyuga", "description": "Hinata é a prima de Neji, com habilidades excepcionais e uma personalidade gentil...", "image": "assets/imagens/hinata-hyuga.jpg"},
            {"id": 20, "name": "Rock Lee", "description": "O ninja que não usa jutsu, conhecido por sua dedicação e habilidades físicas...", "image": "assets/imagens/rock-lee.jpg"}
        ]
    },
    {
        "id": 2,
        "name": "Dragon Ball Z",
        "description": "Uma aventura épica com guerreiros poderosos lutando para proteger o universo...",
        "image": "assets/imagens/dbz.jpg",
        "characters": [
            {"id": 21, "name": "Goku", "description": "O guerreiro Saiyajin que defende a Terra com força e coragem...", "image": "assets/imagens/goku.jpg"},
            {"id": 22, "name": "Vegeta", "description": "O príncipe dos Saiyajins, com um orgulho imenso e habilidades de combate...", "image": "assets/imagens/vegeta.jpg"},
            {"id": 23, "name": "Gohan", "description": "O filho de Goku, conhecido por seu potencial e habilidades únicas...", "image": "assets/imagens/gohan.jpg"},
            {"id": 24, "name": "Piccolo", "description": "O Namekuseijin guerreiro que se tornou um grande aliado da Terra...", "image": "assets/imagens/piccolo.jpg"},
            {"id": 25, "name": "Freeza", "description": "O imperador do universo, conhecido por sua crueldade e poder imenso...", "image": "assets/imagens/freeza.jpg"},
            {"id": 26, "name": "Cell", "description": "O bio-androide perfeito, com habilidades que desafiam os guerreiros da Terra...", "image": "assets/imagens/cell.jpg"},
            {"id": 27, "name": "Majin Boo", "description": "A criatura mágica com poderes devastadores e uma personalidade peculiar...", "image": "assets/imagens/majin-boo.jpg"},
            {"id": 28, "name": "Android 18", "description": "A androide poderosa, conhecida por suas habilidades de combate e força...", "image": "assets/imagens/android-18.jpg"},
            {"id": 29, "name": "Android 17", "description": "O irmão gêmeo de Android 18, com habilidades excepcionais e uma missão própria...", "image": "assets/imagens/android-17.jpg"},
            {"id": 30, "name": "Broly", "description": "O Saiyajin Lendário, com um poder colossal e uma história trágica...", "image": "assets/imagens/broly.jpg"},
            {"id": 31, "name": "Bills", "description": "O Deus da Destruição, com um poder inigualável e uma personalidade única...", "image": "assets/imagens/bills.jpg"},
            {"id": 32, "name": "Whis", "description": "O anjo assistente de Bills, conhecido por sua sabedoria e habilidades...", "image": "assets/imagens/whis.jpg"},
            {"id": 33, "name": "Zamasu", "description": "O Deus da Justiça, com uma visão distorcida sobre o universo...", "image": "assets/imagens/zamasu.jpg"},
            {"id": 34, "name": "Jiren", "description": "O guerreiro mais forte do Universo 11, com habilidades incríveis e determinação...", "image": "assets/imagens/jiren.jpg"},
            {"id": 35, "name": "Hit", "description": "O assassino do Universo 6, conhecido por suas habilidades mortais e estratégia...", "image": "assets/imagens/hit.jpg"},
            {"id": 36, "name": "Gotenks", "description": "A fusão de Goten e Trunks, com habilidades combinadas e uma personalidade divertida...", "image": "assets/imagens/gotenks.jpg"},
            {"id": 37, "name": "Goku Black", "description": "Um dos vilões mais perigosos da saga Dragon Ball Super, Goku Black é uma versão alternativa e maligna de Goku...", "image": "assets/imagens/goku-black.jpg"}
        ]
    },
    {
        "id": 3,
        "name": "One Piece",
        "description": "As aventuras de um grupo de piratas em busca do tesouro lendário...",
        "image": "assets/imagens/onepiece.jpg",
        "characters": [
            {"id": 38, "name": "Monkey D. Luffy", "description": "O capitão dos Piratas do Chapéu de Palha, com um sonho de encontrar o One Piece...", "image": "assets/imagens/luffy.jpg"},
            {"id": 39, "name": "Roronoa Zoro", "description": "O espadachim da tripulação, conhecido por sua habilidade com três espadas...", "image": "assets/imagens/zoro.jpg"},
            {"id": 40, "name": "Nami", "description": "A navegadora da tripulação, com habilidades em navegação e cartografia...", "image": "assets/imagens/nami.jpg"},
            {"id": 41, "name": "Sanji", "description": "O cozinheiro dos Piratas do Chapéu de Palha, com habilidades culinárias e de combate...", "image": "assets/imagens/sanji.jpg"},
            {"id": 42, "name": "Usopp", "description": "O atirador da tripulação, conhecido por suas habilidades com o sniper e sua criatividade...", "image": "assets/imagens/usopp.jpg"},
            {"id": 43, "name": "Tony Tony Chopper", "description": "O médico e reindeer da tripulação, com habilidades médicas e transformações...", "image": "assets/imagens/chopper.jpg"},
            {"id": 44, "name": "Nico Robin", "description": "A arqueóloga da tripulação, com habilidades de leitura de Poneglyphs e poderes únicos...", "image": "assets/imagens/robin.jpg"},
            {"id": 45, "name": "Franky", "description": "O cyborg e carpinteiro, com habilidades de construção e força sobre-humana...", "image": "assets/imagens/franky.jpg"},
            {"id": 46, "name": "Brook", "description": "O músico da tripulação, com habilidades musicais e um corpo esquelético...", "image": "assets/imagens/brook.jpg"},
            {"id": 47, "name": "Jinbe", "description": "O timoneiro e membro dos Homens-Peixe, com habilidades de combate e uma forte lealdade...", "image": "assets/imagens/jinbe.jpg"},
            {"id": 48, "name": "Portgas D. Ace", "description": "O irmão de Luffy e comandante da Segunda Divisão dos Piratas do Barba Branca, com um poder flamejante...", "image": "assets/imagens/ace.jpg"},
            {"id": 49, "name": "Trafalgar D. Water Law", "description": "O capitão dos Piratas Heart, com habilidades de cirurgia e uma personalidade complexa...", "image": "assets/imagens/law.jpg"},
            {"id": 50, "name": "Shanks", "description": "O capitão dos Piratas do Ruivo, com um poder formidável e uma influência global...", "image": "assets/imagens/shanks.jpg"},
            {"id": 51, "name": "Barba Negra", "description": "O maior rival de Luffy, com habilidades únicas e um passado sombrio...", "image": "assets/imagens/barba-negra.jpg"},
            {"id": 52, "name": "Kaido", "description": "Um dos Quatro Imperadores, com um poder devastador e uma presença temida...", "image": "assets/imagens/kaido.jpg"},
            {"id": 53, "name": "Big Mom", "description": "Uma das Quatro Imperadoras, conhecida por sua força e um apetite voraz...", "image": "assets/imagens/big-mom.jpg"}
        ]
    }
]

with open('animes.json', 'w') as file:
    json.dump(animes_data, file, indent=4)
    
print("Arquivo animes.json gerado com sucesso!")
