from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# List of champions to check
champ_list2 = ["Aatrox", "Ahri", "Akshan", "Alistar"]  # Keep short for testing

# Define the XPaths (fixed so each points to a single element)
xpaths = {
    "Champion": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[1]/div/div/div[1]',
    "Gender": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[2]/div/div/span',
    "Position": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[3]/div/div/div/div',
    "Position_2": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[3]/div/div/div/div[2]',
    "Position_3": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[3]/div/div/div/div[3]',
    "Species": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[4]/div/div/div/div',
    "Species_2": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[4]/div/div/div/div[2]',
    "Species_3": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[4]/div/div/div/div[3]',
    "Resource": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[5]/div/div/span',
    "Range Type": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[6]/div/div/div/div',
    "Range Type_2": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[6]/div/div/div/div[2]',
    "Region": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[7]/div/div/div/div',
    "Region2": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[7]/div/div/div/div[2]',
    "Release Year": '//*[@id="gameSubContainer"]/div[2]/div[4]/div[3]/div/div/div[8]/div/div/span'
}

# Open the text file for writing
with open("loldle_champions.txt", "w", encoding="utf-8") as file:

    for champ in champ_list:
        print(f"Processing: {champ}")

        # Open a new browser session for each champion
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in the background
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(options=options)

        try:
            # Open the website
            driver.get("https://loldle.net/classic")
            time.sleep(2)

            # Accept cookie consent if present
            try:
                consent_button = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p"))
                )
                driver.execute_script("arguments[0].click();", consent_button)
                print("✅ Consent popup closed.")
            except:
                print("⚠️ No consent popup found.")

            # Find and interact with the input field
            input_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
            )
            input_field.click()
            input_field.send_keys(champ)
            input_field.send_keys(Keys.RETURN)

            # Wait for results to load
            time.sleep(5)

            # Extract champion data
            file.write(f"Champion: {champ}\n")  # Start with champion name

            for key, xpath in xpaths.items():
                try:
                    element = driver.find_element(By.XPATH, xpath)  # Get SINGLE element
                    value = element.text.strip()
                    file.write(f"{key}: {value if value else 'Not Found'}\n")
                except:
                    file.write(f"{key}: Not Found\n")

            file.write("\n---\n\n")  # Separator between champions
            print(f"✅ Data saved correctly for {champ}")

        except Exception as e:
            print(f"❌ Error processing {champ}: {e}")

        finally:
            driver.quit()  # Close browser

print("\n✅ Text file 'loldle_champions.txt' created successfully!")