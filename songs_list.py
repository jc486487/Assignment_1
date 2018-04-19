"""Name: Sherin Sarah Varghese
Date: 20 April 2018
Brief program details: This program tracks song files the user wishes to learn and songs they have learned.
                       It also allows the user to add songs to the file indicating the title, artist, year,
                       whether it is required (y) or learned (n).
Link to the project on GitHub: https://github.com/jc486487/Assignment_1"""

import csv
def main():
    songs_file = open("songs.csv", 'r+')
    print("Songs to learn 1.0 - by Sherin Sarah Varghese")
    count_songs = sum(1 for row in songs_file) #counts the number of songs in the songs.csv file
    print(count_songs, "songs loaded")
    songs_file.close()

    #displays the menu options the user can choose from
    MENU = """MENU:
    L - List songs 
    A - Add a new song 
    C - Complete a song 
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    #access to this when the user doesn't want to quit the program
    while choice != 'Q':
        if choice == 'L':
            list_songs() #calls the function which displays the list of songs in the csv folder

            print(MENU) #allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        elif choice == 'A':
            add_songs() #calls this function which allows the user to add new songs to the csv file

            print(MENU) #allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()

        elif choice == 'C':
            complete_song() #calls the function which allows the user to change songs to learned "n" form

            print(MENU) #allows the user to choose anything from the menu again, until he quits
            choice = input(">>> ").upper()
        else:
            print("Invalid option. Enter again")
            print(MENU) #displays and allows the user to enter again for wrong entry
            choice = input(">>> ").upper()

    #The program leads to this if the user enters "Q" and wishes to quit the program
    in_file = open("songs.csv", 'r')
    count = sum(1 for get in in_file) #counts the number of songs saved to the csv file
    print(count, "songs saved to songs.csv \nHave a nice day :)")
    in_file.close()

"""function to list all the songs from the csv file
    open file in read mode r
    read csv file 
    serial # = 0
    for loop to take each row from the csv file 
    if the 3rd element in the row is y- character is '*'
    if not- character is just space
    prints each row in the format - serial #. character title - artist (year)
    close file opened in r mood"""

def list_songs():
    with open("songs.csv", 'r') as f:
        read = csv.reader(f)
        sl_no = 0
        for x in read:
            if x[3] == 'y':
                character = "*"
            else:
                character = " "
            print("{}. {} {} - {} ({})".format(sl_no, character, x[0], x[1], x[2]))
            sl_no += 1
    f.close()

"""function to add songs to the list
    input title 
    if title entered is empty - alert and ask for input again 
    input artist 
    if artist entered is empty - alert and ask for input again 
    input year
    error checking for - string entered, if its less than 0, if it exceeds the current year(2018)
    if the title, artist, year entered is correct, display title by artist added to the list
    open songs.csv file in append mood a+
    add - title,artist,year,y- to songs.csv file ('y' indicates it is required)
    close file opened in a+ mood"""

def add_songs():
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
    print("{} by {} added to song list".format(title, artist))
    playlist = open("songs.csv", 'a+')
    print("{},{},{},y".format(title, artist, year), file=playlist)
    playlist.close()

"""function to complete song - change 'y' to 'n'
    open file and count the number of songs (total)
    ask the user to enter the number of the song they wish to change 
    error checking to ensure they dont enter a string, space, number less than 0, number greater than total songs
    
    open file in read and overwrite mood
    read rows in the songs.csv file 
    convert rows to list 
    if the 3rd element in the song # the user entered is already 'n':
    display - you have already learned title 
    if not:
    open songs.csv in overwrite mood w+
    change the 3rd element in that song to 'n'
    overwrite all the rows in songs.csv with change 
    display - title by artist learned
    close file opened in w+ mood 
    close file opened in r+ mood"""

def complete_song():
    check = open("songs.csv", "r")
    total = sum(1 for line in check)
    check.close()
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
        elif int(song_no) >= total:
            print("Invalid song number")
            song_no = input(">>> ")
        else:
            flag = True
    with open("songs.csv", 'r+', newline='') as d:
        reader = csv.reader(d)
        lines = list(reader)
        if lines[int(song_no)][3] == 'n':
            print("You have already learned {}".format(lines[int(song_no)][0]))
        else:
            out_file = open("songs.csv", 'w+')
            lines[int(song_no)][3] = 'n'
            writer = csv.writer(d)
            writer.writerows(lines)
            print("{} by {} learned".format(lines[int(song_no)][0], lines[int(song_no)][1]))
            out_file.close()
    d.close()

main()