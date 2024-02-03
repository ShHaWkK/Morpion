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

