from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017")

# Sélection de la BDD
db = client["turn_in_nightcity_db"]

# Sélection des collections
edgerunners = db["Edgerunners"]
corpos = db["Corpos"]

# Création des documents
edgerunners_roster = [
    {}
]

corpos_roster = [
    {}
]

# Insertion dans la collection des Edgerunnners


#Insertion dans la collection des Corpos