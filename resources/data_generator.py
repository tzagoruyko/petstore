import random

def generate_pet_payload(**overrides):
    pet_id = random.randint(100000, 500000)
    payload = {
        "id": pet_id,
        "category": {
            "id": random.randint(1, 10),
            "name": random.choice(["Dogs", "Cats"])
        },
        "name": random.choice(["Ralf", "Barny"]),
        "photoUrls": [
            "https://animal-photo.com/photo.jpg"
        ],
        "tags": [
            {
                "id": random.randint(1, 10),
                "name": random.choice(["cute", "small"])
            }
        ],
        "status": "available"
    }
    payload.update(overrides)
    return payload

def generate_pet_update_payload(**overrides):
    pet_id = random.randint(500001, 999999)
    payload = {
        "id": pet_id,
        "category": {
            "id": random.randint(11, 20),
            "name": random.choice(["Dogs upd", "Cats upd"])
        },
        "name": random.choice(["Ralf upd", "Barny upd"]),
        "photoUrls": [
            "https://animal-photo-upd.com/photo.jpg"
        ],
        "tags": [
            {
                "id": random.randint(11, 20),
                "name": random.choice(["cute upd", "small upd"])
            }
        ],
        "status": "sold"
    }
    payload.update(overrides)
    return payload

def generate_data_for_update(**overrides):
    data = {"name": random.choice(["Barsik", "Persik"]), "status": "sold"}
    data.update(overrides)
    return data