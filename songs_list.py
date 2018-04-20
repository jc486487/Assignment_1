"""Name: Sherin Sarah Varghese
Date: 20 April 2018
Brief program details: This program tracks the song file- songs.csv,
                        the user wishes to learn and songs they have learned.
                        It also allows the user to add songs to the file indicating
                        the title, artist, year, whether it is required (y) or learned (n).
Link to the project on GitHub: https://github.com/jc486487/Assignment_1"""

import csv

"""Function to list the songs:
    variables l, r to count the number of songs learned and those that are yet to be learned 
    serial # = 0
    for loop to take each row from the list - 'lines' 
    if the 3rd element in the row is y- character is '*'
    if not- character is just space
    prints each row in the format - serial #. character title - artist (year) --> proper spacing to appear in columns
    increase count of serial #
    return l, r"""

def list_songs(lines):
    r = 0
    l = 0
    sl_no = 0
    for x in lines:
        if x[3] == 'y':
            character = "*"
            r += 1
        else:
            character = " "
            l += 1
        print("{0:2}. {1} {2:30} - {3:<30} ({4})".format(sl_no, character, x[0], x[1], x[2]))
        sl_no += 1
    return l, r

"""Function to add songs to the list:
    input title 
    if title entered is empty - alert and ask for input again 
    input artist 
    if artist entered is empty - alert and ask for input again 
    input year
    error checking for - string entered, if its less than 0, if it exceeds the current year(2018)
    converts year to string to save in the list"""

def add_songs():
    t = str(input("Title: "))
    while t == "":
        print("Input cannot be blank")
        t = str(input("Title: "))

    art = str(input("Artist: "))
    while art == "":
        print("Input cannot be blank")
        art = str(input("Artist: "))

    y = input("Year: ")
    success = False
    while not success:
        if y.isalpha():
            print("Invalid input; enter a valid number")
            y = input("Year: ")
        elif int(y) not in range(0, 2019):
            print("Invalid input; enter a valid number")
            y = input("Year: ")
        elif int(y) <= 0:
            print("Number must be > 0")
            y = input("Year: ")
        else:
            success = True
    y = str(y)
    return t, art, y

"""Function to change the unlearned songs to learned: 
    ask the user to enter the number of the song they wish to change 
    error checking to ensure they dont enter a string, space, number less than 0, number greater than total songs
    convert the song # entered to integer 
    
    if the 3rd element in the song # the user entered is already 'n':
    display - you have already learned title 
    if not:
    change the 3rd element in that song to 'n'
    display the song has learned 
    reduce the number of songs to be learned (req) by 1
    return req"""

def complete_song(count_songs, lines, req):
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
        req -= 1
    return req


"""Main function"""

#opens songs.csv file as 'f' in the read and write mood and indicate newline after each song is not needed
with open("songs.csv", 'r+', newline='') as f:

    #reads the songs.csv file
    reader = csv.reader(f)

    #convert songs in the songs.csv file into a list - 'lines'
    lines = list(reader)

    #initial message
    print("Songs to learn 1.0 - by Sherin Sarah Varghese")
    count_songs = len(lines)  # counts the number of songs in the list
    print(count_songs, "songs loaded")

    # displays the menu options the user can choose from
    MENU = """MENU:
L - List songs 
A - Add a new song 
C - Complete a song 
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper() #inputs user's choice

    #variables to count the number of songs learned and those that are yet to be learned
    learn = 0
    require = 0

    # access to this when the user doesn't want to quit the program
    while choice != 'Q':
        if choice == 'L':
            #calls function - list_songs(); parameters - learn, require, access to list of songs ('lines')
            learn, require = list_songs(lines)

            #displays the number of songs learned and the songs yet to be learned
            print("{} songs learned, {} songs still to learn".format(learn, require))

            print(MENU)  # allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        elif choice == 'A':
            #calls function add_songs() which contains the title, artist and year of the new song entered by user
            title, artist, year = add_songs()

            #displays that the song by artist has been added to the list
            print("{0} by {1} ({2}) added to song list".format(title, artist, year))

            #title, artist, year inputed is converted into a list to add to the list of songs- 'lines'
            new_song = [title, artist, year, "y"]
            lines.append(new_song)

            #increases the count of songs to be learned and the total songs in the list 'lines'
            require += 1
            count_songs += 1

            print(MENU)  # allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        elif choice == 'C':
            #if there aren't any songs to be learned, it displays "No more songs to learn
            if require == 0:
                print("No more songs to learn!")

            #if there are songs to be learned:
            else:
                #calls the function - complete_song; parameters - count of songs in the list, access to list 'lines' and number of songs to be learned
                require = complete_song(count_songs, lines, require)

            print(MENU)  # allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        #programs displays the message in this case, if their input is not 'L', 'A', 'C' or 'Q'
        else:
            print("Invalid option. Enter again")
            print(MENU)  # displays and allows the user to enter again for wrong entry
            choice = input(">>> ").upper()

    #when the user decides to quit, and enters 'Q', this code is executed

    # clears content in the songs.csv file to add the new edited list of songs
    f.truncate(0)

    # enables the songs.csv file writable
    writer = csv.writer(f)

    # write the new edited list of songs into the songs.csv file
    writer.writerows(lines)

    #displays the number of songs saved to songs.csv file before ending the program
    print("{} songs saved to songs.csv \nHave a nice day :)".format(count_songs))

#close songs.csv file opened as f
f.close()