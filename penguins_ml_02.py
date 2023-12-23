import pandas as pd

penguin_df = pd.read_csv('penguins.csv')

penguin_df.dropna(inplace=True)
output = penguin_df['species']
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)
print('Here are our output variables')
print(output.head())
print('Here are our feature variables')
print(features.head())

