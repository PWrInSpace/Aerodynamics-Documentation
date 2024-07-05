import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('output.csv')

for col in data.columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

print(data.isna().sum())
print(data.describe())


data.hist(figsize=(10, 8))

plt.show()