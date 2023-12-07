import unittest
from fastapi.testclient import TestClient
from main import app


class TestPokemonAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_pokemon_real(self):
        response = self.client.get("/snorlax")
        self.assertEqual(response.status_code, 200)
        expected_data = {"Name": "Snorlax", "ID": 143, "Type": ["Normal"],
                         "Image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/143.png",
                         "Height": "2.1 m", "Weight": "460.0 kg", "Abilities": ["Immunity", "Thick-fat", "Gluttony"]}
        self.assertEqual(response.json(), expected_data)

    def test_get_pokemon_fake(self):
        response = self.client.get("/dog")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Pokemon not found"})


if __name__ == "__main__":
    unittest.main()
