#######################################
### Password Generator
#######################################

from time import sleep
import string
import secrets

def contain_upper(pwd: str) -> bool:
    for char in pwd:
        if char.isupper():
            return True
        
    return False    

def contain_symbol(pwd: str) -> bool:
    for char in pwd:
        if char in string.punctuation:
            return True
        
    return False

def generate_pwd(length: int, symbol: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbol:
        combination += string.punctuation
    
    if uppercase:
        combination += string.ascii_uppercase
    
    combination_length = len(combination)
    new_pwd: str = ''

    for _ in range(length):
        new_pwd += combination[secrets.randbelow(combination_length)]

    return new_pwd

tries: int = 3
while tries > 0:
    issym: str = input('Password contain Special Symbols? (yes/no) >> ').lower()

    if issym == 'yes':
        symm: bool = True
        tries = 0
    elif issym == 'no':
        symm: bool = False
        tries = 0
    else:
        print('Please input the right answer! You have 2 more tries...')
        tries -= 1
        if tries == 0:
            print('No more tries remaining. Exiting...')
            break

tries1: int = 3
up: bool
while tries1 > 0:
    isup: str = input('Password contain Uppercase letters? (yes/no) >> ').lower()

    if isup == 'yes':
        up: bool = True
        tries1 = 0
    elif isup == 'no':
        up: bool = False
        tries1 = 0
    else:
        print('Please input the right answer! You have 2 more tries...')
        tries1 -= 1
        if tries1 == 0:
            print('No more tries remaining. Exiting...')
            break

print('')
print('Generating password...')
sleep(1)

passw: str = generate_pwd(length=10, symbol=bool(symm), uppercase=bool(up))
#specs: str = f'U: {contain_upper(passw)}, S: {contain_symbol(passw)}'

print(f'Password generated -> {passw}')




