import requests
import json
import colorama
import os
import platform
import sys
import time
import datetime
from time import sleep
from datetime import datetime

def cls():
    os.system("cls")


    

if not os.path.isfile("token.txt"):
    print("You dont have a token.txt file.. please input your token here!")
    
    token = input("Your token: ")
    time.sleep(2)
    cls()
    

else:
    file = open("token.txt", "r")
    token = file.read()
    


if platform.system() == "Windows":
    os.system("title Token Information")
elif platform.system() == "Linux":
    os.system("title Token Information")
else:
    os.system("title Token Information")


headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
}
req = requests.get(f"https://discordapp.com/api/v9/users/@me", headers=headers)
if req.status_code == 200:
    print("Vaild token! [Finding information...]")
    time.sleep(2)
else:
    print("Failed to find information! make sure you have a vaild token!")
    time.sleep(2)
    os._exit(0)


def main():
    info = req.json()
    user_id = info["id"]
    username = info["username"] + "#" + req.json()["discriminator"]
    email = info["email"]
    mfa = info["mfa_enabled"]
    phone = info["phone"]
    language = info["locale"]
    flags = info["flags"]
    avatar_id = info["avatar"]
    verified = info["verified"]
    nitro = False
    creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    nitro = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers)
    nitro_data = nitro.json()
    has_nitro = bool(len(nitro_data) > 0)
    

    


    print("---------------------------------------------")
    print("           Account information               ")
    print("---------------------------------------------")
    
    print(f"Username: {username}")
    print(f"User id: {user_id}")
    print(f"language: {language}")
    print(f"Account token: {token}")
    print(f"Avatar id: {avatar_id}")
    print(f"Flags: {flags}")
    print(f"Created at: {creation_date}")
    print(f"Has nitro: {has_nitro}")
    print(f"Verified: {verified}")

    

    print("----------------------------------------------")
    print("           Security information               ")
    print("----------------------------------------------")
    
    print(f"2fa: {mfa}")
    print(f"phone number: {phone}")
    print(f"email: {email}")

    input("press any key to exit....")
    os._exit(0)


    


main()