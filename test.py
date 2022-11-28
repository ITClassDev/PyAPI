from shtpapi import API as api

if __name__ == "__main__":
    API = api()
    print(API.get_user(1))
