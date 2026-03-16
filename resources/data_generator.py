import random

def generate_pet_payload(**overrides):
    pet_id = random.randint(100000, 999999)
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