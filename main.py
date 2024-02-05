import tkinter as tk
import tkinter.messagebox
import random

# Initialisation du plateau de jeu
def initialiser_plateau():
    return [["" for _ in range(3)] for _ in range(3)]

# Vérification de la condition de victoire
def verifier_gagnant(plateau):
    # Lignes
    for row in plateau:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    # Colonnes
    for col in range(3):
        if plateau[0][col] == plateau[1][col] == plateau[2][col] != "":
            return plateau[0][col]
    # Diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != "":
        return plateau[0][0]
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != "":
        return plateau[0][2]
    # Pas de gagnant
    return None

# Trouve un mouvement aléatoire pour l'IA
def mouvement_ia_aleatoire(plateau):
    cases_vides = [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == ""]
    return random.choice(cases_vides) if cases_vides else None

# Fonction pour dessiner les symboles X et O
def dessiner_symbole(canvas, ligne, colonne, symbole):
    x1, y1 = colonne * 100 + 10, ligne * 100 + 10
    x2, y2 = x1 + 80, y1 + 80
    if symbole == "X":
        canvas.create_line(x1, y1, x2, y2, width=2, fill="red")
        canvas.create_line(x1, y2, x2, y1, width=2, fill="red")
    elif symbole == "O":
        canvas.create_oval(x1, y1, x2, y2, width=2, outline="blue")

# Fonction pour dessiner la grille de jeu
def dessiner_grille(canvas):
    for i in range(1, 3):
        canvas.create_line(i * 100, 0, i * 100, 300, fill="black")
        canvas.create_line(0, i * 100, 300, i * 100, fill="black")


def jeu():
    def sur_clic(event):
        x, y = event.x, event.y
        colonne = x // 100
        ligne = y // 100

        if plateau[ligne][colonne] == "":
            plateau[ligne][colonne] = joueur_actuel
            dessiner_symbole(canvas, ligne, colonne, joueur_actuel)
            gagnant = verifier_gagnant(plateau)

            if gagnant:
                annonce_gagnant(gagnant)
            else:
                changer_joueur()

    def changer_joueur():
        nonlocal joueur_actuel
        joueur_actuel = "O" if joueur_actuel == "X" else "X"
        label_joueur.config(text=f"Joueur actuel: {joueur_actuel}")

    def annonce_gagnant(gagnant):
        if gagnant == "Match nul":
            tkinter.messagebox.showinfo(title="Morpion", message="Match nul!")
        else:
            tkinter.messagebox.showinfo(title="Morpion", message=f"Le joueur {gagnant} gagne!")
        fenetre.after(2000, reinitialiser_jeu)

    def reinitialiser_jeu():
        nonlocal plateau, joueur_actuel
        canvas.delete("all")
        plateau = initialiser_plateau()
        joueur_actuel = "X"
        dessiner_grille(canvas)
        label_joueur.config(text=f"Joueur actuel: {joueur_actuel}")

    plateau = initialiser_plateau()
    joueur_actuel = "X"

    fenetre = tk.Tk()
    fenetre.title("Morpion")

    canvas = tk.Canvas(fenetre, width=300, height=300)
    canvas.pack()
    canvas.bind("<Button-1>", sur_clic)
    dessiner_grille(canvas)

    label_joueur = tk.Label(fenetre, text=f"Joueur actuel: {joueur_actuel}", font=('Helvetica', 14))
    label_joueur.pack()

    fenetre.mainloop()
def ecran_de_demarrage():
    def demarrer_jeu(niveau):
        ecran_principal.destroy()
        jeu(niveau)

    ecran_principal = tk.Tk()
    ecran_principal.title("Morpion - Démarrage")
    ecran_principal.configure(bg="#D3D3D3")  # Couleur de fond

    customFont = tkFont.Font(family="Helvetica", size=12)  # Police personnalisée

    tk.Button(ecran_principal, text="Humain", command=lambda: demarrer_jeu("Humain"), font=customFont).pack()
    tk.Button(ecran_principal, text="Facile", command=lambda: demarrer_jeu("Facile"), font=customFont).pack()
    tk.Button(ecran_principal, text="Moyen", command=lambda: demarrer_jeu("Moyen"), font=customFont).pack()
    tk.Button(ecran_principal, text="Difficile", command=lambda: demarrer_jeu("Difficile"), font=customFont).pack()

    ecran_principal.mainloop()

ecran_de_demarrage()
