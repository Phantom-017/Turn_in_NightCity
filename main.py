from pymongo import MongoClient
from db_init import db, edgerunners, corpos, scores

# Fonction erreur
def error():
     print("€$T'ES TEUBÉ OU QUOI CHOOM !€$")

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

# Choix
def valid_choice(min_val, max_val, user_choice):
    # Vérifie si le choix n'est pas un chiffre
    if not user_choice.isnumeric():
        return False
    # Vérifie si le choix est supérieure à la valeur minimale
    if int(user_choice) < min_val:
        return False
    # Vérifie si le choixest supérieure à la valeur maximale
    if int(user_choice) > max_val:
        return False
    return True

    
def get_valid_choice():
    while True :
        # Entrer choix
        user_choice = input("€$ENTRE UN NUM POUR CHOISIR TON OPTION SALE BLEU€$ : ")
        # Vérifie choix
        if valid_choice(1, 3, user_choice):
            # Renvoi choix
            return int(user_choice)
        else :
            error()

# Fonction is_valid_pseudo
def valid_pseudo(min_char, max_char, username):
    # nom > 3 caractères
    if len(username) < min_char :
        return False
    # nom < 50 caractères
    if len(username) > max_char :
        return False
    # unique dans la db
    not_unique = scores.find()
    if username == not_unique :
        return False
    return True

# Création joueur
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
        else :
            error()

# Fonction principale
def main():
    # Tant que Vrai
    while True :
        main_menu()
        # Vérifier si choix menu valide
        # Récuperer choix menu
        user_choice = get_valid_choice()
        # Choix 1 pour démarrer le jeu
        if int(user_choice) == 1 :
            # Récuperer pseudo valide
            # Création joueur
            create_player()
                # Création equipe
                    # Récuperer équipe
                # Boucle de combat
                # Inscrire score dans db
                # Afficher score
                # Afficher leaderboard
        # Choix 2 pour afficher leaderboard
        elif int(user_choice) == 2 :
            # Récupérer score
            # Afficher leaderboard
            leaderboard()
        # Choix 3 pour quitter le jeu
        elif int(user_choice) == 3 :
            # Quitte le jeu sys.exit
            exit()
main()
    # Fonction is_team
        # Récupère persos dans la base
            # Boucle de 3
                # Afficher persos dispos
                # Récupère choix du joueur
                # Ajoute perso à l'équipe
                # Afficher équipe
                # Actualise la liste des persos dispo

    # Fonction combat
        # nombre de vagues
        # Tant que pv de la team > 0
                    # Récupère ennemi dans la base aléatoirement
                    # Affiche ennemi et stats
                    # Lancement du carnage (phase combat)
                    # +1 au compteur de vagues (scores)
        # Insérer score dans la base
        # Afficher score

    # Fonction récup score
        # Récupérer score dans la base
            # Ouvrir base
            # Accéder à players.score
            # Find
            # Convertir curseur en liste

    # Fonction afficher leaderboard
        # Filtrer score element.waves
            # Afficher top 3 score array[-3;-1"]
        # Quitter leaderboard pour retourner au menu