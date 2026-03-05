from Grupo3_Class import APIClient

ObjectAPIClient = APIClient()

response = ObjectAPIClient.factCats(5, 100, True)

print(response)
