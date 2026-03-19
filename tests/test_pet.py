import pytest
from resources.data_generator import generate_pet_payload, generate_data_for_update, generate_pet_update_payload
from resources.pet_api import ApiPet

def test_create_new_pet():
    payload = generate_pet_payload()
    pets = ApiPet()
    create_response = pets.add_a_new_pet(payload)
    assert create_response.status_code == 200, "Статус код должен быть 200"
    create_body = create_response.json()
    pet_id = create_body["id"]
    print(pet_id)
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

@pytest.mark.delete
def test_delete_pet(created_pet):
    pet_id = created_pet["pet_id"]
    print(pet_id)

    pets = ApiPet()

    delete_response = pets.delete_pet(pet_id)
    assert delete_response.status_code == 200, "Статус код должен быть 200"

    get_response = pets.get_pet_by_id(pet_id)
    get_body = get_response.json()
    assert get_response.status_code == 404, "Статус код должен быть 404"
    assert get_body["type"] == "error"
    assert get_body["message"] == "Pet not found"

@pytest.mark.get
def test_get_pet_by_status(created_pet):
    payload = created_pet["payload"]
    pet_status = payload["status"]
    pet_id = payload["id"]

    pets = ApiPet()

    get_response = pets.get_pets_by_status(pet_status)
    assert get_response.status_code == 200, "Статус код должен быть 200"

    body_response = get_response.json()
    assert any(pet["id"] == pet_id for pet in body_response), "В ответе нет питомца с нужным id"

def test_update_pet_with_form_data(created_and_delete_pet):
    data = generate_data_for_update()
    payload = created_and_delete_pet["payload"]
    pet_id = created_and_delete_pet["pet_id"]
    print(pet_id)

    pets = ApiPet()

    update_response = pets.update_name_and_status_by_form_data(pet_id, data)
    assert update_response.status_code == 200, "Статус код должен быть 200"

    get_response = pets.get_pet_by_id(pet_id)
    assert get_response.status_code == 200, "Статус код должен быть 200"

    body = get_response.json()

    assert body["id"] == pet_id, "id не соответсвует запрошенному"
    assert body["category"]["id"] == payload["category"]["id"], "id категории не соответсвует"
    assert body["category"]["name"] == payload["category"]["name"], "имя категории не соответсвует"
    assert body["name"] == data["name"], "имя не соответсвует"
    assert body["photoUrls"] == payload["photoUrls"], "ссылка на изображение не соответсвует"
    assert body["tags"][0]["id"] == payload["tags"][0]["id"], "id тега не соответсвует"
    assert body["tags"][0]["name"] == payload["tags"][0]["name"], "название тега не соответсвует"
    assert body["status"] == data["status"], "статус не соответсвует"

@pytest.mark.upd
def test_update_pet(created_pet):
    pet_id=created_pet["pet_id"]
    print(pet_id)
    before_payload = created_pet["payload"]
    print(before_payload)
    payload = generate_pet_update_payload(id=pet_id)
    print(payload)

    pets = ApiPet()

    update_response = pets.update_pet(payload)
    assert update_response.status_code == 200, "Статус код должен быть 200"

    get_response = pets.get_pet_by_id(pet_id)
    body = get_response.json()
    print(body)

    assert body["id"] == pet_id, "id не соответсвует запрошенному"
    assert body["category"]["id"] == payload["category"]["id"], "id категории не соответсвует"
    assert body["category"]["name"] == payload["category"]["name"], "имя категории не соответсвует"
    assert body["name"] == payload["name"], "имя не соответсвует"
    assert body["photoUrls"] == payload["photoUrls"], "ссылка на изображение не соответсвует"
    assert body["tags"][0]["id"] == payload["tags"][0]["id"], "id тега не соответсвует"
    assert body["tags"][0]["name"] == payload["tags"][0]["name"], "название тега не соответсвует"
    assert body["status"] == payload["status"], "статус не соответсвует"








