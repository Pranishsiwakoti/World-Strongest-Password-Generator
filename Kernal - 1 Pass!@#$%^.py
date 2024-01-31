# Imported the Random module
import random

# Define character sets for password generation
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '!@#$%^&*'
number = '0123456789'
brackets = '{}[]()'
letter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowerletter = 'qwertyuiopasdfghjklzxcvbnm'
ulsym = ',;.":*=+-_/?|<>~'

# Combine all character sets
all_characters = lower + upper + symbol + number + brackets + letter + lowerletter + ulsym

# Function to generate password based on user input for length
def generate_password(length):
    # Generate password using random.sample() to ensure no repeated characters
    password = "".join(random.sample(all_characters, length))
    return password

# Prompt the user to enter the length of the password
length = int(input("Enter the length of the password: "))

# Generate password and print it
password = generate_password(length)
print("The Generated Password is:", password)
print("Now you can apply this generated password wherever you want!")

# Add input prompt to prevent the window from closing immediately
input("Press Enter to exit...")
