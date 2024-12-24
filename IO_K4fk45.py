import os
import time
import random
from colorama import Fore, init
import instaloader


init(autoreset=True)


world_fig = """
     _____
    /     \\
   |  O O  |
    \  ^  /
     |||||
     |||||
"""


def show_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + world_fig)
    print(Fore.GREEN + "\n\nK4FK45 TARAFINDAN YAPILMIŞTIR!\n")
    time.sleep(2)  


def matrix_effect():
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(20):  
        line = ''.join(random.choice("01") for _ in range(80))
        print(Fore.GREEN + line)
        time.sleep(0.1)


def show_signature():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "\n" * 10) 
    print(Fore.GREEN + "K4FK45 TARAFINDAN YAPILMIŞTIR!")
    time.sleep(3)  


def get_instagram_data(username):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
        
        return {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Bio": profile.biography,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Profile Pic URL": profile.profile_pic_url
        }
    except Exception as e:
        return f"Error retrieving Instagram data: {e}"


if __name__ == "__main__":
    show_intro()  
    matrix_effect()  
    show_signature()  
    

    instagram_username = input(Fore.GREEN + "\nLütfen Instagram kullanıcı adını girin: ")
    
   
    data = get_instagram_data(instagram_username)
    
    if isinstance(data, dict):
        for key, value in data.items():
            print(Fore.GREEN + f"{key}: {value}")
    else:
        print(Fore.RED + data)

    input(Fore.YELLOW + "\nÇıkmak için Enter'a basın...")
