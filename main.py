def initialiser_plateau():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)
