from threading import Timer
from matplotlib.backends.backend_pdf import PdfPages
from collections import Counter
import sys
import matplotlib.pyplot as plt
import time

defusing_kits_bag = 0
bomb_count = 6
defusing_kits_locations = {"reception_desk_refrigerator": 1, "meeting_room_projector": 2, "pantry_coffee_machine": 1,
                           "library_locker": 1, "restroom_tissue_box": 1}
bomb_locations = {"reception_desk_stationary_rack": 1, "meeting_room_under_table": 1,
                  "pantry_microwave": 1, "pantry_sofa": 1, "library_book_shelf": 1, "library_printer": 1}
game_duration_in_min = 10
track_moves = []
time_spend_in_each_rooms = {"reception_cabin": 0, "meeting_room": 0, "pantry": 0, "library": 0, "restroom": 0}


def get_game_description():
    """
    Describes the game plot and what is the goal of game.
    """
    print("Save Maverick")
    print(" You are in front of the office building 'Maverick' the multinational IT company. "
          "The terrorist has planned a series of bombs on the first floor of the building.\n "
          "Your task is to locate the bombs planted on the floor and defuse them off. "
          "For defusing bombs you will require defusing kits.\n Enter into the floor, locate the 6 bombs "
          "and 6 defusing kits, defuse the bombs within 10min and save the office from blasting.")
    while True:
        print("Type start to enter into building")
        user_choice = input()
        if user_choice.casefold() == "start":
            start()
            break
        else:
            print("I didn't get you, are you not interested to save maverick?")


def start_timer():
    """
    Starts the game timer.
    """
    global game_duration_in_min
    game_timer = Timer(game_duration_in_min*60, end_timer)
    game_timer.start()


def end_timer():
    """
    Call back when game timer is end.
    """
    global bomb_count
    if bomb_count == 0:
        print("You won, Good work champ!!\n Thanks for saving Maverick")
        stats()
        print_tracked_moves()
        sys.exit(0)
    else:
        print("You lost, it's bomb blast. You are responsible for all casualties.")
        stats()
        print_tracked_moves()
        sys.exit(0)


def start():
    """
    Directs user where to go on floor to search for bombs and defusing kits.
    """
    time.clock()
    start_timer()
    print("You are on first floor now, You can go to following rooms to search for bombs and defusing kits.")
    get_inventory_and_timer_inf0()
    while True:
        print(" 1.Go left to reception desk\n 2.Go north west to meeting room\n 3.Go straight to pantry\n "
              "4.Go north east to library\n 5.Go right to restroom")
        print("Enter the respective number to enter the room")
        room_no = take_user_choice()
        if room_no == 1:
            go_to_reception_desk()
            break
        elif room_no == 2:
            go_to_meeting_room()
            break
        elif room_no == 3:
            go_to_pantry()
            break
        elif room_no == 4:
            go_to_library()
            break
        elif room_no == 5:
            go_to_restroom()
            break
        else:
            print("Enter proper input")


def go_to_reception_desk():
    """
    Directs user where to go in reception cabin to search for bombs and defusing kits.
    """
    global track_moves
    track_moves.append("reception_cabin")
    describe_room("reception cabin")
    get_inventory_and_timer_inf0()
    entry_time_in_room = time.clock()
    while True:
        print(" 1.Cupboard\n 2.Stationary Rack\n 3.Drawers\n 4.Refrigerator\n "
              "5.Go to meeting room\n 6.Go to restroom")
        user_choice = take_user_choice()
        if user_choice == 1:
            track_moves.append("reception_desk_cupboard")
            chk_bomb("reception_desk_cupboard")
            chk_defusing_kit("reception_desk_cupboard")
        elif user_choice == 2:
            track_moves.append("reception_desk_stationary_rack")
            chk_bomb("reception_desk_stationary_rack")
            chk_defusing_kit("reception_desk_stationary_rack")
        elif user_choice == 3:
            track_moves.append("reception_desk_drawers")
            chk_bomb("reception_desk_drawers")
            chk_defusing_kit("reception_desk_drawers")
        elif user_choice == 4:
            track_moves.append("reception_desk_refrigerator")
            chk_bomb("reception_desk_refrigerator")
            chk_defusing_kit("reception_desk_refrigerator")
        elif user_choice == 5:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "reception_cabin")
            go_to_meeting_room()
            break
        elif user_choice == 6:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "reception_cabin")
            go_to_restroom()
            break
        else:
            print("Enter proper input")
        get_inventory_and_timer_inf0()


