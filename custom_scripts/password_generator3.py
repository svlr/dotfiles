import random
from colorama import init, Fore, Back
import os
from datetime import date
from time import sleep


init(autoreset=True)


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def save_to_file(pswds):
    with open(os.getcwd() + "/passwords_info.txt", "a") as file:
        for i in pswds:
            print(Fore.MAGENTA + i)
            service = input(
                Fore.YELLOW
                + "Enter the name of the service for which this password was used >>> "
            )
            file.write(f"password - {i}; date - {date.today()}; service - {service}\n")


def generator(len, num, answ):
    chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    chars1 = "1234567890"
    chars2 = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passwords = []
    for i in range(num):
        password = ""
        for j in range(len):
            if answ == "n":
                password += random.choice(chars1)
            elif answ == "l":
                password += random.choice(chars2)
            else:
                password += random.choice(chars)
        passwords.append(password)
    for i in passwords:
        print(Fore.MAGENTA + i)
    while True:
        quest = input(
            Fore.GREEN + 'Do you want to save the generated passwords "Y" or "N" >>> '
        ).lower()
        if quest == "y":
            save_to_file(passwords)
            return
        elif quest == "n":
            return
        else:
            print(Fore.RED + "Not the intended answer!!!")


while True:
    cls()
    print(
        Back.MAGENTA
        + """
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝"""
    )
    print(
        Fore.CYAN
        + """Enter "G" to generate the password
Enter "Q" to exit the script
Enter "S" to save the password to a file"""
    )
    answ = input(Fore.CYAN + ">>> ").lower()
    if answ == "g":
        print(
            Fore.GREEN
            + """Do you want to generate a password from numbers, letters or both
Enter "N" to generate a password from numbers
Enter "L" to generate a password from letters
Enter "B" to generate a password from numbers and letters"""
        )
        while True:
            answ2 = input(Fore.CYAN + ">>> ").lower()
            if answ2 == "n":
                break
            elif answ2 == "b":
                break
            elif answ2 == "l":
                break
            else:
                print(Fore.RED + "Not the intended answer!!!")
        while True:
            try:
                len_passwd = int(
                    input(Fore.GREEN + "Enter the password length >>> "))
                if len_passwd == 0:
                    print(Fore.RED + "You can't enter a zero!!!")
                    continue
                break
            except ValueError:
                print(Fore.RED + "You didn't enter a number!!!")
                continue
        while True:
            try:
                num_passwd = int(
                    input(Fore.GREEN + "Enter the number of passwords >>> ")
                )
                if num_passwd == 0:
                    print(Fore.RED + "You can't enter a zero!!!")
                    continue
                break
            except ValueError:
                print(Fore.RED + "You didn't enter a number!!!")
                continue
        generator(len_passwd, num_passwd, answ2)
    elif answ == "q":
        print(Fore.CYAN + "Have a nice day!!!")
        quit()
    elif answ == "s":
        print(
            Fore.GREEN
            + "Enter the passwords that you want to save, separated by semicolons"
        )
        passwords = input(Fore.CYAN + ">>> ").split("; ")
        save_to_file(passwords)
    else:
        print(Fore.RED + "Not the intended answer!!!")
        sleep(3)
