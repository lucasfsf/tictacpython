first = 1
second = 2
third = 3
fourth = 4
fifth = 5
sixth = 6
seventh = 7
eight = 8
ninth = 9

player = 1

def game_board():
    global first, second, third, fourth, fifth, sixth, seventh, eight, ninth

    print(" --- --- ---")
    print("| {} | {} | {} |".format(first, second, third))
    print(" --- --- ---")
    print("| {} | {} | {} |".format(fourth, fifth, sixth))
    print(" --- --- ---")
    print("| {} | {} | {} |".format(seventh, eight, ninth))
    print(" --- --- ---")

def check_user_input(choice):
    range_checker = True
    while((type(choice) != int) and range_checker):
        try:
            choice = int(choice)
            if(choice >= 1 and choice <= 9):
                range_checker = False
                return choice
            else:
                print("Input should be a number and within the range 1 - 9.")
                choice = input("Try again: ")
        except: 
            print("Input should be a number and within the range 1 - 9.")
            choice = input("Try again: ")

def change_square(player_number, choice):
    global first, second, third, fourth, fifth, sixth, seventh, eight, ninth, player
    if (choice == 1):
        if(square_taken(first) == False):
            first = "X" if (player_number == 1) else "O"
    elif (choice == 2):
        square_taken(second)
        second = "X" if (player_number == 1) else "O"
    elif (choice == 3):
        square_taken(third)
        third = "X" if (player_number == 1) else "O"
    elif (choice == 4):
        square_taken(fourth)
        fourth = "X" if (player_number == 1) else "O"
    elif (choice == 5):
        square_taken(fifth)
        fifth = "X" if (player_number == 1) else "O"
    elif (choice == 6):
        square_taken(sixth)
        sixth = "X" if (player_number == 1) else "O"
    elif (choice == 7):
        square_taken(seventh)
        seventh = "X" if (player_number == 1) else "O"
    elif (choice == 8):
        square_taken(eight)
        eight = "X" if (player_number == 1) else "O"
    elif (choice == 9):
        square_taken(ninth)
        ninth = "X" if (player_number == 1) else "O"
    
    

def square_taken(square):
    square_was_taken = False
    if(square == "X" or square == "O"):
        square_was_taken = True
        print("Square already taken, chose another one: ")
        choice = input("")
        choice = check_user_input(choice)
        change_square(player, choice)
    return square_was_taken

def is_game_finished():
    global first, second, third, fourth, fifth, sixth, seventh, eight, ninth, player
    if(first == second == third):
        print("Player {} won!".format(player))
        return True
    elif(first == fourth == fifth):
        print("Player {} won!".format(player))
        return True
    elif(first == fifth == ninth):
        print("Player {} won!".format(player))
        return True
    elif(second == fifth == eight):
        print("Player {} won!".format(player))
        return True
    elif(third == sixth == ninth):
        print("Player {} won!".format(player))
        return True
    elif(third == fifth == seventh):
        print("Player {} won!".format(player))
        return True
    elif(fourth == fifth == sixth):
        print("Player {} won!".format(player))
        return True
    elif(seventh == eight == ninth):
        print("Player {} won!".format(player))
        return True
    elif(type(first) == str and type(second) == str and type(third) == str 
    and type(fourth) == str and type(fifth) == str and type(sixth) == str 
    and type(seventh) == str and type(eight) == str and type(ninth) == str):
        print("No one won")
        return True
    else:
        return False

def reset_board():
    global first, second, third, fourth, fifth, sixth, seventh, eight, ninth, player
    first = 1
    second = 2
    third = 3
    fourth = 4
    fifth = 5
    sixth = 6
    seventh = 7
    eight = 8
    ninth = 9

    player = 1

def main():
    game_finished = False
    while(game_finished == False):
        global first, second, third, fourth, fifth, sixth, seventh, eight, ninth, player
        game_board()
        print("Player {}, please choose a square:\n".format(str(player)))
        choice = input("")
        choice = check_user_input(choice)
        change_square(player, choice)
        game_finished = is_game_finished()
        if(player == 1):
            player = 2
        else: 
            player = 1

    print("Game over!")
    play_again = int(input("Play Again? 1 - Yes 2 - No\n"))
    if(play_again == 1):
        reset_board()
        main()
    else:
        print("Bye")


if __name__ == "__main__":
    main()