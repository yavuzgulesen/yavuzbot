import random

class PinterestClient:
    def __init__(self, config):
        self.__access_token = config.get("pinterest", "access_token")
        self.__board_id = config.get("pinterest", "board_id")

    # def pin(self, board_id):
    #     random_pin = self.__get_pin_from_board(board_id)
    #     self.__delete_pin(random_pin.get("id"))

    def get_pin_from_board(self):
        #url = f"{self.base_url}/boards/{board_id}/pins"
        response = "" #requests.get(url, headers=self.headers)

        if response.status_code == 200:
            random_img = random.Random().choice(response.json())
            #return response.json().get("items", [])
            return random_img
        else:
            print("Failed to fetch pins:", response.json())
            return []

    def delete_pin(self, pin_id):
        url = f"{self.base_url}/pins/{pin_id}"
        response = "" #requests.delete(url, headers=self.headers)
        if response.status_code == 204:
            print("Pin deleted successfully.")
        else:
            print("Failed to delete the pin:", response.json())


