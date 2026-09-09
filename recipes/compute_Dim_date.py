import dataiku
import pandas as pd

# Lire fact_orders pour récupérer la période réelle des commandes
fact_orders = dataiku.Dataset("Fact_order____prepared").get_dataframe()

fact_orders["order_date"] = pd.to_datetime(fact_orders["order_date"])

start_date = fact_orders["order_date"].min()
end_date = fact_orders["order_date"].max()

# Générer le calendrier complet
dates = pd.date_range(
    start=start_date,
    end=end_date,
    freq="D"
)

df = pd.DataFrame({
    "date": dates
})

# Attributs calendaires
df["year"] = df["date"].dt.year
df["quarter"] = df["date"].dt.quarter
df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.month_name()
df["day"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.day_name()
df["is_weekend"] = df["date"].dt.dayofweek >= 5

# Ecrire dans Dataiku
output_dataset = dataiku.Dataset("dim_date")
output_dataset.write_with_schema(df)