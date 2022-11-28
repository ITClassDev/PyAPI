import requests


class API:
    def __init__(self):
        self.GET = requests.get
        self.POST = requests.post
        self.URL = "http://localhost:8080" # local api

    def direct_req(self, endpoint: str, data: dict, req_type) -> dict:
        data = req_type(self.URL + endpoint, data=data).json()
        return data

    def get_user(self, user_id: int) -> dict:
        return self.direct_req(f"/users/{user_id}/info", {}, self.GET)
