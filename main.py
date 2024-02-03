import tkinter as tk
import tkinter.messagebox

def initialiser_plateau():
    return [["" for _ in range(3)] for _ in range(3)]

def verifier_gagnant(plateau):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != "":
            return plateau[i][0], [(i, 0), (i, 2)]
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != "":
            return plateau[0][i], [(0, i), (2, i)]

    if plateau[0][0] == plateau[1][1] == plateau[2][2] != "":
        return plateau[0][0], [(0, 0), (2, 2)]
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != "":
        return plateau[0][2], [(0, 2), (2, 0)]

    return None, None

def dessiner_symbole(canvas, ligne, colonne, symbole):
    x1, y1 = colonne * 100 + 10, ligne * 100 + 10
    x2, y2 = x1 + 80, y1 + 80
    if symbole == "X":
        canvas.create_line(x1, y1, x2, y2, width=2, fill="red")
        canvas.create_line(x1, y2, x2, y1, width=2, fill="red")
    elif symbole == "O":
        canvas.create_oval(x1, y1, x2, y2, width=2, outline="blue")

def dessiner_ligne_gagnante(canvas, alignement):
    x1, y1 = alignement[0][1] * 100 + 50, alignement[0][0] * 100 + 50
    x2, y2 = alignement[1][1] * 100 + 50, alignement[1][0] * 100 + 50
    canvas.create_line(x1, y1, x2, y2, width=4, fill="green")

def jeu():
    def sur_clic(event):
        nonlocal joueur_actuel
        colonne, ligne = event.x // 100, event.y // 100
        if plateau[ligne][colonne] == "":
            plateau[ligne][colonne] = joueur_actuel
            dessiner_symbole(canvas, ligne, colonne, joueur_actuel)
            gagnant, alignement = verifier_gagnant(plateau)
            if gagnant:
                scores[gagnant] += 1
                afficher_scores()
                dessiner_ligne_gagnante(canvas, alignement)
                tkinter.messagebox.showinfo("Morpion", f"Le joueur {gagnant} a gagné!")
                reinitialiser_jeu()
                return
            if all(all(cell != "" for cell in row) for row in plateau):
                tkinter.messagebox.showinfo("Morpion", "Match nul!")
                reinitialiser_jeu()
                return
            joueur_actuel = "O" if joueur_actuel == "X" else "X"

    def reinitialiser_jeu():
        nonlocal plateau, joueur_actuel
        plateau = initialiser_plateau()
        joueur_actuel = "X"
        canvas.delete("all")
        dessiner_grille()

    def afficher_scores():
        score_label.config(text=f"X: {scores['X']}  O: {scores['O']}")

    def dessiner_grille():
        for i in range(4):
            canvas.create_line(0, i * 100, 300, i * 100, fill="black")
            canvas.create_line(i * 100, 0, i * 100, 300, fill="black")

    fenetre = tk.Tk()
    fenetre.title("Morpion")

    scores = {"X": 0, "O": 0}
    joueur_actuel = "X"
    plateau = initialiser_plateau()

    canvas = tk.Canvas(fenetre, width=300, height=300)
    canvas.bind("<Button-1>", sur_clic)
    canvas.pack()
    dessiner_grille()

    score_label = tk.Label(fenetre, text=f"X: {scores['X']}  O: {scores['O']}")
    score_label.pack()

    bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.destroy)
    bouton_quitter.pack()

    fenetre.mainloop()

jeu()