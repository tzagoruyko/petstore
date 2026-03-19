from resources.api_base import ApiBase

class ApiPet(ApiBase):
    PATH = "/pet"

    def add_a_new_pet(self, payload):
        return self.post(self.PATH, json=payload)

    def get_pet_by_id(self, pet_id):
        return self.get(f"{self.PATH}/{pet_id}")

    def get_pets_by_status(self, status):
        return self.get(f"{self.PATH}/findByStatus", params={"status": status})

    def update_pet(self, payload):
        return self.put(self.PATH, json=payload)

    def update_name_and_status_by_form_data(self, pet_id, data):
        return self.post(f"{self.PATH}/{pet_id}", data=data)

    def delete_pet(self, pet_id):
        return self.delete(f"{self.PATH}/{pet_id}")



