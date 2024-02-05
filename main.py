import tkinter as tk
import tkinter.messagebox
import random
import tkinter.font as tkFont

# Fonctions principales du jeu
def initialiser_plateau():
    return [["" for _ in range(3)] for _ in range(3)]

def verifier_gagnant(plateau):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != "":
            return plateau[i][0]
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != "":
            return plateau[0][i]

    if plateau[0][0] == plateau[1][1] == plateau[2][2] != "":
        return plateau[0][0]
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != "":
        return plateau[0][2]

    if all(cell != "" for row in plateau for cell in row):
        return "Match nul"
    return None

def dessiner_symbole(canvas, ligne, colonne, symbole):
    taille_cellule = 100
    x = colonne * taille_cellule
    y = ligne * taille_cellule
    if symbole == "X":
        canvas.create_line(x + 20, y + 20, x + taille_cellule - 20, y + taille_cellule - 20, fill="red", width=2)
        canvas.create_line(x + taille_cellule - 20, y + 20, x + 20, y + taille_cellule - 20, fill="red", width=2)
    elif symbole == "O":
        canvas.create_oval(x + 20, y + 20, x + taille_cellule - 20, y + taille_cellule - 20, outline="blue", width=2)

def dessiner_ligne_gagnante(canvas, alignement):
    if alignement:
        x1, y1 = alignement[0][1] * 100 + 50, alignement[0][0] * 100 + 50
        x2, y2 = alignement[1][1] * 100 + 50, alignement[1][0] * 100 + 50
        canvas.create_line(x1, y1, x2, y2, width=8, fill="green")

def dessiner_grille(canvas):
    taille_cellule = 100
    for i in range(1, 3):
        canvas.create_line(i * taille_cellule, 0, i * taille_cellule, 3 * taille_cellule, fill="black")
        canvas.create_line(0, i * taille_cellule, 3 * taille_cellule, i * taille_cellule, fill="black")

def mouvement_ia_aleatoire(plateau):
    cases_vides = [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == ""]
    return random.choice(cases_vides) if cases_vides else None

def jeu(jouer_contre_ia, niveau_difficulte="Facile"):
    def sur_clic(event):
        nonlocal joueur_actuel
        colonne = event.x // 100
        ligne = event.y // 100

        if plateau[ligne][colonne] == "" and joueur_actuel == "O":
            plateau[ligne][colonne] = joueur_actuel
            dessiner_symbole(canvas, ligne, colonne, joueur_actuel)
            gagnant, alignement = verifier_gagnant(plateau)
            if gagnant:
                annoncer_gagnant(gagnant, alignement)
                return
            joueur_actuel = "X"
            label_joueur.config(text=f"Joueur actuel: {joueur_actuel}")

            if jouer_contre_ia:
                # Ajouter la logique de l'IA ici en fonction du niveau de difficulté
                coup_ia = mouvement_ia_aleatoire(plateau)  # Utilisez votre logique IA ici
                plateau[coup_ia[0]][coup_ia[1]] = "X"
                dessiner_symbole(canvas, coup_ia[0], coup_ia[1], "X")
                gagnant, alignement = verifier_gagnant(plateau)
                if gagnant:
                    annoncer_gagnant(gagnant, alignement)
                    return
                joueur_actuel = "O"
                label_joueur.config(text=f"Joueur actuel: {joueur_actuel}")

    def annoncer_gagnant(gagnant, alignement):
        fin_message = "Match nul !" if gagnant == "Match nul" else f"Le joueur {gagnant} a gagné !"
        tkinter.messagebox.showinfo("Fin de partie", fin_message)
        dessiner_ligne_gagnante(canvas, alignement)
        fenetre.after(2000, reinitialiser_jeu)

    def reinitialiser_jeu():
        nonlocal plateau, joueur_actuel
        joueur_actuel = "O"
        plateau = initialiser_plateau()
        canvas.delete("all")
        dessiner_grille(canvas)

    joueur_actuel = "O"
    plateau = initialiser_plateau()

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
