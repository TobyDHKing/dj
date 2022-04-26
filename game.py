names = [["tom","smith"],["joe","brown"],["ben","storer"],["toby","jasper"]]

def menu():
    print("---------------------------------------------------------")
    print("                     Math Maze\n")
    
    
    print("1 Open commands")                                                  
    print("2 Start game")
    print("3 Exit game")
    print("---------------------------------------------------------")
    choice = input("Enter choice: ")
    
    return choice

def login():
    global name
    names = [["tom","smith"],["joe","brown"],["ben","storer"],["toby","jasper"]]

    correctInfo = False
    
    while correctInfo == False:
        
        name = input("Enter username")
        password = input("Enter Password" )
        attempts = 2
        correctPassword = False

        for i in range(0,len(names)):
            if name == (names[i][0]):
                print("correct username")
                correctInfo = True

                while correctPassword == False and attempts >0:
               
                    if password == (names[i][1]):
                            correctPassword = True
                           
                           

                    else:
                        print("Incorrect password")
                        attempts = attempts -1
                        password = input("Please try again, ")
                           


                if correctPassword == True:
                    print("Correct password")
                    break

               
                if attempts == 0:
                        print("You have zero attempts remaining")
                        break

            else:
               
                if i == len(names) -1:
                    print("Username does not exist")
                    
           
       

def commands():
    print("These are all the possible commands to write")
    print("Move north")
    print("Move east")
    print("Move south")
    print("Move west")

def createaccount():
    global names, accountList
    badPword = True
    
    userExists = True
    while badPword == True:
        digits = False
        
        while userExists == True:
            userExists = False
            print("please enter your desired username")
            username = input()
            
            for i in range(0,len(names)):
                
                if username == (names[i][0]):
                    print("Username exists")
                    userExists = True
                    break

                #else:
                    #userExists = False
                
        print("please enter your desired password")
        password = str(input())

        if len(password) <8:
                
            for character in password:
                if character.isdigit() == True:
                    digits = True
                    print("Please do not use numbers, try again")
        else:
            print("Please use less than 8 characters, try again")


        if digits == False and len(password) <8:

            badPword = False
            print("Account created successfully", username)
            

        if len(password) >8:
            print("Please use less than 8 characters, try again")

    accountList = []
    accountList.append(username)
    accountList.append(password)
    names.append(accountList)
    

   
def startgame():
    ans = input("Would you like to log in or create an account? L or C ")
    if ans == "C":
        print("hello")
        createaccount()
    elif ans == "L":
        print("Selected login")
        login()





#grid = [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']



#namefile = name
loaded = False


roomdesc = [['You are outside the front door','You are in the front door porch','you are in the main hallway','you are in an old kitchen','You are in the storage room'],
        ['You are at the top of the stairs','you are in the upstairs hallway','You are in a bedroom','you are in an old and broken down room','you are in the guest bedroom'],
        ['You are in the upstairs libary','*','*','*','*'],
        ['*','*','*','*','*'],
        ['*','*','*','*','*']]



grid = [['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*']]
traps = [['*','*','*','*','*'],['*','t','*','t','*'],['*','t','*','t','*'],['*','t','*','t','*'],['*','*','*','*','*']]
finexit = [['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','e']]
items = [['*','h','m','*','*'],['*','*','i','*','*'],['*','*','m','*','*'],['*','*','*','*','i'],['*','*','*','*','i']]                                                                                                             



# testing notes, exploit keep leaving map item gains 20 points on repeat if left option is chosen.
# reset item position to * after use.




lives = 3
score = 0
#was just finding first 't' in trap room search and global and local variable problem
#with row,col was stuck at 0,1 everytime

#'grid' is a 2D list which holds all of the '*' to be printed out in rows and collumns.
#'end = "" prevents the starts to be printed on a new line each time.
def drawgrid():

    for row in range (0,5):
       
       
        for col in range (0,5):
            print (grid [row][col], end = "")
     
        print()


#Scans through each row and grid to find the current position of the player. The player is represented by a 'o'
#For loop to repeat each search row and collumn. Looks at every collumn in the first row then the next row etc.
#efficient as the loop stops when 'o' is found
#(players can see this letter)
def curPosition():

    for row in range (0,5):
       
        for col in range (0,5):
            if (grid [row][col]) == 'o':
                print("current position is", row, col)
                return row, col


