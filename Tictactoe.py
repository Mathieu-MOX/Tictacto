# Tictacteo #12539 gagnat 1er jouer

print("Bonjour et bienvenue aux joueurs Galactiens !\n")           # to start and say hello to players

playerO = input("Qui sera le joueur O  ? ")                        # to know who's gonna be the player X so i put unput
print(playerO + " sera le joueur O")                      

playerX = input("Qui sera le joueur X ? ")                         # to know who's gonna be the player O so i put unput
print(playerX + " sera le joueur X")

print("Bienvenue à " + playerO + " et " + playerX + " !")          # to say hello to players 
# === VARIABLES===
largeur = 13                                                       # i count how many - i need 
# === FONCTION ===
def tabgrid():                                                     # i defenied my function
    nb = 0                                                         # to start 
                                                                   # start the quare 
    print("-" * largeur)                                           # first line of my square 
    for i in range(3):                                             # i start with a for here cause i know how mane case i need
        print(f"| {grid[nb]} | {grid[nb+1]} | {grid[nb+2]} |")     # defeny the the middle square 
        print("-" * largeur)                                       # the end of the square 
        nb += 3                                                    # its to add +3 at each line 
# === FONCTION ==
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
# === FONCTIONS ===
def turn():                                                        # définition correcte de la fonction
    global grid                                                     # pour pouvoir modifier la grille
    turn_count = 0                                                  # compteur de tours

    while turn_count < 9:                                           # tant qu’on n’a pas joué 9 fois
        if turn_count % 2 == 0:                                     # pair → joueur O
            currentplayer = playerO
            symbole = "O"
        else:                                                       # impair → joueur X
            currentplayer = playerX
            symbole = "X"

        print(f"C'est le tour de {currentplayer} ({symbole})")
        input_casee = input("Sur quelle case voulez-vous poser le symbole ? ")

        # vérification d’entrée
        if not input_casee.isdigit() or int(input_casee) not in range(1, 10):
            print("Entrée invalide, choisis un chiffre entre 1 et 9 !")
            continue

        input_square_int = int(input_casee)
        grid_index = input_square_int - 1

        if grid[grid_index] in ["O", "X"]:
            print("Cette case est déjà occupée, choisis-en une autre !")
            continue

        grid[grid_index] = symbole
        tabgrid()

        result = Victory()
        if result:
            print(result)
            break

        if turn_count == 8:
            print("Match NUL")
            break

        turn_count += 1                                             # on passe au tour suivant

    tabgrid()  

# === START GAME LOOP ===
while True:
    grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]            # realise new grid to change the older
    tabgrid()                                                       # i call my fonction
    turn()                                                          # start the game
    replay = input("Voulez-vous rejouer ? (o/n) ").lower()          # ask if players want to play again
    if replay != "o":
        print("Merci d'avoir joué ! À bientôt !")
        break

print("Fin de la partie !")                                         

# while dans une fonctoionn trop grande ok c'est bon regait comme demandé par valentin
# #variable globa ou import --- ensuite declaration fonction --- ensuite le code sauvage je pense que OK