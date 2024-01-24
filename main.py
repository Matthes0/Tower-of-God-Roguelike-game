import curses
import random

import input_handler
import actors
import item
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
tower_key = 1
global win, player
turn_counter = -1
turn_list = []
spell_list = []


def main(stdscr):
    global win, player, turn_counter, turn_list
    win = curses.newwin(map_height + 2, map_width + chat_width + 1, 0, 0)
    win.keypad(True)
    curses.curs_set(1)
    # character select, there will be menu
    race = "Human"
    match race:
        case "Human":
            player = actors.Player(15, 15, "@", 'Player', 500, 20, 500, 10, 10, 5, 0)
            terrain.place_actor(player)
            warhammer = item.Warhammer()
            player.equip_weapon(warhammer)
            armor = item.LeatherArmor()
            player.equip_armor(armor)
            import magic
            spell1 = magic.Smite()
            player.known_spells.append(spell1)
            spell2 = magic.Heal()
            player.known_spells.append(spell2)
            spell3 = magic.Pyroblast()
            player.known_spells.append(spell3)
            spell4 = magic.Heroism()
            player.known_spells.append(spell4)
        case "Wraithraiser":
            pass
        case "Rashang":
            pass

    screen.update_terrain()

    while True:
        for current in turn_list:
            while current.current_turn >= 1.0:
                current.current_turn -= 1.0
                if current == player:
                    input_handler.get_input(player)
                    screen.update_chat("")
                else:
                    # y = random.randint(-1, 1)
                    # x = random.randint(-1, 1)
                    # current.move(y, x)
                    result = actors.dijkstra_pathfinding((current.x, current.y), (player.x, player.y))
                    current.move(result[1][1] - result[0][1], result[1][0] - result[0][0])
                    screen.update_chat(f"{result[0][1]},{result[0][0]}, {result[1][1]} - {result[1][0]}")
            current.current_turn += current.speed
            current.tick_temp_effects()
        turn_counter += 1
        screen.update_chat("")


curses.wrapper(main)
