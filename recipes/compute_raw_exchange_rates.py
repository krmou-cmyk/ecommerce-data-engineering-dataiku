import requests

url = "https://api.frankfurter.dev/v1/latest?base=BRL&symbols=EUR"

response = requests.get(url)
response.raise_for_status()

data = response.json()

print(data)