import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / 'data' / 'covid19.csv'


Covid_df = pd.read_csv(csv_path)

Covid_df = Covid_df.loc[:, ['Country', 'Date', 'Confirmed']]

print(Covid_df.head())
print(Covid_df.shape)