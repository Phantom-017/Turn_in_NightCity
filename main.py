# Afficher titre
# Afficher menu
# Choix
# Choix 1 pour démarrer le jeu
    # Création joueur
        # Récuperer pseudo valide
            # while True :
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

# Fonction titre
    # Écirer titre

# Fonction menu
    # Afficher num et texte élément

# Fonction choix
    # Tant que Vrai
        # Récuperer choix menu
        # Vérifier si choix menu valide

# Fonction vérifier choix
    # Si choix valide
        # renvoi choix
    # Sinon 
        # lancer fonction erreur

# Fonction is_pseudo
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