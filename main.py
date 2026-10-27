# Afficher titre
# Afficher menu
    # Afficher num et texte élément
# Choix
# Tant que Vrai
    # Récuperer choix menu
    # Vérifier si choix menu valide
        # Si choix valide
            # renvoi choix
        # Sinon 
            # lancer fonction erreur
# Choix 1 pour démarrer le jeu
    # Demande d'entrer pseudo
    # Entre pseudo
    # Récupère persos dans la base
    # Afficher persos
    # Demande à créer une équipe de 3
    # Boucle de 3
        # Choix 1 à 10 pour chosisir un perso
        # Récupère choix du joueur
            # Sinon
                # Lancer fonction erreur
        # Afficher équipe
        # Actualise la liste des persos
    # Lancement du carnage
# Choix 2 pour afficher le tableau des score
    # Récupérer score dans la base
        # Ouvrir base
        # Accéder à players.score
        # Find
        # Convertir curseur en liste
    # Filtrer score element.waves
        # Afficher top 3 score array[-3;-1"]
    # Quitter tableau des scores pour retourner au menu
# Choix 3 pour quitter le jeu
    # Quitte le jeu sys.exit