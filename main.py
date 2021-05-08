#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []
l_choose = []
n_choose = []
s_choose = []

countL = 0
for l in letters:
  countL += 1

for rl in range(0, nr_letters):
  indexL = random.randint(0, (countL-1))
  l_choose.insert(rl,letters[indexL])

countN = 0
for n in numbers:
  countN += 1

for rn in range(0, nr_numbers):
  indexN = random.randint(0, (countN-1))
  n_choose.insert(rn,numbers[indexN])

countS = 0
for s in symbols:
  countS += 1

for rs in range(0, nr_symbols):
  indexS = random.randint(0, (countS-1))
  s_choose.insert(rl,symbols[indexS])

password.extend(l_choose)
password.extend(n_choose)
password.extend(s_choose)
password.sort

#randomize the position without duplicate values
random.shuffle(password)

password_string = "".join(password)
print(f"\nYour new password is {password_string}")