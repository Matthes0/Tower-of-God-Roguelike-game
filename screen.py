import curses


def update_chat(message):
    import main
    if message == "":
        pass
    else:
        if len(main.message_log) == main.map_height:
            main.message_log.pop(0)
        main.message_log.append(message)
        main.all_message_log.append(message)
    main.win.erase()
    for i in range(len(main.message_log)):
        main.win.addstr(i, main.map_width + 1, main.message_log[i])
    update_terrain()


def show_all_message_log():
    import main
    start_idx = max(0, len(main.all_message_log) - 10)
    end_idx = len(main.all_message_log)
    while True:
        main.win.erase()
        for i in range(start_idx, end_idx):
            main.win.addstr(i - start_idx, 0, main.all_message_log[i])
        main.win.refresh()
        key = main.win.getkey().lower()
        if key == "key_down":
            if end_idx < len(main.all_message_log):
                start_idx = min(len(main.all_message_log) - 10, start_idx + 1)
                end_idx = min(len(main.all_message_log), end_idx + 1)
        elif key == "key_up":
            if start_idx > 0:
                start_idx = max(0, start_idx - 1)
                end_idx = min(len(main.all_message_log), end_idx - 1)
        else:
            update_chat("")
            break


def show_equipment(player):
    import main, string
    start_idx = 0
    end_idx = min(len(player.backpack), start_idx + 10)
    alphabet = string.ascii_letters
    while True:
        main.win.erase()
        for i in range(start_idx, end_idx):
            letter = alphabet[i % 52]
            if player.backpack[i].is_worn is False:
                main.win.addstr(i - start_idx, 0, f"({letter}) {player.backpack[i].name}")
            else:
                main.win.addstr(i - start_idx, 0, f"({letter}) (worn) {player.backpack[i].name}")
        main.win.addstr(0, 40, f"weapon: {player.get_name('weapon')}")
        main.win.addstr(1, 40, f"head: {player.get_name('head')}")
        main.win.addstr(2, 40, f"body: {player.get_name('body')}")
        main.win.addstr(3, 40, f"legs: {player.get_name('legs')}")
        main.win.addstr(4, 40, f"back: {player.get_name('back')}")
        main.win.addstr(5, 40, f"ring 1: {player.get_name('ring_1')}")
        main.win.addstr(6, 40, f"ring 2: {player.get_name('ring_2')}")
        main.win.addstr(7, 40, f"amulet: {player.get_name('amulet')}")
        main.win.refresh()
        key = main.win.getkey()
        if key in alphabet and alphabet.index(key) < len(player.backpack):
            selected_item = player.backpack[alphabet.index(key)]
            if show_item_description(selected_item):
                update_chat("")
                break
        if key == "KEY_DOWN":
            if end_idx < len(player.backpack):
                start_idx = min(start_idx + 1, len(player.backpack) - 10)
                end_idx = min(len(player.backpack), start_idx + 10)
        elif key == "KEY_UP":
            if start_idx > 0:
                start_idx = max(start_idx - 1, 0)
                end_idx = min(len(player.backpack), start_idx + 10)
        else:
            update_chat("")
            break


def show_item_description(item):
    import main, terrain
    while True:
        main.win.erase()
        main.win.addstr(0, 0, f"Type: {item.type} Name: {item.name}")
        if item.type == "weapon" or item.type == "ranged":
            main.win.addstr(1, 0, f"Base damage: {item.damage} Accuracy: {item.hit_modifier}")
        if item.type == "armor":
            main.win.addstr(1, 0, f"Soak: {item.soak} Dodge: {item.dodge}")
        if item.type == "ring":
            main.win.addstr(5, 0, "(e) equip as ring 1, (f) equip as ring 2, (d) drop")
        else:
            main.win.addstr(5, 0, "(e) equip, (d) drop")
        main.win.refresh()
        key = main.win.getkey().lower()
        if key == "d":
            if item.is_worn is True:
                if item.type == "ring":
                    if item == main.player.ring_1:
                        main.player.deequip("ring_1")
                    elif item == main.player.ring_2:
                        main.player.deequip("ring_2")
                else:
                    main.player.deequip(item.type)

            main.player.backpack.remove(item)
            terrain.place_item(item, main.player.y, main.player.x)
            return True
        elif key == "e":
            main.player.equip(item)
            return True
        elif key == "f" and item.type == "ring":
            main.player.equip(item, 1)
            return True
        break


