# TictacteoBetaIA

print("Bonjour et bienvenue aux joueurs Galactiens !\n")

playerO = input("Qui sera le joueur O  ? ")
print(playerO + " sera le joueur O")

playerX = "IA"                                             # Ia is the player X
print("Bienvenue à " + playerO + " et " + playerX + " !")

grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
largeur = 13

def tabgrid():
    nb = 0
    print("-" * largeur)
    for i in range(3):
        print(f"| {grid[nb]} | {grid[nb+1]} | {grid[nb+2]} |")
        print("-" * largeur)
        nb += 3

tabgrid()

def Victory():
    # Ligne
    if grid[0] == grid[1] == grid[2]:
        return grid[0]
    if grid[3] == grid[4] == grid[5]:
        return grid[3]
    if grid[6] == grid[7] == grid[8]:
        return grid[6]
    # Colonne
    if grid[0] == grid[3] == grid[6]:
        return grid[0]
    if grid[1] == grid[4] == grid[7]:
        return grid[1]
    if grid[2] == grid[5] == grid[8]:
        return grid[2]
    # Diagonales
    if grid[0] == grid[4] == grid[8]:
        return grid[0]
    if grid[2] == grid[4] == grid[6]:
        return grid[2]
    return None

                                                           
def Minimax(sim_grid, player):                              # defeny my fonction 
    winner = None
                                                             # Veryfy all the possibility of wining
    if sim_grid[0] == sim_grid[1] == sim_grid[2]:
        winner = sim_grid[0]
    elif sim_grid[3] == sim_grid[4] == sim_grid[5]:
        winner = sim_grid[3]
    elif sim_grid[6] == sim_grid[7] == sim_grid[8]:
        winner = sim_grid[6]
    elif sim_grid[0] == sim_grid[3] == sim_grid[6]:
        winner = sim_grid[0]
    elif sim_grid[1] == sim_grid[4] == sim_grid[7]:
        winner = sim_grid[1]
    elif sim_grid[2] == sim_grid[5] == sim_grid[8]:
        winner = sim_grid[2]
    elif sim_grid[0] == sim_grid[4] == sim_grid[8]:
        winner = sim_grid[0]
    elif sim_grid[2] == sim_grid[4] == sim_grid[6]:
        winner = sim_grid[2]
                                                            # add a new conditon
    if winner == "X":                                       # if the winner is "X"  
        return 1                                            # its IA wining 
    elif winner == "O":                                     # else the winner is "O"
        return -1                                           # the winer is playerO
    elif all(cell in ["O", "X"] for cell in sim_grid):      # verify for each case in each line if there is O or X
        return 0                                            # is the case is full = nul

    scores = []                                             # creat a new var to stock the result 
    for i in range(9):                                      # check from 0 to 8 
        if sim_grid[i] not in ["O", "X"]:                   # check if is o or x or emtpy
            temp = sim_grid[i]                              # if is empty it simulate simgrid
            sim_grid[i] = player                            # simulate what player could play
            next_player = "O" if player == "X" else "X"     # 
            score = Minimax(sim_grid, next_player)          #
            scores.append(score)                            # stock le score optenue 
            sim_grid[i] = temp                              # cancel the fake playe 

    if player == "X":                                       # who's playing 
        return max(scores)                                  # Ia want to maximix the chance to win the simuaton below(fonction)
    else:                                                   # else
        return min(scores)                                  # think that player X want to minimise the score of the IA

                                                            # i start a new fonction for iA for choosing the best way to play that i can call this fonction when ia play
def IA_play():                                              # 
    best_score = -float('inf')                              # this is to start, to compare the possibleresult so i creat a variable  = to give a minimal start
    move = None                                             #  create a var move = nothing, to keep the best possibilyty inside this var
    for i in range(9):                                      # from 0 to 8 ( check if the grid is free and play minimax)
        if grid[i] not in ["O", "X"]:                       # 1 this part is to simulate if there is not a O or X to play
            grid[i] = "X"                                   # 1 t
            score = Minimax(grid, "O")                      # here say's that in the simutaion O havee been pl1
            grid[i] = str(i+1)                              #
            if score > best_score:                          #
                best_score = score                          #
                move = i                                    #
    grid[move] = "X"                                        #


