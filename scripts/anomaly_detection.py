import pandas as pd
from scipy.stats import zscore

# Загрузка данных
df = pd.read_csv("data/sample_feed_data.csv")

# Считаем Z-оценку по показам
df["z_impressions"] = zscore(df["impressions"])

# Фильтрация аномалий
anomalies = df[abs(df["z_impressions"]) > 2]

# Сохраняем
anomalies.to_csv("data/impression_anomalies.csv", index=False)
print("Найдено аномалий:", len(anomalies))
