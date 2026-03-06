import requests
import re

class APIClient:
    def __init__(self):
        self.base_url = "https://catfact.ninja/"
    
    def only1Fact(self, maxlenght):
        try:
            url = f"{self.base_url}fact"
            params = {"max_length":maxlenght}
            response = requests.get(url, params= params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None
        
    def moreThan1Fact(self, factNumber, maxlenght):
        try:
            url = f"{self.base_url}facts"
            params = {"max_length":maxlenght, "limit":factNumber}
            response = requests.get(url, params= params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None
        
    def trollJson(self, json):
        return [elem["fact"].replace("cats", "you").replace(" cat ", " you ").replace("Cats", "You").replace("Cat ", "You ") for elem in json["data"]]
        ###return re.sub("Cats", "People", [elem["fact"] for elem in json["data"]])


        
    
        
    def factCats(self, factNumber = 9999, maxLength = 9999, isTroll = False):
        if factNumber == 1:
            json = self.only1Fact(maxLength)
        else:
            json = self.moreThan1Fact(factNumber, maxLength)

        if isTroll:
            return self.trollJson(json)
        else:
            return [elem["fact"] for elem in json["data"]]
    