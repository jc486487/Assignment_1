"""Name: Sherin Sarah Varghese
Date: 16 April 2018
Brief program details: This program tracks song files the user wishes to learn and songs they have learned.
                       It also allows the user to add songs to the file indicating the title, artist, year,
                       whether it is required (y) or learned (n).
Link to the project on GitHub: https://github.com/jc486487/Assignment_1"""

songs_file = open("songs.csv", 'r+')
print("Songs to learn 1.0 - by Sherin Sarah Varghese")
print(sum(1 for row in songs_file), "songs loaded")

MENU = """MENU:
L - List songs 
A - Add a new song 
C - Complete a song 
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != 'L' and choice != 'A' and choice != 'C' and choice != 'Q':
    print("Invalid option. Enter again")
    print(MENU)
    choice = input(">>> ").upper()

while choice != 'Q':
    if choice == 'L':
        print("Hi")
        print(MENU)
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

        year = str(input("Year: "))
        while int(year) <= 0:
            print("Number must be >= 0")
            year = str(input("Year: "))
        while int(year) not in range(0, 2019):
            print("Invalid input; enter a valid number")
            year = str(input("Year: "))

        print(title, artist, year, "y", file=songs_file)
        print(title, "by", artist, "added to song list")
        print(MENU)
        choice = input(">>> ").upper()
    elif choice == 'C':
        print("Enter the number of the song to mark as learned")
        mark = int(input(">>> "))
        print(MENU)
        choice = input(">>> ").upper()

print(sum(1 for row in songs_file), "songs saved to songs.csv \n Have a nice day :)")