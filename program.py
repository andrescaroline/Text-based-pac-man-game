from main import play, move_ghosts
from ui import wi_print, ui_key, ui_msg_lost, ui_msg_win

# @ -> Our hero
# G -> Ghosts
# P -> Pills
# . -> Empty spaces
# | and - -> Walls

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]

game_finished = False

while not game_finished:
    wi_print(map)
    key = ui_key()
    valid_key, pac_alive, won = play(map, key)

    pac_was_hit = move_ghosts(map)

    if (not pac_alive) or (pac_was_hit):
       ui_msg_lost()
       game_finished = True

    elif won:
       ui_msg_win()
       game_finished = True


