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
                dessiner_ligne_gagnante(canvas, alignement)
                tkinter.messagebox.showinfo("Morpion", f"Le joueur {gagnant} a gagné!")
                fenetre.quit()
                return
            joueur_actuel = "O" if joueur_actuel == "X" else "X"

    fenetre = tk.Tk()
    fenetre.title("Morpion")
    canvas = tk.Canvas(fenetre, width=300, height=300)
    canvas.bind("<Button-1>", sur_clic)
    canvas.pack()

    plateau = initialiser_plateau()
    joueur_actuel = "X"

    for i in range(4):
        canvas.create_line(0, i * 100, 300, i * 100, fill="black")
        canvas.create_line(i * 100, 0, i * 100, 300, fill="black")

    fenetre.mainloop()

jeu()
