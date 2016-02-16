#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document]. Retrieved
#from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

#cppreference.com. (Nov 14, 2015). Retrieved from http://en.cppreference.com/w/cpp/language/ascii

#Tutorials Point. (Nov 14, 2015). Retrieved from http://www.tutorialspoint.com/python/python_dictionary.htm



def main ():
    white=0 #initial white score
    black=0 #initial black score
    
    #repete for the 8 rows of the chessboard starting at the first
    for i in range (1,9):
        #get the input from the user of what each line of the board looks like. Use i to specify which row
        chessboard=input("Please type 8 characters for row {} of the chessboard:".format(i)) 
        #call the W/B score function to get the score of that line and add it to the previous lines
        white=white+Wscore(chessboard) 
        black=black+Bscore(chessboard)
    
    #check who won 
    if white<black: #If white has less points
        winning="Black" #then black is the winner
    
    elif white>black: #else if white has more points
        winning="White" #then white is the winner 
    
    else: #otherwise black and white have the same number of points 
        winning="no one" #no one one, it is a tie
    #display the results (number of points each side has and who is winning)
    print("White has",white,"points and Black has",black, "points so", winning, "is winning") 
    

def Wscore (chessboard):
    #define the values dictionary for each possible outcome/value on the board
    values={"q":10,"r":5,"n":3,"b":3,"p":1,"Q":10,"R":5,"N":3,"B":3,"P":1,"-":0,"k":0,"K":0} 
    white=0 #create the white score variable
    
    #run through each value in the line (aka 8) len chessboard should = 8
    for i in range (len(chessboard)): 
        #get the value at each location on the line
        peice=chessboard[i]
        
        #check if the value is lowercase and therefore white
        if ord(peice)>97:
            #add value to white using the kew to search the dictionary
            white=white+values.get(peice)
    return white
 

def Bscore (chessboard):
    #define the values dictionary for each possible outcome/value on the board
    values={"q":10,"r":5,"n":3,"b":3,"p":1,"Q":10,"R":5,"N":3,"B":3,"P":1,"-":0,"k":0,"K":0}
    black=0#create the black score variable
    
    #run through each value in the line (aka 8) len chessboard should = 8
    for i in range (len(chessboard)):
        #get the value at each location on the line
        peice=chessboard[i]
        
        #check if uppercase or no value and therefore black
        if ord(peice)<97:
             #add value to black using the kew to search the dictionary
            black=black+values.get(peice)
    return black
    
main()