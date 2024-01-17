
def update_chat(message):
    import main
    if message == "":
        pass
    else:
        if len(main.message_log) == 10:
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
        if key == "x":
            if end_idx < len(main.all_message_log):
                start_idx = min(len(main.all_message_log) - 10, start_idx + 1)
                end_idx = min(len(main.all_message_log), end_idx + 1)
        elif key == "w":
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
        main.win.addstr(4, 30, f"hands: {player.get_name('hands')}")
        main.win.addstr(5, 30, f"legs: {player.get_name('legs')}")
        main.win.addstr(6, 30, f"back: {player.get_name('back')}")
        main.win.addstr(7, 30, f"ring 1: {player.get_name('ring_1')}")
        main.win.addstr(8, 30, f"ring 2: {player.get_name('ring_2')}")
        main.win.addstr(9, 30, f"neck: {player.get_name('neck')}")
        main.win.refresh()
        key = main.win.getkey().lower()

        if key == "x":
            start_idx = min(start_idx + 1, len(player.backpack) - 10)
            end_idx = min(len(player.backpack), start_idx + 10)
        elif key == "w":
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
        if key == "a":
            player.known_spells[0].cast(player)
            break
        elif key == "b":
            player.known_spells[1].cast(player)
            break
        elif key == "c":
            player.known_spells[2].cast(player)
            break
        else:
            update_chat("")
            break
def update_terrain():
    import main
    for i in range(main.map_height):
        for j in range(main.map_width):
            if main.terrain_map[i][j].visible is False:
                main.win.addch(i, j, ' ')
            else:
                if main.terrain_map[i][j].actor is not None:
                    main.win.addch(i, j, main.terrain_map[i][j].actor.char)
                else:
                    if hasattr(main.terrain_map[i][j], "items") and len(main.terrain_map[i][j].items) > 0:
                        main.win.addch(i, j, ",")
                    else:
                        main.win.addch(i, j, main.terrain_map[i][j].char)
    main.win.addstr(main.map_height, 0, f"LVL: XD HP: {main.player.current_hp}/{main.player.current_hp}, MP: {main.player.current_mp}/{main.player.max_mp} TURN: {main.turn_counter}")
    main.win.addstr(main.map_height + 1, 0, f"STR: {main.player.strength} DEX: {main.player.dexterity} INT: {main.player.intelligence} LCK: {main.player.luck} CRS: {main.player.curse}")
    main.win.refresh()
