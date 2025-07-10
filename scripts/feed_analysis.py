import pandas as pd

# Загрузка данных
df = pd.read_csv("data/sample_feed_data.csv")

# Вычисляем метрики
df["CTR"] = df["clicks"] / df["impressions"]
df["CPC"] = df["spend"] / df["clicks"]
df["CR"] = df["conversions"] / df["clicks"]

# Группировка по дате
daily_summary = df.groupby("date")[["impressions", "clicks", "conversions", "spend"]].sum()
daily_summary["CTR"] = daily_summary["clicks"] / daily_summary["impressions"]
daily_summary["CPC"] = daily_summary["spend"] / daily_summary["clicks"]

# Сохранение отчета
daily_summary.to_csv("data/daily_summary.csv")
print("Отчет успешно сохранён.")