turn = 0

while turn < 9:

    if turn % 2 == 0:
        currentplayer = playerO
        symbole = "O"
    else:
        currentplayer = playerX
        symbole = "X"

    print(f"C'est le tour de {currentplayer} ({symbole})")

    if currentplayer == playerO:
        input_casee = input("Sur quelle case voulez-vous poser le symbole ? ")
        grid_index = int(input_casee) - 1

        if grid[grid_index] in ["O", "X"]:
            print("Cette case est déjà occupée, choisis-en une autre !")
            continue

        grid[grid_index] = symbole
    else:
        IA_play()                                                # call my fonction

    tabgrid()

    result = Victory()
    if result:
        if result == "O":
            print(f"Bravo {playerO} ! Tu as gagné !")
        else:
            print(f"Bravo {playerX} ! Tu as gagné !")
        break

    if turn == 8:
        print("Match NUL")
        break

    turn += 1

print("Fin de la partie !")


#f rancais 
# speudo code difficulté ia 


""""
#  demander au joueur le niveau de difficulté

afficher "Choisissez le niveau de difficulté de l'IA :"           #Affiche à l’écran une invite pour 
afficher "1 - Facile"                                             #prévenir l’utilisateur qu’il doit choisir un niveau.
afficher "2 - Moyen"                                              #trois options disponibles
afficher "3 - Difficile"

lire choix_joueur                                                 # lis ce que le joueur ecrit donc doit etre stocker dans une var

si choix_joueur == "1" alors                                      #condition en if 
    difficulté ← "facile"
sinon si choix_joueur == "2" alors
    difficulté ← "moyen"
sinon
    difficulté ← "difficile"

afficher "Vous avez choisi le niveau :", difficulté               # mon print


# adapter le comportement du Minimax


fonction Minimax_Difficulté(grille_simulée, joueur, reflexion_de_difficulé)  # une fonction qui prends 3 parametres
    
                                                                             
    si victoire_detectée(grille_simulée) alors                               # Vérifier s’il y a un gagnant comme ma fonction victory()
                                                                             
        retourner score_selon_vainqueur
    
   
    si toutes_cases_remplies(grille_simulée) alors                            # Si la grille est pleine → match nul
        retourner 0

    
    si difficulté == "facile" ET reflexion_de_difficulté >= 1 alors          # Limiter la profondeur selon la difficulté choisie
        retourner 0                                                          # IA ne réfléchit qu’un coup à l’avance
    si difficulté == "moyen" ET reflexion_de_difficulté >= 3 alors
        retourner 0                                                          # IA réfléchit trois coups à l’avance
                                                                             # difficulté "difficile" = pas de limite de profondeur

                                                                              # Explorer les coups possibles
    pour chaque case vide dans grille_simulée faire
       placer le symbole du joueur dans la case
        changer de joueur (O ↔ X)
        score ← Minimax_Difficulté(grille_simulée, nouveau_joueur, reflexion_de_difficukté + 1)
        annuler le coup simulé
        enregistrer le score obtenu

                                                                               # Sélectionner le meilleur score selon le joueur
    si joueur == "X" alors
        retourner le score maximal
    sinon
        retourner le score minimal
fin fonction




fonction IA_Joue()
    meilleur_score ← -infini
    meilleur_coup ← aucune_case

    pour chaque case vide dans la grille faire
        placer "X" dans la case
        score ← Minimax_Difficulté(grille, "O", reflexion_de_difficukté = 0)
        annuler le coup simulé
        si score > meilleur_score alors
            meilleur_score ← score
            meilleur_coup ← cette_case

    placer "X" dans meilleur_coup
arreter la fonction
"""