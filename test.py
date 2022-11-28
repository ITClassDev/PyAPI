from shtpapi import API as api

if __name__ == "__main__":
    API = api()
    json = API.get_user(1)
    obj = API.get_user(1, as_obj=True)
    print(obj)