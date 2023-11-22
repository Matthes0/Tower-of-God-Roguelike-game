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

def update_terrain():
    import main
    for i in range(main.map_height):
        for j in range(main.map_width):
            if main.terrain_map[i][j].actor is not None:
                main.win.addch(i, j, main.terrain_map[i][j].actor.char)
            else:
                if hasattr(main.terrain_map[i][j], "items") and len(main.terrain_map[i][j].items) > 0:
                   main.win.addch(i, j, ",")
                else:
                    main.win.addch(i, j, main.terrain_map[i][j].char)
    main.win.refresh()
