from pymongo import MongoClient
from db_init import db, edgerunners, corpos, scores

# Fonction erreur
def erreur():
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
def valid_choice(min_val, max_val):
    saisie = input()
    # Vérifie si la saisie n'est pas un chiffre
    if not saisie.isnumeric():
        erreur()
    # Vérifie si la valeur saisie est supérieure à la valeur minimale
    if int(saisie) < min_val:
        erreur()
    # Vérifie si la valeur saisie est supérieure à la valeur maximale
    if int(saisie) > max_val:
        erreur()
    # Sinon on peut renvoyer la saisie
    return saisie
    
def get_valid_choice():
    # Recommence tant que le joueur n'entre pas une valeur valide
    print("€$ENTRE UN NUM POUR CHOISIR TON OPTION SALE BLEU€$")
    # Faire un choix
    choice = valid_choice(1, 3)
    # Renvoi choix
    return choice

# Fonction is_valid_pseudo
def valid_pseudo(min_char, max_char):
    username = input()
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
    return username

# Création joueur
def create_player():
     
     print(f"€$YO, T'AS UN BLAZE CHOOM ??€$ : ")
     # Entrer un pseudo
     username = valid_pseudo(3, 50)
     print(f"€$ C'EST ÇA TON BLAZE, {username} ? PARCE QUE C'EST NOVA !€$")


# Fonction principale
# Tant que Vrai
def main():
    main_menu()
    # Vérifier si choix menu valide
    # Récuperer choix menu
    user_choice = get_valid_choice()
    # Choix 1 pour démarrer le jeu
    # Récuperer pseudo valide
    # Création joueur
    create_player()
        # Création equipe
            # Récuperer équipe
        # Boucle de combat
        # Inscrire score dans db
        # Afficher score
        # Afficher leaderboard
main()
    # Choix 2 pour afficher leaderboard
        # Récupérer score
        # Afficher leaderboard
    # Choix 3 pour quitter le jeu
        # Quitte le jeu sys.exit

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