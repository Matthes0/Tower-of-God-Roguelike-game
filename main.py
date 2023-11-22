import curses
import input_handler
import actors
import screen
import terrain

map_height = 10
map_width = 30
chat_width = 100
terrain_map = terrain.generate_terrain(map_height, map_width)
message_log = []
all_message_log = []
global win


def main(stdscr):
    print("hello world")
    global win
    win = curses.newwin(map_height + 1, map_width + chat_width + 1, 0, 0)
    win.keypad(True)
    curses.curs_set(0)
    player = actors.Player(5, 20, "@", 'Player', 10, 3, 3, 3, 0)
    terrain.place_actor(player)

    screen.update_terrain()
    input_handler.get_input(player)


curses.wrapper(main)
