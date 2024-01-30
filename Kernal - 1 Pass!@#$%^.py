print("Hey! Here you can get World Strongest Passwords")
# Imported the Random Here.
import random
# I have add some Accessories for password and you can add what ever you want.
lower = 'abcdefghijklmnopqrtuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '!@#$%^&*'
number = '0123456789'
# Here, I have add Emojis. This is optional. I add this Emojis to make more Password Stronger.
emoji = '😀😁😂🤣😎😛😜😝😡🤬'
brackets = '{}[]()'
letter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lowerletter = 'qwertyuiopasdfghjklzxcvbnm'
# ulsym is ULTRA SYMBOL which is very hard to Guess the Passwords.
ulsym = ',;.":*=+-_/?|<>~'

# Simply Mix all the Accessories by giving '+' Plus icon.
all = lower + upper + symbol + number + emoji + brackets + letter + lowerletter + ulsym
# Put you password length

length = 12
# This is the most Important Code line which Generate the Password.
password = "".join(random.sample(all,length))
# After this I have add a Print to Print the passoword which have been generate. It works to visible to us.
print("The Generated Password is: ",password )
# Here I have add my own Sentence. You can make your own. This is the Sentence after Password have been Generated.
print("Now you can Apply this Generated Password where you want to!")

# Important note:

# If you want to work this Program in you Machine follow this instruction.
# Step1: Copy this Code and Open VS Code or Other Code Editor and Press CTRL+F5 and you can view your Generated Password.
# If any problem you can ask me in GitHUB. Happy Cooding!
