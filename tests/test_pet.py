import pytest
from resources.pet_api import ApiPet

def test_add_a_new_pet_to_the_store():
    payload = {
  "id": 13032026,
  "category": {
    "id": 1,
    "name": "Собаки"
  },
  "name": "Ральф",
  "photoUrls": [
    "https://dogs.com/"
  ],
  "tags": [
    {
      "id": 2,
      "name": "Той пудель"
    }
  ],
  "status": "available"
}
    pets = ApiPet()
    create_response = pets.add_a_new_pet(payload)
    assert create_response.status_code == 200, "Статус код должен быть 200"
    create_body = create_response.json()
    pet_id = create_body["id"]
    assert pet_id == payload["id"]

    get_response = pets.get_pet_by_id(pet_id)
    assert get_response.status_code == 200, "Статус код должен быть 200"
    body = get_response.json()
    assert body["id"] == pet_id, "id не соответсвует запрошенному"
    assert body["category"]["id"] == payload["category"]["id"], "id категории не соответсвует"
    assert body["category"]["name"] == payload["category"]["name"], "имя категории не соответсвует"
    assert body["name"] == payload["name"], "имя не соответсвует"
    assert body["photoUrls"] == payload["photoUrls"], "ссылка на изображение не соответсвует"
    assert body["tags"][0]["id"] == payload["tags"][0]["id"], "id тега не соответсвует"
    assert body["tags"][0]["name"] == payload["tags"][0]["name"], "название тега не соответсвует"
    assert body["status"] == payload["status"], "статус не соответсвует"





