"""
Configuration pour l'application IFT-1004 Solo Immo.

Ce module définit plusieurs constantes utilisées à travers l'application,
notamment les chemins vers les fichiers nécessaires au bon fonctionnement
de l'application.

Constantes:
    - DOSSIER_BASE: Répertoire de base de l'application, défini comme le dossier contenant ce fichier de configuration.
    - FICHIER_UTILISATEURS: Chemin vers le fichier stockant les informations des utilisateurs (utilisateurs.txt).
    - FICHIER_PROPRIETES: Chemin vers le fichier stockant les informations des propriétés (proprietes.txt).
    - FICHIER_SESSION: Chemin vers le fichier stockant la session active (session.txt).

Dépendances:
- `pathlib`: Nécessaire pour manipuler les chemins de fichiers et répertoires de manière portable et efficace.
"""

from pathlib import Path

# Définit le dossier de base de l'application comme étant le dossier contenant ce fichier de configuration.
DOSSIER_BASE = Path(__file__).resolve().parent

# Chemin vers le fichier stockant les informations des utilisateurs.
FICHIER_UTILISATEURS = DOSSIER_BASE / "utilisateurs.txt"

# Chemin vers le fichier stockant les informations des propriétés.
FICHIER_PROPRIETES = DOSSIER_BASE / "proprietes.txt"

# Chemin vers le fichier stockant la session active.
FICHIER_SESSION = DOSSIER_BASE / "session.txt"
