import random
upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','&','*','(',')','+']
print("Welcome to password generator")
n_upper_letters = int(input("How many upper letters you wnat in your password?\n "))
n_lower_letters = int(input("How many lower letters you wnat in your password?\n "))
n_numbers = int(input("How many numbers you wnat in your password?\n "))
n_symbols = int(input("How many symbols letters you wnat in your password?\n "))
password_list = []
for i in range(1,n_upper_letters+1):
    char = random.choice(upper_letters)
    password_list += char
    
for i in range(1,n_lower_letters+1):
    char = random.choice(lower_letters)
    password_list += char

for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password_list += char

for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password_list += char
#print(password_list)
random.shuffle(password_list)
#print(password_list)
password = ""
for i in password_list:
    password += i
print(password)