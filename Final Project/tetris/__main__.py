from game.directing.director import Director


def main():
    director = Director()
    director.start_game()

# If this file was executed like this: % python3 tetris/
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    # Start this program by calling the main function.
    main()