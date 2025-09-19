# Loldle-clone made entirely in python with tkinter
# Creator: https://github.com/Moonlion43
# Original website: https://loldle.net/classic 

from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import random
import textwrap

entry_images = [
    Path(r"misc images\Text Input.webp"),
    Path(r"misc images\Text Input Arrow.webp"),
]

icon_images = [
    Path(r"icons\Qoute.png"),
    Path(r"icons\Ability.png"),
    Path(r"icons\Splash.png"),
]

background_image = Path(r"misc images\Darkened Wallpaper.webp")

lebron_texts = [
    "lebron",
    "lebron james",
    "the goat",
    "goat",
]

champ_header_texts = [
    "Champion",
    "Gender",
    "Position(s)",
    "Species",
    "Resource",
    "Range type",
    "Region(s)",
    "Release Year",
    "Broken?",
]

broken_champs = [
    "Ambessa",
    "Bel'Veth",
    "Cassiopeia",
    "K'Sante",
    "Lulu",
    "Mel",
    "Tahm Kench",
    "Quinn",
    "Yorick",
    "Gragas",
    "Gwen",
    "Karma",
    "Vladimir",
    "Akali",
    "Pantheon",
]

classic_champion_data = {
    'Aatrox': ['Male', 'Top', 'Darkin', 'Manaless', 'Melee', 'Runeterra, Shurima', '2013'],
    'Ahri': ['Female', 'Middle', 'Vastayan', 'Mana', 'Ranged', 'Ionia', '2011'],
    'Akali': ['Female', 'Middle', 'Human', 'Energy', 'Melee', 'Ionia', '2010'],
    'Akshan': ['Male', 'Middle', 'Human', 'Mana', 'Ranged', 'Shurima', '2021'],
    'Alistar': ['Male', 'Support', 'Minotaur', 'Mana', 'Melee', 'Runeterra', '2009'],
    'Ambessa': ['Female', 'Jungle, Top', 'Human', 'Energy', 'Melee', 'Noxus, Piltover', '2024'],
    'Amumu': ['Male', 'Jungle', 'Undead, Yordle', 'Mana', 'Melee', 'Shurima', '2009'],
    'Anivia': ['Female', 'Middle', 'God, Spirit', 'Mana', 'Ranged', 'Freljord', '2009'],
    'Annie': ['Female', 'Middle', 'Human, Magicborn', 'Mana', 'Ranged', 'Noxus, Runeterra', '2009'],
    'Aphelios': ['Male', 'Bottom', 'Human, Spiritualist', 'Mana', 'Ranged', 'Targon', '2019'],
    'Ashe': ['Female', 'Bottom', 'Human, Iceborn', 'Mana', 'Ranged', 'Freljord', '2009'],
    'Aurelion Sol': ['Male', 'Middle', 'Celestial, Dragon', 'Mana', 'Ranged', 'Runeterra, Targon', '2016'],
    'Aurora': ['Female', 'Middle, Top', 'Vastayan', 'Mana', 'Ranged', 'Freljord', '2024'],
    'Azir': ['Male', 'Middle', 'God-Warrior', 'Mana', 'Ranged', 'Shurima', '2014'],
    'Bard': ['Male', 'Support', 'Celestial', 'Mana', 'Ranged', 'Runeterra', '2015'],
    "Bel'Veth": ['Female', 'Jungle', 'Void-Being', 'Manaless', 'Melee', 'Void', '2022'],
    'Blitzcrank': ['Other', 'Support', 'Golem', 'Mana', 'Melee', 'Zaun', '2009'],
    'Brand': ['Male', 'Support', 'Human, Magically Altered', 'Mana', 'Ranged', 'Freljord, Runeterra', '2011'],
    'Braum': ['Male', 'Support', 'Human, Iceborn', 'Mana', 'Melee', 'Freljord', '2014'],
    'Briar': ['Female', 'Jungle', 'Golem', 'Health costs', 'Melee', 'Noxus', '2023'],
    'Caitlyn': ['Female', 'Bottom', 'Human', 'Mana', 'Ranged', 'Piltover', '2011'],
    'Camille': ['Female', 'Top', 'Cyborg, Human', 'Mana', 'Melee', 'Piltover', '2016'],
    'Cassiopeia': ['Female', 'Middle, Top', 'Human, Magically Altered', 'Mana', 'Ranged', 'Noxus, Shurima', '2010'],
    "Cho'Gath": ['Male', 'Top', 'Void-Being', 'Mana', 'Melee', 'Void', '2009'],
    'Corki': ['Male', 'Bottom, Middle', 'Yordle', 'Mana', 'Ranged', 'Bandle City, Piltover', '2009'],
    'Darius': ['Male', 'Top', 'Human', 'Mana', 'Melee', 'Noxus', '2012'],
    'Diana': ['Female', 'Jungle, Middle', 'Aspect, Human', 'Mana', 'Melee', 'Targon', '2012'],
    'Dr. Mundo': ['Male', 'Top', 'Chemically Altered, Human', 'Health costs', 'Melee', 'Zaun', '2009'],
    'Draven': ['Male', 'Bottom', 'Human', 'Mana', 'Ranged', 'Noxus', '2012'],
    'Ekko': ['Male', 'Jungle, Middle', 'Human', 'Mana', 'Melee', 'Zaun', '2015'],
    'Elise': ['Female', 'Jungle', 'Human, Magically Altered', 'Mana', 'Melee, Ranged', 'Noxus, Shadow Isles', '2012'],
    'Evelynn': ['Female', 'Jungle', 'Demon, Spirit', 'Mana', 'Melee', 'Runeterra', '2009'],
    'Ezreal': ['Male', 'Bottom', 'Human, Magicborn', 'Mana', 'Ranged', 'Piltover', '2010'],
    'Fiddlesticks': ['Other', 'Jungle', 'Demon, Spirit', 'Mana', 'Ranged', 'Runeterra', '2009'],
    'Fiora': ['Female', 'Top', 'Human', 'Mana', 'Melee', 'Demacia', '2012'],
    'Fizz': ['Male', 'Middle', 'Yordle', 'Mana', 'Melee', 'Bilgewater', '2011'],
    'Galio': ['Male', 'Middle', 'Golem', 'Mana', 'Melee', 'Demacia', '2010'],
    'Gangplank': ['Male', 'Top', 'Human', 'Mana', 'Melee', 'Bilgewater', '2009'],
    'Garen': ['Male', 'Top', 'Human', 'Manaless', 'Melee', 'Demacia', '2010'],
    'Gnar': ['Male', 'Top', 'Yordle', 'Rage', 'Melee, Ranged', 'Freljord', '2014'],
    'Gragas': ['Male', 'Jungle, Top', 'Human, Iceborn', 'Mana', 'Melee', 'Freljord', '2010'],
    'Graves': ['Male', 'Jungle', 'Human', 'Mana', 'Ranged', 'Bilgewater', '2011'],
    'Gwen': ['Female', 'Jungle, Top', 'Human, Magically Altered', 'Mana', 'Melee', 'Camavor, Shadow Isles', '2021'],
    'Hecarim': ['Male', 'Jungle', 'Undead', 'Mana', 'Melee', 'Camavor, Shadow Isles', '2012'],
    'Heimerdinger': ['Male', 'Middle, Top', 'Yordle', 'Mana', 'Ranged', 'Piltover', '2009'],
    'Hwei': ['Male', 'Middle', 'Human, Magicborn', 'Mana', 'Ranged', 'Ionia', '2023'],
    'Illaoi': ['Female', 'Top', 'Human, Spiritualist', 'Mana', 'Melee', 'Bilgewater', '2015'],
    'Irelia': ['Female', 'Middle, Top', 'Human, Spiritualist', 'Mana', 'Melee', 'Ionia', '2010'],
    'Ivern': ['Male', 'Jungle', 'Human, Magically Altered', 'Mana', 'Ranged', 'Freljord, Ionia', '2016'],
    'Janna': ['Female', 'Support', 'God, Spirit', 'Mana', 'Ranged', 'Shurima, Zaun', '2009'],
    'Jarvan IV': ['Male', 'Jungle', 'Human', 'Mana', 'Melee', 'Demacia', '2011'],
    'Jax': ['Male', 'Jungle, Top', 'Unknown', 'Mana', 'Melee', 'Icathia, Runeterra', '2009'],
    'Jayce': ['Male', 'Middle, Top', 'Human', 'Mana', 'Melee, Ranged', 'Piltover', '2012'],
    'Jhin': ['Male', 'Bottom', 'Human, Spiritualist', 'Mana', 'Ranged', 'Ionia', '2016'],
    'Jinx': ['Female', 'Bottom', 'Chemically Altered, Human', 'Mana', 'Ranged', 'Zaun', '2013'],
    "K'Sante": ['Male', 'Top', 'Human', 'Mana', 'Melee', 'Shurima', '2022'],
    "Kai'Sa": ['Female', 'Bottom', 'Human, Void-Being', 'Mana', 'Ranged', 'Shurima, Void', '2018'],
    'Kalista': ['Female', 'Bottom', 'Undead', 'Mana', 'Ranged', 'Camavor, Shadow Isles', '2014'],
    'Karma': ['Female', 'Support', 'Human, Spiritualist', 'Mana', 'Ranged', 'Ionia', '2011'],
    'Karthus': ['Male', 'Jungle', 'Undead', 'Mana', 'Ranged', 'Noxus, Shadow Isles', '2009'],
    'Kassadin': ['Male', 'Middle', 'Human, Void-Being', 'Mana', 'Melee', 'Shurima, Void', '2009'],
    'Katarina': ['Female', 'Middle', 'Human', 'Manaless', 'Melee', 'Noxus', '2009'],
    'Kayle': ['Female', 'Top', 'Aspect, Human, Magically Altered', 'Mana', 'Melee, Ranged', 'Demacia, Targon', '2009'],
    'Kayn': ['Male', 'Jungle', 'Darkin, Human, Magically Altered', 'Mana', 'Melee', 'Ionia, Noxus', '2017'],
    'Kennen': ['Male', 'Top', 'Yordle', 'Energy', 'Ranged', 'Ionia', '2010'],
    "Kha'Zix": ['Male', 'Jungle', 'Void-Being', 'Mana', 'Melee', 'Void', '2012'],
    'Kindred': ['Other', 'Jungle', 'God, Spirit', 'Mana', 'Ranged', 'Runeterra', '2015'],
    'Kled': ['Male', 'Top', 'Yordle', 'Courage', 'Melee', 'Noxus', '2016'],
    "Kog'Maw": ['Male', 'Bottom', 'Void-Being', 'Mana', 'Ranged', 'Void', '2010'],
    'LeBlanc': ['Female', 'Middle', 'Human, Magically Altered', 'Mana', 'Ranged', 'Noxus', '2010'],
    'Lee Sin': ['Male', 'Jungle', 'Human, Spiritualist', 'Energy', 'Melee', 'Ionia', '2011'],
    'Leona': ['Female', 'Support', 'Aspect, Human', 'Mana', 'Melee', 'Targon', '2011'],
    'Lillia': ['Female', 'Jungle', 'Spirit', 'Mana', 'Melee', 'Ionia', '2020'],
    'Lissandra': ['Female', 'Middle', 'Human, Iceborn', 'Mana', 'Ranged', 'Freljord', '2013'],
    'Lucian': ['Male', 'Bottom', 'Human', 'Mana', 'Ranged', 'Demacia, Shadow Isles', '2013'],
    'Lulu': ['Female', 'Support', 'Yordle', 'Mana', 'Ranged', 'Bandle City', '2012'],
    'Lux': ['Female', 'Middle, Support', 'Human, Magicborn', 'Mana', 'Ranged', 'Demacia', '2010'],
    'Malphite': ['Male', 'Top', 'Golem', 'Mana', 'Melee', 'Ixtal, Shurima', '2009'],
    'Malzahar': ['Male', 'Middle', 'Human, Void-Being', 'Mana', 'Ranged', 'Shurima, Void', '2010'],
    'Maokai': ['Male', 'Support, Top', 'Spirit', 'Mana', 'Melee', 'Shadow Isles', '2011'],
    'Master Yi': ['Male', 'Jungle', 'Human, Spiritualist', 'Mana', 'Melee', 'Ionia', '2009'],
    'Mel': ['Female', 'Middle, Support', 'Human, Magically Altered', 'Mana', 'Ranged', 'Noxus, Piltover', '2025'],
    'Milio': ['Male', 'Support', 'Human, Magicborn', 'Mana', 'Ranged', 'Ixtal', '2023'],
    'Miss Fortune': ['Female', 'Bottom', 'Human', 'Mana', 'Ranged', 'Bilgewater', '2010'],
    'Mordekaiser': ['Male', 'Top', 'Revenant', 'Shield', 'Melee', 'Noxus, Shadow Isles', '2010'],
    'Morgana': ['Female', 'Support', 'Aspect, Human, Magically Altered', 'Mana', 'Ranged', 'Demacia, Targon', '2009'],
    'Naafiri': ['Female', 'Middle', 'Darkin, Dog', 'Mana', 'Melee', 'Shurima', '2023'],
    'Nami': ['Female', 'Support', 'Vastayan', 'Mana', 'Ranged', 'Bilgewater, Runeterra', '2012'],
    'Nasus': ['Male', 'Top', 'God-Warrior', 'Mana', 'Melee', 'Shurima', '2009'],
    'Nautilus': ['Male', 'Support', 'Revenant', 'Mana', 'Melee', 'Bilgewater', '2012'],
    'Neeko': ['Female', 'Middle, Support', 'Vastayan', 'Mana', 'Ranged', 'Ixtal', '2018'],
    'Nidalee': ['Female', 'Jungle', 'Human, Spiritualist', 'Mana', 'Melee, Ranged', 'Ixtal', '2009'],
    'Nilah': ['Female', 'Bottom', 'Human, Magically Altered', 'Mana', 'Melee', 'Bilgewater', '2022'],
    'Nocturne': ['Male', 'Jungle', 'Demon, Spirit', 'Mana', 'Melee', 'Runeterra', '2011'],
    "Nunu & Willump": ['Male', 'Jungle', 'Human, Yeti', 'Mana', 'Melee', 'Freljord', '2009'],
    'Olaf': ['Male', 'Top', 'Human, Iceborn', 'Mana', 'Melee', 'Freljord', '2010'],
    'Orianna': ['Female', 'Middle', 'Golem', 'Mana', 'Ranged', 'Piltover', '2011'],
    'Ornn': ['Male', 'Top', 'God, Spirit', 'Mana', 'Melee', 'Freljord', '2017'],
    'Pantheon': ['Male', 'Support, Top', 'Aspect, Human', 'Mana', 'Melee', 'Targon', '2010'],
    'Poppy': ['Female', 'Support, Top', 'Yordle', 'Mana', 'Melee', 'Demacia', '2010'],
    'Pyke': ['Male', 'Support', 'Revenant', 'Mana', 'Melee', 'Bilgewater', '2018'],
    'Qiyana': ['Female', 'Middle', 'Human, Magicborn', 'Mana', 'Melee', 'Ixtal', '2019'],
    'Quinn': ['Female', 'Top', 'Human', 'Mana', 'Ranged', 'Demacia', '2013'],
    'Rakan': ['Male', 'Support', 'Vastayan', 'Mana', 'Melee', 'Ionia', '2017'],
    'Rammus': ['Male', 'Jungle', 'Unknown', 'Mana', 'Melee', 'Shurima', '2009'],
    "Rek'Sai": ['Female', 'Jungle', 'Void-Being', 'Rage', 'Melee', 'Shurima, Void', '2014'],
    'Rell': ['Female', 'Support', 'Human, Magically Altered, Magicborn', 'Mana', 'Melee', 'Noxus', '2020'],
    'Renata Glasc': ['Female', 'Support', 'Chemically Altered, Human', 'Mana', 'Ranged', 'Zaun', '2022'],
    'Renekton': ['Male', 'Top', 'God-Warrior', 'Fury', 'Melee', 'Shurima', '2011'],
    'Rengar': ['Male', 'Jungle', 'Vastayan', 'Ferocity', 'Melee', 'Ixtal, Shurima', '2012'],
    'Riven': ['Female', 'Top', 'Human', 'Manaless', 'Melee', 'Ionia, Noxus', '2011'],
    'Rumble': ['Male', 'Top', 'Yordle', 'Heat', 'Melee', 'Bandle City', '2011'],
    'Ryze': ['Male', 'Middle, Top', 'Human, Magically Altered', 'Mana', 'Ranged', 'Runeterra', '2009'],
    'Samira': ['Female', 'Bottom', 'Human', 'Mana', 'Ranged', 'Noxus, Shurima', '2020'],
    'Sejuani': ['Female', 'Jungle', 'Human, Iceborn', 'Mana', 'Melee', 'Freljord', '2012'],
    'Senna': ['Female', 'Support', 'Human, Undead', 'Mana', 'Ranged', 'Shadow Isles', '2019'],
    'Seraphine': ['Female', 'Support', 'Human, Magicborn', 'Mana', 'Ranged', 'Piltover, Zaun', '2020'],
    'Sett': ['Male', 'Top', 'Human, Vastayan', 'Grit', 'Melee', 'Ionia', '2020'],
    'Shaco': ['Male', 'Jungle', 'Spirit', 'Mana', 'Melee', 'Runeterra', '2009'],
    'Shen': ['Male', 'Support, Top', 'Human, Spiritualist', 'Energy', 'Melee', 'Ionia', '2010'],
    'Shyvana': ['Female', 'Jungle', 'Dragon, Magically Altered', 'Fury', 'Melee', 'Demacia', '2011'],
    'Singed': ['Male', 'Top', 'Chemically Altered, Human', 'Mana', 'Melee', 'Piltover, Zaun', '2009'],
    'Sion': ['Male', 'Top', 'Revenant', 'Mana', 'Melee', 'Noxus', '2009'],
    'Sivir': ['Female', 'Bottom', 'Human', 'Mana', 'Ranged', 'Shurima', '2009'],
    'Skarner': ['Male', 'Jungle', 'Brackern', 'Mana', 'Melee', 'Ixtal', '2011'],
    'Smolder': ['Male', 'Bottom, Middle', 'Dragon', 'Mana', 'Ranged', 'Camavor, Noxus', '2024'],
    'Sona': ['Female', 'Support', 'Human, Magicborn', 'Mana', 'Ranged', 'Demacia, Ionia', '2010'],
    'Soraka': ['Female', 'Support', 'Celestial', 'Mana', 'Ranged', 'Ionia, Targon', '2009'],
    'Swain': ['Male', 'Support', 'Human, Magically Altered', 'Mana', 'Ranged', 'Noxus', '2010'],
    'Sylas': ['Male', 'Middle', 'Human, Magicborn', 'Mana', 'Melee', 'Demacia, Freljord', '2019'],
    'Syndra': ['Female', 'Middle', 'Human, Magicborn', 'Mana', 'Ranged', 'Ionia', '2012'],
    'Tahm Kench': ['Male', 'Support, Top', 'Demon, Spirit', 'Mana', 'Melee', 'Bilgewater, Runeterra', '2015'],
    'Taliyah': ['Female', 'Jungle, Middle', 'Human, Magicborn', 'Mana', 'Ranged', 'Shurima', '2016'],
    'Talon': ['Male', 'Jungle, Middle', 'Human', 'Mana', 'Melee', 'Noxus', '2011'],
    'Taric': ['Male', 'Support', 'Aspect, Human', 'Mana', 'Melee', 'Demacia, Targon', '2009'],
    'Teemo': ['Male', 'Jungle, Top', 'Yordle', 'Mana', 'Ranged', 'Bandle City', '2009'],
    'Thresh': ['Male', 'Support', 'Undead', 'Mana', 'Ranged', 'Shadow Isles', '2013'],
    'Tristana': ['Female', 'Bottom', 'Yordle', 'Mana', 'Ranged', 'Bandle City', '2009'],
    'Trundle': ['Male', 'Jungle, Top', 'Iceborn, Troll', 'Mana', 'Melee', 'Freljord', '2010'],
    'Tryndamere': ['Male', 'Top', 'Human, Magically Altered', 'Fury', 'Melee', 'Freljord', '2009'],
    'Twisted Fate': ['Male', 'Middle', 'Human, Magicborn', 'Mana', 'Ranged', 'Bilgewater', '2009'],
    'Twitch': ['Male', 'Bottom', 'Chemically Altered, Rat', 'Mana', 'Ranged', 'Zaun', '2009'],
    'Udyr': ['Male', 'Jungle', 'Human, Spiritualist', 'Mana', 'Melee', 'Freljord, Ionia', '2009'],
    'Urgot': ['Male', 'Top', 'Chemically Altered, Cyborg, Human', 'Mana', 'Ranged', 'Noxus, Zaun', '2010'],
    'Varus': ['Male', 'Bottom', 'Darkin, Human', 'Mana', 'Ranged', 'Ionia, Runeterra', '2012'],
    'Vayne': ['Female', 'Bottom', 'Human', 'Mana', 'Ranged', 'Demacia', '2011'],
    'Veigar': ['Male', 'Middle', 'Yordle', 'Mana', 'Ranged', 'Bandle City, Runeterra', '2009'],
    "Vel'Koz": ['Male', 'Middle, Support', 'Void-Being', 'Mana', 'Ranged', 'Void', '2014'],
    'Vex': ['Female', 'Middle', 'Yordle', 'Mana', 'Ranged', 'Bandle City, Shadow Isles', '2021'],
    'Vi': ['Female', 'Jungle', 'Human', 'Mana', 'Melee', 'Piltover, Zaun', '2012'],
    'Viego': ['Male', 'Jungle', 'Undead', 'Manaless', 'Melee', 'Camavor, Shadow Isles', '2021'],
    'Viktor': ['Male', 'Middle', 'Cyborg, Human', 'Mana', 'Ranged', 'Piltover, Zaun', '2011'],
    'Vladimir': ['Male', 'Middle, Top', 'Human, Magically Altered', 'Bloodthirst', 'Ranged', 'Camavor, Noxus', '2010'],
    'Volibear': ['Male', 'Jungle, Top', 'God, Spirit', 'Mana', 'Melee', 'Freljord', '2011'],
    'Warwick': ['Male', 'Jungle, Top', 'Chemically Altered, Cyborg, Human', 'Mana', 'Melee', 'Zaun', '2009'],
    'Wukong': ['Male', 'Jungle, Top', 'Vastayan', 'Mana', 'Melee', 'Ionia', '2011'],
    'Xayah': ['Female', 'Bottom', 'Vastayan', 'Mana', 'Ranged', 'Ionia', '2017'],
    'Xerath': ['Male', 'Middle, Support', 'God-Warrior', 'Mana', 'Ranged', 'Shurima', '2011'],
    'Xin Zhao': ['Male', 'Jungle', 'Human', 'Mana', 'Melee', 'Demacia, Ionia', '2010'],
    'Yasuo': ['Male', 'Middle', 'Human, Magicborn', 'Flow', 'Melee', 'Ionia', '2013'],
    'Yone': ['Male', 'Middle, Top', 'Human, Magically Altered', 'Manaless', 'Melee', 'Ionia', '2020'],
    'Yorick': ['Male', 'Top', 'Human, Magically Altered', 'Mana', 'Melee', 'Shadow Isles', '2011'],
    'Yuumi': ['Female', 'Support', 'Cat, Magically Altered', 'Mana', 'Ranged', 'Bandle City', '2019'],
    'Zac': ['Male', 'Jungle', 'Golem', 'Health costs', 'Melee', 'Zaun', '2013'],
    'Zed': ['Male', 'Middle', 'Human, Magically Altered', 'Energy', 'Melee', 'Ionia', '2012'],
    'Zeri': ['Female', 'Bottom', 'Human, Magicborn', 'Mana', 'Ranged', 'Zaun', '2022'],
    'Ziggs': ['Male', 'Bottom, Middle', 'Yordle', 'Mana', 'Ranged', 'Zaun', '2012'],
    'Zilean': ['Male', 'Support', 'Human, Magicborn', 'Mana', 'Ranged', 'Icathia, Runeterra', '2009'],
    'Zoe': ['Female', 'Middle, Support', 'Aspect, Human', 'Mana', 'Ranged', 'Targon', '2017'],
    'Zyra': ['Female', 'Support', 'Unknown', 'Mana', 'Ranged', 'Ixtal', '2012'],
}

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
    "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy",
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

