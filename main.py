#BY KAI

from requests import get, post
from random import randint
import colorama

BB = '''\033[1;34m ____  _        _    ____ _  __  ____  _     ___   ___  ____   
| __ )| |      / \  / ___| |/ / | __ )| |   / _ \ / _ \|  _ \  
|  _ \| |     / _ \| |   | ' /  |  _ \| |  | | | | | | | | | | 
| |_) | |___ / ___ \ |___| . \  | |_) | |__| |_| | |_| | |_| | 
|____/|_____/_/   \_\____|_|\_\ |____/|_____\___/ \___/|____/  
                                                               \n-BY \33[31mK\033[1;90mA\33[32mI\033[1;34m 
        
-DISCORD = https://discord.gg/BB7\n'''
print (BB)

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant2(token) == True:
                  print(f'\033[32mToken: {token} is Valid\033[37m\n')
                    
                  checked.append(token)
                else:
                    print(f'\033[31mToken: {token} is Invalid\033[37m\n')
        if len(checked) > 0:
            save = input(f'\033[1;34m{len(checked)} valid tokens\nSave to File (y/n)').lower()
            if save == 'y':
                name = randint(100000000, 9999999999)
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'Tokens Save To {name}.txt File!')
        input('Press Enter For Exit...')
    except:
        input('Can`t Open "tokens.txt" File!')