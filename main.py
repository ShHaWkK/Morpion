def initialiser_plateau():
    return [[" " for _ in range(3)] for _ in range(3)]

def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)
def jouer(plateau, joueur, ligne, colonne):
    if plateau[ligne][colonne] == " ":
        plateau[ligne][colonne] = joueur
        return True
    return False

def gagnant(plateau, joueur):
    for i in range(3):
        if all([cell == joueur for cell in plateau[i]]) or \
           all([plateau[j][i] == joueur for j in range(3)]):
            return True
    if plateau[0][0] == joueur and plateau[1][1] == joueur and plateau[2][2] == joueur:
        return True
    if plateau[0][2] == joueur and plateau[1][1] == joueur and plateau[2][0] == joueur:
        return True
    return False

def jeu():
    plateau = initialiser_plateau()
    joueur_actuel = "X"
    nb_coups = 0

    while nb_coups < 9:
        afficher_plateau(plateau)
        ligne = int(input(f"Joueur {joueur_actuel}, choisissez votre ligne: "))
        colonne = int(input(f"Joueur {joueur_actuel}, choisissez votre colonne: "))
        if jouer(plateau, joueur_actuel, ligne, colonne):
            if gagnant(plateau, joueur_actuel):
                afficher_plateau(plateau)
                print(f"Joueur {joueur_actuel} a gagné!")
                return
            joueur_actuel = "O" if joueur_actuel == "X" else "X"
            nb_coups += 1
        else:
            print("Case déjà occupée, veuillez réessayer.")

    afficher_plateau(plateau)
    print("Match nul!")

jeu()