#scans through every collumn of each row in the trap 2D list to locate any letter 't'.
#(players cannot see this letter)
def traproom():
    global row, col
    print("trap func")
    for row in range (0,5):
       
        for col in range (0,5):
            if (traps [row][col]) == 't':
                print(row, col, "in trap func") #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                return True

#scans through every collumn of each row in the 2D list named finexit to locate the letter 'e' which stands for exit.
#(players cannot see this letter)
def finish():
    global score
    #for row in range (0,5):
       
        #for col in range (0,5):
            #if (finexit [row][col]) == 'e':
    if score >= 1:
        print("well done you have completed the game") #if = e and .= 100 then: didnt work as score was too low so else statment was printed everytime west was clicked
        quit()
    else:
        
        print("Your score is too low to leave")
    
    #return True

#room item function allow useable items into the game. the programme scans through another 2D list named 'items'
#if the letter 'm' appears standing for 'map'
#it tell you there is an item in the room and you can pick it up or leave it and stores input into a variable
#if the map is used the 2D list (traps) is printed for the player
#if the user does not use it they get +20 score

def roomitem():
        global row, col, score, lives, traps
    #for row in range (0,5):
       
        #for col in range (0,5):
        if (items [row][col]) == 'm':
            print("there is an item in this room")
            itemchoice = input("What would you like to do next ")
            if itemchoice == ("pick up item"):
                if items[row][col] == 'm':
                    print("you picked up a map")
                    mapanswer = input("Use it now? leave it? ")
                    if mapanswer == 'use':
                        print(traps)
                        items[row][col] = '*'
                    else:
                        print("+20 score")
                        score = score +20

#scans through the items list and looks for letter 'h' stands for health
#lives is increased by 1
        if items[row][col] == 'h':
            print("you picked up an extra life")
            lives = lives +1
            print("You now have", lives, "lives")
                
            

#movement function, this function
def south():
    global row, col, lives, userDiff, score
    
    row, col = curPosition()
    print (roomdesc[row][col])
    grid [row][col] = '*'
    row = row + 1
    if userDiff == "simple":
        score = score +5
        
    elif userDiff == "medium":
        score = score +10
        
    else:
        userDiff == "hard"
        score = score +20
        
    if row == 5:
        print("invalid move")
        row = row -1
        grid[row][col] = 'o'
    else:
        if traps[row][col] == 't':
            lives = lives -1
            print("-1 life")
            print("you have", lives,"remaining")
        grid[row][col] = 'o'
        if items[row][col] == 'i':
            roomitem()
        if finexit[row][col] == 'e':
            finish()

        if items[row][col] in "'m','h','w'":
            
            roomitem()
            
    print()
    print (score)
    drawgrid()    

def west():
    global row, col, lives, userDiff, score, finexit
    row, col = curPosition()
    grid [row][col] = '*'
    col = col +1
    print (roomdesc[row][col], '\n') 
    if userDiff == "simple":
        score = score +5
        
    elif userDiff == "medium":
        score = score +10
        
    else:
        userDiff == "hard"
        score = score +20
    if col == 5:
        print("invalid move")
        col = col -1
        grid[row][col] = 'o'
    else:
        if traps[row][col] == 't':
            lives = lives -1
            print("-1 life")
            print("you have", lives,"remaining")
        grid[row][col] = 'o'
        
        if finexit[row][col] == 'e':
            finish()
    
        if items[row][col] in "'m','h','w'":
            
            roomitem()
        
    print()
    print("Your score is", score)
    drawgrid()

def east():
    global row, col, lives, userDiff, score, finexit
    
    row, col = curPosition()
    grid [row][col] = '*'
    col = col -1
    if col == -1:
        print("invalid move")
        col = col +1
        grid[row][col] = 'o'
    else:
        if traps[row][col] == 't':
            lives = lives -1
            print("-1 life")
            print("you have", lives,"remaining")
        grid[row][col] = 'o'
        
        if finexit[row][col] == 'e':
            finish()
        if items[row][col] == 'i':
            roomitem()

        if items[row][col] in "'m','h','w'":
            
            roomitem()
            
    print()
    print("Your score is", score)
    drawgrid()
    
