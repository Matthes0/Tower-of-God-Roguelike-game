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
            break
        if key == 'w':
            player.move(-1, 0)
            break
        if key == 'e':
            player.move(-1, 1)
            break
        if key == 'a':
            player.move(0, -1)
            break
        if key == 's':
            player.move(0, 0)
            break
        if key == 'd':
            player.move(0, 1)
            break
        if key == 'z':
            player.move(1, -1)
            break
        if key == 'x':
            player.move(1, 0)
            break
        if key == 'c':
            player.move(1, 1)
            break
        if key == 'i':
            screen.show_equipment(player)
        if key == 'l':
            if len(main.turn_list) > 1:
                break
            else:
                screen.update_chat(f"{player.y}, {player.x}")
                if main.terrain_map[player.y][player.x].name == "Upstairs":
                    main.terrain_map[player.y][player.x].actor = None
                    if main.terrain_map[player.y][player.x].level >= len(main.tower_of_beginning):
                        main.tower_of_beginning.append(terrain.generate_terrain(50,50,"1",main.terrain_map[player.y][player.x].level+1))
                    main.terrain_map = main.tower_of_beginning[main.terrain_map[player.y][player.x].level]
                    for i in range(0,main.total_map_size_y-1):
                        for j in range(0,main.total_map_size_x-1):
                            if main.terrain_map[i][j].name == "Downstairs":
                                player.y = i
                                player.x = j
                                break
                    main.current_level = main.terrain_map[player.y][player.x].level
                    main.terrain_map[player.y][player.x].actor = player
                    screen.update_chat("")
                    break
                if main.terrain_map[player.y][player.x].name == "Downstairs":
                    main.terrain_map[player.y][player.x].actor = None
                    if main.terrain_map[player.y][player.x].level == 1:
                        main.terrain_map = main.lobby
                    else:
                        main.terrain_map = main.tower_of_beginning[main.terrain_map[player.y][player.x].level-2]
                    for i in range(0,main.total_map_size_y-1):
                        for j in range(0,main.total_map_size_x-1):
                            if main.terrain_map[i][j].name == "Upstairs":
                                player.y = i
                                player.x = j
                                break
                    main.current_level = main.terrain_map[player.y][player.x].level
                    main.terrain_map[player.y][player.x].actor = player
                    screen.update_chat("")
            break
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
                    human = actors.HumanWithLeatherArmorAndLongsword(1, 4)
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
                    sword = item.Item(5, 10, "Sword")
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
            break
        if key == 'v':
            screen.show_spells(player)
            break


def targetting(player, mode="single"):
    import main, screen
    screen.update_chat("")
    tmp_y = player.y
    tmp_x = player.x
    real_y = player.y
    real_x = player.x
    if tmp_y > int(main.map_height/2):
        offset = tmp_y - int(main.map_height/2)
        tmp_y -= offset
    if tmp_x > int(main.map_width/2):
        offset = tmp_x - int(main.map_width/2)
        tmp_x -= offset

    main.win.move(tmp_y, tmp_x)
    while True:
        key = main.win.getkey().lower()
        if key == 'q':
            if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x - 1 < main.map_width and 0 <= real_y - 1 < main.total_map_size_y and 0 <= real_x - 1 < main.total_map_size_x:
                tmp_y -= 1
                tmp_x -= 1
                real_y -= 1
                real_x -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == 'w':
            if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x < main.map_width and 0 <= real_y - 1 < main.total_map_size_y and 0 <= real_x < main.total_map_size_x:
                tmp_y -= 1
                real_y -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == 'e':
            if 0 <= tmp_y - 1 < main.map_height and 0 <= tmp_x + 1 < main.map_width and 0 <= real_y - 1 < main.total_map_size_y and 0 <= real_x + 1 < main.total_map_size_x:
                tmp_y -= 1
                tmp_x += 1
                real_y -= 1
                real_x += 1
                main.win.move(tmp_y, tmp_x)
        elif key == 'a':
            if 0 <= tmp_y < main.map_height and 0 <= tmp_x - 1 < main.map_width and 0 <= real_y < main.total_map_size_y and 0 <= real_x - 1 < main.total_map_size_x:
                tmp_x -= 1
                real_x -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == 's':
            tmp_y -= 0
            tmp_x -= 0
            main.win.move(tmp_y, tmp_x)
        elif key == 'd':
            if 0 <= tmp_y < main.map_height and 0 <= tmp_x + 1 < main.map_width and 0 <= real_y < main.total_map_size_y and 0 <= real_x + 1 < main.total_map_size_x:
                tmp_x += 1
                real_x += 1
                main.win.move(tmp_y, tmp_x)
        elif key == 'z':
            if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x - 1 < main.map_width and 0 <= real_y + 1 < main.total_map_size_y and 0 <= real_x - 1 < main.total_map_size_x:
                tmp_y += 1
                tmp_x -= 1
                real_y += 1
                real_x -= 1
                main.win.move(tmp_y, tmp_x)
        elif key == 'x':
            if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x < main.map_width and 0 <= real_y + 1 < main.total_map_size_y and 0 <= real_x < main.total_map_size_x:
                tmp_y += 1
                real_y += 1
                main.win.move(tmp_y, tmp_x)
        elif key == 'c':
            if 0 <= tmp_y + 1 < main.map_height and 0 <= tmp_x + 1 < main.map_width and 0 <= real_y + 1 < main.total_map_size_y and 0 <= real_x + 1 < main.total_map_size_x:
                tmp_y += 1
                tmp_x += 1
                real_y += 1
                real_x += 1
                main.win.move(tmp_y, tmp_x)
        elif key == '\n':
            match mode:
                case "single":
                    if main.terrain_map[real_y][real_x].actor is not None:
                        return main.terrain_map[real_y][real_x].actor
                    else:
                        screen.update_chat("You didn't target enemy.")
                        break
                case "aoe":
                    actors_list = []
                    for i in range(real_y-1, real_y+1):
                        for j in range(real_x-1, real_x+1):
                            if 0 < real_y < main.total_map_size_y and 0 < real_x < main.total_map_size_x:
                                if main.terrain_map[i][j].actor is not None:
                                    actors_list.append(main.terrain_map[i][j].actor)
                    return actors_list

        else:
            # screen.update_chat(key)
            screen.update_chat("")
            break
