import curses
import random

import input_handler
import actors
import item
import screen
import terrain

map_height = 10
map_width = 30
chat_width = 100
terrain_map = terrain.generate_terrain(map_height, map_width)
terrain_map[4][5] = terrain.IndestructibleWall(4, 5)
message_log = []
all_message_log = []
global win, player
turn_counter = 0
turn_list = []
spell_list = []

def main(stdscr):
    global win, player, turn_counter, turn_list
    win = curses.newwin(map_height + 5, map_width + chat_width + 1, 0, 0)
    win.keypad(True)
    curses.curs_set(1)
    # character select, there will be menu
    race = "Human"
    match race:
        case "Human":
            player = actors.Player(5, 20, "@", 'Player', 500, 20, 10, 10, 10, 10, 10)
            terrain.place_actor(player)
        case "Wraithraiser":
            pass
        case "Rashang":
            pass

    dotestow = actors.HumanWithLeatherArmorAndLongsword(3, 19)
    terrain.place_actor(dotestow)
    # dotestow = actors.HumanWithLeatherArmorAndLongsword(2, 15)
    # terrain.place_actor(dotestow)
    screen.calculate_circle(player, 4.5)
    warhammer = item.Warhammer()
    player.equip_weapon(warhammer)
    armor = item.LeatherArmor()
    player.equip_armor(armor)
    screen.update_terrain()

    while True:
        for current in turn_list:
            while current.current_turn >= 1.0:
                current.current_turn -= 1.0
                if current == player:
                    input_handler.get_input(player)
                else:
                    y = random.randint(-1, 1)
                    x = random.randint(-1, 1)
                    current.move(y, x)
            current.current_turn += current.speed
            current.tick_temp_effects()
            if current == player:
                turn_counter += 1


curses.wrapper(main)
