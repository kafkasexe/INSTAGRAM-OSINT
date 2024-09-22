import os
import time
import random
from colorama import Fore, init
import instaloader

# Colorama başlatma
init(autoreset=True)

# Dünya figürü
world_fig = """
     _____
    /     \\
   |  O O  |
    \  ^  /
     |||||
     |||||
"""

# K4FK45 TARAFINDAN YAPILMIŞTIR yazısı
def show_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + world_fig)
    print(Fore.GREEN + "\n\nK4FK45 TARAFINDAN YAPILMIŞTIR!\n")
    time.sleep(2)  # 2 saniye bekleme

# Matrix sayıları efekti
def matrix_effect():
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(20):  # Ekrana 20 satır döktürür
        line = ''.join(random.choice("01") for _ in range(80))
        print(Fore.GREEN + line)
        time.sleep(0.1)

# K4FK45 TARAFINDAN YAPILMIŞTIR yazısı Matrix sonrasında
def show_signature():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "\n" * 10)  # Ekranın ortasına almak için boş satırlar
    print(Fore.GREEN + "K4FK45 TARAFINDAN YAPILMIŞTIR!")
    time.sleep(3)  # 3 saniye bekleme

# Instagram veri çekme fonksiyonu
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

# Ana program
if __name__ == "__main__":
    show_intro()  # Dünya figürü ve yazı
    matrix_effect()  # Matrix sayı efekti
    show_signature()  # Ortada K4FK45 yazısı
    
    # Kullanıcıdan Instagram kullanıcı adını sor
    instagram_username = input(Fore.GREEN + "\nLütfen Instagram kullanıcı adını girin: ")
    
    # Kullanıcı bilgilerini çek ve ekrana yazdır
    data = get_instagram_data(instagram_username)
    
    if isinstance(data, dict):
        for key, value in data.items():
            print(Fore.GREEN + f"{key}: {value}")
    else:
        print(Fore.RED + data)

    input(Fore.YELLOW + "\nÇıkmak için Enter'a basın...")
