"""
Ce module fournit un ensemble de fonctions utilitaires pour l'application IFT-1004 Solo Immo,
couvrant diverses fonctionnalités telles que le hachage de mots de passe, le formatage de montants
monétaires et l'affichage de données sous forme de tableaux.

Fonctions:
- `hacher_mot_de_passe(mot_de_passe)`: Hache un mot de passe en utilisant l'algorithme SHA-256.
- `garantir_existence_fichier(chemin_fichier)`: S'assure qu'un fichier existe; le crée vide le cas échéant.
- `formater_argent(montant_en_dollars)`: Convertit un montant en dollars en une chaîne formatée.
- `afficher_banniere(titre)`: Affiche une bannière contenant un titre centré.
- `afficher_tableau(lignes, en_tetes)`: Affiche des données sous forme de tableau dans la console.

Dépendances:
- `os`: Utilisé pour vérifier l'existence de fichiers et les créer si nécessaire.
- `hashlib`: Nécessaire pour le hachage de mots de passe en utilisant SHA-256.
- `secrets`: Pour comparer les hachages (https://docs.python.org/3/library/secrets.html#secrets.compare_digest).

Note:
    Les fonctions de ce module sont conçues pour être réutilisables et facilement intégrables dans divers points de
    l'application, contribuant à la modularité et à la maintenance du code.
"""

import os
import hashlib
import secrets


def hacher_mot_de_passe(mot_de_passe):
    """Hache un mot de passe en utilisant l'algorithme SHA-256.

    Cette fonction prend un mot de passe en clair comme entrée et retourne
    son hash SHA-256, offrant une forme sécurisée pour stocker ou comparer
    des mots de passe.

    Args:
        mot_de_passe (str): Le mot de passe en clair à hacher.

    Returns:
        str: Le hash SHA-256 du mot de passe.

    Exemple:
        >>> hacher_mot_de_passe("motdepasse123")
        '75216c44a46bfff78f692d1fe695c02a407a2136625dcc17ca6cf3141e0c4c72'
    """
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()


def garantir_existence_fichier(chemin_fichier):
    """Assure l'existence d'un fichier spécifié par son chemin. Le crée vide si absent.

    Cette fonction vérifie si un fichier existe à l'emplacement spécifié par `chemin_fichier`.
    Si le fichier n'existe pas, il est créé vide, permettant ainsi de garantir son existence
    pour les opérations futures.

    Args:
        chemin_fichier (str): Le chemin complet vers le fichier à vérifier ou à créer.
    """
    if not os.path.isfile(chemin_fichier):
        with open(chemin_fichier, "w") as fichier:
            pass  # Créer simplement le fichier sans rien écrire


def formater_argent(montant_en_dollars):
    """Convertit un montant en dollars en une chaîne formatée.

    Cette fonction prend en entrée un montant en dollars et le formate en chaîne
    de caractères avec deux chiffres après le point décimal et des virgules séparant les milliers.

    Args:
        montant_en_dollars (float): Le montant en dollars à formater.

    Returns:
        str: Le montant formaté en dollars, sous forme de chaîne de caractères,
             avec deux chiffres après le point décimal et des virgules séparant
             les milliers. Suffixé du symbole dollar ($).

    Exemples:
        >>> formater_argent(1234.56)
        '1,234.56 $'

        >>> formater_argent(1234567.89)
        '1,234,567.89 $'

        >>> formater_argent(0.99)
        '0.99 $'
    """
    return "{:,.2f} $".format(montant_en_dollars)


def afficher_banniere(titre):
    """Affiche une bannière contenant un titre centré.

    Args:
        titre (str): Le titre à afficher au centre de la bannière.
    """
    largeur_banniere = len(titre) + 20
    print(largeur_banniere * "#")
    print(f"{titre:^{largeur_banniere}}")
    print(largeur_banniere * "#")


