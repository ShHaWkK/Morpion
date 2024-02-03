import tkinter as tk
import tkinter.messagebox
import random


def initialiser_plateau():
    return [["" for _ in range(3)] for _ in range(3)]


def verifier_gagnant(plateau, joueur):
    for i in range(3):
        if all([cell == joueur for cell in plateau[i]]) or \
                all([plateau[j][i] == joueur for j in range(3)]):
            return True
    if plateau[0][0] == joueur and plateau[1][1] == joueur and plateau[2][2] == joueur:
        return True
    if plateau[0][2] == joueur and plateau[1][1] == joueur and plateau[2][0] == joueur:
        return True
    return False


def coup(plateau, ligne, colonne, joueur):
    if plateau[ligne][colonne] == "":
        plateau[ligne][colonne] = joueur
        return True
    return False


def jeu():
    def sur_clic(ligne, colonne):
        nonlocal joueur_actuel
        if coup(plateau, ligne, colonne, joueur_actuel):
            boutons[ligne][colonne].config(text=joueur_actuel)
            if verifier_gagnant(plateau, joueur_actuel):
                tkinter.messagebox.showinfo("Morpion", f"Le joueur {joueur_actuel} a gagné!")
                fenetre.quit()
            joueur_actuel = "O" if joueur_actuel == "X" else "X"

    fenetre = tk.Tk()
    fenetre.title("Morpion")
    plateau = initialiser_plateau()
    joueur_actuel = "X"
    boutons = [[tk.Button(fenetre, text="", font="Arial 20", width=5, height=2,
                          command=lambda i=i, j=j: sur_clic(i, j))
                for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            boutons[i][j].grid(row=i, column=j)

    fenetre.mainloop()


jeu()
