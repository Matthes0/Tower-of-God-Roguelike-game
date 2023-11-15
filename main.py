import curses, input_handler, actors, screen, terrain

map_height = 10
map_width = 30
chat_width = 100
terrain_map = terrain.generate_terrain(map_height, map_width)
message_log = ["0","1","2","3","4","5","6","7","8","9"]
all_message_log = ["0","1","2","3","4","5","6","7","8","9"]
tmp_message_log = ["0","1","2","3","4","5","6","7","8","9"]
tmp_message_log_end_index = 10
statistics = []
global win

def main(stdscr):
    global win
    win = curses.newwin(map_height + 1, map_width + chat_width + 1, 0, 0)
    win.keypad(True)
    curses.curs_set(0)
    player = actors.Player(5, 20, "@", 'Player', 10, 10, 5, 5, 5, 5, 5)
    terrain.place_actor(player)

    screen.update_terrain()
    input_handler.get_input(player)


curses.wrapper(main)
