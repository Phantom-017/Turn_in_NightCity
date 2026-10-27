from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017")

# Sélection de la BDD
db = client["turn_in_nightcity_db"]

# Sélection des collections
edgerunners = db["Edgerunners"]
corpos = db["Corpos"]

# Supprime la collection afin d'éviter les doublons
edgerunners.drop()

# Création des documents
edgerunners_roster = [
    {"name": "David Martinez", "ATK": 95, "DEF": 75, "PV": 480},
    {"name": "Lucy", "ATK": 85, "DEF": 55, "PV": 320},
    {"name": "Rebecca", "ATK": 110, "DEF": 40, "PV": 350},
    {"name": "Maine", "ATK": 80, "DEF": 95, "PV": 600},
    {"name": "Kiwi", "ATK": 75, "DEF": 50, "PV": 300},
    {"name": "Weak « King » Kingsley", "ATK": 115, "DEF": 60, "PV": 420},
    {"name": "D", "ATK": 88, "DEF": 65, "PV": 380},
    {"name": "Talia Yang", "ATK": 98, "DEF": 80, "PV": 440},
    {"name": "Omi", "ATK": 77, "DEF": 70, "PV": 450},
    {"name": "Capri", "ATK": 130, "DEF": 140, "PV": 300}
]

corpos.drop()

corpos_roster = [
    {"name": "Katsuo Tanaka", "ATK": 40, "DEF": 30, "PV": 200},
    {"name": "James Tanaka", "ATK": 55, "DEF": 50, "PV": 300},
    {"name": "Faraday", "ATK": 70, "DEF": 55, "PV": 380},
    {"name": "Commandant Militech", "ATK": 85, "DEF": 70, "PV": 480},
    {"name": "Kiril", "ATK": 100, "DEF": 80, "PV": 550},
    {"name": "Chef de Sécurité Arasaka", "ATK": 110, "DEF": 105, "PV": 680},
    {"name": "Richard", "ATK": 125, "DEF": 90, "PV": 620},
    {"name": "Kitano", "ATK": 135, "DEF": 115, "PV": 750},
    {"name": "Prototype Cyberpsychotique", "ATK": 150, "DEF": 100, "PV": 850},
    {"name": "Adam Smasher", "ATK": 180, "DEF": 140, "PV": 1200}
]

# Insertion dans la collection des Edgerunnners
insert_edgerunners = edgerunners.insert_many(edgerunners_roster)

#Insertion dans la collection des Corpos
insert_corpos = corpos.insert_many(corpos_roster)

# Affichage de la liste des personnages insérés
print("-------EDGERUNNERS AJOUTÉS------- ", insert_edgerunners)
print("-------CORPOS AJOUTÉS------- ", insert_corpos)