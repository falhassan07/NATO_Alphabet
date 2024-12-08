import pandas as pd 

df = pd.read_csv('nato_phonetic_alphabet.csv')

df_dict = { row.letter:row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        nato_list = [ df_dict[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()

    else:
        print(nato_list)


generate_phonetic()
        
    

