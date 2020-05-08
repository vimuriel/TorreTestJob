import requests

class User:

    @classmethod
    def getDataUser(user):
        url= f'https://bio.torre.co/api/bios/{user}'
        return   requests.get(url)
