import curses, input_handler, actors, screen, terrain

map_height = 10
map_width = 30
chat_width = 69
terrain_map = terrain.generate_terrain(map_height, map_width)
message_log = []
statistics = []


def main(stdscr):
    win = curses.newwin(map_height + 1, map_width + chat_width + 1, 0, 0)
    win.keypad(True)
    curses.curs_set(0)
    player = actors.Player(5, 20, "@",10,10,5,5,5,5,5)
    terrain_map[5][20].actor = player
    screen.update_terrain(win, terrain_map, map_height, map_width)
    input_handler.get_input(win, player)


curses.wrapper(main)
