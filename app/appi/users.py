import requests

class User:

    @classmethod
    def getDataUser(user):
        url= f'https://bio.torre.co/api/bios/{user}'
        return   requests.get(url)


    def formatSkills(skills):
        lista = " "
        for skill in skills:
            lista = lista + " - " + skill
        return lista

