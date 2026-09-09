import dataiku
import pandas as pd

# Lire les taux Silver
input_dataset = dataiku.Dataset("Silver_exchange_rates_prepared")
df = input_dataset.get_dataframe()

# S'assurer que rate_date est bien une date
df["rate_date"] = pd.to_datetime(df["rate_date"])

# Trier
df = df.sort_values("rate_date")

# Créer un calendrier journalier complet
full_dates = pd.DataFrame({
    "rate_date": pd.date_range(
        start=df["rate_date"].min(),
        end=df["rate_date"].max(),
        freq="D"
    )
})

# Joindre les taux existants
daily = full_dates.merge(
    df[["rate_date", "base_currency", "target_currency", "exchange_rate"]],
    on="rate_date",
    how="left"
)

# Propager le dernier taux connu
daily[["base_currency", "target_currency", "exchange_rate"]] = (
    daily[["base_currency", "target_currency", "exchange_rate"]].ffill()
)

# Écrire le résultat
output_dataset = dataiku.Dataset("exchange_rates_daily")
output_dataset.write_with_schema(daily)