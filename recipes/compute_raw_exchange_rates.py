import requests
import pandas as pd
import dataiku

url = "https://api.frankfurter.dev/v1/2016-01-01..2018-12-31?base=BRL&symbols=EUR"

response = requests.get(url)
response.raise_for_status()

data = response.json()

rows = []

for date, rates in data["rates"].items():
    rows.append({
        "date": date,
        "base_currency": "BRL",
        "target_currency": "EUR",
        "exchange_rate": rates["EUR"]
    })

df = pd.DataFrame(rows)

output_dataset = dataiku.Dataset("raw_exchange_rates")
output_dataset.write_with_schema(df)