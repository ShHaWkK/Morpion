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


def verifier_match_nul(plateau):
    return all(all(cell != "" for cell in row) for row in plateau)


def minimax(plateau, profondeur, est_maximisant):
    if verifier_gagnant(plateau, "O"):
        return -1
    if verifier_gagnant(plateau, "X"):
        return 1
    if verifier_match_nul(plateau):
        return 0

    if est_maximisant:
        meilleur_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == "":
                    plateau[i][j] = "X"
                    score = minimax(plateau, profondeur + 1, False)
                    plateau[i][j] = ""
                    meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = float("inf")
        for i in range(3):
            for j in range(3):
                if plateau[i][j] == "":
                    plateau[i][j] = "O"
                    score = minimax(plateau, profondeur + 1, True)
                    plateau[i][j] = ""
                    meilleur_score = min(meilleur_score, score)
        return meilleur_score


def meilleur_coup(plateau):
    meilleur_score = -float("inf")
    coup = None
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == "":
                plateau[i][j] = "X"
                score = minimax(plateau, 0, False)
                plateau[i][j] = ""
                if score > meilleur_score:
                    meilleur_score = score
                    coup = (i, j)
    return coup

jeu()
