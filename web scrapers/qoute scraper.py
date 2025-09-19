from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

champ_list = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Ambessa", "Amumu", "Anivia", "Annie", "Aphelios",
    "Ashe", "Aurelion Sol", "Aurora", "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand",
    "Braum", "Briar", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki", "Darius",
    "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks",
    "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen",
    "Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV",
    "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin",
    "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw",
    "K'Sante", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu",
    "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Mel", "Milio", "Miss Fortune",
    "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee",
    "Nilah", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy",
    "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc",
    "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna",
    "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir",
    "Skarner", "Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah",
    "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere",
    "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz",
    "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong",
    "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed",
    "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra",
]

champ2_list = [
    "Aatrox", "Ziggs", "K'Sante", "Zoe", "Xin Zhao"
]

def format_name(champ):
    """Format champion name for URL."""
    return champ.replace(" ", "_").replace("'", "%27")

def check_for_bans(text, banned_strings):
    """Check if the quote contains any banned strings."""
    for banned_string in banned_strings:
        if banned_string in text:
            return True
    return False

def scrape_quotes_selenium(chosen_champ):
    url = f"https://wiki.leagueoflegends.com/en-us/{format_name(chosen_champ)}/Audio"
    
    # Set up Chrome options for headless mode.
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    # Initialize the webdriver (ensure chromedriver is in your PATH)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)  # wait for page to load

    # Attempt to locate the Trivia section and get its vertical position.
    try:
        trivia_element = driver.find_element(By.XPATH, '//span[@class="mw-headline" and @id="Trivia"]')
        trivia_y = trivia_element.location['y']
    except Exception as e:
        trivia_y = None  # If not found, we will scrape all quotes

    quotes = []
    
    banned_strings = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "%", 
        "grunts", "SFX", "sighs", "weeps", "pauses", 
        "shouts", "exhales", "huffs", "laughs", "scoffs",
        "Sound Effect", "clears", "yawns", "chuckles", 
        "exclaims", "Transmission static", "attack quotes",
        "hums", "Willump", "(", ")", "Resurrection", "gasps",
        "roars", "screams", 
    ]
    
    # Find all <i> elements (quotes) in the page
    quote_elements = driver.find_elements(By.TAG_NAME, "i")
    for el in quote_elements:
        # Get vertical position of the quote element
        el_y = el.location['y']
        
        # If Trivia section exists and this element is below it, stop processing.
        if trivia_y is not None and el_y > trivia_y:
            break
        
        text = el.text.strip()
        
        # Exclude quotes that are too short or contain banned terms
        if len(text) > 20 and not check_for_bans(text, banned_strings):
            if text[0] == '"':
                quotes.append(text)
    
    driver.quit()
    return quotes

def save_quotes(champ_name, quotes):
    filename = f"{champ_name}_quotes.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for quote in quotes:
            file.write(quote + "\n")

# Example usage:
for i in range(len(champ_list)):   
    chosen_champ = champ_list[i]  # or any champion name
    scraped_quotes = scrape_quotes_selenium(chosen_champ)
    save_quotes(chosen_champ, scraped_quotes)
    print(f"Scraped {len(scraped_quotes)} quotes for {chosen_champ}.")
