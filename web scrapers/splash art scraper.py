import os
import requests

# Where to save images
SPLASH_BASE = r"C:\Users\henri\OneDrive - AARHUS TECH\2. G\Programmering\Skoleprojekter\Eksamen\splash_images"

# Get champion list from Data Dragon
version = "15.9.1"
champ_list_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
champ_list = requests.get(champ_list_url).json()["data"]
champion_names = list(champ_list.keys())

def download_splash_image(champion_name, skin_num):
    url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champion_name}_{skin_num}.jpg"
    folder = os.path.join(SPLASH_BASE, champion_name)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{champion_name}_{skin_num}.jpg")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"  ✅ Saved: {champion_name}/{champion_name}_{skin_num}.jpg")
    except Exception as e:
        print(f"  ⚠️ Failed to download splash {champion_name}_{skin_num}: {e}")

def download_all_splashes():
    for champ in champion_names:
        try:
            print(f">>> Processing splashes for {champ}")
            champ_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{champ}.json"
            champ_data = requests.get(champ_url).json()
            champ_skins = champ_data["data"][champ]["skins"]
            for skin in champ_skins:
                skin_num = skin["num"]
                download_splash_image(champ, skin_num)
        except Exception as e:
            print(f"!!! ERROR with {champ}: {e}")

download_all_splashes()