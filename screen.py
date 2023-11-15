def update_chat(message):
    import main
    if message == "":
        pass
    else:
        if len(main.message_log) == 10:
            main.message_log.pop()
            main.tmp_message_log.pop()
        main.message_log.insert(0, message)
        main.tmp_message_log_end_index += 1
        main.tmp_message_log.insert(0, message)
        main.all_message_log.insert(0, message)
    main.win.erase()
    for i in range(len(main.message_log)):
        main.win.addstr(9-i, main.map_width + 1, main.message_log[i])
    update_terrain()


def show_all_message_log(action):
    import main
    main.win.erase()

    if action == 0:
        for i in range(len(main.tmp_message_log)):
            main.win.addstr(9-i, 0, main.tmp_message_log[i])
    elif action == 1:
        if len(main.all_message_log) <= 10:
            for i in range(len(main.tmp_message_log)):
                main.win.addstr(9-i, 0, main.tmp_message_log[i])
        else:
            if len(main.all_message_log) > main.tmp_message_log_end_index - 9:
                main.tmp_message_log.pop(0)
                main.tmp_message_log.append(main.all_message_log[main.tmp_message_log_end_index - 9])
                main.tmp_message_log_end_index -= 1
                for i in range(len(main.tmp_message_log)):
                    main.win.addstr(9-i, 0, main.tmp_message_log[i])
    elif action == 2:
        if len(main.all_message_log) <= 10:
            pass
        else:
            if main.tmp_message_log_end_index < len(main.all_message_log):
                main.tmp_message_log.pop(0)
                main.tmp_message_log.insert(9, main.all_message_log.index(main.tmp_message_log_end_index + 1))
                for i in range(len(main.tmp_message_log)):
                    main.win.addstr(9-i, 0, main.tmp_message_log[i])
    main.win.refresh()
    for i in range(len(main.tmp_message_log)):
        main.tmp_message_log[i] = main.message_log[i]


def update_terrain():
    import main
    for i in range(main.map_height):
        for j in range(main.map_width):
            if main.terrain_map[i][j].actor is not None:
                main.win.addch(i, j, main.terrain_map[i][j].actor.char)
            else:
                main.win.addch(i, j, main.terrain_map[i][j].char)
    main.win.refresh()