def north():
    global row, col, lives, userDiff, score, finexit
    row,col = curPosition()
    grid[row][col] = '*'
    row = row -1
    if row == -1:
        print("invalid move")
        row = row +1
        grid[row][col] = 'o'
    else:
        if traps[row][col] == 't':
            lives = lives -1
            print("current position N is", row, col)
            print("-1 life")
            print("you have", lives,"remaining")
        grid[row][col] = 'o'
        if items[row][col] == 'i':
            roomitem()
            
        if finexit[row][col] == 'e':
            finish()
            
        if items[row][col] in "'m','h','w'":
            
            roomitem()
        
    print()
    print("Your score is", score)
    drawgrid()


def questionAsk():
    import random

    minnum = 1
    maxnum = 1
    typedans = False
    global userDiff, row, col, lives, score, loaded, name
    
    while typedans == False:
        print("Please choose a difficulty, The Higher the difficulty the more score! ")
        if loaded == False:
            print("simple, medium, hard, save game or load game")
        else:
            print("simple, medium, hard or save game")
        userDiff = input().lower()
        if userDiff == "simple":
            minnum = 1
            maxnum = 10
            typedans = True
        elif userDiff == "medium":
            minnum = 10
            maxnum = 99
            typedans = True
        elif userDiff == "hard":
            minnum = 100
            maxnum = 999
            typedans = True
        elif userDiff == "save game":
            file = open("savedgames.txt", "a") #opens text file saved games and opens it in append mode.
            row,col = curPosition()
            file.write(name + "," + str(score) + "," + str(lives) + "," + str(row) + "," + str(col) + "\n")
            file.close()
            typedans = True
            print("You have saved your game")
            exitans = input("Would you like to exit? ")
            if exitans == "yes":
                quit()
            else:
                return "continue"
        elif userDiff == "load game":
            loaded = True
            grid [0][0] = '*'
            validFile = False
            try:
                file = open("savedgames.txt", "r")
                validFile = True
            except:
                print("file not found")
                grid [0][0] = 'o'
                
            if validFile == True:
                tempscore = 0
                foundplayer = False
                #for line in (file):
                    
                for loop in range(20):   #reads 100 lines 
                    line = file.readline()  #reads each line
                    line = line.rstrip()  #strips off \n at the end of each line
                    #print("line is2", line)  
                    data = line.split(",") #splits each item at the comma allowing each item to be read by itself creating a list.
                    #print("data is", data)
                    if data[0] == name:  #if there is  name set foundlpayer to True and it will load that players saved game
                        foundplayer = True
                        #print(data[1],data[2],data[3],data[4])
                        if int(data[1]) >= tempscore: # if score is greater than the tempscore then
                            
                            tempscore = int(data[1]) # tempscore is set to score for that entry
                            score = int(data[1])
                            lives = int(data[2]) # all others are being assigned to the list's indexes
                            row = int(data[3])
                            col = int(data[4])
                if foundplayer == False: #  if there is no saved game able to load then found player is false as stated at the top and game not found will print and a new game will be created.
                    print("Game not found")
                    grid [0][0] = 'o'  #resets player position only if there is no name in the text file
                else:
                    grid [row][col] = 'o'  #if there is a name it puts the players position in the saved position 
                    
                        
                        
                file.close()  #closes the 'saved game' text file
                print(score, lives)
                
                #grid [0][0] = 'o' # sets the position 0,0 in the grid to an 'o' which then resets the game
                drawgrid()

            else:
                drawgrid()

        else:
            print("Please try again")
            
       
    number1 = random.randint(minnum,maxnum)
    number2 = random.randint(minnum,maxnum)

    answer = number1 + number2
    print("Add these numbers")
    print(number1, number2)
    userinput = (int(input()))
    
    if userinput == answer:
       # print("correct")
        return 'correct'
    else:
        print("incorrect")
        return 'incorrect'




option = menu() 



if option == '1':
    commands()
    menu()

elif option == '2':
   
    startgame()

elif option == '3':
    quit()





grid [0][0] = 'o'
print()


drawgrid()
movement = True

while movement == True:

    questionAns = questionAsk()
    print(questionAns)
    if questionAns == 'correct':
        option = input("please choose an option or command, N, S, E, W ").lower()
        
        if option == 's':
            south()

        if option == 'w':
            west()
            
        if option == 'e':
            east()

        if option == 'n':
            north()

        #if option == 'use map':
            #mapitem()

