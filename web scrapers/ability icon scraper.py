import os
import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil

# List of champions to scrape
iterate_list = ["Cho'Gath"]

# Path to save images
BASE_PATH = r"C:\Users\henri\OneDrive - AARHUS TECH\2. G\Programmering\Skoleprojekter\Eksamen\ability icons"
os.makedirs(BASE_PATH, exist_ok=True)

# Set up Chrome for Selenium (DO NOT TOUCH THIS PART)
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)  # Your ChromeDriver setup is assumed to be correct

# Full list of edge‐case champion keys for Data Dragon
EXCEPTION_KEYS = {
    "Wukong":            "MonkeyKing",
    "Nunu & Willump":    "Nunu",
    "Renata Glasc":      "Renata",
    "Dr. Mundo":         "DrMundo",
    "LeBlanc":           "Leblanc",
    "Kai'Sa":            "Kaisa",
    "Kha'Zix":           "Khazix",
    "Bel'Veth":          "Belveth",
    "Vel'Koz":           "Velkoz",
    "K'Sante":           "KSante",
    "Rek'Sai":           "RekSai",
    "Cho'Gath":          "Chogath",
    "Kog'Maw":           "KogMaw",
}

def get_champ_key(champion_name: str) -> str:
    """Turn a raw champion name into the exact Data Dragon key."""
    # 1) If it’s one of our known exceptions, return that
    if champion_name in EXCEPTION_KEYS:
        return EXCEPTION_KEYS[champion_name]
    # 2) Otherwise strip non‐alphanumerics, title‐case, and remove spaces
    cleaned = re.sub(r'[^A-Za-z0-9 ]', '', champion_name)
    return cleaned.title().replace(" ", "")

def clear_champion_folder(champion_name):
    """
    Delete all files (and subfolders, if any) in BASE_PATH/champion_name,
    then recreate the empty folder.
    """
    champ_folder = os.path.join(BASE_PATH, champion_name)
    if os.path.exists(champ_folder):
        shutil.rmtree(champ_folder)         # remove folder and all contents
    os.makedirs(champ_folder, exist_ok=True)  # recreate empty folder

def scrape_and_download(champion_name):
    """
    Download passive + Q/W/E/R icons for the given champion
    using Riot’s Data Dragon API, clearing out any existing files first.
    """
    # 0) Clear out old images
    clear_champion_folder(champion_name)

    # 1) Get the latest Data Dragon version
    versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
    latest = versions[0]

    # 2) Load the champion JSON
    champ_key = get_champ_key(champion_name)
    url = f"https://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion/{champ_key}.json"
    data = requests.get(url).json()["data"][champ_key]

    # 3) Build a list of (filename, full-url)
    icons = []
    # passive
    p = data["passive"]["image"]["full"]
    icons.append((p, f"https://ddragon.leagueoflegends.com/cdn/{latest}/img/passive/{p}"))
    # spells Q/W/E/R
    for spell in data["spells"]:
        f = spell["image"]["full"]
        icons.append((f, f"https://ddragon.leagueoflegends.com/cdn/{latest}/img/spell/{f}"))

    # 4) Download each icon
    for idx, (fname, src) in enumerate(icons, start=1):
        try:
            download_image(src, champion_name, idx)
        except Exception as e:
            print(f"  ⚠️ Failed to download {fname} for {champion_name}: {e}")
        
def download_image(img_url, champion_name, icon_number):
    """Download image and save it locally under BASE_PATH."""
    try:
        # Get image content
        response = requests.get(img_url)
        response.raise_for_status()

        # Make sure the directory exists under your BASE_PATH
        dir_path = os.path.join(BASE_PATH, champion_name)
        os.makedirs(dir_path, exist_ok=True)

        # Construct the file path and save the image
        img_filename = f"{champion_name}_{icon_number}.png"
        img_path = os.path.join(dir_path, img_filename)
        
        # Write image to file
        with open(img_path, 'wb') as f:
            f.write(response.content)
        print(f"  ✅ Image saved to {img_path}")

    except requests.exceptions.RequestException as e:
        print(f"  ❌ Failed to download image for {champion_name} ability icon {icon_number}: {e}")


def rename_files_sequentially(champ_folder):
    """Rename all files in the folder sequentially (1.png, 2.png, ...)."""
    if not os.path.exists(champ_folder):
        print(f"  Folder does not exist: {champ_folder}")
        return
    
    files = sorted(
        [f for f in os.listdir(champ_folder) if f.endswith(".png")],
        key=lambda x: os.path.getmtime(os.path.join(champ_folder, x))
    )
    
    if not files:
        print(f"  No .png files found in {champ_folder}")
        return
    
    for i, file in enumerate(files):
        old_path = os.path.join(champ_folder, file)
        new_name = f"{i + 1}.png"
        new_path = os.path.join(champ_folder, new_name)
        os.rename(old_path, new_path)
        print(f"  Renamed: {old_path} -> {new_path}")

def main():
    for champ in iterate_list:
        try:
            print(f"\n>>> Processing: {champ}")
            scrape_and_download(champ)

            champ_folder = os.path.join(BASE_PATH, champ)
            rename_files_sequentially(champ_folder)
        except Exception as e:
            print(f"!!! ERROR with {champ}: {e}")
    
    driver.quit()

if __name__ == "__main__":
    main()
