# Tictacteo

print("Bonjour et bienvenue aux joueurs Galactiens !\n")           # to start and say hello to players

playerO = input("Qui sera le joueur O  ? ")                        # to know who's gonna be the player X so i put unput
print(playerO + " sera le joueur O")                      

playerX = input("Qui sera le joueur X ? ")                         # to know who's gonna be the player O so i put unput
print(playerX + " sera le joueur X")

print("Bienvenue à " + playerO + " et " + playerX + " !")          # to say hello to players 

grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]               # realise my grid 
largeur = 13                                                       # i count how many - i need 


def tabgrid():                                                     # i defenied my function
    nb = 0                                                         # to start 
                                                                   # start the quare 
    print("-" * largeur)                                           # first line of my square 
    for i in range(3):                                             # i start with a for here cause i know how mane case i need
        print(f"| {grid[nb]} | {grid[nb+1]} | {grid[nb+2]} |")     # defeny the the middle square 
        print("-" * largeur)                                       # the end of the square 
        nb += 3                                                    # its to add +3 at each line 

tabgrid()                                                          # i call my fonction

def Victory():
    # Line
    if grid[0] == grid[1] == grid[2]:
        return f"Bravo {playerO if grid[0]=='O' else playerX} ! Tu as gagné!"
    if grid[3] == grid[4] == grid[5]:
        return f"Bravo {playerO if grid[3]=='O' else playerX} ! Tu as gagné!"
    if grid[6] == grid[7] == grid[8]:
        return f"Bravo {playerO if grid[6]=='O' else playerX} ! Tu as gagné!"

    # Column
    if grid[0] == grid[3] == grid[6]:
        return f"Bravo {playerO if grid[0]=='O' else playerX} ! Tu as gagné!"
    if grid[1] == grid[4] == grid[7]:
        return f"Bravo {playerO if grid[1]=='O' else playerX} ! Tu as gagné!"
    if grid[2] == grid[5] == grid[8]:
        return f"Bravo {playerO if grid[2]=='O' else playerX} ! Tu as gagné!"

    # Diagonals
    if grid[0] == grid[4] == grid[8]:
        return f"Bravo {playerO if grid[0]=='O' else playerX} ! Tu as gagné!"
    if grid[2] == grid[4] == grid[6]:
        return f"Bravo {playerO if grid[2]=='O' else playerX} ! Tu as gagné!"

    return None                                                                              


# starting counting truns

turn = 0                                                           # stratingt my count 

while turn < 9:                                                    # while we didnt do 9 loop

    if turn % 2 == 0:                                              # determinate who's gonna play even and odd
        currentplayer = playerO                                    # if the turn is even (0, 2, 4…), it's t playerO who play
        symbole = "O"                                              # determinate what symbole's gonna have  the player
    else:                                                          # else if the turn is odd(1,3,5..), it's playerX
        currentplayer = playerX                                    # determinate what symbol's goonna have the player
        symbole = "X"

    print(f"C'est le tour de {currentplayer} ({symbole})")         # print who has to play with the symbol
    
    input_casee = input("Sur quelle case voulez-vous poser le symbole ? ")

    input_square_int = int(input_casee)                             # that transform a str to a int
    grid_index = input_square_int - 1    
    
    if grid[grid_index] in ["O", "X"]:                              # Verify in the grid if there is already a symbol
       print("Cette case est déjà occupée, choisis-en une autre !") # print error
       continue                                                     # else continue to play

    
    
                                                                    # the player chosse a number bettween 1 to 9, grid - 1 cause 
    grid[grid_index] = symbole                                      # upgraded the grid, change the number to the symbol.

    tabgrid()  
    
    result = Victory()                                              # Verify if the a winner
    if result:
        print(result)
        break
    if turn == 8:                                                   # condition to add 'match nul'
        print("Match NUL")
        break

    

    turn = turn + 1                                                 # go up to start tto count the turn

print("Fin de la partie !")                                         


    
     