def afficher_tableau(lignes, en_tetes):
    """Affiche un tableau formaté à partir d'une liste de lignes et d'en-têtes.

    Crée et afficher un tableau formaté dans la console. Les en-têtes définissent les colonnes du tableau,
    et chaque ligne représente les données d'une ligne du tableau.

    Args:
        lignes (list of list): Une liste de listes, où chaque sous-liste représente les
            données d'une ligne du tableau à afficher.
        en_tetes (list of str): Une liste de chaînes de caractères représentant les
            noms des colonnes du tableau.

    Exemple:
        >>> afficher_tableau([["Alice", 30], ["Bob", 25]], ["Nom", "Âge"])
        +-------+-----+
        |  Nom  | Âge |
        +-------+-----+
        | Alice |  30 |
        |  Bob  |  25 |
        +-------+-----+
    """
    # Trouver la largeur maximale de chaque colonne
    largeurs = [
        len(max([str(ligne[idx]) for ligne in lignes] + [en_tete], key=len))
        for idx, en_tete in enumerate(en_tetes)
    ]

    # Créer la ligne d'en-tête
    en_tete_formate = " | ".join(
        en_tete.center(largeurs[idx]) for idx, en_tete in enumerate(en_tetes)
    )

    # Créer la ligne de séparation
    ligne_separation = "+-" + "-+-".join("-" * largeur for largeur in largeurs) + "-+"

    # Afficher l'en-tête
    print(ligne_separation)
    print("| " + en_tete_formate + " |")
    print(ligne_separation)

    # Afficher chaque ligne de données
    for ligne in lignes:
        ligne_formatee = " | ".join(
            str(item).center(largeurs[idx]) for idx, item in enumerate(ligne)
        )
        print("| " + ligne_formatee + " |")

    print(ligne_separation)


def tests_hacher_mot_de_passe():
    # Teste si la fonction retourne un résultat.
    mot_de_passe = "secret"
    assert hacher_mot_de_passe(mot_de_passe) is not None

    # Teste si le hash a une longueur de 64 caractères.
    mot_de_passe = "secret"
    assert len(hacher_mot_de_passe(mot_de_passe)) == 64

    # Teste la consistance du hash pour le même mot de passe.
    mot_de_passe = "secret"
    hachage_1 = hacher_mot_de_passe(mot_de_passe)
    hachage_2 = hacher_mot_de_passe(mot_de_passe)
    # Note: La fonction `secrets.compare_digest` est spécialement conçue pour résister aux attaques par analyse
    # de temps, car elle compare les chaînes de caractères de manière à prendre toujours le même temps,
    # indépendamment du nombre de caractères qui correspondent.
    # Cela empêche les attaquants de pouvoir deviner le mot de passe basé sur le temps que prend
    # la comparaison, ajoutant ainsi une couche supplémentaire de sécurité.
    assert secrets.compare_digest(hachage_1, hachage_2)

    # Teste que deux mots de passe différents produisent des hachages différents.
    mot_de_passe_1 = "secret"
    mot_de_passe_2 = "secret2"
    hachage_1 = hacher_mot_de_passe(mot_de_passe_1)
    hachage_2 = hacher_mot_de_passe(mot_de_passe_2)
    assert not secrets.compare_digest(hachage_1, hachage_2)

    # Teste le comportement de la fonction avec un mot de passe vide.
    mot_de_passe = ""
    assert hacher_mot_de_passe(mot_de_passe) is not None
    assert len(hacher_mot_de_passe(mot_de_passe)) == 64

    # Teste le comportement de la fonction avec un très long mot de passe.
    mot_de_passe = "a" * 1000  # Un mot de passe de 1000 caractères 'a'
    assert hacher_mot_de_passe(mot_de_passe) is not None
    assert len(hacher_mot_de_passe(mot_de_passe)) == 64


def tests_formater_argent():
    # Teste si la fonction retourne une chaîne de caractères.
    assert isinstance(formater_argent(100), str)

    # Teste le formatage correct du montant.
    assert formater_argent(1234.56) == "1,234.56 $"

    # Teste le formatage d'un montant rond.
    assert formater_argent(1000.00) == "1,000.00 $"

    # Teste le formatage d'un montant avec des décimales.
    assert formater_argent(99.99) == "99.99 $"

    # Teste le formatage de grands montants.
    assert formater_argent(1_234_567.89) == "1,234,567.89 $"

    # Teste le formatage d'un montant négatif.
    assert formater_argent(-500.75) == "-500.75 $"

    # Teste le formatage de zéro.
    assert formater_argent(0) == "0.00 $"


if __name__ == "__main__":
    print("Exécution des tests unitaires du module 'utilitaires'...")
    tests_hacher_mot_de_passe()
    tests_formater_argent()
    print("Tests réussis!")
