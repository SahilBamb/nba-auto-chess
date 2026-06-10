"""
Generates the NBA player name mapping for the pkm section of the translation JSON.
Run: python3 scripts/nba_names.py
"""
import json, os

NBA_NAMES = {
    "DEFAULT": "MissingNo.",
    "EGG":     "Draft Pick",
    "DITTO":   "The Chameleon",
    "SUBSTITUTE": "The Bench",
    "PILLAR_WOOD":     "Wooden Post",
    "PILLAR_IRON":     "Iron Post",
    "PILLAR_CONCRETE": "Concrete Post",

    # ── COMMON 3-stage lines ────────────────────────────────────────
    # Charmander → LeBron James
    "CHARMANDER":  "Young LeBron",
    "CHARMELEON":  "King James",
    "CHARIZARD":   "The GOAT LeBron",

    # Squirtle → Stephen Curry
    "SQUIRTLE":    "Baby-Faced Curry",
    "WARTORTLE":   "Chef Curry",
    "BLASTOISE":   "Baby-Faced Assassin",

    # Geodude → Charles Oakley
    "GEODUDE":     "Young Oak",
    "GRAVELER":    "Oakley",
    "GOLEM":       "Charles Oakley",

    # Alolan Geodude → Alec Burks (electric-rock role player)
    "ALOLAN_GEODUDE":  "Young Burks",
    "ALOLAN_GRAVELER": "Alec Burks",
    "ALOLAN_GOLEM":    "Buckets Burks",

    # Azurill → John Stockton
    "AZURILL":     "Young Stockton",
    "MARILL":      "Stockton",
    "AZUMARILL":   "John Stockton",

    # Zubat → Vince Carter
    "ZUBAT":       "Young VC",
    "GOLBAT":      "Air Canada",
    "CROBAT":      "Vince Carter",

    # Mareep → Ray Allen
    "MAREEP":      "Young Ray",
    "FLAFFY":      "Ray Allen",
    "AMPHAROS":    "Jesus Shuttlesworth",

    # Caterpie → Muggsy Bogues
    "CATERPIE":    "Young Muggsy",
    "METAPOD":     "Muggsy",
    "BUTTERFREE":  "Muggsy Bogues",

    # Weedle → Spud Webb
    "WEEDLE":      "Young Spud",
    "KAKUNA":      "Spud Webb",
    "BEEDRILL":    "Slam Dunk Champ",

    # Pidgey → Kawhi Leonard
    "PIDGEY":      "Young Kawhi",
    "PIDGEOTTO":   "The Klaw",
    "PIDGEOT":     "Kawhi Leonard",

    # Rattata → Tony Allen
    "RATTATA":         "Young T-Allen",
    "RATICATE":        "Tony Allen",
    "ALOLAN_RATTATA":  "Young Grindfather",
    "ALOLAN_RATICATE": "Grindfather",

    # Spearow → Ron Artest
    "SPEAROW":     "Young Artest",
    "FEAROW":      "Ron Artest",

    # Poliwag → Gary Payton
    "POLIWAG":     "Young GP",
    "POLIWHIRL":   "The Glove",
    "POLIWRATH":   "Gary Payton",
    "POLITOED":    "GP II",

    # Machop → Shaquille O'Neal
    "MACHOP":      "Young Shaq",
    "MACHOKE":     "Diesel",
    "MACHAMP":     "Shaquille O'Neal",

    # Aron → Joel Embiid
    "ARON":        "Young Embiid",
    "LAIRON":      "The Process",
    "AGGRON":      "Joel Embiid",

    # Magnemite → Nikola Jokic
    "MAGNEMITE":   "Young Joker",
    "MAGNETON":    "Joker",
    "MAGNEZONE":   "Nikola Jokic",

    # Klink → Pau Gasol
    "KLINK":       "Young Pau",
    "KLANG":       "Pau Gasol",
    "KLINKLANG":   "Smooth Operator",

    # Litwick → Kevin Love
    "LITWICK":     "Young Love",
    "LAMPENT":     "Kevin Love",
    "CHANDELURE":  "K-Love",

    # Goomy → Nikola Vucevic
    "GOOMY":       "Young Vucevic",
    "SLIGOO":      "Nikola Vucevic",
    "HISUI_SLIGGOO": "Vooch Alt",
    "GOODRA":      "Vooch",
    "HISUI_GOODRA":  "Vooch Prime",

    # Lillipup → Patrick Beverley
    "LILLIPUP":    "Young Bev",
    "HERDIER":     "Pat Bev",
    "STOUTLAND":   "Patrick Beverley",

    # Zigzagoon → Shane Battier
    "ZIGZAGOON":          "Young Battier",
    "LINOONE":            "Shane Battier",
    "GALARIAN_ZIGZAGOON": "Young Obstagoon",
    "GALARIAN_LINOONE":   "Battier Alt",
    "OBSTAGOON":          "The Glue Guy",

    # Chespin → Rudy Gobert
    "CHESPIN":     "Young Gobert",
    "QUILLADIN":   "The Stifle Tower",
    "CHESNAUGHT":  "Rudy Gobert",

    # Blipbug → Chet Holmgren
    "BLIPBUG":     "Young Holmgren",
    "DOTTLER":     "Chet",
    "ORBEETLE":    "Chet Holmgren",

    # Fennekin → Steph Curry Alt (or use different player)
    "FENNEKIN":    "Young Dragic",
    "BRAIXEN":     "Goran Dragic",
    "DELPHOX":     "The Dragon",

    # Treecko → Russell Westbrook
    "TREECKO":     "Young Brodie",
    "GROVYLE":     "Brodie",
    "SCEPTILE":    "Russell Westbrook",

    # Torchic → James Harden
    "TORCHIC":     "Young Harden",
    "COMBUSKEN":   "The Beard",
    "BLAZIKEN":    "James Harden",

    # Mudkip → Chris Paul
    "MUDKIP":      "Young CP3",
    "MARSHTOMP":   "CP3",
    "SWAMPERT":    "Chris Paul",

    # Turtwig → DeMarcus Cousins
    "TURTWIG":     "Young Boogie",
    "GROTLE":      "DeMarcus Cousins",
    "TORTERRA":    "Boogie Cousins",

    # Chimchar → Kyrie Irving
    "CHIMCHAR":    "Young Kyrie",
    "MONFERNO":    "Uncle Drew",
    "INFERNAPE":   "Kyrie Irving",

    # Piplup → Kemba Walker
    "PIPLUP":      "Young Kemba",
    "PRINPLUP":    "Kemba",
    "EMPOLEON":    "Kemba Walker",

    # Seedot → Luol Deng
    "SEEDOT":      "Young Deng",
    "NUZLEAF":     "Luol Deng",
    "SHIFTRY":     "Loul Deng",

    # Starly → Paul George
    "STARLY":      "Young PG",
    "STARAVIA":    "PG-13",
    "STARAPTOR":   "Paul George",

    # ── UNCOMMON 3-stage lines ──────────────────────────────────────
    # Cleffa → Steve Nash
    "CLEFFA":      "Young Nash",
    "CLEFAIRY":    "Nash",
    "CLEFABLE":    "Steve Nash",

    # Igglybuff → Reggie Miller
    "IGGLYBUFF":   "Young Reggie",
    "JIGGLYPUFF":  "Reggie Miller",
    "WIGGLYTUFF":  "The Knick Killer",

    # Nidoranm → Patrick Ewing
    "NIDORANM":    "Young Ewing",
    "NIDORINO":    "Ewing",
    "NIDOKING":    "Patrick Ewing",

    # Nidoranf → Manu Ginobili
    "NIDORANF":    "Young Manu",
    "NIDORINA":    "El Contusion",
    "NIDOQUEEN":   "Manu Ginobili",

    # Duskull → Jayson Tatum
    "DUSKULL":     "Young Tatum",
    "DUSCLOPS":    "JT",
    "DUSKNOIR":    "Jayson Tatum",

    # Horsea → Dirk Nowitzki
    "HORSEA":      "Young Dirk",
    "SEADRA":      "Dirk",
    "KINGDRA":     "Dirk Nowitzki",

    # Bagon → Kobe Bryant
    "BAGON":       "Young Kobe",
    "SHELGON":     "Black Mamba",
    "SALAMENCE":   "Kobe Bryant",

    # Deino → Donovan Mitchell
    "DEINO":       "Young Spida",
    "ZWEILOUS":    "Donovan Mitchell",
    "HYDREIGON":   "Spida Mitchell",

    # Duskull (already done) …

    # Ralts → Luka Doncic
    "RALTS":       "Young Luka",
    "KIRLIA":      "Luka Magic",
    "GARDEVOIR":   "Luka Doncic",
    "GALLADE":     "Luka 77",

    # Magnemite (already done) …

    # Machop (already done) …

    # Sandshrew → Dennis Rodman (scrappy, gritty)
    "SANDSHREW":       "Young Worm",
    "SANDSLASH":       "Dennis Rodman",
    "ALOLAN_SANDSHREW":"Young Worm Alt",
    "ALOLAN_SANDSLASH":"Worm Alt",

    # Ekans → Bruce Bowen
    "EKANS":       "Young Bowen",
    "ARBOK":       "Bruce Bowen",

    # Diglett → Nate Robinson
    "DIGLETT":         "Young Nate",
    "DUGTRIO":         "Nate Robinson",
    "ALOLAN_DIGLETT":  "Young Nate Alt",
    "ALOLAN_DUGTRIO":  "Nate Robinson Alt",

    # Growlithe → Draymond Green
    "GROWLITHE":       "Young Dray",
    "ARCANINE":        "Draymond Green",
    "HISUI_GROWLITHE": "Young Dray Alt",
    "HISUI_ARCANINE":  "Draymond Prime",

    # Krabby → Rajon Rondo
    "KRABBY":      "Young Rondo",
    "KINGLER":     "Rajon Rondo",

    # Voltorb → Baron Davis
    "VOLTORB":         "Young B-Diddy",
    "ELECTRODE":       "Baron Davis",
    "HISUI_VOLTORB":   "Young Baron Alt",
    "HISUI_ELECTRODE": "B-Diddy Alt",

    # Tentacool → Rajon Rondo Alt (already used Krabby for Rondo)
    # Let's use Arvydas Sabonis
    "TENTACOOL":   "Young Sabonis",
    "TENTACRUEL":  "Arvydas Sabonis",

    # Slowpoke → Marc Gasol
    "SLOWPOKE":         "Young Marc",
    "SLOWBRO":          "Marc Gasol",
    "SLOWKING":         "Big Fella",
    "GALARIAN_SLOWPOKE":"Young Marc Alt",
    "GALARIAN_SLOWBRO": "Marc Alt",
    "GALARIAN_SLOWKING":"Big Fella Alt",

    # Magby → DeMar DeRozan
    "MAGBY":       "Young DeRozan",
    "MAGMAR":      "DeMar",
    "MAGMORTAR":   "DeMar DeRozan",

    # Munchlax → Bam Adebayo
    "MUNCHLAX":    "Young Bam",
    "SNORLAX":     "Bam Adebayo",

    # Aipom → Dejounte Murray
    "AIPOM":       "Young Dejounte",
    "AMBIPOM":     "Dejounte Murray",

    # Buneary → Jaylen Brown
    "BUNEARY":     "Young JB",
    "LOPUNNY":     "Jaylen Brown",
    "MEGA_LOPUNNY":"JB Prime",

    # Electrike → Bradley Beal
    "ELECTRIKE":       "Young Beal",
    "MANECTRIC":       "Bradley Beal",
    "MEGA_MANECTRIC":  "Beal Prime",

    # Hoothoot → Dwight Howard
    "HOOTHOOT":    "Young Dwight",
    "NOCTOWL":     "Superman Dwight",

    # Spinarak → Matisse Thybulle
    "SPINARAK":    "Young Thybulle",
    "ARIADOS":     "Matisse Thybulle",

    # Seel → Brook Lopez
    "SEEL":        "Young Brook",
    "DEWGONG":     "Brook Lopez",

    # Grimer → Tristan Thompson
    "GRIMER":          "Young TT",
    "MUK":             "Tristan Thompson",
    "ALOLAN_GRIMER":   "Young TT Alt",
    "ALOLAN_MUK":      "TT Alt",

    # Magnemite → already done

    # Koffing → Bismack Biyombo
    "KOFFING":         "Young Biyombo",
    "WEEZING":         "Bismack Biyombo",
    "GALARIAN_WEEZING":"Biyombo Alt",

    # Onix → Gorgui Dieng
    "ONIX":        "Young Onix",
    "STEELIX":     "Gorgui Dieng",
    "MEGA_STEELIX":"Dieng Prime",

    # Mime Jr → Ricky Rubio
    "MIME_JR":     "Young Rubio",
    "MR_MIME":     "Ricky Rubio",

    # Jynx (Smoochum) → Sabrina Ionescu (or keep NBA: use Gilbert Arenas)
    "SMOOCHUM":    "Young Gil",
    "JYNX":        "Agent Zero",

    # Horsea (already done)

    # Misdreavus → OG Anunoby
    "MISDREAVUS":  "Young OG",
    "MISMAGIUS":   "OG Anunoby",

    # Bronzor → Thaddeus Young
    "BRONZOR":     "Young Thad",
    "BRONZONG":    "Thaddeus Young",

    # Hoothoot (done)

    # Buizel → Ja Morant
    "BUIZEL":      "Young Ja",
    "FLOATZEL":    "Ja Morant",

    # Chinchou → Elfrid Payton
    "CHINCHOU":    "Young Elfrid",
    "LANTURN":     "Elfrid Payton",

    # Poochyena → Jordan Clarkson
    "POOCHYENA":   "Young Clarkson",
    "MIGHTYENA":   "Jordan Clarkson",

    # Drifloon → Bogdan Bogdanovic
    "DRIFLOON":    "Young Bogdan",
    "DRIFBLIM":    "Bogdan Bogdanovic",

    # Shroomish → Marcus Morris
    "SHROOMISH":   "Young Morris",
    "BRELOOM":     "Marcus Morris",

    # Snubull → Markieff Morris
    "SNUBULL":     "Young Markieff",
    "GRANBULL":    "Markieff Morris",

    # Corphish → Kyle Kuzma
    "CORPHISH":    "Young Kuz",
    "CRAWDAUNT":   "Kyle Kuzma",

    # Cacnea → Boris Diaw
    "CACNEA":      "Young Diaw",
    "CACTURNE":    "Boris Diaw",

    # Numel → Tobias Harris
    "NUMEL":       "Young Tobi",
    "CAMERUPT":    "Tobias Harris",
    "MEGA_CAMERUPT":"Tobias Harris Prime",

    # Spoink → Kyle Anderson
    "SPOINK":      "Young Slo-Mo",
    "GRUMPIG":     "Kyle Anderson",

    # Swablu → Anthony Edwards
    "SWABLU":      "Young Ant",
    "ALTARIA":     "Anthony Edwards",
    "MEGA_ALTARIA":"Ant-Man",

    # Lotad → Kyle Lowry
    "LOTAD":       "Young Lowry",
    "LOMBRE":      "Kyle Lowry",
    "LUDICOLO":    "Lowry Dancing",

    # Spheal (done)

    # Tympole → Tyus Jones
    "TYMPOLE":     "Young Tyus",
    "PALPITOAD":   "Tyus Jones",
    "SEISMITOAD":  "Tyus Jones Prime",

    # Venipede → Myles Turner
    "VENIPEDE":    "Young Turner",
    "WHIRLIPEDE":  "Myles Turner",
    "SCOLIPEDE":   "The Dungeon",

    # Sewaddle → Kelly Oubre
    "SEWADDLE":    "Young Oubre",
    "SWADLOON":    "Kelly Oubre",
    "LEAVANNY":    "Swaggy Oubre",

    # Timburr → Julius Randle
    "TIMBURR":     "Young Randle",
    "GURDURR":     "Julius Randle",
    "CONKELDURR":  "The Randle",

    # Tynamo → Cole Anthony
    "TYNAMO":      "Young Cole",
    "EELEKTRIK":   "Cole Anthony",
    "EELEKTROSS":  "Cole Anthony Prime",

    # Snivy → Jaylen Brown Alt → use Shai Gilgeous-Alexander
    "SNIVY":       "Young SGA",
    "SERVINE":     "SGA",
    "SERPERIOR":   "Shai Gilgeous-Alexander",

    # Scorbunny → Zach LaVine
    "SCORBUNNY":   "Young LaVine",
    "RABOOT":      "Zach LaVine",
    "CINDERACE":   "Air LaVine",

    # Grookey → De'Aaron Fox
    "GROOKEY":     "Young Fox",
    "THWACKEY":    "De'Aaron Fox",
    "RILLABOOM":   "Swipa Fox",

    # Sobble → Tyrese Haliburton
    "SOBBLE":      "Young Hali",
    "DRIZZILE":    "Haliburton",
    "INTELEON":    "Tyrese Haliburton",

    # Fuecoco → Jalen Green
    "FUECOCO":     "Young Jalen",
    "CROCALOR":    "Jalen Green",
    "SKELEDIRGE":  "Jalen Green Prime",

    # Sprigatito → Victor Wembanyama
    "SPRIGATITO":  "Young Wemby",
    "FLORAGATO":   "Wemby",
    "MEOWSCARADA": "Victor Wembanyama",

    # Rookidee → Miles Bridges
    "ROOKIDEE":    "Young Bridges",
    "CORVISQUIRE": "Miles Bridges",
    "CORVIKNIGHT": "Bridges Prime",

    # Oshawott → Andre Drummond
    "OSHAWOTT":    "Young Drum",
    "DEWOTT":      "Andre Drummond",
    "SAMUROTT":    "Drummond Prime",
    "HISUI_SAMUROTT": "Drummond Alt",

    # Scatterbug → Cade Cunningham
    "SCATTERBUG":      "Young Cade",
    "SPEWPA":          "Cade Cunningham",
    "VIVILLON":        "Cade Prime",

    # Vivillon forms → Regional draft picks (same player concept)
    "VIVILLON_ICY_SNOW":     "Cade (North)",
    "VIVILLON_POLAR":        "Cade (Arctic)",
    "VIVILLON_TUNDRA":       "Cade (Tundra)",
    "VIVILLON_CONTINENTAL":  "Cade (Continental)",
    "VIVILLON_GARDEN":       "Cade (Garden State)",
    "VIVILLON_ELEGANT":      "Cade (Elegant)",
    "VIVILLON_MODERN":       "Cade (Modern)",
    "VIVILLON_MARINE":       "Cade (Marine)",
    "VIVILLON_ARCHIPELAGO":  "Cade (Island)",
    "VIVILLON_HIGH_PLAINS":  "Cade (Plains)",
    "VIVILLON_SANDSTORM":    "Cade (Desert)",
    "VIVILLON_RIVER":        "Cade (River City)",
    "VIVILLON_MONSOON":      "Cade (Monsoon)",
    "VIVILLON_SAVANNA":      "Cade (Savanna)",
    "VIVILLON_SUN":          "Cade (Sunshine)",
    "VIVILLON_OCEAN":        "Cade (Ocean)",
    "VIVILLON_JUNGLE":       "Cade (Jungle)",
    "VIVILLON_FANCY":        "Cade (Fancy)",
    "VIVILLON_POKE_BALL":    "Cade (Classic)",

    # ── RARE 3-stage lines ─────────────────────────────────────────
    # Bulbasaur → Kevin Durant
    "BULBASAUR":   "Young KD",
    "IVYSAUR":     "KD",
    "VENUSAUR":    "Slim Reaper",

    # Totodile → Blake Griffin
    "TOTODILE":    "Young Blake",
    "CROCONAW":    "Lob City Blake",
    "FERALIGATR":  "Blake Griffin",

    # Larvitar → Tim Duncan
    "LARVITAR":    "Young TD",
    "PUPITAR":     "The Big Fundamental",
    "TYRANITAR":   "Tim Duncan",

    # Magby (done as 3-stage)

    # Deino (done)

    # Bergmite → Robin Lopez
    "BERGMITE":    "Young R-Lopez",
    "AVALUGG":     "Robin Lopez",
    "HISUI_AVALUGG":"R-Lopez Alt",

    # Bunnelby → Khris Middleton
    "BUNNELBY":    "Young Khris",
    "DIGGERSBY":   "Khris Middleton",

    # Kabuto → Karl-Anthony Towns
    "KABUTO":      "Young KAT",
    "KABUTOPS":    "Karl-Anthony Towns",

    # Omanyte → Clint Capela
    "OMANYTE":     "Young Clint",
    "OMASTAR":     "Clint Capela",

    # Goldeen → Kemba (used) → use Chauncey Billups
    "GOLDEEN":     "Young Chauncey",
    "SEAKING":     "Chauncey Billups",

    # Staryu → Jrue Holiday
    "STARYU":      "Young Jrue",
    "STARMIE":     "Jrue Holiday",

    # Vulpix → Klay Thompson
    "VULPIX":          "Young Klay",
    "NINETALES":       "Klay Thompson",
    "ALOLAN_VULPIX":   "Young Klay Alt",
    "ALOLAN_NINETALES":"Splash Bro Klay",

    # Shellder → Anthony Davis
    "SHELLDER":    "Young AD",
    "CLOYSTER":    "Anthony Davis",

    # Ledyba → Marcus Smart
    "LEDYBA":      "Young Smart",
    "LEDIAN":      "Marcus Smart",

    # Hisui Growlithe (done with Growlithe)

    # Paras → Ben Wallace
    "PARAS":       "Young Big Ben",
    "PARASECT":    "Ben Wallace",

    # Lotad (done)

    # Croagunk → Dillon Brooks
    "CROAGUNK":    "Young Brooks",
    "TOXICROAK":   "Dillon Brooks",

    # Sandile → Marcus Camby
    "SANDILE":     "Young Camby",
    "KROKOROK":    "Marcus Camby",
    "KROOKODILE":  "Camby Prime",

    # Solosis → Nikola Mirotic
    "SOLOSIS":     "Young Mirotic",
    "DUOSION":     "Nikola Mirotic",
    "REUNICLUS":   "Mirotic Prime",

    # Natu → P.J. Tucker
    "NATU":        "Young Tucker",
    "XATU":        "P.J. Tucker",

    # Munna → Robert Covington
    "MUNNA":       "Young RoCo",
    "MUSHARNA":    "Robert Covington",

    # Carvanha → Mo Bamba
    "CARVANHA":    "Young Bamba",
    "SHARPEDO":    "Mo Bamba",

    # Drilbur → Larry Nance Jr.
    "DRILBUR":     "Young Nance",
    "EXCADRILL":   "Larry Nance Jr.",

    # Golett → DeAndre Jordan
    "GOLETT":      "Young DJ",
    "GOLURK":      "DeAndre Jordan",

    # Joltik → Patty Mills
    "JOLTIK":      "Young Patty",
    "GALVANTULA":  "Patty Mills",

    # Binacle → Serge Ibaka
    "BINACLE":     "Young Serge",
    "BARBARACLE":  "Serge Ibaka",

    # Mienfoo → T.J. Warren
    "MIENFOO":     "Young TJ",
    "MIENSHAO":    "T.J. Warren",

    # Makuhita → Hassan Whiteside
    "MAKUHITA":    "Young Whiteside",
    "HARIYAMA":    "Hassan Whiteside",

    # Finneon → Isaiah Stewart
    "FINNEON":     "Young Stew",
    "LUMINEON":    "Isaiah Stewart",

    # Electrike (done)

    # Drifloon (done)

    # Glimmet → Paolo Banchero
    "GLIMMET":     "Young Paolo",
    "GLIMMORA":    "Paolo Banchero",

    # Honedge → Scottie Barnes
    "HONEDGE":     "Young Barnes",
    "DOUBLADE":    "Scottie Barnes",
    "AEGISLASH":   "Barnes Prime",
    "AEGISLASH_BLADE": "Barnes Unleashed",

    # Deerling seasons → seasonal award winners
    "DEERLING_SPRING": "Young Spring Star",
    "DEERLING_SUMMER": "Young Summer Star",
    "DEERLING_AUTUMN": "Young Fall Star",
    "DEERLING_WINTER": "Young Winter Star",
    "SAWSBUCK_SPRING": "All-Star Spring",
    "SAWSBUCK_SUMMER": "All-Star Summer",
    "SAWSBUCK_AUTUMN": "All-Star Autumn",
    "SAWSBUCK_WINTER": "All-Star Winter",

    # Lileep → Bol Bol
    "LILEEP":      "Young Bol",
    "CRADILY":     "Bol Bol",

    # Anorith → P.J. Washington
    "ANORITH":     "Young Wash",
    "ARMALDO":     "P.J. Washington",

    # Archen → Cam Payne
    "ARCHEN":      "Young Payne",
    "ARCHEOPS":    "Cameron Payne",

    # Tirtouga → Wendell Carter Jr.
    "TIRTOUGA":    "Young WCJ",
    "CARRACOSTA":  "Wendell Carter Jr.",

    # Cranidos → Walker Kessler
    "CRANIDOS":    "Young Kessler",
    "RAMPARDOS":   "Walker Kessler",

    # Tyrunt → Evan Mobley
    "TYRUNT":      "Young Mobley",
    "TYRANTRUM":   "Evan Mobley",

    # Cacnea (done)

    # Golbat (done)

    # Venonat → Norman Powell
    "VENONAT":     "Young Powell",
    "VENOMOTH":    "Norman Powell",

    # Sneasel → Saddiq Bey
    "SNEASEL":         "Young Bey",
    "WEAVILE":         "Saddiq Bey",
    "HISUI_SNEASEL":   "Young Bey Alt",
    "SNEASLER":        "Bey Alt",

    # Chewtle → Precious Achiuwa
    "CHEWTLE":     "Young Precious",
    "DREDNAW":     "Precious Achiuwa",

    # Burmy forms → Cam Johnson
    "BURMY_PLANT":    "Young Cam J",
    "BURMY_SANDY":    "Young Cam J Alt",
    "BURMY_TRASH":    "Young Cam J Trash",
    "WORMADAM_PLANT": "Cam Johnson",
    "WORMADAM_SANDY": "Cam Johnson Alt",
    "WORMADAM_TRASH": "Cam Johnson Hustle",
    "MOTHIM":         "Cam Johnson Prime",

    # Smoliv → Josh Giddey
    "SMOLIV":      "Young Giddey",
    "DOLLIV":      "Josh Giddey",
    "ARBOLIVA":    "Giddey Prime",

    # Nymble → Dyson Daniels
    "NYMBLE":      "Young Daniels",
    "LOKIX":       "Dyson Daniels",

    # Pidove → Anfernee Simons
    "PIDOVE":      "Young Simons",
    "TRANQUILL":   "Anfernee Simons",
    "UNFEZANT":    "Simons Prime",

    # Wooloo → Georges Niang
    "WOOLOO":      "Young Niang",
    "DUBWOOL":     "Georges Niang",

    # Yamper → Tyrese Maxey
    "YAMPER":      "Young Maxey",
    "BOLTUND":     "Tyrese Maxey",

    # Fidough → Santi Aldama
    "FIDOUGH":     "Young Santi",
    "DACHSBUN":    "Santi Aldama",

    # Capsakid → Immanuel Quickley
    "CAPSAKID":    "Young IQ",
    "SCOVILLAIN":  "Immanuel Quickley",

    # Swirlix → Bojan Bogdanovic
    "SWIRLIX":     "Young Bojan",
    "SLURPUFF":    "Bojan Bogdanovic",

    # Nacli → Nick Claxton
    "NACLI":       "Young Claxton",
    "NACLSTACK":   "Nick Claxton",
    "GARGANACL":   "Claxton Prime",

    # Lechonk → Gary Trent Jr.
    "LECHONK":     "Young GTJ",
    "OINKOLOGNE_MALE": "Gary Trent Jr.",

    # Skwovet → Garrison Mathews
    "SKWOVET":     "Young Mathews",
    "GREEDENT":    "Garrison Mathews",

    # Quaxly → Alperen Sengun
    "QUAXLY":      "Young Sengun",
    "QUAXWELL":    "Alperen Sengun",
    "QUAQUAVAL":   "Sengun Prime",

    # Greavard → Keyonte George
    "GREAVARD":    "Young George",
    "HOUNDSTONE":  "Keyonte George",

    # Flabebe lines → Flower-themed players (colorful role players)
    "FLABEBE":         "Young Bogdanovic",
    "FLABEBE_WHITE":   "Young Bogdanovic (White)",
    "FLABEBE_YELLOW":  "Young Bogdanovic (Yellow)",
    "FLABEBE_BLUE":    "Young Bogdanovic (Blue)",
    "FLABEBE_ORANGE":  "Young Bogdanovic (Orange)",
    "FLOETTE":         "Bogdanovic",
    "FLOETTE_WHITE":   "Bogdanovic (White)",
    "FLOETTE_YELLOW":  "Bogdanovic (Yellow)",
    "FLOETTE_BLUE":    "Bogdanovic (Blue)",
    "FLOETTE_ORANGE":  "Bogdanovic (Orange)",
    "FLORGES":         "Bogdan Bogdanovic",
    "FLORGES_WHITE":   "Bogdan (White)",
    "FLORGES_YELLOW":  "Bogdan (Yellow)",
    "FLORGES_BLUE":    "Bogdan (Blue)",
    "FLORGES_ORANGE":  "Bogdan (Orange)",

    # ── EPIC 3-stage lines ─────────────────────────────────────────
    # Trapinch → Giannis
    "TRAPINCH":    "Young Giannis",
    "VIBRAVA":     "Greek Freak",
    "FLYGON":      "Giannis Antetokounmpo",

    # Dratini → Larry Bird
    "DRATINI":     "Young Bird",
    "DRAGONAIR":   "Larry Legend",
    "DRAGONITE":   "Larry Bird",

    # Slakoth → Zion Williamson
    "SLAKOTH":     "Young Zion",
    "VIGOROTH":    "Zion",
    "SLAKING":     "Zion Williamson",

    # Beldum → Kevin Garnett
    "BELDUM":      "Young KG",
    "METANG":      "The Big Ticket",
    "METAGROSS":   "Kevin Garnett",

    # Gible → Devin Booker
    "GIBLE":       "Young Book",
    "GABITE":      "Book",
    "GARCHOMP":    "Devin Booker",

    # Elekid → Jimmy Butler
    "ELEKID":      "Young Butler",
    "ELECTABUZZ":  "Jimmy Buckets",
    "ELECTIVIRE":  "Jimmy Butler",

    # Riolu → Ben Simmons
    "RIOLU":       "Young Simmons",
    "LUCARIO":     "Ben Simmons",

    # Mankey → Amar'e Stoudemire
    "MANKEY":      "Young STAT",
    "PRIMEAPE":    "STAT",
    "ANNIHILAPE":  "Amar'e Stoudemire",

    # Gible (done)

    # Slakoth (done)

    # Jangmo-o → Alperen Sengun (alt - already used, use Nikola Jokic alt)
    "JANGMO_O":    "Young Jokic Alt",
    "HAKAMO_O":    "Joker Jr.",
    "KOMMO_O":     "Jokic Alt",

    # Budew → Jaylen Brown
    "BUDEW":       "Young JB",
    "ROSELIA":     "JB",
    "ROSERADE":    "Jaylen Brown",

    # Girafarig → Pascal Siakam
    "GIRAFARIG":   "Young Siakam",
    "FARIGIRAF":   "Pascal Siakam",

    # Murkrow → Anfernee Simons (used Pidove already) → use Marcus Thornton
    "MURKROW":     "Young Thornton",
    "HONCHKROW":   "Marcus Thornton",

    # Doduo → Draymond (used) → use Andre Iguodala
    "DODUO":       "Young Iggy",
    "DODRIO":      "Andre Iguodala",

    # Gligar → Josh Hart
    "GLIGAR":      "Young Hart",
    "GLISCOR":     "Josh Hart",

    # Cubchoo → Boban Marjanovic
    "CUBCHOO":     "Young Boban",
    "BEARTIC":     "Boban Marjanovic",

    # Meditite → Luol Deng (used) → use Al Horford
    "MEDITITE":    "Young Horford",
    "MEDICHAM":    "Al Horford",

    # Ponyta → Damian Lillard (already Shinx) → use Carmelo in alternate
    "PONYTA":          "Young Anthony",
    "RAPIDASH":        "Carmelo Anthony",
    "GALARIAN_PONYTA": "Young Melo Alt",
    "GALARIAN_RAPIDASH":"Melo Alt",

    # Houndour → Lou Williams
    "HOUNDOUR":    "Young Sweet Lou",
    "HOUNDOOM":    "Sweet Lou",
    "MEGA_HOUNDOOM":"Lou Williams",

    # Darumaka → Goran Dragic (already Fennekin) → use John Wall
    "DARUMAKA":        "Young Wall",
    "DARMANITAN":      "John Wall",
    "DARMANITAN_ZEN":  "Wall Mode",
    "GALARIAN_DARUMAKA":    "Young Wall Alt",
    "GALARIAN_DARMANITAN":  "Wall Alt",
    "GALARIAN_DARMANITAN_ZEN":"Wall Zen",

    # Dwebble → Brandon Ingram
    "DWEBBLE":     "Young BI",
    "CRUSTLE":     "Brandon Ingram",

    # Litten → LeBron Alt → use Kawhi Alt → no, use Kawhi already done
    # Use Paul Pierce
    "LITTEN":      "Young Pierce",
    "TORRACAT":    "The Truth",
    "INCINEROAR":  "Paul Pierce",

    # Exeggcute → Wilt's era alt... use David West
    "EXEGGCUTE":       "Young West",
    "EXEGGUTOR":       "David West",
    "ALOLAN_EXEGGUTOR":"West Alt",

    # Cubone → Luol (used) → use Derrick Favors
    "CUBONE":          "Young Favors",
    "MAROWAK":         "Derrick Favors",
    "ALOLAN_MAROWAK":  "Favors Alt",

    # Misdreavus (done)

    # Duskull (done)

    # Gastly → Allen Iverson
    "GASTLY":      "Young AI",
    "HAUNTER":     "The Answer",
    "GENGAR":      "Allen Iverson",

    # Corsola → Nikola Vucevic (already Goomy) → use Robin Williams — wait that's not NBA
    # Use Bismack (used)
    # Use Mason Plumlee
    "CORSOLA":         "Young Plumlee",
    "GALAR_CORSOLA":   "Young Plumlee Alt",
    "CURSOLA":         "Mason Plumlee",

    # Inkay → Mike Conley
    "INKAY":       "Young Conley",
    "MALAMAR":     "Mike Conley",

    # Cherubi → CJ McCollum
    "CHERUBI":         "Young CJ",
    "CHERRIM":         "CJ McCollum",
    "CHERRIM_SUNLIGHT":"CJ in the Sun",

    # Hippopotas → Jonas Valanciunas
    "HIPPOPOTAS":  "Young JV",
    "HIPPODOWN":   "Jonas Valanciunas",

    # Barboach → Royce O'Neale
    "BARBOACH":    "Young Royce",
    "WHISCASH":    "Royce O'Neale",

    # Mudbray → Domantas Sabonis
    "MUDBRAY":     "Young Dom",
    "MUDSDALE":    "Domantas Sabonis",

    # Buizel (done - Ja Morant)

    # Ducklett → De'Andre Hunter
    "DUCKLETT":    "Young Hunter",
    "SWANNA":      "De'Andre Hunter",

    # Scraggy → Kevin Porter Jr.
    "SCRAGGY":     "Young KPJ",
    "SCRAFTY":     "Kevin Porter Jr.",

    # Gligar (done)

    # Winged pests → Reggie Bullock
    "WINGULL":     "Young Bullock",
    "PELIPPER":    "Reggie Bullock",

    # Bounsweet → Mikal Bridges
    "BOUNSWEET":   "Young Mikal",
    "STEENEE":     "Mikal Bridges",
    "TSAREENA":    "The Bridge",

    # Combee → Joe Ingles
    "COMBEE":      "Young Ingles",
    "VESPIQUEN":   "Joe Ingles",

    # Larvesta → Jayson Tatum (already Duskull) → use Terry Rozier
    "LARVESTA":    "Young Scary Terry",
    "VOLCARONA":   "Terry Rozier",

    # Karrablast → Markelle Fultz
    "KARRABLAST":  "Young Fultz",
    "ESCAVALIER":  "Markelle Fultz",

    # Ferroseed → Kristaps Porzingis
    "FERROSEED":   "Young KP",
    "FERROTHORN":  "Kristaps Porzingis",

    # Turtwig (done)

    # Magikarp → Derrick Rose
    "MAGIKARP":    "Young Rose",
    "GYARADOS":    "Derrick Rose",

    # Helioptile → Delon Wright
    "HELIOPTILE":  "Young Delon",
    "HELIOLISK":   "Delon Wright",

    # Pancham → Anthony Black
    "PANCHAM":     "Young Black",
    "PANGORO":     "Anthony Black",

    # Pawmi → Scoot Henderson
    "PAWMI":       "Young Scoot",
    "PAWMO":       "Scoot Henderson",
    "PAWMOT":      "Scoot Prime",

    # Varoom → Markus Howard
    "VAROOM":      "Young Howard Jr",
    "REVAVROOM":   "Markus Howard",

    # Tarountula → Gradey Dick
    "TAROUNTULA":  "Young Dick",
    "SPIDOPS":     "Gradey Dick",

    # Nincada → Kris Dunn
    "NINCADA":     "Young Dunn",
    "NINJASK":     "Kris Dunn",
    "SHEDINJA":    "Dunn Ghost",

    # Noibat → Coby White
    "NOIBAT":      "Young Coby",
    "NOIVERN":     "Coby White",

    # Pumpkaboo → Alex Len
    "PUMPKABOO":   "Young Len",
    "GOURGEIST":   "Alex Len",

    # Surskit → Tyrese Haliburton (already Sobble) → use Lonzo Ball
    "SURSKIT":     "Young Lonzo",
    "MASQUERAIN":  "Lonzo Ball",

    # ── ULTRA 3-stage lines ────────────────────────────────────────
    # Gastly → Allen Iverson (done, ultra)

    # Rhyhorn → Charles Barkley
    "RHYHORN":     "Young Barkley",
    "RHYDON":      "Round Mound",
    "RHYPERIOR":   "Sir Charles",

    # Happiny → Nikola Jokic (already Magnemite) → use Karl Malone
    "HAPPINY":     "Young Mailman",
    "CHANSEY":     "The Mailman",
    "BLISSEY":     "Karl Malone",

    # Fletchling → Jaylen Brown (already Buneary) → use Aaron Gordon
    "FLETCHLING":  "Young AG",
    "FLETCHINDER": "Aaron Gordon",
    "TALONFLAME":  "AG Prime",

    # Frigibax → Scottie Pippen (already Scyther) → use Lamar Odom
    "FRIGIBAX":    "Young Odom",
    "ARCTIBAX":    "Lamar Odom",
    "BAXCALIBUR":  "L.O.",

    # Porygon → Tracy McGrady
    "PORYGON":     "Young T-Mac",
    "PORYGON_2":   "T-Mac",
    "PORYGON_Z":   "Tracy McGrady",

    # ── SPECIAL lines ──────────────────────────────────────────────
    # Magikarp (done - Derrick Rose, special)

    # Chikorita → Carmelo Anthony
    "CHIKORITA":   "Young Melo",
    "BAYLEEF":     "Carmelo",
    "MEGANIUM":    "Carmelo Anthony",

    # Cyndaquil → Dwyane Wade
    "CYNDAQUIL":   "Young Wade",
    "QUILAVA":     "Flash",
    "TYPHLOSION":  "Dwyane Wade",
    "HISUIAN_TYPHLOSION": "D-Wade",

    # Eevee → multi-form versatile player (Magic Johnson evolutions)
    "EEVEE":       "Magic Johnson",
    "VAPOREON":    "Magic (Playmaker)",
    "JOLTEON":     "Magic (Scorer)",
    "FLAREON":     "Magic (Finisher)",
    "ESPEON":      "Magic (IQ)",
    "UMBREON":     "Magic (Defender)",
    "LEAFEON":     "Magic (Athletic)",
    "GLACEON":     "Magic (Clutch)",
    "SYLVEON":     "Magic (Leader)",

    # Oddish → Scottie Pippen (already Scyther... use Horace Grant)
    "ODDISH":      "Young Grant",
    "GLOOM":       "Horace Grant",
    "VILEPLUME":   "Horace Grant Prime",
    "BELLOSSOM":   "Grant Ascended",

    # Hoppip → Penny Hardaway
    "HOPPIP":      "Young Penny",
    "SKIPLOOM":    "Penny Hardaway",
    "JUMPLUFF":    "Anfernee Hardaway",

    # Bellsprout → Reggie Miller (already Igglybuff) → use Dell Curry
    "BELLSPROUT":  "Young Dell",
    "WEEPINBELL":  "Dell Curry",
    "VICTREEBEL":  "Dell Curry Prime",

    # Feebas → Luka Doncic (already Ralts) → use Gilbert Arenas
    "FEEBAS":      "Young Gil",
    "MILOTIC":     "Agent Zero",

    # Meltan → special
    "MELTAN":      "Metal Ball",

    # Arrokuda → Gabe Vincent
    "ARROKUDA":    "Gabe Vincent",

    # Falinks → Team player
    "FALINKS_TROOPER": "Five-Man Unit",
    "FALINKS_BRASS":   "Five-Man Unit Prime",

    # Wishiwashi → James Wiseman
    "WISHIWASHI":        "Young Wiseman",
    "WISHIWASHI_SCHOOL": "James Wiseman",

    # ── HATCH lines ────────────────────────────────────────────────
    # Axew → Jaylen Brown Alt (already Buneary) → use Christian Wood
    "AXEW":        "Young C-Wood",
    "FRAXURE":     "Christian Wood",
    "HAXORUS":     "C-Wood Prime",

    # Dreepy → Franz Wagner
    "DREEPY":      "Young Franz",
    "DRAKLOAK":    "Franz Wagner",
    "DRAGAPULT":   "Franz Prime",

    # Froakie → Nikola Jokic (already) → use Jordan Poole
    "FROAKIE":     "Young Poole",
    "FROGADIER":   "Jordan Poole",
    "GRENINJA":    "Poole Prime",

    # Gothita → Buddy Hield
    "GOTHITA":     "Young Buddy",
    "GOTHORITA":   "Buddy Hield",
    "GOTHITELLE":  "Buddy Prime",

    # Grubbin → Jonathan Kuminga
    "GRUBBIN":     "Young Kuminga",
    "CHARJABUG":   "Jonathan Kuminga",
    "VIKAVOLT":    "Kuminga Prime",

    # ── UNIQUE (single units) ──────────────────────────────────────
    "ABSOL":           "Shawn Kemp",
    "AERODACTYL":      "Dominique Wilkins",
    "ALCREMIE_VANILLA":    "Sweets",
    "ALCREMIE_RUBY":       "Sweet Ruby",
    "ALCREMIE_MATCHA":     "Sweet Matcha",
    "ALCREMIE_MINT":       "Sweet Mint",
    "ALCREMIE_LEMON":      "Sweet Lemon",
    "ALCREMIE_SALTED":     "Sweet Salted",
    "ALCREMIE_RUBY_SWIRL": "Ruby Swirl",
    "ALCREMIE_CARAMEL_SWIRL": "Caramel Swirl",
    "ALCREMIE_RAINBOW_SWIRL": "Rainbow Swirl",
    "APPLIN":          "Young Hardaway Jr",
    "APPLETUN":        "Tim Hardaway Jr",
    "FLAPPLE":         "Hardaway Jr. Alt",
    "DIPPLIN":         "Hardaway Jr. Dip",
    "HYDRAPPLE":       "Hardaway Prime",
    "ARCHALUDON":      "Jakob Poeltl",
    "ARCTOVISH":       "Frozen Prospect",
    "ARCTOZOLT":       "Zolt Prospect",
    "AUDINO":          "Steve Blake",
    "AZELF":           "Sam Cassell",
    "BASCULEGION_MALE":   "Leapfrog Legend",
    "BASCULEGION_FEMALE": "Leapfrog Legend F",
    "BASCULIN_RED":    "Red Basculin",
    "BASCULIN_BLUE":   "Blue Basculin",
    "BASCULIN_WHITE":  "White Basculin",
    "BRUXISH":         "Richard Jefferson",
    "CARNIVINE":       "Sean Williams",
    "CASTFORM":        "Chameleon Player",
    "CASTFORM_SUN":    "Hot Streak",
    "CASTFORM_RAIN":   "Cold Stretch",
    "CASTFORM_HAIL":   "Frozen Streak",
    "CERULEDGE":       "Immanuel Quickley Alt",
    "CHARCADET":       "Young IQ Alt",
    "CHATOT":          "Charlie Ward",
    "CHIMECHO":        "Ronnie Price",
    "CHINGLING":       "Young Ronnie",
    "COMFEY":          "Kyle Korver",
    "COSMOEM":         "Rising Star",
    "COSMOG":          "Draft Lottery",
    "CRAMORANT":       "Nerlens Noel",
    "CRYOGONAL":       "Meyers Leonard",
    "CYCLIZAR":        "Jordan Nwora",
    "DEDENNE":         "Isaiah Canaan",
    "DELIBIRD":        "Corey Brewer",
    "DHELMISE":        "Joakim Noah",
    "DONDOZO":         "Tacko Fall",
    "DRACOVISH":       "Fossil Hybrid 1",
    "DRACOZOLT":       "Fossil Hybrid 2",
    "DRAMPA":          "Vlade Divac",
    "DRUDDIGON":       "Joel Anthony",
    "DUDUNSPARCE":     "Peja Stojakovic",
    "DUNSPARCE":       "Young Peja",
    "DURALUDON":       "Young Poeltl",
    "DURANT":          "Nate Thurmond",
    "EISCUE":          "Luke Babbitt",
    "EISCUE_NOICE":    "Luke Babbitt Thawed",
    "EMOLGA":          "Matt Bonner",
    "FALINKS_BRASS":   "Five-Man Unit Prime",
    "FARFETCH_D":      "Gus Williams",
    "FINIZEN":         "Young Palafin",
    "FLAPPLE":         "Hardaway Jr. Alt",
    "FLUTTER_MANE":    "Rod Strickland",
    "FURFROU":         "Dapper Dan",
    "GALARIAN_FARFETCH_D": "Gus Williams Alt",
    "GHOLDENGO":       "Lauri Markkanen",
    "GIMMIGHOUL":      "Young Markkanen",
    "GREAT_TUSK":      "Wendell Carter Alt",
    "HAWLUCHA":        "Rex Chapman",
    "HEATMOR":         "Corey Maggette",
    "HERACROSS":       "Udonis Haslem",
    "HISUIAN_QWILFISH":"Vintage Guard",
    "HITMONCHAN":      "Floyd Patterson Jr.",
    "HITMONLEE":       "Jake LaMotta Jr.",
    "HITMONTOP":       "Spinning Guard",
    "HOOPA":           "Ty Lawson",
    "HOOPA_UNBOUND":   "Ty Lawson Unleashed",
    "HYDRAPPLE":       "Hardaway Prime",
    "ILLUMISE":        "Becky Hammon",
    "INDEEDEE_FEMALE": "Maya Moore",
    "INDEEDEE_MALE":   "Shabazz Muhammad",
    "IRON_BUNDLE":     "AI Robot",
    "IRON_HANDS":      "Robo Banger",
    "IRON_THORNS":     "Robo Rock",
    "KANGASKHAN":      "Karl-Anthony Towns Alt",
    "KECLEON":         "Chameleon Sixth Man",
    "KLEAVOR":         "Pippen Prime",
    "KLEFKI":          "Key Keeper",
    "KOMALA":          "Zaza Pachulia",
    "KUBFU":           "Young Urshifu",
    "LAPRAS":          "Alonzo Mourning",
    "LATIAS":          "Cynthia Cooper",
    "LATIOS":          "Dan Majerle",
    "LUNATONE":        "Kyle Lowry Alt",
    "LUVDISC":         "Scott Skiles",
    "MANTINE":         "Robert Horry",
    "MANTYKE":         "Young Robert Horry",
    "MARACTUS":        "Nene Hilario",
    "MAUSHOLD_FOUR":   "Four-Man Squad",
    "MAUSHOLD_THREE":  "Three-Man Squad",
    "MAWILE":          "Clyde Drexler",
    "MEGA_SABLEYE":    "Master Manipulator",
    "MESPRIT":         "Tony Wroten",
    "MILCERY":         "Sweet Shooter",
    "MILTANK":         "Shaquille O'Neal Jr.",
    "MIMIKYU":         "Copycat Guard",
    "MIMIKYU_BUSTED":  "Exposed Copycat",
    "MINIOR":          "Shooting Star",
    "MINIOR_KERNEL_BLUE":   "Blue Kernel",
    "MINIOR_KERNEL_GREEN":  "Green Kernel",
    "MINIOR_KERNEL_ORANGE": "Orange Kernel",
    "MINIOR_KERNEL_RED":    "Red Kernel",
    "MINUN":           "Doug Christie",
    "MORPEKO":         "Hungry Baller",
    "MORPEKO_HANGRY":  "Hangry Baller",
    "ORTHWORM":        "Byron Mullens",
    "OVERQWIL":        "Quin Snyder Jr.",
    "PACHIRISU":       "Earl Boykins",
    "PALAFIN":         "Palafin",
    "PALAFIN_HERO":    "Palafin Hero",
    "PINCURCHIN":      "Dennis Rodman Jr.",
    "PINSIR":          "Charles Barkley Alt",
    "PLUSLE":          "Nate Archibald Jr.",
    "POIPOLE":         "Young Naganadel",
    "PYUKUMUKU":       "Enes Kanter",
    "QWILFISH":        "Vintage Shooter",
    "RELICANTH":       "Bob Love",
    "ROTOM_DRONE":     "Drone Guard",
    "ROTOM_FAN":       "Fan Favorite",
    "ROTOM_FROST":     "Frozen Guard",
    "ROTOM":           "Rotom Base",
    "ROTOM_HEAT":      "Hot Guard",
    "ROTOM_MOW":       "Lawn Guard",
    "ROTOM_WASH":      "Wash Guard",
    "SABLEYE":         "Shane Battier Alt",
    "SCIZOR":          "Scottie Pippen",
    "SCREAM_TAIL":     "Clyde Drexler Alt",
    "SCYTHER":         "Young Pippen",
    "SEVIPER":         "Gerald Wallace",
    "SHUCKLE":         "Mark Price",
    "SIGILYPH":        "Lamar Odom Alt",
    "SKARMORY":        "David Robinson Alt",
    "SLITHER_WING":    "Veteran Wing",
    "SMEARGLE":        "Michael Beasley",
    "SOLROCK":         "Luke Walton",
    "SPINDA":          "Jason Williams",
    "SPIRITOMB":       "Metta World Peace",
    "STANTLER":        "Stacey Augmon",
    "STONJOURNER":     "Brook Lopez Alt",
    "TANDEMAUS":       "Dynamic Duo",
    "TAPU_BULU":       "Kevon Looney",
    "TAPU_FINI":       "Stephen Jackson",
    "TAPU_KOKO":       "Isaiah Thomas Alt",
    "TAPU_LELE":       "DeMar DeRozan Alt",
    "TAUROS":          "Xavier McDaniel",
    "TAUROS_AQUA_BREED":   "Xavier (Aqua)",
    "TAUROS_BLAZE_BREED":  "Xavier (Blaze)",
    "TAUROS_COMBAT_BREED": "Xavier (Combat)",
    "TOGEDEMARU":      "Jose Juan Barea",
    "TORKOAL":         "Amir Johnson",
    "TROPIUS":         "Kenyon Martin",
    "TURTONATOR":      "Willie Cauley-Stein",
    "TYROGUE":         "Young Ty",
    "UXIE":            "Mookie Blaylock",
    "VELUZA":          "Jalen Smith",
    "VOLBEAT":         "Jason Kapono",
    "WYRDEER":         "Nate McMillan",
    "ZANGOOSE":        "Rashard Lewis",
    "ZERAORA":         "John Starks",

    # ── LEGENDARY ─────────────────────────────────────────────────
    "MEWTWO":          "Michael Jordan",
    "SHADOW_MEWTWO":   "Dark Side Jordan",
    "MEW":             "Pete Maravich",
    "LUGIA":           "Wilt Chamberlain",
    "SHADOW_LUGIA":    "Wilt Unleashed",
    "ARTICUNO":        "Jerry West",
    "ZAPDOS":          "Julius Erving",
    "MOLTRES":         "Elgin Baylor",
    "GALARIAN_ARTICUNO": "Jerry West Alt",
    "GALARIAN_ZAPDOS":   "Dr. J Alt",
    "GALARIAN_MOLTRES":  "Elgin Baylor Alt",
    "DIALGA":          "Hakeem Olajuwon",
    "PALKIA":          "David Robinson",
    "GIRATINA":        "Dennis Rodman",
    "ORIGIN_GIRATINA": "Rodman Unleashed",
    "SUICUNE":         "Bob Cousy",
    "RAIKOU":          "Bob Pettit",
    "ENTEI":           "George Mikan",
    "REGICE":          "Walt Frazier",
    "REGIROCK":        "Bill Walton",
    "REGISTEEL":       "Moses Malone",
    "REGIGIGAS":       "Wilt's Peak",
    "REGIDRAGO":       "Dragon Elder",
    "REGIELEKI":       "Electric Elder",
    "KYOGRE":          "Kareem Abdul-Jabbar",
    "PRIMAL_KYOGRE":   "Kareem Prime",
    "GROUDON":         "Bill Russell",
    "PRIMAL_GROUDON":  "Bill Russell Prime",
    "RAYQUAZA":        "Magic Johnson",
    "MEGA_RAYQUAZA":   "Magic Prime",
    "CELEBI":          "Oscar Robertson",
    "HO_OH":           "Elvin Hayes",
    "VICTINI":         "Allen Iverson Alt",
    "JIRACHI":         "Earl Monroe",
    "SHAYMIN":         "Clyde Drexler",
    "SHAYMIN_SKY":     "Clyde Drexler Sky",
    "MANAPHY":         "Nate Archibald",
    "DARKRAI":         "Latrell Sprewell",
    "CRESSELIA":       "Cheryl Miller",
    "HEATRAN":         "Alonzo Mourning Alt",
    "COBALION":        "Robert Parish",
    "TERRAKION":       "Elvin Hayes Alt",
    "VIRIZION":        "Willis Reed",
    "KELDEO":          "Dave Cowens",
    "LANDORUS":        "Wes Unseld",
    "THUNDURUS":       "Calvin Murphy",
    "TORNADUS":        "Jo Jo White",
    "ENAMORUS":        "Ann Meyers",
    "RESHIRAM":        "Dominique Wilkins Alt",
    "ZEKROM":          "Charles Barkley Leg.",
    "KYUREM":          "Patrick Ewing Leg.",
    "XERNEAS":         "Cynthia Cooper Leg.",
    "YVELTAL":         "Spencer Haywood",
    "ZYGARDE_10":      "Zygarde 10",
    "ZYGARDE_50":      "Zygarde 50",
    "ZYGARDE_100":     "Zygarde 100",
    "DIANCIE":         "Brittney Griner",
    "HOOPA":           "Ty Lawson",
    "HOOPA_UNBOUND":   "Ty Lawson Unleashed",
    "VOLCANION":       "Bob Lanier",
    "TAPU_KOKO":       "Isaiah Thomas Alt",
    "TAPU_LELE":       "DeMar Alt",
    "TAPU_BULU":       "Kevon Looney",
    "TAPU_FINI":       "Stephen Jackson",
    "COSMOG":          "Draft Lottery",
    "COSMOEM":         "Rising Star",
    "SOLGALEO":        "Shawn Marion",
    "LUNALA":          "Sheryl Swoopes",
    "NIHILEGO":        "Eric Bledsoe",
    "BUZZWOLE":        "Zion Alt",
    "PHEROMOSA":       "Bones Hyland",
    "XURKITREE":       "Dennis Rodman Alt",
    "CELESTEELA":      "Kareem Alt",
    "KARTANA":         "Klay Thompson Leg.",
    "GUZZLORD":        "Oliver Miller",
    "NECROZMA":        "Jordan Composite",
    "ULTRA_NECROZMA":  "Ultra Jordan",
    "STAKATAKA":       "Twin Towers",
    "BLACEPHALON":     "World B. Free",
    "MAGEARNA":        "Mechanical Center",
    "MARSHADOW":       "Jerome Kersey",
    "ZERAORA":         "John Starks",
    "ETERNATUS":       "Fossil Legend",
    "GLASTRIER":       "Ice Horse",
    "SPECTRIER":       "Ghost Horse",
    "CALYREX":         "The Crown",
    "REGIELEKI":       "Electric Elder",
    "REGIDRAGO":       "Dragon Elder",
    "IRON_VALIANT":    "Future Guard",
    "ROARING_MOON":    "Ancient Moon",
    "WALKING_WAKE":    "Ancient Wake",
    "FLUTTER_MANE":    "Ancient Mane",
    "SLITHER_WING":    "Ancient Wing",
    "CHI_YU":          "Chi-Yu Legend",
    "GENESECT":        "Cyborg Legend",
    "FEZANDIPITI":     "Teal Legend F",
    "OKIDOGI":         "Teal Legend O",
    "MUNKIDORI":       "Teal Legend M",
    "PECHARUNT":       "Peach Legend",
    "ZACIAN":          "Golden Sword",
    "ZACIAN_CROWNED":  "Crowned Sword",
    "ZARUDE":          "Forest King",
    "ENAMORUS":        "Ann Meyers",
    "URSHIFU_SINGLE":  "Single Strike Legend",
    "URSHIFU_RAPID":   "Rapid Strike Legend",
    "OGERPON_TEAL":         "Ogre Teal",
    "OGERPON_TEAL_MASK":    "Ogre Teal Mask",
    "OGERPON_WELLSPRING":   "Ogre Water",
    "OGERPON_WELLSPRING_MASK": "Ogre Water Mask",
    "OGERPON_HEARTHFLAME":  "Ogre Fire",
    "OGERPON_HEARTHFLAME_MASK": "Ogre Fire Mask",
    "OGERPON_CORNERSTONE":  "Ogre Rock",
    "OGERPON_CORNERSTONE_MASK": "Ogre Rock Mask",

    # Arceus forms → LeBron James in different eras
    "ARCEUS":              "LeBron James",
    "ARCEUS_BUG":          "LeBron (Bug)",
    "ARCEUS_DARK":         "LeBron (Dark)",
    "ARCEUS_DRAGON":       "LeBron (Dragon)",
    "ARCEUS_ELECTRIC":     "LeBron (Electric)",
    "ARCEUS_FAIRY":        "LeBron (Fairy)",
    "ARCEUS_FIGHTING":     "LeBron (Fighting)",
    "ARCEUS_FIRE":         "LeBron (Heat Era)",
    "ARCEUS_FLYING":       "LeBron (Flying)",
    "ARCEUS_GHOST":        "LeBron (Ghost)",
    "ARCEUS_GRASS":        "LeBron (Grass)",
    "ARCEUS_GROUND":       "LeBron (Ground)",
    "ARCEUS_ICE":          "LeBron (Ice)",
    "ARCEUS_POISON":       "LeBron (Poison)",
    "ARCEUS_PSYCHIC":      "LeBron (Psychic)",
    "ARCEUS_ROCK":         "LeBron (Rock)",
    "ARCEUS_STEEL":        "LeBron (Steel)",
    "ARCEUS_WATER":        "LeBron (Cavs Comeback)",
    "ARCEUS_WATER":        "LeBron (Water)",

    # Silvally forms → Kevin Durant different teams
    "TYPE_NULL":           "KD Pre-Draft",
    "SILVALLY":            "Kevin Durant",
    "SILVALLY_FIGHTING":   "KD (Fighting)",
    "SILVALLY_FLYING":     "KD (Flying)",
    "SILVALLY_POISON":     "KD (Poison)",
    "SILVALLY_GROUND":     "KD (Ground)",
    "SILVALLY_ROCK":       "KD (Rock)",
    "SILVALLY_BUG":        "KD (Bug)",
    "SILVALLY_GHOST":      "KD (Ghost)",
    "SILVALLY_STEEL":      "KD (Steel)",
    "SILVALLY_FIRE":       "KD (Warriors Era)",
    "SILVALLY_WATER":      "KD (Water)",
    "SILVALLY_GRASS":      "KD (Grass)",
    "SILVALLY_ELECTRIC":   "KD (Electric)",
    "SILVALLY_PSYCHIC":    "KD (Nets Era)",
    "SILVALLY_ICE":        "KD (Ice)",
    "SILVALLY_DRAGON":     "KD (Suns Era)",
    "SILVALLY_DARK":       "KD (Dark)",
    "SILVALLY_FAIRY":      "KD (Fairy)",

    # Deoxys forms → Devin Booker forms (already used Gible for Booker... use Derrick Coleman)
    "DEOXYS":          "Derrick Coleman",
    "DEOXYS_ATTACK":   "Coleman Attack",
    "DEOXYS_DEFENSE":  "Coleman Defense",
    "DEOXYS_SPEED":    "Coleman Speed",

    # Meloetta forms
    "MELOETTA":            "Spud Webb Alt",
    "PIROUETTE_MELOETTA":  "Spud Webb Spin",

    # Giratina (done)

    # Ogerpon (done)

    # UNOWN A-Z → players by letter nickname
    "UNOWN_A": "Arenas",
    "UNOWN_B": "Boozer",
    "UNOWN_C": "Camby",
    "UNOWN_D": "Dampier",
    "UNOWN_E": "Erick Dampier",
    "UNOWN_F": "Flip Murray",
    "UNOWN_G": "Ginobili",
    "UNOWN_H": "Hibbert",
    "UNOWN_I": "Iguodala",
    "UNOWN_J": "Jamison",
    "UNOWN_K": "Kirilenko",
    "UNOWN_L": "Lenard",
    "UNOWN_M": "Marion",
    "UNOWN_N": "Nocioni",
    "UNOWN_O": "Okafor",
    "UNOWN_P": "Pietrus",
    "UNOWN_Q": "Quinn",
    "UNOWN_R": "Ratliff",
    "UNOWN_S": "Swift",
    "UNOWN_T": "Turkoglu",
    "UNOWN_U": "Udoka",
    "UNOWN_V": "Voskuhl",
    "UNOWN_W": "Welsch",
    "UNOWN_X": "Xavier Silas",
    "UNOWN_Y": "Yogi Ferrell",
    "UNOWN_Z": "Zeljko Rebraca",
    "UNOWN_QUESTION":    "Mystery Player",
    "UNOWN_EXCLAMATION": "Clutch Player",

    # ── Remaining 119 missing mappings ────────────────────────────
    # Pichu line → Isaiah Thomas
    "PICHU":           "Young IT",
    "PIKACHU":         "Isaiah Thomas",
    "PIKACHU_SURFER":  "IT Surf Mode",
    "RAICHU":          "IT Prime",
    "ALOLAN_RAICHU":   "IT Alt",

    # Spheal line → Enes Freedom
    "SPHEAL":          "Young Enes",
    "SEALEO":          "Enes Kanter",
    "WALREIN":         "Enes Freedom",

    # Togepi line → Tyson Chandler
    "TOGEPI":          "Young Tyson",
    "TOGETIC":         "Tyson Chandler",
    "TOGEKISS":        "Chandler Prime",

    # Shinx line → Damian Lillard
    "SHINX":           "Young Dame",
    "LUXIO":           "Dame Dolla",
    "LUXRAY":          "Damian Lillard",

    # Abra line → Steve Nash (alt — Nash used Cleffa; use John Havlicek)
    "ABRA":            "Young Havlicek",
    "KADABRA":         "Hondo",
    "ALAKAZAM":        "John Havlicek",

    # Swinub line → Anderson Varejao
    "SWINUB":          "Young Varejao",
    "PILOSWINE":       "Anderson Varejao",
    "MAMOSWINE":       "Wild Thing",

    # Snorunt line → Danilo Gallinari
    "SNORUNT":         "Young Gallo",
    "GLALIE":          "Danilo Gallinari",
    "FROSLASS":        "Gallo Alt",

    # Snover line → Jusuf Nurkic
    "SNOVER":          "Young Nurkic",
    "ABOMASNOW":       "Jusuf Nurkic",
    "MEGA_ABOMASNOW":  "The Bosnian Beast",

    # Vanillite line → Tony Parker
    "VANILLITE":       "Young TP",
    "VANILLISH":       "Tony Parker",
    "VANILLUXE":       "TP Prime",

    # Meowth line → Jamal Crawford
    "MEOWTH":          "Young Jamal",
    "PERSIAN":         "Jamal Crawford",
    "ALOLAN_MEOWTH":   "Young J-Crossover",
    "ALOLAN_PERSIAN":  "J-Crossover",

    # Amaura line → Kelly Olynyk
    "AMAURA":          "Young Olynyk",
    "AURORUS":         "Kelly Olynyk",

    # Shieldon line → Ivica Zubac
    "SHIELDON":        "Young Zubac",
    "BASTIODON":       "Ivica Zubac",

    # Shuppet line → Matt Barnes
    "SHUPPET":         "Young Barnes",
    "BANETTE":         "Matt Barnes",
    "MEGA_BANETTE":    "Barnes Unleashed",

    # Whismur line → Glen Davis
    "WHISMUR":         "Young Big Baby",
    "LOUDRED":         "Big Baby",
    "EXPLOUD":         "Glen Davis",

    # Pikipek line → Montrezl Harrell
    "PIKIPEK":         "Young Trez",
    "TRUMBEAK":        "Montrezl Harrell",
    "TOUCANNON":       "Trez Prime",

    # Hatenna line → Sue Bird
    "HATENNA":         "Young Sue",
    "HATTREM":         "Sue Bird",
    "HATTERENE":       "Sue Bird Prime",

    # Clamperl line → Goran Dragic (Fennekin already used — use Nick Anderson)
    "CLAMPERL":        "Young Nick A",
    "HUNTAIL":         "Nick Anderson",
    "GOREBYSS":        "Anderson Prime",

    # Carbink/Diancie → Brittney Griner (Diancie already assigned)
    "CARBINK":         "Young Griner",

    # Popplio line → Damion Lee
    "POPPLIO":         "Young Lee",
    "BRIONNE":         "Damion Lee",
    "PRIMARINA":       "Lee Prime",

    # Melmetal → already legendary, add here
    "MELMETAL":        "Wilt's Peak",

    # Bonsley line → Bismack Biyombo (already Koffing) → use Andrew Bogut
    "BONSLEY":         "Young Bogut",
    "SUDOWOODO":       "Andrew Bogut",

    # Tinkatink line → Diana Taurasi
    "TINKATINK":       "Young DT",
    "TINKATUFF":       "Diana Taurasi",
    "TINKATON":        "The GOAT DT",

    # Sentret line → Nate Archibald (already Manaphy) → use Muggsy Bogues (already Caterpie) → use Norm Nixon
    "FURRET":          "Norm Nixon",
    "SENTRET":         "Young Nixon",

    # Woobat line → Thabo Sefolosha
    "WOOBAT":          "Young Thabo",
    "SWOOBAT":         "Thabo Sefolosha",

    # Clauncher line → Clint Capela (already Omanyte) → use Robin Lopez (Bergmite) → use Nene
    "CLAUNCHER":       "Young Nene",
    "CLAWITZER":       "Nene Hilario",

    # Bidoof line → Udonis Haslem (already Wobbuffet) → use Mike Miller
    "BIDOOF":          "Young Miller",
    "BIBAREL":         "Mike Miller",

    # Baltoy line → Caron Butler
    "BALTOY":          "Young Caron",
    "CLAYDOL":         "Caron Butler",

    # Kricketot line → Anthony Morrow
    "KRICKETOT":       "Young Morrow",
    "KRICKETUNE":      "Anthony Morrow",

    # Lickitung line → Oliver Miller (already Guzzlord) → use Jon Koncak
    "LICKITUNG":       "Young Koncak",
    "LICKILICKY":      "Jon Koncak",

    # Dewpider line → Torrey Craig
    "DEWPIDER":        "Young Craig",
    "ARAQUANID":       "Torrey Craig",

    # Impidimp line → Patrick Beverley (already Lillipup) → use Elfrid Payton (already Chinchou) → use Reggie Jackson
    "IMPIDIMP":        "Young Reggie J",
    "MORGREM":         "Reggie Jackson",
    "GRIMMSNARL":      "Reggie Jackson Prime",

    # Crabrawler line → Zach Collins
    "CRABRAWLER":      "Young Collins",
    "CRABOMINABLE":    "Zach Collins",

    # Cutiefly line → Isaiah Thomas Alt → use TJ McConnell
    "CUTIEFLY":        "Young TJ Mac",
    "RIBOMBEE":        "TJ McConnell",

    # Drowzee line → Rick Barry
    "DROWZEE":         "Young Barry",
    "HYPNO":           "Rick Barry",

    # Tangela line → Bob McAdoo
    "TANGELA":         "Young McAdoo",
    "TANGROWTH":       "Bob McAdoo",

    # Psyduck line → Rafer Alston
    "PSYDUCK":         "Young Skip",
    "GOLDUCK":         "Skip to My Lou",

    # Naganadel → legendary already
    "NAGANADEL":       "Poison Legend",

    # Elgyem line → Trae Young
    "ELGYEM":          "Young Trae",
    "BEHEEYEM":        "Trae Young",

    # Fomantis line → OG Anunoby (already Misdreavus) → use Doug McDermott
    "FOMANTIS":        "Young Doug Mac",
    "LURANTIS":        "Doug McDermott",

    # Armarouge → Immanuel Quickley (already Charcadet line) → use Dalano Banton
    "ARMAROUGE":       "Dalano Banton",

    # Glameow line → Goga Bitadze
    "GLAMEOW":         "Young Goga",
    "PURUGLY":         "Goga Bitadze",

    # Cottonee line → Shake Milton
    "COTTONEE":        "Young Shake",
    "WHIMSICOTT":      "Shake Milton",

    # Minccino line → Jevon Carter
    "MINCCINO":        "Young Jevon",
    "CINCCINO":        "Jevon Carter",

    # Espurr line → Donte DiVincenzo
    "ESPURR":          "Young Donte",
    "MEOWSTIC_MALE":   "Donte DiVincenzo",
    "MEOWSTIC_FEMALE": "Donte DiVincenzo F",

    # Gossifleur line → Damyean Dotson
    "GOSSIFLEUR":      "Young Dotson",
    "ELDEGOSS":        "Damyean Dotson",

    # Roggenrola line → Isaiah Hartenstein
    "ROGGENROLA":      "Young Hartenstein",
    "BOLDORE":         "Isaiah Hartenstein",
    "GIGALITH":        "Hartenstein Prime",

    # Galarian Yamask line → Jakob Poeltl (already Archaludon) → use Khem Birch
    "GALARIAN_YAMASK": "Young Birch",
    "RUNERIGUS":       "Khem Birch",

    # Clobbopus line → Gorgui Dieng (already Tentacool) → use Bismack (used) → use Ekpe Udoh
    "CLOBBOPUS":       "Young Ekpe",
    "GRAPPLOCT":       "Ekpe Udoh",

    # Mareanie line → Jaxson Hayes
    "MAREANIE":        "Young Hayes",
    "TOXAPEX":         "Jaxson Hayes",

    # Cetoddle line → Boban Marjanovic (already Cubchoo) → use Tacko Fall (already Dondozo) → use Isaiah Joe
    "CETODDLE":        "Young Joe",
    "CETITAN":         "Isaiah Joe",

    # Misc remaining
    "TEPIG":       "Young Noel",
    "PIGNITE":     "Nerlens Noel",
    "EMBOAR":      "Noel Prime",
    "WYNAUT":      "Young Wobbuffet",
    "WOBBUFFET":   "Udonis Haslem Alt",
    "SUNKERN":     "Young Sunflower",
    "SUNFLORA":    "Sunflower Player",
    "PATRAT":      "Young Watchog",
    "WATCHOG":     "Watchog Player",
    "WURMPLE":     "Young Silcoon",
    "SILCOON":     "Silcoon Player",
    "BEAUTIFLY":   "Beautifly Player",
    "CASCOON":     "Cascoon Player",
    "DUSTOX":      "Dustox Player",
    "ZIGZAGOON":   "Young Battier",
    "LINOONE":     "Shane Battier",
    "SKITTY":      "Young Delcatty",
    "DELCATTY":    "Delcatty Player",
    "NOSEPASS":    "Young Probopass",
    "PROBOPASS":   "Probopass Player",
    "SURSKIT":     "Young Lonzo",
    "MASQUERAIN":  "Lonzo Ball",
    "VOLBEAT":     "Jason Kapono",
    "ILLUMISE":    "Becky Hammon",
    "GULPIN":      "Young Swalot",
    "SWALOT":      "Swalot Player",
    "PINECO":      "Young Forretress",
    "FORRETRESS":  "Forretress Player",
    "YANMA":       "Young Yanmega",
    "YANMEGA":     "Yanmega Player",
    "WOOPER":      "Young Quagsire",
    "QUAGSIRE":    "Quagsire Player",
    "PALDEA_WOOPER":"Young Clodsire",
    "CLODSIRE":    "Clodsire Player",
    "GLIGAR":      "Young Hart",
    "GLISCOR":     "Josh Hart",
    "TEDDIURSA":   "Young Ursaring",
    "URSARING":    "Ursaring Player",
    "URSALUNA":    "Ursaluna Player",
    "URSALUNA_BLOODMOON": "Ursaluna Bloodmoon",
    "SLUGMA":      "Young Magcargo",
    "MAGCARGO":    "Magcargo Player",
    "SKARMORY":    "David Robinson Alt",
    "HOUNDOUR":    "Young Sweet Lou",
    "HOUNDOOM":    "Sweet Lou",
    "STANTLER":    "Stacey Augmon",
    "SMEARGLE":    "Michael Beasley",
    "MILTANK":     "Shaq Jr.",
    "REMORAID":    "Young Octillery",
    "OCTILLERY":   "Octillery Player",
    "MANTINE":     "Robert Horry",
    "SKIDDO":      "Young Gogoat",
    "GOGOAT":      "Gogoat Player",
    "SILICOBRA":   "Young Sandaconda",
    "SANDACONDA":  "Sandaconda Player",
    "PHANPY":      "Young Donphan",
    "DONPHAN":     "Donphan Player",
    "TRUBBISH":    "Young Garbodor",
    "GARBODOR":    "Garbodor Player",
    "SINISTEA":    "Young Polteageist",
    "POLTEAGEIST": "Polteageist Player",
    "YAMASK":      "Young Cofagrigus",
    "COFAGRIGUS":  "Cofagrigus Player",
    "NICKIT":      "Young Thievul",
    "THIEVUL":     "Thievul Player",
    "WATTREL":     "Young Kilowattrel",
    "KILOWATTREL": "Kilowattrel Player",
    "STUFFUL":     "Young Bewear",
    "BEWEAR":      "Bewear Player",
    "VULLABY":     "Young Mandibuzz",
    "MANDIBUZZ":   "Mandibuzz Player",
    "SIZZLIPEDE":  "Young Centiskorch",
    "CENTISKORCH": "Centiskorch Player",
    "SANDYGAST":   "Young Palossand",
    "PALOSSAND":   "Palossand Player",
    "SKORUPI":     "Young Drapion",
    "DRAPION":     "Drapion Player",
    "WIMPOD":      "Young Golisopod",
    "GOLISOPOD":   "Golisopod Player",
    "WIGLETT":     "Young Wugtrio",
    "WUGTRIO":     "Wugtrio Player",
    "TADBULB":     "Young Bellibolt",
    "BELLIBOLT":   "Bellibolt Player",
    "PHANTUMP":    "Young Trevenant",
    "TREVENANT":   "Trevenant Player",
    "TOXEL":       "Young Toxtricity",
    "TOXTRICITY":  "Toxtricity Player",
    "ROCKRUFF":    "Young Lycanroc",
    "LYCANROC_DAY":   "Lycanroc Day",
    "LYCANROC_DUSK":  "Lycanroc Dusk",
    "LYCANROC_NIGHT": "Lycanroc Night",
    "PAWNIARD":    "Young Bisharp",
    "BISHARP":     "Bisharp Player",
    "KINGAMBIT":   "Kingambit Player",
    "PETILIL":     "Young Liligant",
    "LILIGANT":    "Liligant Player",
    "HISUIAN_LILLIGANT": "Liligant Alt",
    "RUFFLET":     "Young Braviary",
    "BRAVIARY":    "Braviary Player",
    "TAILLOW":     "Young Swellow",
    "SWELLOW":     "Swellow Player",
    "SHELLOS_WEST_SEA": "Shellos West",
    "GASTRODON_WEST_SEA": "Gastrodon West",
    "SHELLOS_EAST_SEA": "Shellos East",
    "GASTRODON_EAST_SEA": "Gastrodon East",
    "PURRLOIN":    "Young Liepard",
    "LIEPARD":     "Liepard Player",
    "STUNKY":      "Young Skuntank",
    "SKUNTANK":    "Skuntank Player",
    "SKRELP":      "Young Dragalge",
    "DRAGALGE":    "Dragalge Player",
    "SALANDIT":    "Young Salazzle",
    "SALAZZLE":    "Salazzle Player",
    "PHIONE":      "Phione Player",
    "SNOM":        "Young Frosmoth",
    "FROSMOTH":    "Frosmoth Player",
    "WAILMER":     "Young Wailord",
    "WAILORD":     "Wailord Player",
    "ROWLET":      "Young Decidueye",
    "DARTIX":      "Decidueye Mid",
    "DECIDUEYE":   "Decidueye Player",
    "ZORUA":       "Young Zoroark",
    "ZOROARK":     "Zoroark Player",
    "HISUI_ZORUA":     "Young Zoroark Alt",
    "HISUI_ZOROARK":   "Zoroark Alt",
    "SWABLU":      "Young Ant",
    "TATSUGIRI_CURLY":   "Curly Tatsu",
    "TATSUGIRI_DROOPY":  "Droopy Tatsu",
    "TATSUGIRI_STRETCHY":"Stretchy Tatsu",
    "OINKOLOGNE_FEMALE": "Oinkologne F",
    "WISHIWASHI":        "Young Wiseman",
    "WISHIWASHI_SCHOOL": "James Wiseman",
}

def main():
    translation_path = os.path.join(
        os.path.dirname(__file__),
        "../app/public/dist/client/locales/en/translation.json"
    )
    with open(translation_path) as f:
        data = json.load(f)

    pkm = data["pkm"]
    updated = 0
    missing = []

    for key in pkm:
        if key in NBA_NAMES:
            pkm[key] = NBA_NAMES[key]
            updated += 1
        else:
            missing.append(key)

    data["pkm"] = pkm
    with open(translation_path, "w") as f:
        json.dump(data, f, indent="\t", ensure_ascii=False)

    print(f"Updated: {updated}/{len(pkm)}")
    if missing:
        print(f"Missing mappings ({len(missing)}):")
        for m in missing:
            print(f"  {m}")

if __name__ == "__main__":
    main()
