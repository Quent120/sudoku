from tkinter import *
from copy import*
from math import sqrt
import time



def main():
    


#E : sol : liste contenant la grille de SUDOKU troué
#S : affiche dans un canvas de la grille en cours de remplissage
def resolution_sudoku(sol):
    p = 0
    N = int(sqrt(len(sol)+1)) - 1
    global est_arrive
    est_arrive = False
    global sol2
    placer(p,N,sol)
    
#E :sol : liste du SUDOKU 
#   N : longueur d'une ligne
#S :affiche en sortie une fenetre represantant graphiquement le SUDOKU en fonction de sol
def afficher_sol(sol, N):
    time.sleep(0)
    canvas.delete(ALL) #efface tout pour remplir pour le sol suivant
    for i in range(N+1):
        canvas.create_line((450//(N+1))*i,0,(450//(N+1))*i, 450, fill = 'gray')
        canvas.create_line(0,(450//(N+1))*i, 450, (450//(N+1))*i, fill = 'gray')

    for i in range(int(sqrt(N+1))):
        canvas.create_line((450//int(sqrt(N+1)))*i,0,(450//int(sqrt(N+1)))*i, 450, fill = 'black')
        canvas.create_line(0,(450//int(sqrt(N+1)))*i, 450, (450//int(sqrt(N+1)))*i, fill = 'black')
    
    for i in range(N+1):
        for j in range(N+1):
            if(sol[i*(N+1)+j] != 0):
                canvas.create_text(25+50*j, 25+50*i, text=sol[i*(N+1)+j])
    
    fenetre.update()
    
    
    
#E :p : rang ou un nombre va etre place (sol[p] == 0)
#   N : longueur d'une ligne
#   sol : liste du SUDOKU
#S :pas de sortie pour cette fonction, seulement un affichage (afficher_sol) pour chaque nombre essayer dans chaque case
def placer(p, N, sol):
    if( p == (N+1)**2): #si l'indice courant est 80 (dernier indice)
        afficher_sol(sol, N)
        global est_arrive
        est_arrive = True
    else:
        if(sol[p] == 0):
            for i in range(1, N+2):
                sol[p] = i
                if(not est_arrive):
                    afficher_sol(sol, N)
                if(ajout_possible(p, N, sol)):
                    placer(p+1, N, sol)
                  
                else:
                    sol[p] = 0
        else:
            placer(p+1, N,sol)
                
#E :p : rang ou un nombre va etre place (1<= sol[p] <= 9)
#   N : longueur d'une ligne
#   sol : liste du SUDOKU
#S :retourne vrai si la valeur sol[p] peut-etre ajoute sur l'indice p, false dans le cas contraire
def ajout_possible(p, N, sol):
    l = l_ligne(p,N,sol)
    c = l_colonne(p,N,sol)
    r = l_region(p,N,sol)
    for i in range(0,N+1):
        if(l[i][0] == sol[p] and p != l[i][1]): #cherche si sol[p] est deja sur la ligne
            return False
        if(c[i][0] == sol[p] and p != c[i][1]): #cherche si sol[p] est deja sur la colonne
            return False
        if(r[i][0] == sol[p] and p != r[i][1]): #cherche si sol[p] est deja sur la region
            return False
    return True
    
    
#E :p : rang ou un nombre va etre place (1<= sol[p] <= 9)
#   N : longueur d'une ligne
#   sol : liste du SUDOKU
#S :retourne une liste contenant toute les valeurs corrsepondantes a la ligne du SUDOKU ou se trouve p
def l_ligne(p, N, sol):
    ligne = []
    for i in range (0, len(sol)):
        if(i//(N + 1) == p//(N +1)): 
            ligne.append((sol[i], i))
    return ligne

#E :p : rang ou un nombre va etre place (1<= sol[p] <= 9)
#   N : longueur d'une ligne
#   sol : liste du SUDOKU
#S :retourne une liste contenant toute les valeurs corrsepondantes a la colonne du SUDOKU ou se trouve p
def l_colonne(p,N, sol):
    col = []
    for i in range(0, len(sol)):
        if(i%(N+1) == p %(N+1)):
            col.append((sol[i], i))
    return col


#E :p : rang ou un nombre va etre place (1<= sol[p] <= 9)
#   N : longueur d'une ligne
#   sol : liste du SUDOKU
#S :retourne une liste contenant toute les valeurs corrsepondantes a la region du SUDOKU ou se trouve p
def l_region(p,N,sol):
    reg = []
    for i in range(0,len(sol)):
        if(i//(((N+1)**2)//3) == p//(((N+1)**2)//3)):
            if(i%(N+1) < int(sqrt(N+1)) and p%(N+1) < int(sqrt(N+1))):
                reg.append((sol[i],i))
            if(i%(N+1) < 2*int(sqrt(N+1)) and i%(N+1) >= int(sqrt(N+1)) and p%(N+1) < 2*int(sqrt(N+1)) and p%(N+1) >= int(sqrt(N+1))):
                reg.append((sol[i],i))
            if(i%(N+1) < N+1 and i%(N+1) >= 2*int(sqrt(N+1)) and p%(N+1) < N+1 and p%(N+1) >=2*int(sqrt(N+1))):
                reg.append((sol[i], i))
                
    return reg


s = [0, 8, 7, 0, 0, 0, 5, 2, 0,
9, 1, 0, 5, 0, 2, 0, 4, 6,
2, 0, 0, 0, 0, 0, 0, 0, 7,
0, 9, 0, 0, 2, 0, 0, 1, 0,
0, 0, 0, 1, 0, 6, 0, 0, 0,
0, 4, 0, 0, 9, 0, 0, 8, 0,
6, 0, 0, 0, 0, 0, 0, 0, 3,
5, 7, 0, 3, 0, 1, 0, 6, 8,
0, 3, 8, 0, 0, 0, 9, 5, 0]



######################################################################################################################################################################
#Initialisation du canvas

fenetre = Tk()

canvas = Canvas(fenetre, width=900, height=450, background='white')
canvas.pack()

resolution_sudoku(s)

fenetre.mainloop()