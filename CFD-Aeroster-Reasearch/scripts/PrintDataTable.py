import pandas as pd
import itertools

# Define the values for columns 1 and 2
values = [-30,-20, -10, 0, 10, 20, 30]

# Generate all possible ordered pairs
pairs = list(itertools.product(values, repeat=2))

# Create a DataFrame with 6 columns
df = pd.DataFrame(pairs, columns=['Column1', 'Column2'])

# Fill column 0 with 0.1
df.insert(0, 'Column0', 0)

# Fill the remaining columns with 0.1
for i in range(3, 6):
    df[f'Column{i}'] = 0

# Output the DataFrame to a CSV file with ',' as the decimal separator
df.to_csv('output.csv', index=False, decimal=',')