def go_to_meeting_room():
    """
    Directs user where to go in meeting room to search for bombs and defusing kits.
    """
    global track_moves
    track_moves.append("meeting_room")
    describe_room("meeting room")
    get_inventory_and_timer_inf0()
    entry_time_in_room = time.clock()
    while True:
        print(" 1.Laptops\n 2.Projector\n 3.Chair Rack\n 4.Under Table\n "
              "5.Go to reception desk\n 6.Go to pantry")
        user_choice = take_user_choice()
        if user_choice == 1:
            track_moves.append("meeting_room_laptops")
            chk_bomb("meeting_room_laptops")
            chk_defusing_kit("meeting_room_laptops")
        elif user_choice == 2:
            track_moves.append("meeting_room_projector")
            chk_bomb("meeting_room_projector")
            chk_defusing_kit("meeting_room_projector")
        elif user_choice == 3:
            track_moves.append("meeting_room_chair_rack")
            chk_bomb("meeting_room_chair_rack")
            chk_defusing_kit("meeting_room_chair_rack")
        elif user_choice == 4:
            track_moves.append("meeting_room_under_table")
            chk_bomb("meeting_room_under_table")
            chk_defusing_kit("meeting_room_under_table")
        elif user_choice == 5:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "meeting_room")
            go_to_reception_desk()
            break
        elif user_choice == 6:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "meeting_room")
            go_to_pantry()
            break
        else:
            print("Enter proper input")
        get_inventory_and_timer_inf0()


def go_to_pantry():
    """
    Directs user where to go in pantry to search for bombs and defusing kits.
    """
    global track_moves
    track_moves.append("pantry")
    describe_room("pantry")
    get_inventory_and_timer_inf0()
    entry_time_in_room = time.clock()
    while True:
        print(" 1.Microwave\n 2.Refrigerator\n 3.Coffee Machine\n 4.Sofa\n "
              "5.Go to library\n 6.Go to meeting room\n 7.Go to restroom\n 8.Go to reception desk")
        user_choice = take_user_choice()
        if user_choice == 1:
            track_moves.append("pantry_microwave")
            chk_bomb("pantry_microwave")
            chk_defusing_kit("pantry_microwave")
        elif user_choice == 2:
            track_moves.append("pantry_refrigerator")
            chk_bomb("pantry_refrigerator")
            chk_defusing_kit("pantry_refrigerator")
        elif user_choice == 3:
            track_moves.append("pantry_coffee_machine")
            chk_bomb("pantry_coffee_machine")
            chk_defusing_kit("pantry_coffee_machine")
        elif user_choice == 4:
            track_moves.append("pantry_sofa")
            chk_bomb("pantry_sofa")
            chk_defusing_kit("pantry_sofa")
        elif user_choice == 5:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "pantry")
            go_to_library()
            break
        elif user_choice == 6:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "pantry")
            go_to_meeting_room()
            break
        elif user_choice == 7:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "pantry")
            go_to_restroom()
            break
        else:
            print("Enter proper input")
        get_inventory_and_timer_inf0()


def go_to_library():
    """
    Directs user where to go in library to search for bombs and defusing kits.
    """
    global track_moves
    track_moves.append("library")
    describe_room("library")
    get_inventory_and_timer_inf0()
    entry_time_in_room = time.clock()
    while True:
        print(" 1.Bookshelf\n 2.Printer\n 3.Locker\n 4.Computers\n "
              "5.Go to pantry\n 6.Go to restroom")
        user_choice = take_user_choice()
        if user_choice == 1:
            track_moves.append("library_book_shelf")
            chk_bomb("library_book_shelf")
            chk_defusing_kit("library_book_shelf")
        elif user_choice == 2:
            track_moves.append("library_printer")
            chk_bomb("library_printer")
            chk_defusing_kit("library_printer")
        elif user_choice == 3:
            track_moves.append("library_locker")
            chk_bomb("library_locker")
            chk_defusing_kit("library_locker")
        elif user_choice == 4:
            track_moves.append("library_computers")
            chk_bomb("library_computers")
            chk_defusing_kit("library_computers")
        elif user_choice == 5:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "library")
            go_to_pantry()
            break
        elif user_choice == 6:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "library")
            go_to_restroom()
            break
        else:
            print("Enter proper input")
        get_inventory_and_timer_inf0()


def go_to_restroom():
    """
    Directs user where to go in restroom to search for bombs and defusing kits.
    """
    global track_moves
    track_moves.append("restroom")
    describe_room("restroom")
    get_inventory_and_timer_inf0()
    entry_time_in_room = time.clock()
    while True:
        print(" 1.Dustbin\n 2.Tissues box\n 3.Basin\n 4.Water Tank\n "
              "5.Go to library\n 6.Go to reception desk")
        user_choice = take_user_choice()
        if user_choice == 1:
            track_moves.append("restroom_dustbin")
            chk_bomb("restroom_dustbin")
            chk_defusing_kit("restroom_dustbin")
        elif user_choice == 2:
            track_moves.append("restroom_tissue_box")
            chk_bomb("restroom_tissue_box")
            chk_defusing_kit("restroom_tissue_box")
        elif user_choice == 3:
            track_moves.append("restroom_basin")
            chk_bomb("restroom_basin")
            chk_defusing_kit("restroom_basin")
        elif user_choice == 4:
            track_moves.append("restroom_water_tank")
            chk_bomb("restroom_water_tank")
            chk_defusing_kit("restroom_water_tank")
        elif user_choice == 5:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "restroom")
            go_to_library()
            break
        elif user_choice == 6:
            exit_time_in_room = time.clock()
            calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, "restroom")
            go_to_reception_desk()
            break
        else:
            print("Enter proper input")
        get_inventory_and_timer_inf0()


