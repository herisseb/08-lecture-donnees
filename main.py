"""Lecture donnée"""
#### Imports et définition des variables globales
import os
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    if not os.path.exists(filename):
        print(f"Erreur : Le fichier {filename} est introuvable.")
        return []

    with open(filename, mode='r', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            if line:
                elements_str = line.split(';')
                elements_int = [int(x) for x in elements_str]
                l.append(elements_int)
    return l

def get_list_k(data, k):
    """
    Retourne la kième liste de la structure data.
    Retourne None si k est hors limites.
    """
    if 0 <= k < len(data):
        return data[k]
    return None

def get_first(l):
    """Retourne le premier élément de la liste l"""
    if len(l) > 0:
        return l[0]
    return None

def get_last(l):
    """Retourne le dernier élément de la liste l"""
    if len(l) > 0:
        return l[-1]
    return None

def get_max(l):
    """Retourne le maximum de la liste l"""
    if len(l) > 0:
        return max(l)
    return None

def get_min(l):
    """Retourne le minimum de la liste l"""
    if len(l) > 0:
        return min(l)
    return None

def get_sum(l):
    """Retourne la somme de la liste l"""
    if len(l) > 0:
        return sum(l)
    return 0

#### Fonction principale


def main():
    """Appels des fonctions"""
    data = read_data(FILENAME)
    if not data:
        print("Fichier vide ou introuvable.")
        return
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()