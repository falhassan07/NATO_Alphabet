import pandas as pd 

df = pd.read_csv('nato_phonetic_alphabet.csv')

df_dict = { row.letter:row.code for (index, row) in df.iterrows()}

print(df_dict)