def describe_room(room_name):
    """
    Detail description of room
    :param room_name: Name of the room in which player is.
    """
    print("You are in {} now, there are couple of places here "
          "where you can search for bombs or defusing kits. select one option from below:".format(room_name))


def take_user_choice():
    """
    Validates and check int type of user inputted value.
    :return: int value what user inputs, for any other values it returns 0.
    """
    try:

        user_choice = int(input())
    except ValueError:
        user_choice = 0
    return user_choice


def chk_bomb(location):
    """
    Check if location contains bomb.
    :param location: name of place looking for bomb.
    """
    global defusing_kits_bag, bomb_count, bomb_locations
    if location in bomb_locations and bomb_locations[location] > 0:
        print("Hey you found {} bomb".format(bomb_locations[location]))
        if defusing_kits_bag > 0:
            print("You have defusing kit in bag use it to defuse bomb, type yes to defuse or no to go ahead")
            user_input = input()
            if user_input.casefold() == "yes":
                print("Bomb is defused")
                defusing_kits_bag -= 1
                bomb_count -= 1
                bomb_locations[location] -= 1
                if bomb_count == 0:
                    print("You won, Good work champ!!\n Thanks for saving Maverick")
                    stats()
                    print_tracked_moves()
                    sys.exit(0)
            else:
                print("Go ahead")
        else:
            print("You don't have defusing kit in bag, keep noted the location of bomb to find it back and go "
                  "search for defusing kit.")
    else:
        print("There is no bomb here")


def chk_defusing_kit(location):
    """
    Check if location contains defusing kits.
    :param location: name of place looking for defusing kits.
    """
    global defusing_kits_bag, defusing_kits_locations
    if location in defusing_kits_locations and defusing_kits_locations[location] > 0:
        print("Hey you found {} defusing kit, it's put in your bag.".format(defusing_kits_locations[location]))
        defusing_kits_bag += defusing_kits_locations[location]
        defusing_kits_locations[location] -= defusing_kits_locations[location]
    else:
        print("There is no defusing kit here, go search at some other places")


def get_inventory_and_timer_inf0():
    """
    Prints the details of number of bombs left to defuse, number of defusing kits left to pick, and time left.
    """
    global bomb_count, defusing_kits_bag, game_duration_in_min
    print("No.of bombs left to defuse:{}, No.of defusing kits in your bag:{}, Time left:{}min".format(bomb_count,
           defusing_kits_bag, game_duration_in_min - round(time.clock()/60, 2)))


def calculate_time_spend_in_room(entry_time_in_room, exit_time_in_room, room_name):
    """
    Calculate time spend in room till that point in game.
    :param entry_time_in_room: time entered in room.
    :param exit_time_in_room:  time exit in room.
    :param room_name:  room name.
    """
    global time_spend_in_each_rooms
    time_spend_in_room = round((exit_time_in_room - entry_time_in_room)/60, 2)
    time_spend_in_each_rooms[room_name] += time_spend_in_room


def stats():
    """
    Calculate the stats of the game and append the visualization graph in specific pdf file.
    """
    global track_moves, time_spend_in_each_rooms, game_duration_in_min
    total_time_spend_in_rooms = 0
    try:
        pdf = PdfPages("Statistics.pdf")
        rooms_name = ["reception_cabin", "meeting_room", "pantry", "library", "restroom"]
        places_visit_count = dict(Counter(track_moves))
        rooms_visited = []
        count_room_visited = []
        for room, count in places_visit_count.items():
            if room in rooms_name:
                rooms_visited.append(room)
                count_room_visited.append(count)
        fig_count_of_rooms_visited = plt.figure()
        plt.bar(rooms_visited, count_room_visited, width=0.3, color='orange')
        plt.xlabel("Room name")
        plt.ylabel("Number of times visited")
        plt.title("Count of number of times rooms visited")
        pdf.savefig(fig_count_of_rooms_visited)
        fig_time_spend_in_each_room = plt.figure()
        time_in_room_visited = []
        for room, count in time_spend_in_each_rooms.items():
            if room in rooms_visited:
                time_in_room_visited.append(count)
                total_time_spend_in_rooms += count
        time_spend_at_entrance = game_duration_in_min - total_time_spend_in_rooms
        rooms_visited.append("At Entrance")
        time_in_room_visited.append(time_spend_at_entrance)
        plt.pie(time_in_room_visited, labels=rooms_visited, autopct='%1.1f%%', shadow=True)
        plt.title("Time spend in each room")
        plt.axis("equal")
        pdf.savefig(fig_time_spend_in_each_room)
        print("Look in Statistics.pdf for visualizing stats generated.")
        pdf.close()
    except IOError:
        print("Please close the Statistics.pdf file opened to generate statistics.")


def print_tracked_moves():
    """
    Print the tracked moves in console.
    """
    print("where you have been in this game is tracked as below:")
    for moves in track_moves:
        print(moves)

get_game_description()
