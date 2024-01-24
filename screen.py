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

def in_circle(actor, y, x, radius):
    import math
    dy = actor.y - y
    dx = actor.x - x
    dist = dx *dx + dy *dy
    return dist <= radius * radius


def calculate_circle(actor, radius):
    import math, main
    top = math.ceil(actor.y - radius)
    bottom = math.floor(actor.y + radius)
    left = math.ceil(actor.x - radius)
    right = math.floor(actor.x + radius)
    for i in range(0, main.map_height):
        for j in range(0, main.map_width):
            main.terrain_map[i][j].visible = False
    for i in range(top, bottom +1):
        for j in range(left, right +1):
            if 0 <= i < main.map_height and 0 <= j < main.map_width and in_circle(actor, i, j, radius):
                main.terrain_map[i][j].visible = True

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
    alphabet = string.ascii_lowercase
    while True:
        main.win.erase()
        for i in range(start_idx, end_idx):
            letter = alphabet[i % 26]
            main.win.addstr(i - start_idx, 0, f"({letter}) {player.backpack[i].name}")
        main.win.addstr(0, 30, f"left hand: {player.get_name('left_hand')}")
        main.win.addstr(1, 30, f"right hand: {player.get_name('right_hand')}")
        main.win.addstr(2, 30, f"head: {player.get_name('head')}")
        main.win.addstr(3, 30, f"body: {player.get_name('body')}")
        main.win.addstr(4, 30, f"legs: {player.get_name('legs')}")
        main.win.addstr(5, 30, f"back: {player.get_name('back')}")
        main.win.addstr(6, 30, f"ring 1: {player.get_name('ring_1')}")
        main.win.addstr(7, 30, f"ring 2: {player.get_name('ring_2')}")
        main.win.addstr(8, 30, f"neck: {player.get_name('neck')}")
        main.win.refresh()
        key = main.win.getkey().lower()
        if key in alphabet and alphabet.index(key) < len(player.backpack):
            selected_item = player.backpack[start_idx + alphabet.index(key)]
            update_chat(f"{selected_item.name}")
        if key == "key_down":
            start_idx = min(start_idx + 1, len(player.backpack) - 10)
            end_idx = min(len(player.backpack), start_idx + 10)
        elif key == "key_up":
            start_idx = max(start_idx - 1, 0)
            end_idx = min(len(player.backpack), start_idx + 10)
        else:
            update_chat("")
            break

def show_spells(player):
    import main, string
    start_idx = 0
    end_idx = min(len(player.known_spells), start_idx + 10)
    alphabet = string.ascii_lowercase
    while True:
        main.win.erase()
        for i in range(start_idx, end_idx):
            letter = alphabet[i % 26]
            main.win.addstr(i - start_idx, 0, f"({letter}) {player.known_spells[i].name}")
        main.win.refresh()
        key = main.win.getkey().lower()
        if key in alphabet and alphabet.index(key) < len(player.known_spells):
            if player.known_spells[start_idx + alphabet.index(key)].cast(player):
                return True
            else:
                return False
        else:
            update_chat("")
            return False

def update_terrain():
    curses.init_pair(1,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    import main
    if main.player.y - int(main.map_height/2) < 0:
        start_y = 0
    else:
        start_y = main.player.y - int(main.map_height/2)
    if main.player.x - int(main.map_width/2) < 0:
        start_x = 0
    else:
        start_x = main.player.x - int(main.map_width/2)
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
            # if main.terrain_map[i][j].visible is False:
            #     main.win.addch(tmp_y, tmp_x, ' ')
            # else:
            if main.terrain_map[i][j].actor is not None:
                main.win.addch(tmp_y,tmp_x, main.terrain_map[i][j].actor.char)
            else:
                if hasattr(main.terrain_map[i][j], "items") and len(main.terrain_map[i][j].items) > 0:
                    main.win.addch(tmp_y,tmp_x, ",")
                else:
                    main.win.addch(tmp_y,tmp_x, main.terrain_map[i][j].char)
            tmp_x += 1
    main.win.addstr(main.map_height, 0, f"LVL: {main.current_level} HP: {main.player.current_hp}/{main.player.max_hp}, MP: {main.player.current_mp}/{main.player.max_mp} TURN: {main.turn_counter}")
    main.win.addstr(main.map_height + 1, 0, f"STR: {main.player.strength} DEX: {main.player.dexterity} INT: {main.player.intelligence} LCK: {main.player.luck} CRS: {main.player.curse}")
    main.win.refresh()
