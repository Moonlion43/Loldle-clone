# Dictionary of champions with empty lists
champions = {
    "Aatrox": [], "Ahri": [], "Akali": [], "Alistar": [], "Amumu": [], "Anivia": [], "Annie": [], "Aphelios": [], "Ashe": [],
    "Aurelion Sol": [], "Aurora": [], "Azir": [], "Bard": [], "Bel'Veth": [], "Blitzcrank": [], "Brand": [], "Braum": [],
    "Caitlyn": [], "Camille": [], "Cassiopeia": [], "Cho'Gath": [], "Corki": [], "Darius": [], "Diana": [], "Dr. Mundo": [],
    "Draven": [], "Ekko": [], "Elise": [], "Evelynn": [], "Ezreal": [], "Fiddlesticks": [], "Fiora": [], "Fizz": [],
    "Galio": [], "Gangplank": [], "Garen": [], "Gnar": [], "Gragas": [], "Graves": [], "Gwen": [], "Hecarim": [],
    "Heimerdinger": [], "Illaoi": [], "Irelia": [], "Ivern": [], "Janna": [], "Jarvan IV": [], "Jax": [], "Jayce": [],
    "Jhin": [], "Jinx": [], "K'Sante": [], "Kai'Sa": [], "Kalista": [], "Karma": [], "Karthus": [], "Kassadin": [],
    "Katarina": [], "Kayle": [], "Kayn": [], "Kennen": [], "Kha'Zix": [], "Kindred": [], "Kled": [], "Kog'Maw": [],
    "LeBlanc": [], "Lee Sin": [], "Leona": [], "Lillia": [], "Lissandra": [], "Lucian": [], "Lulu": [], "Lux": [],
    "Malphite": [], "Malzahar": [], "Maokai": [], "Master Yi": [], "Milio": [], "Miss Fortune": [], "Mordekaiser": [],
    "Morgana": [], "Naafiri": [], "Nami": [], "Nasus": [], "Nautilus": [], "Neeko": [], "Nidalee": [], "Nilah": [],
    "Nocturne": [], "Nunu '&' Willump": [], "Olaf": [], "Orianna": [], "Ornn": [], "Pantheon": [], "Poppy": [], "Pyke": [],
    "Qiyana": [], "Quinn": [], "Rakan": [], "Rammus": [], "Rek'Sai": [], "Rell": [], "Renata Glasc": [], "Renekton": [],
    "Rengar": [], "Riven": [], "Rumble": [], "Ryze": [], "Samira": [], "Sejuani": [], "Senna": [], "Seraphine": [],
    "Sett": [], "Shaco": [], "Shen": [], "Shyvana": [], "Singed": [], "Sion": [], "Sivir": [], "Skarner": [], "Smolder": [],
    "Sona": [], "Soraka": [], "Swain": [], "Sylas": [], "Syndra": [], "Tahm Kench": [], "Taliyah": [], "Talon": [],
    "Taric": [], "Teemo": [], "Thresh": [], "Tristana": [], "Trundle": [], "Tryndamere": [], "Twisted Fate": [],
    "Twitch": [], "Udyr": [], "Urgot": [], "Varus": [], "Vayne": [], "Veigar": [], "Vel'Koz": [], "Vex": [], "Vi": [],
    "Viego": [], "Viktor": [], "Vladimir": [], "Volibear": [], "Warwick": [], "Wukong": [], "Xayah": [], "Xerath": [],
    "Xin Zhao": [], "Yasuo": [], "Yone": [], "Yorick": [], "Yuumi": [], "Zac": [], "Zed": [], "Zeri": [], "Ziggs": [],
    "Zilean": [], "Zoe": [], "Zyra": []
}

# Open and read the .txt file
with open("loldle_champions.txt", "r", encoding="utf-8") as file:
    current_champion = None  # Track the current champion

    for line in file:
        line = line.strip()  # Remove leading/trailing spaces
        line = line.replace("’", "'")  # Normalize apostrophes

        # Check if the line specifies a champion
        if line.startswith("Champion: Not Found"):
            champion_name = ""
        elif line.startswith("Champion: "):
            champion_name = line.replace("Champion: ", "").strip()
            if champion_name == "Not Found":
                champion_name = ""
            
            if champion_name in champions:
                current_champion = champion_name
                print(f"✔ Found champion: {current_champion}")  # Debug print
            else:
                current_champion = None
                print(f"❌ Champion not found in dictionary: {champion_name}")  # Debug print
            
        # If a champion is found, extract attributes
        elif current_champion and ": " in line:
            key, value = line.split(": ", 1)  # Split into key and value
            value = value.strip()  # Remove extra spaces

            # Skip 'Not Found' values
            if value != "Not Found":
                champions[current_champion].append(value)
                print(f"✅ Added '{value}' to {current_champion}")  # Debug print

# Print updated dictionary
import pprint
pprint.pprint(champions)

