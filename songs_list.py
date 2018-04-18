"""Name: Sherin Sarah Varghese
Date: 16 April 2018
Brief program details: This program tracks song files the user wishes to learn and songs they have learned.
                       It also allows the user to add songs to the file indicating the title, artist, year,
                       whether it is required (y) or learned (n).
Link to the project on GitHub: https://github.com/jc486487/Assignment_1"""
import csv

def main():
    songs_file = open("songs.csv", 'r+')
    print("Songs to learn 1.0 - by Sherin Sarah Varghese")
    count = sum(1 for row in songs_file)
    print(count, "songs loaded")

    MENU = """MENU:
    L - List songs 
    A - Add a new song 
    C - Complete a song 
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != 'Q':
        if choice == 'L':
            with open("songs.csv") as f:
                reader = csv.reader(f)
                sl_no = 0
                for x in reader:
                    if x[3] == 'y':
                        character = "*"
                    else:
                        character = " "
                    print("{}. {} {} - {} ({})".format(sl_no, character, x[0], x[1], x[2]))
                    sl_no += 1
            f.close()
            print(MENU)
            choice = input(">>> ").upper()

        elif choice == 'A':
            count = add_song(count, songs_file)
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == 'C':
            with open("songs.csv", 'r+', newline='') as d:
                reader = csv.reader(d)
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
                    elif int(song_no) > count:
                        print("Invalid song number")
                        song_no = input(">>> ")
                    else:
                        flag = True

                lines = list(reader)
                if lines[int(song_no)][3] == 'n':
                    print("You have already learned {}".format(lines[int(song_no)][0]))
                else:
                    song_file = open("songs.csv", 'w+')
                    lines[int(song_no)][3] = 'n'
                    writer = csv.writer(d)
                    writer.writerows(lines)
                    print("{} by {} learned".format(lines[int(song_no)][0], lines[int(song_no)][1]))
                    song_file.close()
            d.close()

            print(MENU)
            choice = input(">>> ").upper()
        else:
            print("Invalid option. Enter again")
            print(MENU)
            choice = input(">>> ").upper()
    print(count, "songs saved to songs.csv \nHave a nice day :)")
    #songs_file.close()

def add_song(count, songs_file):
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
    print(title, ",", artist, ",", year, ",", "y", file=songs_file)
    count += 1
    return count

main()