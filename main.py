import tkinter as tk
import tkinter.messagebox
import random
import tkinter.font as tkFont

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

    if all(cell != "" for row in plateau for cell in row):
        return "Match nul", None

    return None, None

def dessiner_symbole(canvas, ligne, colonne, symbole):
    taille_cellule = 100
    x = colonne * taille_cellule
    y = ligne * taille_cellule
    
    if symbole == "X":
        canvas.create_line(x + 20, y + 20, x + taille_cellule - 20, y + taille_cellule - 20, fill="red", width=4)
        canvas.create_line(x + taille_cellule - 20, y + 20, x + 20, y + taille_cellule - 20, fill="red", width=4)
        
    elif symbole == "O":
        canvas.create_oval(x + 20, y + 20, x + taille_cellule - 20, y + taille_cellule - 20, outline="blue", width=4)

def dessiner_ligne_gagnante(canvas, alignement):
    
    if alignement:
        x1, y1 = alignement[0][1] * 100 + 50, alignement[0][0] * 100 + 50
        x2, y2 = alignement[1][1] * 100 + 50, alignement[1][0] * 100 + 50
        canvas.create_line(x1, y1, x2, y2, width=8, fill="green")

def dessiner_grille(canvas):
    for i in range(1, 3):
        canvas.create_line(i * 100, 0, i * 100, 300, width=4)
        canvas.create_line(0, i * 100, 300, i * 100, width=4)

def mouvement_ia_aleatoire(plateau):
    
    cases_vides = [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == ""]
    return random.choice(cases_vides) if cases_vides else None

def jeu(jouer_contre_ia, niveau_difficulte="Facile"):
    
    scores = {'X': 0, 'O': 0}
    joueur_actuel = "O"
    plateau = initialiser_plateau()

    fenetre = tk.Tk()
    fenetre.title("Morpion")

    canvas = tk.Canvas(fenetre, width=600, height=600)
    canvas.pack()
    dessiner_grille(canvas)

    label_joueur = tk.Label(fenetre, text=f"Joueur actuel: {joueur_actuel}", font=('Helvetica', 14))
    label_joueur.pack()

    score_label = tk.Label(fenetre, text=f"Score: X - {scores['X']}, O - {scores['O']}", font=('Helvetica', 14))
    score_label.pack()

    def sur_clic(event):
        
        nonlocal joueur_actuel
        colonne = event.x // 100
        ligne = event.y // 100

        if plateau[ligne][colonne] == "" and joueur_actuel == "O":
            plateau[ligne][colonne] = joueur_actuel
            
            dessiner_symbole(canvas, ligne, colonne, joueur_actuel)
            verifier_et_gerer_fin_de_jeu()
            
            if jouer_contre_ia and joueur_actuel == "X":
                fenetre.after(500, jouer_coup_ia)

    def jouer_coup_ia():
        coup = mouvement_ia_aleatoire(plateau)
        
        if coup:
            plateau[coup[0]][coup[1]] = "X"
            dessiner_symbole(canvas, coup[0], coup[1], "X")
            verifier_et_gerer_fin_de_jeu()

    def verifier_et_gerer_fin_de_jeu():
        
        nonlocal joueur_actuel
        gagnant, alignement = verifier_gagnant(plateau)
        if gagnant:
            dessiner_ligne_gagnante(canvas, alignement)
            fenetre.after(500, lambda: annoncer_gagnant(gagnant))
        else:
            joueur_actuel = "X" if joueur_actuel == "O" else "O"
            label_joueur.config(text=f"Joueur actuel: {joueur_actuel}")

    def annoncer_gagnant(gagnant):
        
        fin_message = "Match nul !" if gagnant == "Match nul" else f"Le joueur {gagnant} a gagné !"
        tkinter.messagebox.showinfo("Fin de partie", fin_message)
        
        scores[gagnant] += 1 if gagnant != "Match nul" else 0
        score_label.config(text=f"Score: X - {scores['X']}, O - {scores['O']}")
        reinitialiser_jeu()

    def reinitialiser_jeu():
        
        nonlocal plateau, joueur_actuel
        plateau = initialiser_plateau()
        joueur_actuel = "O"
        canvas.delete("all")
        dessiner_grille(canvas)
        label_joueur.config(text=f"Joueur actuel: {joueur_actuel}")

    canvas.bind("<Button-1>", sur_clic)

    fenetre.mainloop()

def ecran_de_demarrage():
    
    def demarrer_jeu(jouer_contre_ia, niveau_difficulte):
        ecran_principal.destroy()
        jeu(jouer_contre_ia, niveau_difficulte)

    ecran_principal = tk.Tk()
    ecran_principal.title("Morpion - Démarrage")
    customFont = tkFont.Font(family="Helvetica", size=12)

    tk.Button(ecran_principal, text="Joueur vs Joueur", command=lambda: demarrer_jeu(False, "Humain"), font=customFont).pack()
    tk.Button(ecran_principal, text="Facile", command=lambda: demarrer_jeu(True, "Facile"), font=customFont).pack()
    tk.Button(ecran_principal, text="Moyen", command=lambda: demarrer_jeu(True, "Moyen"), font=customFont).pack()
    tk.Button(ecran_principal, text="Difficile", command=lambda: demarrer_jeu(True, "Difficile"), font=customFont).pack()

    ecran_principal.mainloop()

ecran_de_demarrage()
