import pandas as pd 

df = pd.read_csv('nato_phonetic_alphabet.csv')

df_dict = { row.letter:row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: ").upper()

nato_list = [ df_dict[char] for char in user_input if char.isalpha()]

print(nato_list)