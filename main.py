from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()


def preprocess_response(poke_info):
    poke_dict = {"Name": poke_info["name"].capitalize(),
                 "ID": poke_info["id"],
                 "Type": [t["type"]["name"].capitalize() for t in poke_info["types"]],
                 "Image": poke_info["sprites"]["other"]["home"]["front_default"],
                 "Height": f"{int(poke_info['height'])*0.1} m",
                 "Weight": f"{int(poke_info['weight'])*0.1} kg",
                 "Abilities": [a['ability']['name'].capitalize() for a in poke_info["abilities"]]}
    return poke_dict


@app.get("/{pokemon_name}")
def get_pokemon_info(pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    with httpx.Client() as client:
        response = client.get(url)

    if response.status_code == 200:
        return preprocess_response(response.json())
    else:
        raise HTTPException(status_code=response.status_code, detail="Pokemon not found")

