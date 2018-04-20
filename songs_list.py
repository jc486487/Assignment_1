"""Name: Sherin Sarah Varghese
Date: 20 April 2018
Brief program details: This program tracks song files the user wishes to learn and songs they have learned.
                       It also allows the user to add songs to the file indicating the title, artist, year,
                       whether it is required (y) or learned (n).
Link to the project on GitHub: https://github.com/jc486487/Assignment_1"""

import csv

with open("songs.csv", 'r+', newline='') as f:
    reader = csv.reader(f)
    lines = list(reader)

    print("Songs to learn 1.0 - by Sherin Sarah Varghese")
    count_songs = len(lines)  # counts the number of songs in the songs.csv file
    print(count_songs, "songs loaded")

    # displays the menu options the user can choose from
    MENU = """MENU:
    L - List songs 
    A - Add a new song 
    C - Complete a song 
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    learn = 0
    require = 0

    # access to this when the user doesn't want to quit the program
    while choice != 'Q':
        if choice == 'L':
            require = 0
            learn = 0
            sl_no = 0
            for x in lines:
                if x[3] == 'y':
                    character = "*"
                    require += 1
                else:
                    character = " "
                    learn += 1
                print("{}. {} {:30} - {:<30} ({})".format(sl_no, character, x[0], x[1], x[2]))
                sl_no += 1
            print("{} songs learned, {} songs still to learn".format(learn, require))

            print(MENU)  # allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        elif choice == 'A':
            title = str(input("Title: "))
            while title == "":
                print("Input cannot be blank")
                title = str(input("Title: "))

            artist = str(input("Artist: "))
            while artist == "":
                print("Input cannot be blank")
                artist = str(input("Artist: "))

            year = input("Year: ")
            success = False
            while not success:
                if year.isalpha():
                    print("Invalid input; enter a valid number")
                    year = str(input("Year: "))
                elif int(year) not in range(0, 2019):
                    print("Invalid input; enter a valid number")
                    year = input("Year: ")
                elif int(year) <= 0:
                    print("Number must be > 0")
                    year = input("Year: ")
                else:
                    success = True
            year = str(year)

            print("{} by {} added to song list".format(title, artist))
            new_song = [title, artist, year, "y"]
            lines.append(new_song)
            require += 1
            count_songs += 1

            print(MENU)  # allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        elif choice == 'C':
            if require == 0:
                print("No more songs to learn!")

            else:
                print("Enter the number of the song to mark as learned")
                song_no = input(">>> ")
                flag = False
                while not flag:
                    if song_no.isalpha():
                        print("Invalid input; enter a valid number")
                        song_no = input(">>> ")
                    elif song_no.isspace():
                        print("Input cannot be blank; enter a valid number")
                        song_no = input(">>> ")
                    elif int(song_no) < 0:
                        print("Number must be >= 0")
                        song_no = input(">>> ")
                    elif int(song_no) >= count_songs:
                        print("Invalid song number")
                        song_no = input(">>> ")
                    else:
                        flag = True
                song_no = int(song_no)

                if lines[song_no][3] == 'n':
                    print("You have already learned {}".format(lines[song_no][0]))
                else:
                    lines[song_no][3] = 'n'
                    print("{} by {} learned".format(lines[song_no][0], lines[song_no][1]))
                    require -= 1

            print(MENU)  # allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        else:
            print("Invalid option. Enter again")
            print(MENU)  # displays and allows the user to enter again for wrong entry
            choice = input(">>> ").upper()

    f.truncate(0)
    writer = csv.writer(f)
    writer.writerows(lines)
    print("{} songs saved to songs.csv \nHave a nice day :)".format(count_songs))
f.close()