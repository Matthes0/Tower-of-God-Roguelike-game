def update_chat(win, message):
    import main

    if len(main.message_log) == 10:
        main.message_log.pop()
    main.message_log.insert(0, message)
    win.erase()
    for i in range(len(main.message_log)):
        win.addstr(i, 31, main.message_log[i])
    update_terrain(win, main.terrain_map, main.map_height, main.map_width)


def update_terrain(win, terrain_map, map_height, map_width):
    for i in range(map_height):
        for j in range(map_width):
            if terrain_map[i][j].actor is not None:
                win.addch(i, j, terrain_map[i][j].actor.char)
            else:
                win.addch(i, j, terrain_map[i][j].char)
    win.refresh()
