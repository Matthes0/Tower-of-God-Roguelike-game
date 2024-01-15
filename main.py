import curses
import input_handler
import actors
import item
import screen
import terrain

map_height = 10
map_width = 30
chat_width = 100
terrain_map = terrain.generate_terrain(map_height, map_width)
terrain_map[4][5] = terrain.IndestructibleWall(4,5)
message_log = []
all_message_log = []
global win


def main(stdscr):
    global win
    win = curses.newwin(map_height + 1, map_width + chat_width + 1, 0, 0)
    win.keypad(True)
    curses.curs_set(1)
    player = actors.Player(5, 20, "@", 'Player', 10, 20,10, 10, 10, 10)
    terrain.place_actor(player)
    screen.calculate_circle(player,4.5)
    warhammer = item.Warhammer()
    player.equip_weapon(warhammer)
    screen.update_terrain()
    input_handler.get_input(player)


curses.wrapper(main)
