def update_chat(message):
    import main
    if len(main.message_log) == 10:
        main.message_log.pop()
    main.message_log.insert(0, message)
    main.win.erase()
    for i in range(len(main.message_log)):
        main.win.addstr(i, 31, main.message_log[i])
    update_terrain()


def update_terrain():
    import main
    for i in range(main.map_height):
        for j in range(main.map_width):
            if main.terrain_map[i][j].actor is not None:
                main.win.addch(i, j, main.terrain_map[i][j].actor.char)
            else:
                main.win.addch(i, j, main.terrain_map[i][j].char)
    main.win.refresh()
