import secrets

# Maze dimensions
MAZE_WIDTH = 10
MAZE_HEIGHT = 10

# Maze symbols
WALL = '#'
EMPTY = ' '
PLAYER = 'P'
EXIT = 'E'
ITEM = '*'

# Score
score = 0 

# Function to initialize the maze
def initialize_maze():
    maze = [[EMPTY] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]
    # Place walls
    for i in range(MAZE_HEIGHT):
        maze[i][0] = WALL
        maze[i][-1] = WALL
    for j in range(MAZE_WIDTH):
        maze[0][j] = WALL
        maze[-1][j] = WALL
    # Place player
    maze[1][1] = PLAYER
    # Place exit
    maze[MAZE_HEIGHT - 2][MAZE_WIDTH - 2] = EXIT
    # Place items randomly
    for _ in range(3):  # Adjust the number of items as needed
        while True:
            x = secrets.SystemRandom().randint(1, MAZE_WIDTH - 2)
            y = secrets.SystemRandom().randint(1, MAZE_HEIGHT - 2)
            if maze[y][x] == EMPTY:
                maze[y][x] = ITEM
                break
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))

# Function to move the player
def move_player(maze, direction, score):
    player_pos = find_player(maze)
    new_pos = (player_pos[0] + direction[0], player_pos[1] + direction[1])
    if maze[new_pos[0]][new_pos[1]] != WALL:
        if maze[new_pos[0]][new_pos[1]] == ITEM:
            print("Item collected!")
            score += 1  # Increment score for item collection
        maze[player_pos[0]][player_pos[1]] = EMPTY
        maze[new_pos[0]][new_pos[1]] = PLAYER
        if new_pos == (MAZE_HEIGHT - 2, MAZE_WIDTH - 2):  # Check if the new position is the exit
            return "EXIT", score
        return True, score
    return False, score

# Function to find the player's position
def find_player(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == PLAYER:
                return (i, j)

# Main function to run the game with item collection scoring
def main():
    maze = initialize_maze()
    score = 0  # Initialize the score for the game
    print("Welcome to the maze game!")
    print("Use WASD to move. Try to find the exit (E) while collecting items (*) for points!")
    while True:
        print_maze(maze)
        direction = input("Enter your move (WASD): ").upper()
        if direction == 'W':
            moved, score = move_player(maze, (-1, 0), score)
        elif direction == 'S':
            moved, score = move_player(maze, (1, 0), score)
        elif direction == 'A':
            moved, score = move_player(maze, (0, -1), score)
        elif direction == 'D':
            moved, score = move_player(maze, (0, 1), score)
        else:
            print("Invalid move! Use WASD.")
            continue
        if not moved:
            print("Cannot move there! Try another direction.")
        else:
            if moved == "EXIT":
                print(f"Congratulations! You found the exit with a score of {score}!")
                break

if __name__ == "__main__":
    main()
