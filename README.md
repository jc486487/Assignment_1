# Assignment_1
A1 by Sherin Sarah Varghese

This program tracks the song file- songs.csv, the user wishes to learn and songs they have learned.
It also allows the user to add songs to the file indicating the title, artist, year, whether it is required (y) or learned (n).

Function to list the songs:

    variables l, r to count the number of songs learned and those that are yet to be learned 
    serial # = 0
    for loop to take each row from the list - 'lines' 
    if the 3rd element in the row is y- character is '*'
    if not- character is just space
    prints each row in the format - serial #. character title - artist (year) --> proper spacing to appear in columns
    increase count of serial #
    return l, r
    
Function to add songs to the list:

    input title 
    if title entered is empty - alert and ask for input again 
    input artist 
    if artist entered is empty - alert and ask for input again 
    input year
    error checking for - string entered, if its less than 0, if it exceeds the current year(2018)
    converts year to string to save in the list
    
 Function to change the unlearned songs to learned: 
 
    ask the user to enter the number of the song they wish to change 
    error checking to ensure they dont enter a string, space, number less than 0, number greater than total songs
    convert the song # entered to integer 
    
    if the 3rd element in the song # the user entered is already 'n':
    display - you have already learned title 
    if not:
    change the 3rd element in that song to 'n'
    display the song has learned 
    reduce the number of songs to be learned (req) by 1
    return req
    
 Main function:
 
 displaying the menu with choices, execution of the entire program, displaying changes made and finally, overwrites the songs.csv file with changes
 
 
