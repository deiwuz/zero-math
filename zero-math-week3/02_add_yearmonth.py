import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / 'data' / 'countries-aggregated.csv'

df = pd.read_csv(csv_path)

df['Date'] = pd.to_datetime(df['Date'])
df['YearMonth'] = df['Date'].dt.strftime('%Y-%m')

print(df.head())