import curses
import random
import input_handler
import actors
import screen
import terrain

map_height = 13
map_width = 26
chat_width = 100
total_map_size_y = 50
total_map_size_x = 50
lobby = terrain.generate_terrain(total_map_size_y, total_map_size_x, "lobby")
terrain_map = lobby
tower_of_beginning = []
tower_of_trials = []
tower_of_god = []
message_log = []
current_level = 0
all_message_log = []
tower_key = 0
tower_points = 0
global win, player, race, gain_level
turn_counter = -1
turn_list = []


def main(stdscr):
    global win, player, turn_counter, turn_list, race, gain_level
    win = curses.newwin(map_height + 3, map_width + chat_width + 1, 0, 0)
    win.keypad(True)
    curses.curs_set(1)
    screen.pick_race()
    gain_level = False
    screen.update_chat("")
    while True:
        for current in turn_list:
            while current.current_turn >= 1.0:
                current.current_turn -= 1.0
                if current == player:
                    input_handler.get_input(player)
                    screen.update_chat("")
                    if gain_level:
                        if len(turn_list) == 1:
                            screen.level_up()
                            gain_level = False
                            screen.update_chat("")
                else:
                    result = actors.dijkstra_pathfinding((current.x, current.y), (player.x, player.y))
                    if len(result) < 10 and result is not None:
                        current.move(result[1][1] - result[0][1], result[1][0] - result[0][0])
                        # screen.update_chat(f"{result[0][1]},{result[0][0]}, {result[1][1]} - {result[1][0]}")
                    else:
                        y = random.randint(-1, 1)
                        x = random.randint(-1, 1)
                        current.move(y, x)
            current.current_turn += current.speed
            current.tick_temp_effects()
        turn_counter += 1
        screen.update_chat("")


curses.wrapper(main)