def show_items_on_floor(player):
    import main, string
    start_idx = 0
    end_idx = min(len(main.terrain_map[player.y][player.x].items), start_idx + 10)
    alphabet = string.ascii_letters
    while True:
        main.win.erase()
        for i in range(start_idx, end_idx):
            letter = alphabet[i % 52]
            main.win.addstr(i - start_idx, 0, f"({letter}) {main.terrain_map[player.y][player.x].items[i].name}")
        main.win.refresh()
        key = main.win.getkey()
        if key in alphabet and alphabet.index(key) < len(main.terrain_map[player.y][player.x].items):
            player.pick_item(alphabet.index(key))
            if len(main.terrain_map[player.y][player.x].items) == 0:
                break
            end_idx = min(len(main.terrain_map[player.y][player.x].items), start_idx + 10)
        elif key == "KEY_DOWN":
            if end_idx < len(main.terrain_map[player.y][player.x].items):
                start_idx = min(start_idx + 1, len(main.terrain_map[player.y][player.x].items) - 10)
                end_idx = min(len(main.terrain_map[player.y][player.x].items), start_idx + 10)
        elif key == "KEY_UP":
            if start_idx > 0:
                start_idx = max(start_idx - 1, 0)
                end_idx = min(len(main.terrain_map[player.y][player.x].items), start_idx + 10)
        else:
            update_chat("")
            break
def death_screen():
    import main
    main.win.clear()
    main.win.addstr(0,0,f"Your story ends here, after {main.turn_counter} turns.")
    main.win.addstr(1,0,f"You, as a {main.race}, managed to get to level {main.player.player_level} before dying.")
    main.win.addstr(3,0,"Will you try to succeed in climbing the Tower of God again?")
    main.win.addstr(4,0,"Press any button to quit.")
    main.win.refresh()
    main.win.getkey()
    exit()
def win_screen():
    import main
    main.win.clear()
    main.win.addstr(0,0,f"Your story ends here, after {main.turn_counter} turns.")
    main.win.addstr(1,0,f"You, as a {main.race}, managed to earn the right to fulfill any of your wishes.")
    main.win.addstr(3,0,"Will you try to succeed in climbing the Tower of God again?")
    main.win.addstr(4,0,"Press any button to quit.")
    main.win.refresh()
    main.win.getkey()
    exit()



def show_spells():
    import main, string
    start_idx = 0
    end_idx = min(len(main.player.known_spells), start_idx + 10)
    alphabet = string.ascii_letters
    while True:
        main.win.erase()
        for i in range(start_idx, end_idx):
            letter = alphabet[i % 52]
            main.win.addstr(i - start_idx, 0, f"({letter}) {main.player.known_spells[i].name}")
        main.win.refresh()
        key = main.win.getkey()
        if key in alphabet and alphabet.index(key) < len(main.player.known_spells):
            if main.player.known_spells[start_idx + alphabet.index(key)].cast(main.player):
                return True
            else:
                return False
        elif key == "KEY_DOWN":
            if end_idx < len(main.player.known_spells):
                start_idx = min(start_idx + 1, len(main.player.known_spells) - 10)
                end_idx = min(len(main.player.known_spells), start_idx + 10)
        elif key == "KEY_UP":
            if start_idx > 0:
                start_idx = max(start_idx - 1, 0)
                end_idx = min(len(main.player.known_spells), start_idx + 10)
        else:
            update_chat("")
            return False

def level_up():
    import main
    if main.race == "Human":
        choices = 7
    else:
        choices = 5
    while choices > 0:
        main.win.clear()
        main.win.addstr(0, 0, f"Distribute your points. {choices} left.")
        main.win.addstr(1, 0, "(a) Strength")
        main.win.addstr(2, 0, "(b) Dexterity")
        main.win.addstr(3, 0, "(c) Intelligence")
        main.win.addstr(4, 0, "(d) Luck")
        main.win.addstr(5, 0, "(e) Curse")
        key = main.win.getkey().lower()
        match key:
            case "a":
                main.player.modify_stat("strength", 1)
                main.player.modify_stat("max_hp", 3)
                choices -= 1
            case "b":
                main.player.modify_stat("dexterity", 1)
                choices -= 1
            case "c":
                main.player.modify_stat("intelligence", 1)
                main.player.modify_stat("max_mp", 3)
                choices -= 1
            case "d":
                main.player.modify_stat("luck", 1)
                choices -= 1
            case "e":
                main.player.modify_stat("curse", 1)
                choices -= 1



