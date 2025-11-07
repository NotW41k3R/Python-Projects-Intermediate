import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv", index_col="letter")
nato_dict_df = nato_df.to_dict()

# pandas way: simpler and same result
# nato_dict = nato_df["code"].to_dict()

# Using Comprehension
nato_dict = { key:value for key,value in nato_dict_df['code'].items()}

# Error Catching
# Using a function
def convert_to_nato():
    user_input = input("Enter anything: ").upper()
    try:
        input_to_nato = [nato_dict[value] for value in user_input]
    except KeyError:
        print("Sorry only alphabets are allowed")
        convert_to_nato()
    else:
        print(input_to_nato)

convert_to_nato()
# Using a Loop
# is_on = True
# while is_on:
#     user_input = input("Enter anything: ").upper()
#     try:
#         input_to_nato = [nato_dict[value] for value in user_input]
#         is_on = False
#     except KeyError:
#         print("Sorry only alphabets are allowed")
#         is_on = True
#     else:
#         print(input_to_nato)