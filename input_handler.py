import curses

import actors
import screen
import terrain


def get_input(player):
    import main
    while True:
        key = main.win.getkey().lower()
        if key == 'q':
            player.move(-1, -1)
        if key == 'w':
            player.move(-1, 0)
        if key == 'e':
            player.move(-1, 1)
        if key == 'a':
            player.move(0, -1)
        if key == 's':
            player.move(0, 0)
        if key == 'd':
            player.move(0, 1)
        if key == 'z':
            player.move(1, -1)
        if key == 'x':
            player.move(1, 0)
        if key == 'c':
            player.move(1, 1)
        if key == 'i':
            screen.show_equipment(player)
        if key == "t":
            key = main.win.getkey().lower()
            if key == "1":
                terrain.can_place_actor(5, 20)
                terrain.can_place_actor(100, 10)
                terrain.can_place_actor(10, 20)
                terrain.can_place_actor(0, 0)
                terrain.can_place_actor(4, 20)
            if key == "2":
                if terrain.can_place_actor(1, 4) == 1:
                    human = actors.Human(1, 4)
                    terrain.place_actor(human)
                if terrain.can_place_actor(100, 100) == 1:
                    human = actors.Human(100, 100)
                    terrain.place_actor(human)
                if terrain.can_place_actor(2, 7) == 1:
                    dog = actors.Dog(2, 7)
                    terrain.place_actor(dog)
            if key == "3":
                if terrain.can_place_actor(2, 7) == 2:
                    terrain.delete_actor(2, 7)
                if terrain.can_place_actor(100, 7) == 2:
                    terrain.delete_actor(100, 7)
            if key == "4":
                terrain.can_place_item(5, 10)
                terrain.can_place_item(100, 100)
            if key == "5":
                if terrain.can_place_item(5, 10) == 1:
                    import item
                    sword = item.Item(True, 5, 10, "Sword")
                    terrain.place_item(sword)
            if key == "6":
                if hasattr(main.terrain_map[5][10], "items") and len(main.terrain_map[5][10].items) > 0:
                    terrain.delete_item(5, 10)
            if key == "7":
                terrain.print_actors_and_items()
        if key == "m":
            screen.show_all_message_log()
        if key == ',':
            player.pick_item()
        if key == 'v':
            import main
            tmp_y = player.y
            tmp_x = player.x
            main.win.move(player.y, player.x)
            while True:
                key = main.win.getkey().lower()
                if key == 'q':
                    if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x - 1 < main.map_width:
                        tmp_y -= 1
                        tmp_x -= 1
                        main.win.move(tmp_y, tmp_x)
                elif key == 'w':
                    if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x < main.map_width:
                        tmp_y -= 1
                        main.win.move(tmp_y, tmp_x)
                elif key == 'e':
                    if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x + 1 < main.map_width:
                        tmp_y -= 1
                        tmp_x += 1
                        main.win.move(tmp_y, tmp_x)
                elif key == 'a':
                    if 0 <= tmp_y < main.map_height and 0 <= tmp_x - 1 < main.map_width:
                        tmp_x -= 1
                        main.win.move(tmp_y, tmp_x)
                elif key == 's':
                    tmp_y -= 0
                    tmp_x -= 0
                    main.win.move(tmp_y, tmp_x)
                elif key == 'd':
                    if 0 <= tmp_y < main.map_height and 0 <= tmp_x + 1 < main.map_width:
                        tmp_x += 1
                        main.win.move(tmp_y, tmp_x)
                elif key == 'z':
                    if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x - 1 < main.map_width:
                        tmp_y += 1
                        tmp_x -= 1
                        main.win.move(tmp_y, tmp_x)
                elif key == 'x':
                    if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x < main.map_width:
                        tmp_y += 1
                        tmp_x -= 0
                        main.win.move(tmp_y, tmp_x)
                elif key == 'c':
                    if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x + 1 < main.map_width:
                        tmp_y += 1
                        tmp_x += 1
                        main.win.move(tmp_y, tmp_x)
                else:
                    screen.update_chat("")
                    break
