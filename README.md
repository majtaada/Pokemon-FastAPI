# Python Mikroslužba pre spracovánie dát

## Instalace

1. Nainštalujte requirements: !pip install -r requirements.txt
2. Spusťte: !uvicorn main:app --reload

## Použití

#### Spustenie dockeru
1. !docker build -t my-fastapi-app .
2. !docker run -p 8000:8000 -d my-fastapi-app


#### Otvoríte prehliadač a zadáte adresu a nakoniec pridáte meno pokémona, o ktorom chcete info získať
- **Endpoint:** /{pokemon_name}
#### napr.
- <http://127.0.0.1:8000/snorlax>

#### Alebo do terminálu zadáte príkaz
- !curl http://127.0.0.1:8000/pokemon/snorlax

#### Testy spustíme príkazom
- !python3 -m unittest unittests.py
#### Alebo pri spustenom dockeri
- !docker exec -it *číslo docker containera* python3 unittest.py


#### Vysvetlenie logiky

Táto mikroslužba používa framework FastAPI pre vytvorenie jednoduchého webového API, ktoré poskytuje informácie o Pokemónovi na základe mena. Je to riešené HTTP GET requestom na PokeAPI a získaná odpoveď je spracovaná vo formáte JSON.
