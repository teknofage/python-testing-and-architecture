# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


user_name_input = input('Please enter your username: ')
save_into_db(user_name_input)
user_birth_input = int(input('Please enter your birth year: '))
age = 2020 - user_birth_input
print("You are",age, "years old.")