# Creates a new line for each comma in the different elements in the value-list of the key in classic_champion_data for readability
for i in range(len(champ_list)):
    for j in range(len(classic_champion_data[champ_list[i]])):
        classic_champion_data[champ_list[i]][j] = classic_champion_data[champ_list[i]][j].replace(", ", ",\n")

# Creates a dictionary with keys as champion names and gives relative file-paths as values
champ_icon_dictionary = {}
file_path = "champ_icons\\"
for i in range(170):
    champ_name = champ_list[i]
    champ_icon_dictionary.update({str(champ_name): f"{file_path}{champ_list[i]}Square.webp"})

class Classic:
    def __init__(self, frame, champion_info, window, number_of_guesses, chosen_champ, handling_size):
        # Initializing certain labels, a window, a frame and certain field-values
        self.frame = frame
        self.champion_guess = StringVar()
        self.champion_info = champion_info
        self.window = window
        self.number_of_guesses = number_of_guesses
        self.chosen_champ = chosen_champ
        self.max_displayed_champs = 5
        self.handling_size = handling_size

        # Different lists 
        self.champ_list = list(champion_info.keys())
        self.information_labels = []
        self.guess_labels = []
        # self.champ_guesses = []
        self.all_guesses = []
        self.displayed_champ_widgets = []
        self.Classic_widgets = []
        self.hint_commands = [self.qoute_hint, self.ability_hint, self.splash_hint]
        self.hint_labels = []
        self.images = []
        self.hint_buttons = []

        # Keep track of guessed champion names in set to prevent duplicates
        self.guessed_champions = set()
        
        self.game_won = False
        self.qoute_used = False
        self.ability_used = False
        self.splash_used = False
        
    def guess_colorer(self, guess_labels, champ_name):
        """Changes the color of the champion labels based on whether or not they are correct.
        Green for correct, orange for partially correct and red for wrong."""
        chosen_data = classic_champion_data[self.chosen_champ]

        if self.chosen_champ in broken_champs: # Determines if the chosen champ is broken (as determined by myself)
            label_text = "Broken"
        else:
            label_text = "Balanced"
        chosen_data.append(label_text)

        correct_guess = (champ_name == self.chosen_champ) # Chooses the correct guess
        all_correct = True # Assumes the user guessed correctly initially

        if guess_labels: # Checks if there are even guess_labels (has there been a guess)
            for i in range(len(guess_labels)):
                extra_checks = [] # Checks for partials in a correct manner

                if("\n" in guess_labels[i]["text"]): # Checks if there are multiple values in the labels
                    extra_checks = guess_labels[i]["text"].replace("\n", "").split(",")

                if(len(extra_checks) > 0): # If multiple values do exist, loops through one by one
                    amountFound = 0
                    for j in range(len(extra_checks)):
                        if extra_checks[j] in chosen_data[i]: # Checks how many individual values match with the chosen data values
                            amountFound += 1
                    
                    if amountFound == len(extra_checks): 
                        guess_labels[i].config(bg="#21ed1a") # Green if they are 100% equal to each other
                    elif amountFound > 0:
                        guess_labels[i].config(bg="#f78d23") # Orange if there are similarities but not 100%
                        all_correct = False
                    else:
                        guess_labels[i].config(bg="#f52727") # Red if not the two prior options
                        all_correct = False
                else: # If no extra values, use standard procedure
                    if guess_labels[i]["text"] == chosen_data[i]:
                        guess_labels[i].config(bg="#21ed1a")  # Green for 100% similarity
                    elif guess_labels[i]["text"] in chosen_data[i]:
                        guess_labels[i].config(bg="#f78d23")  # Orange for partially similar
                        all_correct = False
                    else:
                        guess_labels[i].config(bg="#f52727")  # Red for not similar
                        all_correct = False
                
                if guess_labels[i]["text"] == "Mana" and chosen_data[i] == "Manaless":
                    guess_labels[i].config(bg="#f52727")

        if correct_guess and all_correct and not self.game_won: # If user guessed correct and game hasn't been won yet
            self.game_won = True
            self.show_victory_popup() # Victory pop-up screen to congratulate

    def show_victory_popup(self):
        """Function for creating a popup window to congratulate user and ask if the user wants to play again."""
        popup = Toplevel(self.window) # Creates a popup window
        popup.title("Congratulations!")
        
        # Calculate position to center the popup
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        popup_width = 400 # Static but customizable
        popup_height = 250 # Static but customizable
        x_position = self.window.winfo_x() + (window_width - popup_width) // 2
        y_position = self.window.winfo_y() + (window_height - popup_height) // 2
        
        # Set popup size and position
        popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")
        popup.resizable(False, False)
        
        # Make popup appear on top, stay on top and grab focus
        popup.transient(self.window)
        popup.grab_set()
        popup.focus_set()
        popup.configure(bg="#1E2328", highlightthickness=5, highlightcolor="#01708D")
        
        # Create a frame for content
        content_frame = Frame(popup, bg="#1E2328", padx=20, pady=20)
        content_frame.pack(expand=True, fill="both")
        
        # Victory message
        victory_label = Label(
            content_frame,
            text=f"Congratulations!\nYou guessed the champion: {self.chosen_champ}!",
            font=("Copperplate Gothic Bold", 16),
            bg="#1E2328",
            fg="#EDB933", # Gold color for premium feels
            justify="center",
            wraplength=350 # Forces new line every 350 pixels (25 pixels each side at least)
        )
        victory_label.pack(pady=10)
        
        # Add label with number of guesses used
        stats_label = Label(
            content_frame,
            text=f"Number of guesses: {self.number_of_guesses}",
            font=("Arial Bold", 14),
            bg="#1E2328",
            fg="white"
        )
        stats_label.pack(pady=5)
        
        button_frame = Frame(content_frame, bg="#1E2328")
        button_frame.pack(pady=10)

        # Close button
        close_button = Button(
            button_frame,
            text="Close",
            font=("Arial Bold", 13),
            bg="#01708D",
            fg="white",
            command=popup.destroy,
        )
        close_button.pack(padx=10, side="left")

        # Play again button
        playA_button = Button(
            button_frame,
            text="Play Again",
            font=("Arial Bold", 13),
            bg="#01708D",
            fg="white",
            command=self.play_again,
        )
        playA_button.pack(padx=10, side="left")

    def guess_sign_creator(self):
        """Creates a label with text for guessing champions.
        Also displays if u have already guessed champ."""
        self.guess_sign = Label(
            self.frame, 
            text="Guess today's League of Legends champion!", 
            font=("Copperplate Gothic Bold", 30),
            bg="#1E2328",
            fg="white", 
            highlightbackground="#EDB933",
            highlightcolor="#EDB933",
            highlightthickness=2
            )
        self.guess_sign.grid(row=4, rowspan=2, column=1, columnspan=11)
        
        self.hint_sign = Label(self.frame)
    
    def image_loader(self, path, resize_number):
        """Loads an image from a given path and resizes the images."""
        self.window.update_idletasks()
        size_parameter = min(self.window.winfo_height(), self.window.winfo_width())/5
        try: # Opens image with PIL, resizes it and returns tkinter-image
            image = Image.open(path) 
            image = image.resize((int(size_parameter*resize_number), int(size_parameter*resize_number)), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e: # Error printed with path and Exception
            print(f"Could not load image, {path}: {e}")
            return None
            
    def create_icons(self):
        """Function to create icons for the different gamemodes."""
        # Creates the title with golden border
        self.Loldle_title = Label(
            self.frame, 
            text="LOLDLE-CLONE", 
            font=("Copperplate Gothic Bold", 45),
            bg="#1E2328",
            fg="white", 
            highlightbackground="#EDB933",
            highlightcolor="#EDB933",
            highlightthickness=3
        )
        self.Loldle_title.grid(row=0, rowspan=4, column=2, columnspan=9)

    def lebronmination(self):
        """Easter Egg function that displays lebron images instead of champion info if u type certain words."""
        guess = self.champion_guess.get().strip().lower()

        if guess in lebron_texts:
            lebron_image = self.image_loader(r"misc images/Lebron.png", 0.3)

            # Loops through the widgets and removes text and adds an image of lebron
            for widget_list in self.displayed_champ_widgets:
                for widget in widget_list:
                    widget.config(
                        text="",
                        image=lebron_image
                    )
                    widget.image = lebron_image # Keep a reference for tkinter-issues
            
            lebron_background = self.image_loader(r"misc images\lebronflash.jpg", 7)

            bg_img_L.config(image = lebron_background)
            bg_img_L.image = lebron_background

            self.window.update_idletasks()  # Force UI update
    
    def guess_champ(self):
        """Function for creating entry and button for guessing champions."""
        self.champ_guess_field = Entry(
            self.frame, 
            bg="#1E2328", 
            fg="white", 
            textvariable=self.champion_guess, 
            font=("Copperplate Gothic Bold", 18),
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness=2
        )
        self.champ_guess_field.grid(row=12, column=2, columnspan=8, sticky=N+S+E+W)

        # Creates the essential and immensly powerful listbox widget :D
        self.dropdown_listbox = Listbox(
            self.frame, 
            font=("Copperplate Gothic Bold", 14), 
            height=5, 
            bg="#1E2328", 
            fg="white",
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=2,
        )
        self.dropdown_listbox.place_forget() # Makes it hidden initially

        self.champ_guess_field.bind("<KeyRelease>", self.update_autofill) # Whenever user types a letter, will update the list
        self.dropdown_listbox.bind("<<ListboxSelect>>", self.select_from_list) # When you press something in the list, runs self.select_from_list
        self.champ_guess_field.bind("<Tab>", self.tab_autocomplete) # Calls autocomplete function if u press tab
        self.champ_guess_field.bind("<Return>", lambda event: self.display_champ_info()) # Does a guess when you press enter

        # Button for making a guess which runs the display_champ_info method
        self.arrow_button = Button(
            self.frame, 
            bg="#1E2328", 
            command = self.display_champ_info,
            text="➤",
            fg="white",
            font=("Copperplate Gothic Bold", 18)
        )
        self.arrow_button.grid(row=12, column=10, columnspan=1, sticky=N+S+E+W)

    def update_autofill(self, event=None):
        """Function for autofilling the words (from letters) that the user types."""
        typed_text = self.champion_guess.get().strip()

        if not typed_text:
            self.dropdown_listbox.place_forget()  # Hide dropdown if empty
            return

        # Filter out champions that have already been guessed
        available_champs = []
        for champion in self.champ_list:  
            champ_name = champion.lower()  
            user_input = typed_text.lower()  

            if champ_name.startswith(user_input) and champion not in self.guessed_champions:  
                available_champs.append(champion)

        # Hide dropdown if the typed text is an exact match or already guessed
        if typed_text in self.champ_list and typed_text not in self.guessed_champions:
            self.dropdown_listbox.place_forget()
            return

        self.dropdown_listbox.delete(0, END)  # Clear previous list

        if available_champs:
            for champ in available_champs:
                self.dropdown_listbox.insert(END, champ)

            # Set height dynamically (max height = 5)
            dropdown_height = min(len(available_champs), 5)  
            self.dropdown_listbox.config(height=dropdown_height)  

            # Position the dropdown under the entry field
            self.dropdown_listbox.place(
                x=self.champ_guess_field.winfo_x(),
                y=self.champ_guess_field.winfo_y() + self.champ_guess_field.winfo_height(),
                width=self.champ_guess_field.winfo_width()
            )

        else:
            self.dropdown_listbox.place_forget()  # Hide dropdown if no matches
    
    def tab_autocomplete(self, event):
        """Function for selecting the first champion in the listbox."""
        if self.dropdown_listbox.size() > 0:  # Ensure listbox has items
            selected_champ = self.dropdown_listbox.get(0)  # Get the first champion
            self.champion_guess.set(selected_champ)  # Set entry text to first champion
            self.dropdown_listbox.place_forget()  # Hide dropdown
            return "break"  # Prevents default Tab behavior

    def select_from_list(self, event):
        """Function for setting the guess to the champ pressed from the list."""
        selected_index = self.dropdown_listbox.curselection()
        if selected_index:
            selected_champ = self.dropdown_listbox.get(selected_index[0])
            self.champion_guess.set(selected_champ)
            self.dropdown_listbox.place_forget()  # Hide dropdown after selection
    
    def display_champ_headers(self):
        """Function for creating information labels for the different categories."""
        self.information_labels = []
        self.line_labels = []

        for i in range(9):
            information = Label(
                self.frame, 
                text=f"{champ_header_texts[i]}\n──────", 
                font=("Copperplate Gothic Bold", 12),
                fg="white",
                bg="#1E2328",
                highlightbackground="#01708D",
                highlightcolor="#01708D",
                highlightthickness=1
            )
            information.grid(row=14, column=i+2)
            self.information_labels.append(information)

    def clear_displayed_champs(self):
        """Removes all currently displayed champion widgets"""
        for widget_set in self.displayed_champ_widgets:
            for widget in widget_set:
                widget.grid_forget()
        self.displayed_champ_widgets = []

    def show_duplicate_warning(self, champ_name):
        """Function for showing a warning if making the same guess."""
        # Update the guess sign to show the duplicate warning
        original_text = self.guess_sign["text"]
        self.guess_sign.config(
            text=f"You've already guessed {champ_name}!",
            fg="#f52727"  # Red text for warning
        )
        
        # Schedule reverting back to original text after 2 seconds
        self.window.after(2000, lambda: self.guess_sign.config(
            text=original_text,
            fg="white"  # Revert to original color
        ))

    def display_champ_info(self):
        """Function for creating data widgets and moving them according to order.
        Also updates the hint in x guesses for each guess made."""
        if self.game_won:
            return
        
        champ_guess = self.champion_guess.get().strip()
        
        self.lebronmination()

        # Check if the champion exists in the dictionary
        if champ_guess not in champ_icon_dictionary:
            return
            
        # Check if this champion has already been guessed
        if champ_guess in self.guessed_champions:
            self.show_duplicate_warning(champ_guess)
            return
            
        # Add the champion to the guessed set
        self.guessed_champions.add(champ_guess)
            
        # Clear the entry field after guessing
        self.champion_guess.set("")
        
        # Increment guess counter
        self.number_of_guesses += 1
        
        # Create new guess info
        champ_info = self.champion_info[champ_guess]
        
        # Determine if champion is broken or balanced
        if champ_guess not in broken_champs:
            brokentext = "Balanced"
        else:
            brokentext = "Broken"
        
        # Create a list to store all widgets for this guess
        guess_widgets = []
        guess_labels = []
        
        # Champion icon
        champ_icon = self.image_loader(champ_icon_dictionary[champ_guess], 0.3)
        champion_label = Label(self.frame, font="Arial", image=champ_icon, bg="#1E2328")
        champion_label.image = champ_icon
        guess_widgets.append(champion_label)
        
        # Champion information labels
        for i in range(7):
            info_label = Label(self.frame, text=champ_info[i], font="Arial")
            guess_widgets.append(info_label)
            guess_labels.append(info_label)
        
        # Broken/Balanced label
        broken_label = Label(self.frame, text=brokentext, font="Arial")
        guess_widgets.append(broken_label)
        guess_labels.append(broken_label)
        
        # Add this guess to the beginning of our list
        self.all_guesses.insert(0, {
            'widgets': guess_widgets,
            'labels': guess_labels,
            'name': champ_guess
        })
        
        # Clear the currently displayed champions
        self.clear_displayed_champs()
        
        # Display only the most recent 5 guesses (or fewer if less than 5 guesses made)
        displayed_guesses = self.all_guesses[:self.max_displayed_champs]
        
        # Display each guess
        for idx, guess in enumerate(displayed_guesses):
            row_position = 15 + (idx * 2)  # Each guess takes 2 rows, starting from row 15
            
            # Place champion icon
            guess['widgets'][0].grid(row=row_position, rowspan=2, column=2, sticky=N+S+E+W, padx=4, pady=4)
            
            # Place champion info labels
            for i in range(7):
                guess['widgets'][i+1].grid(row=row_position, rowspan=2, column=i+3, sticky=N+S+E+W, padx=4, pady=4)
            
            # Place broken/balanced label
            guess['widgets'][8].grid(row=row_position, rowspan=2, column=10, sticky=N+S+E+W, padx=4, pady=4)
            
            # Save references to displayed widgets
            self.displayed_champ_widgets.append(guess['widgets'])

            # Apply coloring and check for victory
            self.guess_colorer(guess['labels'], guess['name'])
        
        # Updates text in hint labels to match the amount of guesses
        for i in range(len(self.hint_labels)):
            if i == 0 and self.qoute_used:
                continue
            if i == 1 and self.ability_used:
                continue
            if i == 2 and self.splash_used:
                continue

            if i == 0 and self.number_of_guesses > 4: # Qoute
                self.hint_labels[i].config(text="Hint now! \n \n \n \n")
            elif i == 1 and self.number_of_guesses > 9: # Qoute
                self.hint_labels[i].config(text="Hint now! \n \n \n \n")
            elif i == 2 and self.number_of_guesses > 14: # Qoute
                self.hint_labels[i].config(text="Hint now! \n \n \n \n")
            else:
                self.hint_labels[i].config(
                    text=f"Hint in {(5+i*5) - self.number_of_guesses} guesses \n \n \n \n "
                )
                
    def hint_creators(self):
        """Function for creating the hint labels with buttons."""
        for i in range(2):
            hint_label = Label(
            self.frame,
            text=f"Hint in {(5+i*10) - self.number_of_guesses} guesses \n \n \n \n ",
            font=("Copperplate Gothic Bold", 15),  
            fg="white",
            bg="#1E2328",
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness=1
            )
            hint_label.grid(row=7, rowspan=4, column=2+6*i, columnspan=3, sticky=N+S+E+W)
            self.hint_labels.append(hint_label)
        
        # Logic for order of labels, cause the middle widget layout was different
        kept_label = self.hint_labels[1]
        self.hint_labels.pop(1)
            
        ability_label = Label(
            self.frame,
            text=f"Hint in {10 - self.number_of_guesses} guesses \n \n \n \n",
            font=("Copperplate Gothic Bold", 15),  
            fg="white",
            bg="#1E2328",
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness=1
        )
        ability_label.grid(row=7, rowspan=4, column=5, columnspan=3, sticky=N+S+E+W, padx=30)
        self.hint_labels.append(ability_label)
        self.hint_labels.append(kept_label)
        
        # Creates the 3 buttons with corresponding images
        for i in range(3):
            hint_image =  self.image_loader(icon_images[i], 0.3)
            hint_button = Button(self.frame, image = hint_image, bg="#1E2328", command=self.hint_commands[i])
            hint_button.image = hint_image
            hint_button.grid(row=9, rowspan=1, column=3+3*i, columnspan=1)
            self.hint_buttons.append(hint_button)
            
    def qoute_hint(self):
        """Function for placing the qoute text when the qoute hint is ready."""
        if self.number_of_guesses < 5 or self.qoute_used:
            pass
        else:
            chosen_qoute = random.choice(open(f"champ_qoute_texts\\{self.chosen_champ}_quotes.txt").readlines()) # Choose a random line in the document
            formatted_qoute = textwrap.fill(chosen_qoute, width=40) # Make sure the qoute cannot exceed 40 characters
            
            self.hint_labels[0].config(font=("Copperplate Gothic", 15), text=f"Which champion says: \n \n {formatted_qoute}")
            self.hint_buttons[0].grid_forget()

            self.qoute_used = True
    
    def ability_hint(self):
        """Function for opening the ability image in the ability hint."""
        if self.number_of_guesses < 9 or self.ability_used:
            pass
        else:
            folder = Path(f"ability_icons\\{self.chosen_champ}")
            files = []

            # Chooese a random image from the selected champs ability icon folder
            for file_ in folder.iterdir():
                if file_.is_file():
                    files.append(file_)
            chosen_ability = str(random.choice(files))

            self.hint_labels[1].config(font=("Copperplate Gothic", 15), text="Which champion has this ability: \n \n \n \n")
            self.hint_buttons[1].grid_forget()

            # Loads image and creates label with it in the center of the ability hint widget
            icon_image = self.image_loader(chosen_ability, 0.3)
            displayed_ability_icon = Label(self.frame, image = icon_image)
            displayed_ability_icon.grid(row=9, column=6)
            displayed_ability_icon.image = icon_image

            self.ability_used = True
    
    def splash_hint(self):
        """Function for displaying the splash art when the splash hint is used."""
        if self.number_of_guesses < 14 or self.splash_used:
            pass # mangler
        else:
            self.splash_used = True

            folder = Path(f"splash_images\\{self.chosen_champ}")
            files = []

            # Chooese a random image from the selected champs splash art folder
            for file_ in folder.iterdir():
                if file_.is_file():
                    files.append(file_)
            chosen_splash = str(random.choice(files))

            image = Image.open(chosen_splash)
            image = image.resize((16*13, 9*13), Image.Resampling.LANCZOS) # Resize for different format than square so no image_loader()
            splash_image = ImageTk.PhotoImage(image)

            self.hint_labels[2].config(font=("Copperplate Gothic", 15), text="Which champion has this splash:\n \n \n \n \n \n \n")
            self.hint_buttons[2].grid_forget()

            displayed_splash = Label(self.frame, image = splash_image)
            displayed_splash.grid(row=8, rowspan=3, column=9, pady=5)
            displayed_splash.image = splash_image
        
    def play_again(self):
        """Function for playing again"""
        self.window.destroy() # Destroy current window
        Classic.make_gui() # Create a new window
        
    def make_gui():
        """The central function for creating a GUI in a frame in a window"""       
        global bg_img_L

        # Global window 
        window = Tk()
        window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
        window.title("Loldle Clone")
        window.resizable(width = False, height = False)

        # Global frame
        frame = Frame(window, bg="white", bd=0)
        frame.grid(sticky=N+S+E+W)

        # Creating the variables for parameters in the Classic-class initilization
        number_of_guesses = 0
        chosen_champ = random.choice(list(classic_champion_data.keys())) # Randomly chooses a champion

        # Override for testing:g
        # chosen_champ = "Dr. Mundo"

        handling_size = int(min(window.winfo_height(), window.winfo_width())/10)

        # Creates an instance of the Classic class, recieving different parameters
        classic_game = Classic(frame, classic_champion_data, window, number_of_guesses, chosen_champ, handling_size)

        # Creating weights for the window and the frame
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)

        for i in range(30):
            frame.rowconfigure(i, weight=1)
        for i in range(13):
            frame.columnconfigure(i, weight=1)
        
        # Opens the background image, can't use image_loader() because of @staticmethod
        bg_image = Image.open(background_image)
        bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_img_L = Label(frame, image=bg_image)
        bg_img_L.grid(row=0, rowspan=50, column=0, columnspan=15)
        bg_img_L.image = bg_image

        # Creates the different widgets from functions of the instance classic_game
        classic_game.guess_sign_creator()
        classic_game.display_champ_headers()
        classic_game.create_icons()
        classic_game.guess_champ()
        classic_game.hint_creators()

        # Makes sure the game runs in a loop
        window.mainloop()

# Calls the make_gui method from the Classic-class, running the whole shabang
Classic.make_gui()