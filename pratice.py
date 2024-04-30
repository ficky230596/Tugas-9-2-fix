import requests

api_key = "27eda5be-7693-43d5-bb5d-fd6c3194bf11"
word = "potato"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

res =requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)