import random, ascii_magic, pyttsx3

def sum(a,b,c):
    return a+b+c


def PrintBoard(x,y):
    zero='X' if x[0] else('O' if y[0] else 0)
    one='X' if x[1] else('O' if y[1] else 1)
    two='X' if x[2] else('O' if y[2] else 2)
    three='X' if x[3] else('O' if y[3] else 3)
    four='X' if x[4] else('O' if y[4] else 4)
    five='X' if x[5] else('O' if y[5] else 5)
    six='X' if x[6] else('O' if y[6] else 6)
    seven='X' if x[7] else('O' if y[7] else 7)
    eight='X' if x[8] else('O' if y[8] else 8)
    print('|----|---|----|')
    print('|',zero,' |',one,'|',two,' |')
    print('|----|---|----|')
    print('|',three,' |',four,'|',five,' |')
    print('|----|---|----|')
    print('|',six,' |',seven,'|',eight,' |')
    print('|----|---|----|')


def CheckWin(x,y):
    pos=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for k in pos:
        if c1=='X' and c2=='O':
            if (sum(x[k[0]],x[k[1]],x[k[2]])==3):
                print(p1,"won the match")
                return 1
            if (sum(y[k[0]],y[k[1]],y[k[2]])==3):
                print(p2,"won the match")
                return 0
            
        if c1=='O' and c2=='X':
            if (sum(x[k[0]],x[k[1]],x[k[2]])==3):           
                print(p2,"won the match")
                return 1
            if (sum(y[k[0]],y[k[1]],y[k[2]])==3):
                print(p1,"won the match")
                return 0
    return -1


ans='s'
while ans.lower()=='s':
 output = ascii_magic.from_image_file("tictactoe.gif", columns=200, char='@')
 ascii_magic.to_terminal(output)
 print()
 output=ascii_magic.from_image_file("images.png",columns=125,char='@')
 ascii_magic.to_terminal(output)
 print()   
 text_speech = pyttsx3.init()
 a = "welcome to tic tac toe game"
 text_speech.setProperty("rate", 110)
 text_speech.say(a)
 text_speech.runAndWait()
 print()

 p1=input("Enter the name of player 1: ").upper()
 print(p1, end='')
 c1=input(" -- What you will take Noughts(O) or Crosses(X) ?: ").upper()
 if c1=='X':
    c2='O'
 if c1=='O':
    c2='X'
 p2=input("Enter the name of player 2: ").upper()
 print(p2,", since",p1,"have taken",c1,"so you have to take",c2,"as there is no other option left for you :)")

 print()

 x=[0,0,0,0,0,0,0,0,0]
 y=[0,0,0,0,0,0,0,0,0]
 turn=1
 while True:
    print()
    PrintBoard(x,y)
   
    if c1=='X' and c2=='O':
        if turn==1:
            print(p1,"'s Chance")
            val=int(input("Enter block number: "))
            if val>8:
                print("Wrong input, please enter correct block number")
                val=int(input("Enter block number: "))
                if val>8:
                    print("Alas! you missed the chance")
                    val=random.randint(0,8)
            x[val]=1
        else:
            print(p2,"'s Chance")
            val=int(input("Enter block number: "))
            if val>8:
                print("Wrong input, please enter correct block number")
                val=int(input("Enter block number: "))
                if val>8:
                    print("Alas! you missed the chance")
                    val=random.randint(0,8)
            y[val]=1
        
    elif c1=='O' and c2=='X':
        if turn==1:
            print(p1,"'s Chance")
            val=int(input("Enter block number: "))
            if val>8:
                print("Wrong input, please enter correct block number")
                val=int(input("Enter block number: "))
                if val>8:
                    print("Alas! you missed the chance")
                    val=random.randint(0,8)
            y[val]=1
        else:
            print(p2,"'s Chance")
            val=int(input("Enter block number: "))
            if val>8:
                print("Wrong input, please enter correct block number")
                val=int(input("Enter block number: "))
                if val>8:
                    print("Alas! you missed the chance")
                    val=random.randint(0,8)
            x[val]=1
        
    else:
       print("# WRONG INPUT !! ...Please don't enter any other letter except 'X' or 'O' ~~")
        
    
    cwin=CheckWin(x,y)
    if cwin!=-1:
        print()        
        output = ascii_magic.from_image_file("autocollants-game-over.jpg", columns=180, char='@')
        ascii_magic.to_terminal(output)        
        print()
        
        text_speech = pyttsx3.init()
        a = "thank you for playing Tic Tac Toe"
        text_speech.setProperty("rate", 110)
        text_speech.say(a)
        text_speech.runAndWait()
        
        output = ascii_magic.from_image_file("how-to-respond-to-thank-you.webp", columns=150, char='@')
        ascii_magic.to_terminal(output)
        
        print()
        ans=input("Press 's' or 'S' to start the game again or Press 'e' or 'E' to exit: ").lower()
        print()
        break
            
    turn=1-turn