from pymongo import MongoClient
from db_init import db, edgerunners, corpos

# Fonction erreur
def erreur():
     print("€$TU SAIS PAS ÉCRIRE OU QUOI CHOOM !")

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
def valid_choice(min_val, max_val, saisie):
    # Vérifie si la saisie n'est pas un chiffre
    if not saisie.isnumeric():
        return False
    # Vérifie si la valeur saisie est supérieure à la valeur minimale
    if int(saisie) < min_val:
        return False
    # Vérifie si la valeur saisie est supérieure à la valeur maximale
    if int(saisie) > max_val:
            return False
    return True

def get_valid_choice():
    # Recommence tant que le joueur n'entre pas une valeur valide
    while True :
        # Saisi de la valeur
        saisie = input("€$POUR CHOISIR UNE OPTION ENTRE UN CHIFFRE CHOOM€$ : ")
        # Vérifier la valeur
        if valid_choice(min_val, max_val, saisie):
             return int(saisie)
        else :
             print(erreur)

# Tant que Vrai
while True :
    main_menu()
    # Vérifier si choix menu valide
    valid_choice()
    # Récuperer choix menu
    get_valid_choice()
    # Choix 1 pour démarrer le jeu
        # Création joueur
            # Récuperer pseudo valide
                # while True :
                    # Si choix valide
                        # renvoi choix
                    # Sinon 
                        # lancer fonction erreur
                    # Demander rentrer pseudo
                    # Si nom valide
                        # return nom
                    # Sinon
                        # Lancer fonction erreur
        # Création equipe
            # Récuperer équipe
        # Boucle de combat
        # Inscrire score dans db
        # Afficher score
        # Afficher leaderboard

    # Choix 2 pour afficher leaderboard
        # Récupérer score
        # Afficher leaderboard
    # Choix 3 pour quitter le jeu
        # Quitte le jeu sys.exit

    # Fonction is_valid_pseudo
        # nom > 3 caractères
        # nom < 50 caractères
        # unique dans la db

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