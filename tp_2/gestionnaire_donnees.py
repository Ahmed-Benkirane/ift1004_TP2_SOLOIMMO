"""
Ce module est responsable de la gestion des données de l'application IFT-1004 Solo Immo,
incluant le chargement et la sauvegarde des utilisateurs et des propriétés dans des fichiers texte.

Fonctions:
- `charger_utilisateurs()`: Charge les utilisateurs depuis le fichier des utilisateurs.
- `sauvegarder_utilisateurs(utilisateurs)`: Sauvegarde les utilisateurs dans le fichier des utilisateurs.
- `charger_proprietes()`: Charge toutes les propriétés depuis le fichier des propriétés.
- `sauvegarder_propriete(new_property)`: Sauvegarde une nouvelle propriété.

Dépendances:
- `configuration`: Pour accéder à des constantes globales comme les chemins des fichiers.
"""

from configuration import FICHIER_UTILISATEURS, FICHIER_PROPRIETES


def charger_utilisateurs():
    """Charge les utilisateurs depuis le fichier des utilisateurs.

    Returns:
        dict: Un dictionnaire des utilisateurs avec leurs mots de passe hachés.
    """
  
    utilisateurs = {}
    with open(FICHIER_UTILISATEURS, "r") as fichier:
        # Ignorer la ligne d'en-tête
        fichier.readline()
        for ligne in fichier:
            ligne = ligne.strip()
            if ligne:
                utilisateur, hash_mot_de_passe = ligne.split(",")
                utilisateurs[utilisateur] = hash_mot_de_passe
    return utilisateurs


def sauvegarder_utilisateurs(utilisateurs):
    """Écrit les informations des utilisateurs dans un fichier texte, en les formatant avec une ligne d'en-tête.

    Cette fonction prend un dictionnaire d'utilisateurs et écrit chaque paire
    nom d'utilisateur/mot de passe haché dans le fichier spécifié. Chaque ligne du fichier
    représente un utilisateur unique, avec les informations de l'utilisateur séparées par des virgules.

    La première ligne du fichier contient une ligne d'en-tête ("utilisateur,hash") pour indiquer les champs.

    Args:
        utilisateurs (dict): Un dictionnaire où chaque clé est un nom d'utilisateur (str)
                             et chaque valeur est le mot de passe haché (str) correspondant.

    Le fichier est entièrement écrasé chaque fois que cette fonction est appelée.
    """
    
    with open(FICHIER_UTILISATEURS, "w") as fichier:
        
        fichier.write("utilisateur,hash\n")
        
        for utilisateur, hash_mot_de_passe in utilisateurs.items():
    
            fichier.write(f"{utilisateur},{hash_mot_de_passe}\n")
    # TODO


def charger_proprietes():
    """Charge et retourne la liste des propriétés disponibles depuis le fichier des propriétés.

    Cette fonction lit le fichier des propriétés contenant les informations des propriétés,
    avec chaque propriété sur une ligne distincte et les champs séparés par des virgules.
    La première ligne du fichier est une ligne d'en-tête qui est ignorée.

    Chaque ligne de propriété est convertie en un dictionnaire contenant les champs suivants :
        - "prix" (int) : Prix de la propriété.
        - "ville" (str) : Ville où se situe la propriété.
        - "type" (str) : Type de la propriété (par exemple, Maison ou Condo).
        - "chambres" (int) : Nombre de chambres dans la propriété.
        - "salles_de_bains" (int) : Nombre de salles de bains dans la propriété.

    Les valeurs numériques (prix, chambres, salles de bains) sont converties en entiers.

    Returns:
        list: Une liste de dictionnaires, où chaque dictionnaire représente une propriété.
               Si le fichier est vide, une liste vide est retournée.
    """
    # TODO
    proprietes = []  

    try:
        with open(FICHIER_PROPRIETES, "r") as fichier:
            
            fichier.readline()
            for ligne in fichier:
                ligne = ligne.strip()  
                if ligne: 
                   
                    champs = ligne.split(",")
                   
                    propriete = {
                        "prix": int(champs[0]), 
                        "ville": champs[1],
                        "type": champs[2],
                        "chambres": int(champs[3]),  
                        "salles_de_bains": int(champs[4])  
                    }
                    proprietes.append(propriete)  

    except FileNotFoundError:
        print("Le fichier des propriétés n'a pas été trouvé.")  
    except Exception as e:
        print(f"Erreur lors du chargement des propriétés : {e}")  

    return proprietes


def sauvegarder_propriete(nouvelle_propriete):
    """Sauvegarde une nouvelle propriété.

    Args:
        nouvelle_propriete (dict): Dictionnaire contenant les informations de la nouvelle propriété.
    """
    # Charger les propriétés existantes
    proprietes = charger_proprietes()

    proprietes.append(nouvelle_propriete)

    with open(FICHIER_PROPRIETES, "w") as fichier:
        # Écrire la ligne d'en-tête
        fichier.write("prix,ville,type,chambres,salles_de_bains\n")

        for propriete in proprietes:
            # Écrire chaque propriété en format CSV
            fichier.write(
                f"{propriete['prix']},{propriete['ville']},{propriete['type']},"
                f"{propriete['chambres']},{propriete['salles_de_bains']}\n"
            )
