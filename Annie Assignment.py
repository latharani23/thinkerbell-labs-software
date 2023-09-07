import random

# these are constants representing the different elements in the game
EMPTY = '-' 
RABBIT = 'r'
RABBIT_HOLDING_CARROT = 'R'
CARROT = 'c'
RABBIT_HOLE = 'O'

# Function to generate a random map
def generate_random_map(size, num_carrots, num_holes):
    # Create an empty map
    game_map = [[EMPTY for _ in range(size)] for _ in range(size)]

    # Place rabbit randomly
    rabbit_x, rabbit_y = random.randint(0, size - 1), random.randint(0, size - 1)
    game_map[rabbit_x][rabbit_y] = RABBIT

    # Place carrots randomly
    for _ in range(num_carrots):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if game_map[x][y] == EMPTY:
                game_map[x][y] = CARROT
                break

    # Place rabbit holes randomly
    for _ in range(num_holes):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if game_map[x][y] == EMPTY:
                game_map[x][y] = RABBIT_HOLE
                break

    return game_map, rabbit_x, rabbit_y

# Function to display the map This function displays the current state of the game map on the command line.
def display_map(game_map):
    for row in game_map:
        print(" ".join(row))

# Function to check  rabbit picked up the carrot 
def is_game_won(game_map):
    for row in game_map:
        if CARROT in row:
            return False
    return True

# Function to play the game
def play_game(size, num_carrots, num_holes):
    game_map, rabbit_x, rabbit_y = generate_random_map(size, num_carrots, num_holes)
    holding_carrot = False

    while not is_game_won(game_map):
        display_map(game_map)
        move = input("Enter move (a/d/w/s/p/j/q): ").lower()

        if move == 'q':   #quit
            break

        x, y = rabbit_x, rabbit_y

        if move == 'a':  #left
            y -= 1
        elif move == 'd':   #right
            y += 1
        elif move == 'w':    #up
            x -= 1
        elif move == 's':    #down
            x += 1
        elif move == 'p':     #pick up carrot
            if game_map[x][y] == CARROT:
                game_map[x][y] = EMPTY
                holding_carrot = True
        elif move == 'j':      #jump over rabit holes
            if game_map[x][y] == RABBIT_HOLE:
                game_map[x][y] = EMPTY
                if rabbit_x < x:
                    x += 1
                elif rabbit_x > x:
                    x -= 1
                elif rabbit_y < y:
                    y += 1
                else:
                    y -= 1

        if 0 <= x < size and 0 <= y < size:
            if holding_carrot:
                game_map[rabbit_x][rabbit_y] = EMPTY
                rabbit_x, rabbit_y = x, y
                game_map[rabbit_x][rabbit_y] = RABBIT_HOLDING_CARROT
            elif game_map[x][y] != RABBIT_HOLE:
                game_map[rabbit_x][rabbit_y] = EMPTY
                rabbit_x, rabbit_y = x, y
                game_map[rabbit_x][rabbit_y] = RABBIT

    if is_game_won(game_map):
        print("Rabbit has picked up the carrot")

if __name__ == "__main__":               
    size = int(input("Enter the size of the map: "))  #It takes user input for the size of the map.
    num_carrots = int(input("Enter the number of carrots: "))   #It takes user input for the number of carrots.
    num_holes = int(input("Enter the number of rabbit holes: "))  #It takes user input for  the number of rabbit holes.
    play_game(size, num_carrots, num_holes)  # it calls the play_game function to start the game.
