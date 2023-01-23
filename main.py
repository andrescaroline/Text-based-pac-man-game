


import random



# current location of the pac.
def find_pac(map):
    pac_x = -1
    pac_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pac_x = x
                pac_y = y
    return pac_x, pac_y





def move_pac(map, next_pac_x, next_pac_y):

    pac_x, pac_y = find_pac(map)
    # the place where the pacman was is now empty
   

    everything_to_the_left = map[pac_x][0:pac_y]
    everything_to_the_right = map[pac_x][pac_y+1:]
    map[pac_x] = everything_to_the_left + "." + everything_to_the_right

    # the new place has the pacman
    everything_to_the_left = map[next_pac_x][0:next_pac_y]
    everything_to_the_right = map[next_pac_x][next_pac_y+1:]
    map[next_pac_x] = everything_to_the_left + "@" + everything_to_the_right

# this function returns two booleans
# the first indicates whether the pressed key was a valid key
# the second indicates whether the pacman is still alive
# the third indicates whether the pacman won the game

def play(map, key):
    next_x, next_y = next_position(map, key)

    # if it is a invalid key
    is_an_invalid_key = next_x == -1 and next_y == -1
    if is_an_invalid_key:
        return False, True, False

    # if it is not within borders
    if not within_borders(map, next_x, next_y):
        return False, True, False

    # if it is a wall
    if is_a_wall(map, next_x, next_y):
        return False, True, False

    is_a_ghost = map[next_x][next_y] == 'G'
    if is_a_ghost:
        return True, False, False

    move_pac(map, next_x, next_y)

    remaining_pills = total_pills(map)
    if remaining_pills == 0:
        return True, True, True
    else:
        return True, True, False



def is_a_wall(map, next_x, next_y):
    is_a_wall = map[next_x][next_y] == '|' or map[next_x][next_y] == '-'
    return is_a_wall

def is_a_ghost(map, next_x, next_y):
    return map[next_x][next_y] == 'G'

def is_a_pill(map, next_x, next_y):
    return map[next_x][next_y] == 'P'

def is_pac(map, next_x, next_y):
    return map[next_x][next_y] == '@'




def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows

    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns

    return x_is_valid and y_is_valid 

# total of pills
def total_pills(map):
    count = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                count += 1
    return count


def next_position(map, key):
    x, y = find_pac(map) # with current location, we can define your destination.
    next_x = -1
    next_y = -1

    if key == 'a': # move to the left
        next_x = x  # keep the pac in the same row
        next_y = y - 1
    elif key == 'd': 
        next_x = x
        next_y = y + 1 # move to the right
    elif key == 'w':
        next_x = x - 1 # up
        next_y = y # keep the pac in the same column
    elif key == 's':
        next_x = x + 1 # down
        next_y = y

    return next_x, next_y

def find_ghosts(map):
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "G":
               all_ghosts.append([x,y])
    return all_ghosts

def move_ghosts(map):
    all_ghosts = find_ghosts(map)

    for ghost in all_ghosts:
        ghosts_x = ghost[0]
        ghosts_y = ghost[1]

        possible_directions = [
            [ghosts_x, ghosts_y + 1],
            [ghosts_x, ghosts_y - 1],
            [ghosts_x - 1, ghosts_y], #up
            [ghosts_x + 1, ghosts_y] #down
        ]

        # select a random possible movement
        # and get the x,y of the movement

        random_number = random.randint(0,3)
        next_ghost_x = possible_directions[random_number][0]
        next_ghost_y = possible_directions[random_number][1]

        # checks before actually moving it!
        if not within_borders(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_wall(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_ghost(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_pill(map, next_ghost_x, next_ghost_y):
            continue

        if is_pac(map, next_ghost_x, next_ghost_y):
            return True

        # move the ghost to the random position
        everything_to_the_left = map[ghosts_x][0:ghosts_y]
        everything_to_the_right = map[ghosts_x][ghosts_y +1:]
        map[ghosts_x] = everything_to_the_left + "." + everything_to_the_right

        # the new place has the pacman
        everything_to_the_left = map[next_ghost_x][0:next_ghost_y]
        everything_to_the_right = map[next_ghost_x][next_ghost_y + 1:]
        map[next_ghost_x] = everything_to_the_left + "G" + everything_to_the_right

    return False















