import requests
from prototypes import User


class API:
    def __init__(self):
        self.GET = requests.get
        self.POST = requests.post
        self.URL = "http://localhost:8080"  # local api
        self.authed = False

    def direct_req(self, endpoint: str, data: dict, req_type) -> dict:
        data = req_type(self.URL + endpoint, json=data, headers={"Authorization": f"Bearer {self.authed}"})
        if data.status_code == 200:
            return data.json()
        else:
            return {"status": False, "req_failed": data.status_code}

    def get_user(self, user_id: int, as_obj: bool = False) -> dict:
        res = self.direct_req(f"/users/{user_id}/info", {}, self.GET)
        if as_obj:
            return User(res)
        else:
            return res
    
    def auth(self, login: str, password: str, auth_api: bool = True):
        auth_data = self.direct_req("/auth/login", {"email": login, "password": password}, self.POST)
        if not "req_failed" in auth_data:
            if auth_api:
                self.authed = auth_data['accessToken']
            return auth_data['accessToken']
        else:
            return False
