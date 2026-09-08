"base_currency"import requests
import pandas as pd
import dataiku

url = "https://api.frankfurter.dev/v1/latest?base=BRL&symbols=EUR"

response = requests.get(url)
response.raise_for_status()

data = response.json()

df = pd.DataFrame([{
    "date": data["date"],
    "base_currency": data["base"],
    "target_currency": "EUR",
    "exchange_rate": data["rates"]["EUR"]
}])

output_dataset = dataiku.Dataset("raw_exchange_rates")
output_dataset.write_with_schema(df)