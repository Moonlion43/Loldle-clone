# Loldle-clone made entirely in python with tkinter
# Creator: https://github.com/Moonlion43
# Original website: https://loldle.net/classic 

from tkinter import *
import tkinter.font
from PIL import ImageTk, Image
from pathlib import Path
import random
import time

icon_images = [
    Path(r"icons\Classic.png"),
    Path(r"icons\Qoute.png"),
    Path(r"icons\Ability.png"),
    Path(r"icons\Emoji.png"),
    Path(r"icons\Splash.png"),
]

entry_images = [
    Path(r"misc images\Text Input.webp"),
    Path(r"misc images\Text Input Arrow.webp"),
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
    "Skarner",
    "Ambessa",
    "Bel'Veth",
    "Cassiopeia",
    "K'Sante",
    "Lulu",
    "Mel",
    "Tahm Kench",
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

champion_qoutes = {
    "Aatrox": ["I am a fat negro", "I hate many people", "Jews are pretty greedy", "Blacks like chicken and watermelon"],
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

ability_icons = {}
ability_icons.update({"Aatrox": [champ_icon_dictionary["Aatrox"], champ_icon_dictionary["Ahri"], champ_icon_dictionary["Zac"]]})

class Qoute:
    def __init__(self, frame, window, chosen_champ_qoute):
        self.frame = frame
        self.window = window
        self.champion_guess = StringVar()
        self.max_displayed_champs = 5
        self.number_of_guesses = 0

        self.game_won = False

        # Labels as fields, None atm
        self.guess_sign = None
        self.chosen_champ_qoute = chosen_champ_qoute

        self.icon_labels = []
        self.guessed_champions = []
        self.all_guesses = []
        self.displayed_champ_widgets = []
        self.champ_list = champ_list
        self.images = []
        for i in range(len(icon_images)):
            self.images.append(self.image_loader(icon_images[i])) # Adds icon images to self.images
        
        self.window.after(100, lambda: self.window.bind("<Configure>", self.resize_handler))
    
    def resize_handler(self, event=None):
        pass

    def title_creator(self):
        """Creates a label with text for guessing champions.
        Also displays if u have already guessed champ."""
        self.Loldle_title = Label(
            self.frame, 
            text="LOLDLE-CLONE", 
            font=("Copperplate Gothic Bold", 50),
            bg="#1E2328",
            fg="white", 
            highlightbackground="#EDB933",
            highlightcolor="#EDB933",
            highlightthickness=3
        )
        self.Loldle_title.grid(row=0, rowspan=4, column=2, columnspan=9)
    
    def image_loader(self, path):
        """Loads an image from a given path and resizes the images."""
        self.window.update_idletasks()
        size_parameter = min(self.window.winfo_height(), self.window.winfo_width())/5
        try: # Opens image with PIL, resizes it and returns tkinter-image
            image = Image.open(path) 
            image = image.resize((int(size_parameter*0.3),int(size_parameter*0.3)), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e: # Error printed with path and Exception
            print(f"Could not load image, {path}: {e}")
            return None
    
    def qoute_creater(self):
        labeltest = Label(
            self.frame, 
            text=f'Which champion says: "{self.chosen_champ_qoute}"', 
            font=("Copperplate Gothic Bold", 20),
            fg = "white",
            bg="#1E2328",
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness="3",
        )
        labeltest.grid(row=9, rowspan=4, column=1, columnspan=11, sticky=N+S+E+W)

    def gamemode_buttons_creator(self):
        columns = [2, 4, 6, 8, 10]
        for i in range(5):
            icon_label = Button(
                self.frame,
                bg="#1E2328",
                highlightbackground="#EDB933",
                highlightcolor="#EDB933",
                highlightthickness=3,
                image=self.images[i],
            )
            icon_label.grid(row=5, rowspan=2, column=columns[i], sticky=N+S+E+W)
            self.icon_labels.append(icon_label) # Adds labels to list for future editing
    
    def select_from_list(self, event):
        selected_index = self.dropdown_listbox.curselection()
        if selected_index:
            selected_champ = self.dropdown_listbox.get(selected_index[0])
            self.champion_guess.set(selected_champ)
            self.dropdown_listbox.place_forget()  # Hide dropdown after selection
        
    def tab_autocomplete(self, event):
        if self.dropdown_listbox.size() > 0:  # Ensure listbox has items
            selected_champ = self.dropdown_listbox.get(0)  # Get the first champion
            self.champion_guess.set(selected_champ)  # Set entry text to first champion
            self.dropdown_listbox.place_forget()  # Hide dropdown
            return "break"  # Prevents default Tab behavior
    
    def update_autofill(self, event=None):
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
    
    def create_guess_field(self):
        """Function for creating entry and button for guessing champions."""
        self.champ_guess_field = Entry(
            self.frame, 
            bg="#1E2328", 
            fg="white", 
            textvariable=self.champion_guess, 
            font=("Copperplate Gothic Bold", 15),
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness=2
        )
        self.champ_guess_field.grid(row=14, column=1, columnspan=9, sticky=N+S+E+W)

        # Creates the essential and immensly powerful listbox widget :D
        self.dropdown_listbox = Listbox(
            self.frame, 
            font=("Copperplate Gothic Bold", 15), 
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
        self.champ_guess_field.bind("<Return>", lambda event: self.display_champ_guess()) # Does a guess when you press enter

        # Button for making a guess which runs the display_champ_info method
        self.arrow_button = Button(
            self.frame, 
            bg="#1E2328", 
            command = self.display_champ_guess,
            text="➤",
            fg="white",
            font="Arial"
        )
        self.arrow_button.grid(row=14, column=10, columnspan=2, sticky=N+S+E+W)
    
    def show_duplicate_warning(self, champ_name):
        """Function for showing a warning if making the same guess"""
        # Update the guess sign to show the duplicate warning
        original_text = self.labeltest["text"]
        self.labeltest.config(
            text=f"You've already guessed {champ_name}!",
            fg="#f52727"  # Red text for warning
        )

        # Schedule reverting back to original text after 2 seconds
        self.window.after(2000, lambda: self.guess_sign.config(
            text=original_text,
            fg="white"  # Revert to original color
        ))

    def clear_displayed_champs(self):
        """Removes all currently displayed champion widgets"""
        for widget_set in self.displayed_champ_widgets:
            for widget in widget_set:
                widget.grid_forget()
        self.displayed_champ_widgets = []
    
    def guess_colorer(self,  guess_labels, champ_name):
        """Changes the color of the champion labels based on whether or not they are correct.
        Green for correct, orange for partially correct and red for wrong."""

        guess_labels[i].config(bg="#21ed1a") # grøn
        guess_labels[i].config(bg="#f52727") # rød

        correct_guess = (champ_name == self.random_chosen_champ) # Chooses the correct guess
        all_correct = True # Assumes the user guessed correctly initially

        if correct_guess and all_correct and not self.game_won: # If user guessed correct and game hasn't been won yet
            self.game_won = True
            self.show_victory_popup() # Victory pop-up screen to congratulate

    def display_champ_guess(self):
        if self.game_won:
            return

        champ_guess = self.champion_guess.get().strip()

        # Check if the champion exists in the dictionary
        if champ_guess not in champ_icon_dictionary:
            print(f"Champion {champ_guess} not found in dictionary.")
            return

        # Check if this champion has already been guessed
        if champ_guess in self.guessed_champions:
            self.show_duplicate_warning(champ_guess)
            return

        # Add the champion to the guessed list (fixing .add() issue)
        self.guessed_champions.append(champ_guess)

        # Clear the entry field after guessing
        self.champion_guess.set("")

        # Increment guess counter
        self.number_of_guesses += 1

        guess_widgets = []
        
        # Load champion icon
        champ_icon = self.image_loader(champ_icon_dictionary[champ_guess])
        if champ_icon is None:
            print(f"Failed to load image for {champ_guess}")
            return

        # Store reference to prevent garbage collection
        self.current_champ_icon = champ_icon  

        # Champion icon label
        champion_label = Label(self.frame, image=self.current_champ_icon, bg="#1E2328")
        champion_label.image = self.current_champ_icon
        guess_widgets.append(champion_label)

        # Champion information label
        info_label = Label(self.frame, text=f"{champ_guess}")
        guess_widgets.append(info_label)

        # Add this guess to the beginning of our list
        self.all_guesses.insert(0, {
            'widgets': guess_widgets,
            'name': champ_guess
        })

        # Clear previously displayed champions
        self.clear_displayed_champs()

        # Display only the most recent 5 guesses (or fewer if less than 5 guesses made)
        displayed_guesses = self.all_guesses[:self.max_displayed_champs]

        for idx, guess in enumerate(displayed_guesses):
            row_position = 15 + (idx * 2)  # Each guess takes 2 rows, starting from row 15

            # Place champion icon
            guess['widgets'][0].grid(row=row_position, rowspan=2, column=2, sticky=N+S+E+W, padx=0, pady=4)

            # Place champion text / label
            guess['widgets'][1].grid(row=row_position, rowspan=2, column=3, columnspan=7, sticky=N+S+E+W, padx=0, pady=4)

            # Save references to displayed widgets
            self.displayed_champ_widgets.append(guess['widgets'])

            # Apply coloring and check for victory
            self.guess_colorer(guess['widgets'], guess['name'])

        print(f"Displaying: {champ_guess}")  # Debug print to confirm the function runs

    def guess_label_creator(self):
        guessed_champ = 4

    def guess_label_colorer(self):
        pass

    def redo_gui():
        random_chosen_champ = random.choice(list(champion_qoutes.keys()))
        chosen_champ_qoute = random.choice(champion_qoutes[random_chosen_champ])

        bg_image = Image.open(background_image)
        bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_img_L = Label(frame, image=bg_image)
        bg_img_L.grid(row=0, rowspan=50, column=0, columnspan=15)
        bg_img_L.image = bg_image

        qoute_game = Qoute(frame, window, chosen_champ_qoute)

        qoute_game.qoute_creater()
        qoute_game.title_creator()
        qoute_game.gamemode_buttons_creator()
        qoute_game.create_guess_field()

    # Potentially useful functions from the Classic class
    # -------------------------------------------------------------
    # Classic.guess_champ, only certain elements that can be copied
    # Classic.clear_displayed_champs
    # Classic.select_from_list
    # Classic.tab_autocomplete
    # Classic.update_autofill
    
    # New functions needed
    # ----------------------------------
    # A function to create the qoute label with the qoute
    # A new function to display the 5 most recently guessed champions
    # A function to color the champs based on if they're correct
    
    # Other
    # -------------------------------------------------------------------------------------------------
    # Website to easily webscrape qoutes from using BeautifulSoup: https://www.thyquotes.com/league-of-legends/

class Ability:
    def __init__(self, frame, window, champion_info):
        self.frame = frame
        self.window = window
        self.champion_guess = StringVar()
        self.champion_info = champion_info
        
        self.champ_list = list(champion_info.keys())
        
        self.guessed_champions = set()
        self.images = []
        for path in icon_images:
            self.images.append(self.image_loader(path, 1)) # Adds icon images to self.images
        
        self.Loldle_title = None
        self.ability_icon_label = None
        self.ability_text_label = None
        
        self.window.after(100, lambda: self.window.bind("<Configure>", lambda event: self.resize_handler()))
        
    def resize_handler(self):
        #self.ability_icon_label.config()
        pass
        # self.ability_text_label.config()
            
    def title_creator(self):
        """Function to create icons for the different gamemodes."""
        # Creates the title with golden border
        self.Loldle_title = Label(
            self.frame, 
            text="LOLDLE-CLONE", 
            font=("Copperplate Gothic Bold", 40),
            bg="#1E2328",
            fg="white", 
            highlightbackground="#EDB933",
            highlightcolor="#EDB933",
            highlightthickness=3
        )
        self.Loldle_title.grid(row=0, rowspan=4, column=2, columnspan=9)

        # Creates two lists for the gamemode icon labels
        columns = [2, 4, 6, 8, 10]
        self.icon_labels = []

        for i in range(5):
            icon_label = Button(
                self.frame,
                bg="#1E2328",
                highlightbackground="#EDB933",
                highlightcolor="#EDB933",
                highlightthickness=3,
                image=self.images[i],
            )
            icon_label.grid(row=5, rowspan=2, column=columns[i], sticky=N+S+E+W)
            self.icon_labels.append(icon_label) # Adds labels to list for future editing
    
    def image_loader(self, path, resizing_factor):
        """Loads an image from a given path and resizes the images."""
        self.window.update_idletasks()
        size_parameter = min(self.window.winfo_height(), self.window.winfo_width())/5 * resizing_factor
        try: # Opens image with PIL, resizes it and returns tkinter-image
            image = Image.open(path) 
            image = image.resize((int(size_parameter*0.3),int(size_parameter*0.3)), Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e: # Error printed with path and Exception
            print(f"KUN IKKE LOADE IMAGE :( {path}: {e}")
            return None
        
    def ability_label_creator(self):
        chosen_champ = random.choice(list(ability_icons.keys()))
        chosen_ability = random.choice(ability_icons[chosen_champ])
        
        ability_image = self.image_loader(chosen_ability, 2)
        
        self.ability_icon_label = Label(
            self.frame, 
            image=ability_image, 
            bg="#1E2328",
            #height=100,
            #width=100,
        )
        self.ability_icon_label.image = ability_image
        self.ability_icon_label.grid(row=11, rowspan=2, column=4, columnspan=5, pady=4)
        
        self.ability_text_label = Label(
            self.frame,
            text="Guess which champion this ability belongs to!",
            font=("Copperplate Gothic Bold", 23),
            fg="white",
            bg="#1E2328",
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness=3
        )
        self.ability_text_label.grid(row=9, rowspan=2, column=1, columnspan=11, sticky=N+S+E+W)
    
    def guess_champ(self):
        """Function for creating entry and button for guessing champions."""
        self.champ_guess_field = Entry(
            self.frame, 
            bg="#1E2328", 
            fg="white", 
            textvariable=self.champion_guess, 
            font=("Copperplate Gothic Bold", 15),
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness=2
        )
        self.champ_guess_field.grid(row=14, column=1, columnspan=9, sticky=N+S+E+W)

        # Creates the essential and immensly powerful listbox widget :D
        self.dropdown_listbox = Listbox(
            self.frame, 
            font=("Copperplate Gothic Bold", 15), 
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
            text="➤",
            fg="white",
            font="Arial"
        )
        self.arrow_button.grid(row=14, column=10, columnspan=2, sticky=N+S+E+W)

    def update_autofill(self, event=None):
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
        if self.dropdown_listbox.size() > 0:  # Ensure listbox has items
            selected_champ = self.dropdown_listbox.get(0)  # Get the first champion
            self.champion_guess.set(selected_champ)  # Set entry text to first champion
            self.dropdown_listbox.place_forget()  # Hide dropdown
            return "break"  # Prevents default Tab behavior

    def select_from_list(self, event):
        selected_index = self.dropdown_listbox.curselection()
        if selected_index:
            selected_champ = self.dropdown_listbox.get(selected_index[0])
            self.champion_guess.set(selected_champ)
            self.dropdown_listbox.place_forget()  # Hide dropdown after selection
    
    def create_guesses(self):
        """Function to create a label of the guessed champion."""
        guess_label = Label(
            self.frame,
            text=f"{self.champion_guess}",
            fg="white",
            font=("Copperplate Gothic Bold", 15),
            bg="red",
        )
        #guess_label.grid(row=y, rowspan=y, column=x, columnspan=x) # CHANGE
        
        guess_image_label = Label(
            self.frame,
            image=self.image_loader(champ_icon_dictionary[self.champion_guess]),
            bg="red",
        )
        #guess_image_label.grid(row=y, rowspan=y, column=x, columnspan=x) # CHANGE
    
    @staticmethod
    def redo_gui():
        
        bg_image = Image.open(background_image)
        bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_img_L = Label(frame, image=bg_image)
        bg_img_L.grid(row=0, rowspan=30, column=0, columnspan=15)
        bg_img_L.image = bg_image
        
        ability_game = Ability(frame, window, classic_champion_data)
        ability_game.ability_label_creator()
        ability_game.title_creator()
        ability_game.guess_champ()

class Emoji:
    def __init__(self):
        pass

class Splash:
    def __init__(self):
        pass

class Classic:
    def __init__(self, frame, champion_info, window, lol_font_large, lol_font_small, number_of_guesses, chosen_champ):
        
        # Initializing certain labels, a window, a frame and certain field-values
        self.frame = frame
        self.champion_guess = StringVar()
        self.champion_info = champion_info
        self.window = window
        self.lol_font_large = lol_font_large
        self.lol_font_small = lol_font_small
        self.number_of_guesses = number_of_guesses
        self.chosen_champ = chosen_champ
        self.max_displayed_champs = 5

        # Different lists 
        self.champ_list = list(champion_info.keys())
        self.icon_labels = []
        self.information_labels = []
        self.guess_labels = []
        # self.champ_guesses = []
        self.all_guesses = []
        self.displayed_champ_widgets = []
        self.Classic_widgets = []

        # Keep track of guessed champion names to prevent duplicates
        self.guessed_champions = set()
        self.images = []
        for path in icon_images:
            self.images.append(self.image_loader(path)) # Adds icon images to self.images
        
        # Game won flag
        self.game_won = False
         
        # List for switching GUI:
        self.gui_switches = [
            self.switch_to_Classic,
            self.switch_to_Qoute,
            self.switch_to_Ability,
            self.switch_to_Emoji,
            self.switch_to_Splash,
        ]
        
        # Labels as fields, defined as None atm.
        self.guess_sign = None
        self.Loldle_title = None
        self.icon_label = None
        self.champ_guess_field = None
        self.arrow_button = None
        self.information = None
        self.line = None

        # Initializing certain functions
        self.create_icons()
        self.guess_sign_creator()
        self.guess_champ()
        self.display_champ_headers()

        # Resizes certain elements when resizing window
        self.window.after(100, lambda: self.window.bind("<Configure>", lambda event: self.resize_handler()))
    
    def resize_handler(self):
        """Function for resizing different elements based on self.handling_size"""
        self.handling_size = int(min(self.window.winfo_height(), self.window.winfo_width())/10)
        if self.Loldle_title: # Configures the title size
            self.Loldle_title.config(font=("Copperplate Gothic Bold", int(self.handling_size*0.5)))
        if self.guess_sign: # Configures the guess sign size
            self.guess_sign.config(font=("Copperplate Gothic Bold", int(self.handling_size*0.3)))
        if self.icon_label: # Configures the icon images size
            for i in range(len(self.images)):
                original_image = Image.open(icon_images[i])
                resized_image = original_image.resize((int(self.handling_size*0.5), int(self.handling_size*0.5)), Image.Resampling.BILINEAR)
                self.images[i] = ImageTk.PhotoImage(resized_image)
                self.icon_label.config(image=self.images[i])
                self.icon_label.config(width=int(self.handling_size*0.5), height=int(self.handling_size*0.5))
        if self.information: # Configures the labels (with champ info)
            for i in range(len(self.information_labels)):
                self.information_labels[i].config(font=("Copperplate Gothic Bold", int(self.handling_size*0.1)))
    
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

        if correct_guess and all_correct and not self.game_won: # If user guessed correct and game hasn't been won yet
            self.game_won = True
            self.show_victory_popup() # Victory pop-up screen to congratulate

    def show_victory_popup(self):
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
        
        # Close button
        close_button = Button(
            content_frame,
            text="Close",
            font=("Arial Bold", 13),
            bg="#01708D",
            fg="white",
            command=popup.destroy,
        )
        close_button.pack(pady=10)
        
        # Animation for pop-up screen
        popup.attributes("-alpha", 0.0) # 100% transparent
        for i in range(1, 11):
            popup.attributes("-alpha", i/10) # Increases visibility
            popup.update()
            time.sleep(0.02)

    def guess_sign_creator(self):
        """Creates a label with text for guessing champions.
        Also displays if u have already guessed champ."""
        self.guess_sign = Label(
            self.frame, 
            text="Guess today's League of Legends champion!", 
            font="Arial",
            bg="#1E2328",
            fg="white", 
            highlightbackground="#EDB933",
            highlightcolor="#EDB933",
            highlightthickness=2
            )
        self.guess_sign.grid(row=9, rowspan=2, column=1, columnspan=11)
    
    def image_loader(self, path):
        """Loads an image from a given path and resizes the images."""
        self.window.update_idletasks()
        size_parameter = min(self.window.winfo_height(), self.window.winfo_width())/5
        try: # Opens image with PIL, resizes it and returns tkinter-image
            image = Image.open(path) 
            image = image.resize((int(size_parameter*0.3),int(size_parameter*0.3)), Image.Resampling.LANCZOS)
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
            font="Arial",
            bg="#1E2328",
            fg="white", 
            highlightbackground="#EDB933",
            highlightcolor="#EDB933",
            highlightthickness=3
        )
        self.Loldle_title.grid(row=0, rowspan=4, column=2, columnspan=9)

        # Creates two lists for the gamemode icon labels
        columns = [2, 4, 6, 8, 10]
        self.icon_labels = []

        for i in range(5):
            icon_label = Button(
                self.frame,
                bg="#1E2328",
                highlightbackground="#EDB933",
                highlightcolor="#EDB933",
                highlightthickness=3,
                image=self.images[i],
                command=self.gui_switches[i])
            icon_label.grid(row=5, rowspan=2, column=columns[i], sticky=N+S+E+W)
            self.icon_labels.append(icon_label) # Adds labels to list for future editing

    def lebronmination(self):
        """Easter Egg function that displays lebron images instead of champion info if u type certain words."""
        guess = self.champion_guess.get().strip().lower()

        if guess in lebron_texts:
            lebron_image = self.image_loader(r"misc images/Lebron.png")
            
            if lebron_image is None: # If there is an error with loading image, simply returns None for error handling
                return
            
            self.lebron_image_ref = lebron_image # Store image reference in self to prevent garbage collection

            # Loops through the widgets and removes text and adds an image of lebron
            for widget_list in self.displayed_champ_widgets:
                for widget in widget_list:
                    widget.config(
                        text="",
                        image=self.lebron_image_ref
                    )
                    widget.image = self.lebron_image_ref # Keep a reference for tkinter-issues

            self.window.update_idletasks()  # Force UI update
    
    def guess_champ(self):
        """Function for creating entry and button for guessing champions."""
        self.champ_guess_field = Entry(
            self.frame, 
            bg="#1E2328", 
            fg="white", 
            textvariable=self.champion_guess, 
            font=self.lol_font_small,
            highlightbackground="#01708D",
            highlightcolor="#01708D",
            highlightthickness=2
        )
        self.champ_guess_field.grid(row=12, column=1, columnspan=9, sticky=N+S+E+W)

        # Creates the essential and immensly powerful listbox widget :D
        self.dropdown_listbox = Listbox(
            self.frame, 
            font=self.lol_font_small, 
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
            font="Arial"
        )
        self.arrow_button.grid(row=12, column=10, columnspan=2, sticky=N+S+E+W)

    def update_autofill(self, event=None):
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
        if self.dropdown_listbox.size() > 0:  # Ensure listbox has items
            selected_champ = self.dropdown_listbox.get(0)  # Get the first champion
            self.champion_guess.set(selected_champ)  # Set entry text to first champion
            self.dropdown_listbox.place_forget()  # Hide dropdown
            return "break"  # Prevents default Tab behavior

    def select_from_list(self, event):
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
                font="Arial",
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
        champ_icon = self.image_loader(champ_icon_dictionary[champ_guess])
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

    def clear_gui(self):
        for widget in self.frame.winfo_children():
            widget.grid_forget()
    
    def switch_to_Classic(self):
        pass

    def switch_to_Qoute(self):
        self.clear_gui()
        Qoute.redo_gui()

    def switch_to_Ability(self):
        self.clear_gui()
        Ability.redo_gui()

    def switch_to_Emoji(self):
        pass

    def switch_to_Splash(self):
        pass

    @staticmethod # Removes make_gui from self. attributes, but remains in the class
    def make_gui():
        """The central function for creating a GUI in a frame in a window"""       
        global window 
        window = Tk()
        window.geometry("1200x900")
        window.title("NBA Youngboy can sing!!!!")

        global frame
        frame = Frame(window, bg="white", bd=0)
        frame.grid(sticky=N+S+E+W)

        # Creating the variables for parameters in the Classic-class initilization
        custom_font_large = tkinter.font.Font(family="MPH 2B Damase", size=30, weight="bold") # Making custom font similar to LOL's, large
        custom_font_small = tkinter.font.Font(family="MPH 2B Damase", size=14, weight="bold") # Making custom font similar to LOL's, small
        number_of_guesses = 0
        chosen_champ = random.choice(list(classic_champion_data.keys())) # Randomly chooses a champion

        # Creates an instance of the Classic class, recieving different parameters
        classic_game = Classic(frame, classic_champion_data, window, custom_font_large, custom_font_small, number_of_guesses, chosen_champ)

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

        # Makes sure the game runs in a loop
        window.mainloop()

# Calls the make_gui method from the Classic-class, running the whole shabang
Classic.make_gui()