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
        if key == "t":
            import tests
            key = main.win.getkey().lower()
            if key == "1":
                tests.can_place_actor(5, 20)
                tests.can_place_actor(100, 10)
                tests.can_place_actor(10, 20)
                tests.can_place_actor(0, 0)
                tests.can_place_actor(4, 20)
            if key == "2":
                if tests.can_place_actor(1,4) == 1:
                    human = actors.Human(1,4)
                    terrain.place_actor(human)
                if tests.can_place_actor(100,100) == 1:
                    human = actors.Human(100,100)
                    terrain.place_actor(human)
                if tests.can_place_actor(2,7) == 1:
                    dog = actors.Dog(2,7)
                    terrain.place_actor(dog)
            if key == "3":
                if tests.can_place_actor(2,7) == 2:
                    terrain.delete_actor(2, 7)
                if tests.can_place_actor(100,7) == 2:
                    terrain.delete_actor(100, 7)
            if key == "4":
                pass
        if key == "m":
            screen.show_all_message_log(0)
            key = ""
            while key != "m":
                key = main.win.getkey().lower()
                if key == "w":
                    screen.show_all_message_log(1)
                elif key == "x":
                    screen.show_all_message_log(2)
            screen.update_chat("")

