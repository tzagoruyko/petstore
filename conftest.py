import pytest
from resources.pet_api import ApiPet
from resources.data_generator import generate_pet_payload


@pytest.fixture
def created_pet():
    payload = generate_pet_payload()
    pets = ApiPet()

    create_response = pets.add_a_new_pet(payload)
    assert create_response.status_code == 200, "Статус код должен быть 200"
    response_body = create_response.json()

    return {
        "pet_id": response_body["id"],
        "payload": payload
    }


@pytest.fixture
def created_and_delete_pet():
    payload = generate_pet_payload()
    pets = ApiPet()

    create_response = pets.add_a_new_pet(payload)
    assert create_response.status_code == 200, "Статус код должен быть 200"
    response_body = create_response.json()
    pet_id = response_body["id"]

    yield {
        "pet_id": pet_id,
        "payload": payload
    }

    delete_response = pets.delete_pet(pet_id)
    assert delete_response.status_code == 200, "Статус код должен быть 200"

