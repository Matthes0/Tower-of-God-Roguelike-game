def get_input(win, player):
    while True:
        key = win.getkey().lower()
        if key == 'q':
            player.move(win, -1, -1)
        if key == 'w':
            player.move(win, -1, 0)
        if key == 'e':
            player.move(win, -1, 1)
        if key == 'a':
            player.move(win, 0, -1)
        if key == 's':
            player.move(win, 0, 0)
        if key == 'd':
            player.move(win, 0, 1)
        if key == 'z':
            player.move(win, 1, -1)
        if key == 'x':
            player.move(win, 1, 0)
        if key == 'c':
            player.move(win, 1, 1)