def pick_race():
    import main, actors, terrain, magic, item
    main.win.addstr(0, 0, "Pick your race (press 'a', 'b', or 'c')")
    main.win.addstr(1, 0, "(a) Human")
    main.win.addstr(2, 0, "(b) Wraithraiser")
    main.win.addstr(3, 0, "(c) Rashang")
    while True:
        choice = main.win.getkey().lower()
        if choice == 'a':
            main.race = "Human"
            main.player = actors.Player(15, 15, "@", 'Player', 30, 5, 7, 7, 7, 0, 0)
            terrain.place_actor(main.player)
            main.terrain_map[main.player.y][main.player.x].items.append(item.LongSword())
            main.tower_points = 200
            main.player.known_spells.append(magic.Shoot())
            main.player.known_spells.append(magic.ThrowCrystal())

            break
        elif choice == 'b':
            main.race = "Wraithraiser"
            main.player = actors.Player(15, 15, "@", 'Player', 60, 30, 25, 25, 2, 0, 5)
            main.player.speed = 0.9
            terrain.place_actor(main.player)

            spell1 = magic.Heroism()
            main.player.known_spells.append(spell1)
            main.tower_points = 100
            break
        elif choice == 'c':
            main.race = "Rashang"
            main.player = actors.Player(15, 15, "@", 'Player', 10, 30, 5, 5, 10, 0, 0)
            terrain.place_actor(main.player)
            main.tower_points = 100
            main.player.known_spells.append(magic.Shoot())
            main.player.known_spells.append(magic.ThrowCrystal())
            main.player.known_spells.append(magic.Smite())
            main.player.known_spells.append(magic.Heal())

            # spell4 = magic.Heroism()
            # main.player.known_spells.append(spell4)
            break
def update_terrain():
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    import main
    if main.player.y - int(main.map_height / 2) < 0:
        start_y = 0
    else:
        start_y = main.player.y - int(main.map_height / 2)
    if main.player.x - int(main.map_width / 2) < 0:
        start_x = 0
    else:
        start_x = main.player.x - int(main.map_width / 2)
    if start_y + main.map_height > main.total_map_size_y:
        end_y = main.total_map_size_y
    else:
        end_y = start_y + main.map_height
    if start_x + main.map_width > main.total_map_size_x:
        end_x = main.total_map_size_x
    else:
        end_x = start_x + main.map_width
    tmp_y = -1
    for i in range(start_y, end_y):
        tmp_y += 1
        tmp_x = 0
        for j in range(start_x, end_x):
            if main.terrain_map[i][j].actor is not None:
                main.win.addch(tmp_y, tmp_x, main.terrain_map[i][j].actor.char)
            else:
                if hasattr(main.terrain_map[i][j], "items") and len(main.terrain_map[i][j].items) > 0:
                    main.win.addch(tmp_y, tmp_x, ",")
                else:
                    main.win.addch(tmp_y, tmp_x, main.terrain_map[i][j].char)
            tmp_x += 1
    main.win.addstr(main.map_height, 0,
                    f"LVL: {main.player.player_level} HP: {main.player.current_hp}/{main.player.max_hp}, MP: {main.player.current_mp}/{main.player.max_mp} TURN: {main.turn_counter} FLOOR: {main.current_level}")
    main.win.addstr(main.map_height + 1, 0,
                    f"STR: {main.player.strength} DEX: {main.player.dexterity} INT: {main.player.intelligence} LCK: {main.player.luck} CRS: {main.player.curse} SPD: {main.player.speed}")
    main.win.addstr(main.map_height + 2, 0,
                    f"DMG: {main.player.total_damage} HR: {main.player.total_hit_modifier} DODGE: {main.player.total_dodge} SOAK: {main.player.total_soak} TP: {main.tower_points}")

    main.win.refresh()
