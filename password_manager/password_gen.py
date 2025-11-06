import random

def password_generator():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
        password_numbers = [random.choice(numbers) for _ in range(random.randint(4,6))]
        password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]

        password=[x for lst in [password_letters,password_numbers,password_symbols] for x in lst]
        #password = password_letters + password_numbers + password_symbols
        random.shuffle(password)

        passkey="".join(password)
        return passkey