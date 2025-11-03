import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv", index_col="letter")
nato_dict_df = nato_df.to_dict()

# pandas way — simpler, same result
# nato_dict = nato_df["code"].to_dict()

# Using Comprehension
nato_dict = { key:value for key,value in nato_dict_df['code'].items()}

user_input = input("Enter anything: ").upper()

input_to_nato = [nato_dict[value] for value in user_input]

print(input_to_nato)