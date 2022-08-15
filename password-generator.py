import random

# Python password generator project.

# Alphabet plus numbers and symbols for the password generator function.
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

# Cluster variable for the random function.
For_password = lower_case + upper_case + number + symbols

# Length of the password.
length_of_password = 8

def password_generator():
  user_input = input("For new password type 'Go' to the console: ").upper()  # User input Variable.
  while (True):
   if user_input == "GO":
    password = "".join(random.sample(For_password, length_of_password))
    print("Your new password is: " + password)
    user_input = input("For new password type 'Go' to the console. To quit the program type 'Quit' to the console: ").upper()
   elif user_input != "GO" and user_input != "QUIT":
    print("Please enter the correct statement (Go).")
    user_input = input("For new password type 'Go' to the console. To quit the program type 'Quit' to the console: ").upper()
   elif user_input == "QUIT":
    print("Password generator has stopped.")
    break

password_generator()