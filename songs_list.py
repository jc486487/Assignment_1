"""Name: Sherin Sarah Varghese
Date: 16 April 2018
Brief program details: This program tracks song files the user wishes to learn and songs they have learned.
                       It also allows the user to add songs to the file indicating the title, artist, year,
                       whether it is required (y) or learned (n).
Link to the project on GitHub: https://github.com/jc486487/Assignment_1"""

songs_file = open("songs_file.csv", 'r+')
print("Songs to learn 1.0 - by Sherin Sarah Varghese")
MENU = """L - List songs 
          A - Add a new song 
          C - Complete a song 
          Q - Quit"""
print(len(songs_file), "songs loaded")