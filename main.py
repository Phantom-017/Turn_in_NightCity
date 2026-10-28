from pymongo import MongoClient
from db_init import db, edgerunners, corpos, scores

# Fonction principale
def main():
    # Tant que Vrai
    while True :
        main_menu()
        # Vérifier si choix menu valide
        # Récuperer choix menu
        user_choice = get_valid_choice(1, 3, "€$ENTRE UN NUM POUR CHOISIR TON OPTION SALE BLEU€$")
        # Choix 1 pour démarrer le jeu
        if int(user_choice) == 1 :
            start_game()
        # Choix 2 pour afficher leaderboard
        elif int(user_choice) == 2 :
            # Récupérer score
            # Afficher leaderboard
            leaderboard()
        # Choix 3 pour quitter le jeu
        elif int(user_choice) == 3 :
            # Quitte le jeu sys.exit
            exit()

# Afficher menu principal
def main_menu():
    # Afficher num et texte élément
    print(
            "///////////////////////////\n"
            "/////TURN IN NIGHTCITY/////\n"
            "///////////////////////////\n"
            "\n///////MENU\n"
            "\n///1. COMMENCER UN CARNAGE\n"
            "///2. CLASSEMENTS DES LÉGENDES\n"
            "///3. BYE CHOOM !\n"
        )

# Vérifier choix
def valid_choice(min_val, max_val, user_choice):
    # Vérifie si le choix n'est pas un chiffre
    if not user_choice.isnumeric():
        error("€$EUH CHOOM, ON T'A DEMANDÉ UN CHIFFRE LÀ !€$")
        return False
    # Vérifie si le choix est supérieure à la valeur minimale
    if int(user_choice) < min_val:
        error("€$BAH VA EN NÉGATIF TANT QUE T'Y EST !€$")
        return False
    # Vérifie si le choixest supérieure à la valeur maximale
    if int(user_choice) > max_val:
        error("€$TU COMPTE DÉJÀ VISER LE CIEL ALORS QUE T'ES AUSSI BAS QUE NOS ÉGOUTS ?!€$")
        return False
    return True

# Récuperer choix
def get_valid_choice(min_val, max_val, message):
    while True :
        # Demande de faire un choix
        print(message)
        # Entrer choix
        user_choice = input()
        # Vérifie choix
        if valid_choice(min_val, max_val, user_choice):
            # Renvoi choix
            return int(user_choice)

# Si choix 1 lancer le jeu
def start_game():
    # Créatin du joueur
    create_player()
    # Création de l'équipe
    create_team()
    # Lancement du carnage
    carnage()
    # Affichage leaderboard à la fin de la partie
    leaderboard()


# Vérifier pseudo
def valid_pseudo(min_char, max_char, username):
    # nom > 3 caractères
    if len(username) < min_char :
        error("€$T'AS UN BLAZE IL EST EN DUO QUEUE OU QUOI !€$")
        return False
    # nom < 50 caractères
    if len(username) > max_char :
        error("€$DONC TON BLAZE C'EST LE LAROUSSE AUSSI !€$")
        return False
    # unique dans la db
    not_unique = scores.find()
    if username == not_unique :
        error("€$EH SOIS ORIGINAL AUSSI STP LÀ !€$")
        return False
    return True

# Récuperer pseudo
def create_player():
     while True :
        # Entrer un pseudo
        username = input(f"€$YO, T'AS UN BLAZE CHOOM ??€$ : ")
        # Vérifie pseudo
        if valid_pseudo(3, 50, username):
            # Affiche le pseudo rentré
            print(f"€$ C'EST ÇA TON BLAZE, {username} ? PARCE QUE C'EST NOVA !€$")
            # Renvoi pseudo
            return(username)

# Fonction récuperer Edgerunners
def get_edgerunners_db():
    # Liste vide des Edgerunners
    edgerunners_list = []
    # Chercher Edgerunners dans la DB
    search_edgerunners = edgerunners.find({}, {"name":1, "ATK":1, "DEF":1, "PV":1, "_id":0})
    # Pour chaque entrée d'Edgerunners à la liste
    for entree in search_edgerunners:
        edgerunners_list.append(entree)
    # Retourne la liste des Edgerunners
    return edgerunners_list

# Afficher Edgerunners
def show_edgerunners(search_edgerunners):
    # Attribuer un numéro à chaque Edgerunner
    n = 0
    # Boucle listant les Edgeunners
    for i in search_edgerunners :
        # Afficher Edgerunners
        print(f"{n}. NAME : {i["name"]}, ATK : {i["ATK"]}, DEF : {i["DEF"]}, PV : {i["PV"]}\n ")
        # Augmente la valeur de la variable pour numéroté le héros suivant
        n = n + 1

# Créer l'équipe
def create_team():
    # Récupère persos dans la base
    team = []
    available_edgerunners = get_edgerunners_db()
    # Boucle de 3
    for i in range(3):
        # Afficher persos dispos
        show_edgerunners(available_edgerunners)
        # Récupère choix du joueur
        choose_edgerunners = available_edgerunners[get_valid_choice(0, 9, "€$ALLEZ CHOISI AVEC QUI TU VAS CANER CHOOM€$")]
        # Ajoute perso à l'équipe
        team.append(choose_edgerunners)
        # Afficher équipe
        print("€$VOILÀ TA TEAM CHOOM€$", team)
        # Actualise la liste des persos dispo
        available_edgerunners.remove(choose_edgerunners)

# Fonction récuperer Corpos
def get_corpos_db():
    # Liste vide des Corpos
    corpos_list = []
    # Chercher Corpos dans la DB
    search_corpos = corpos.find({}, {"name":1, "ATK":1, "DEF":1, "PV":1, "_id":0})
    # Pour chaque entrée Corpos à la liste
    for entree in search_corpos:
        corpos_list.append(entree)
    # Retourne la liste des Corpos
    return corpos_list

def corpos_randomizer(search_corpos):
    # Configuration du pipelin pour un seul corpos aléatoire
    pipeline = get_corpos_db([{"$sample": {"size": 1}}])
    # Récupère corpos
    print(pipeline)

# Fonction combat
def carnage():
    # nombre de vagues
    wave = 1
    # Tant que pv de la team > 0
        # Récupère ennemi dans la base aléatoirement
    corpos_randomizer()
        # Affiche ennemi et stats
        # Lancement du carnage (phase combat)
        # +1 au compteur de vagues (scores)
    # Insérer score dans la base
    # Afficher score

# Si choix 2 afficher leaderboard
def leaderboard():
    # Numéroté les joueurs pour visualiser u classement compétitif
    p = 1
    # On récupère les scores
    score = scores.find()
    # Boucle s'arrêtant aux 3 premiers du classement
    for i in score[:3]:
        print(f"#{p} Player : {i["USERNAME"]} -> Score : {i["SCORE"]}")
        # Augmente la valeur de la variable pour numéroté le joueur suivant
        p = p + 1

# Fonction erreur
def error(error_message):
     print(error_message)


main()


        

    # Fonction récup score
        # Récupérer score dans la base
            # Ouvrir base
            # Accéder à players.score
            # Find
            # Convertir curseur en liste