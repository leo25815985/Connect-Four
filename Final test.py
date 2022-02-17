#Final project
#Cheng Yu Sung
#10/21/2018

from graphics import*
####Class of player 
class player:
    
    def __init__(self,name,color,num):
        self.name=name
        self.color=color
        self.num=num
        
        self.list=table
    def move(self,win):
        dfs
        

########Drawing Section#####################
def setUpWindow():
    win=GraphWin("Connect 4",800,800)
    win.setBackground("blue")
    win.setCoords(0,0,8,8)
    cir=Circle(Point(.8,.8),0.45)
    cir.setFill("white")
    cir.draw(win)
    #make clones of white circles 
    for i in range(6):
        cirClone=cir.clone()
        cirClone.move(0,i)
        cirClone.draw(win)
        for j in range(7):
            circClone=cirClone.clone()
            circClone.move(j,0)
            circClone.draw(win)
    return win
##def DrawCircle(win,num):
##    Circ=Circle
def GameLabels(win):
    Name=Text(Point(1.3,7.8),"Enter your name:")
    Name.setSize(15)
    Name.setFill("white")
    Name.draw(win)
    p2=Text(Point(1.3,7),"Second player name:")
    p2.setSize(15)
    p2.setFill("white")
    p2.draw(win)

def DrawTitles(win):
    Title1=Text(Point(5,7.8),"Welcome to Connect 4!")
    #Title1.setFace("courier")
    Title1.setFill("white")
    Title1.setSize(20)
    Title1.draw(win)
    Title2=Text(Point(4.8,7.5),"Player vs. Player")
    Title2.setFill("white")
    #Title2.setFace("courier")
    Title2.setSize(20)
    Title2.draw(win)
    
def drawNameBoxes(win):
    
    nameBox=Entry(Point(1.3,7.5),12)
    nameBox.setFill("white")
    nameBox.setText("")
    nameBox.setSize(15)
    nameBox.draw(win)
    nameBox2=Entry(Point(1.3,6.7),12)
    nameBox2.setFill("white")
    nameBox2.setText("")
    nameBox2.setSize(15)
    nameBox2.draw(win)
    #Submit box
    submitBox=Rectangle(Point(2,7.65),Point(2.5,7.35))
    submitBox.setFill("red")
    submitBox.draw(win)
    submitText=Text(Point(2.25,7.5),"Submit")
    submitText.setSize(11)
    submitText.draw(win)
    submitBox2=Rectangle(Point(2,6.85),Point(2.5,6.55))
    submitBox2.setFill("red")
    submitBox2.draw(win)
    submitText2=Text(Point(2.25,6.7),"Submit")
    submitText2.setSize(11)
    submitText2.draw(win)
    #rectangle of submit
    
    return nameBox,nameBox2  
##def OrderBoxes(win):
##    first=Rectangle(Point(3.5,6.9),Point(4,7.15))
##    first.setFill("red")
##    first.draw(win)
##    firsttext=Text(Point(3.75,7.025),"first")
##    firsttext.setSize(11)
##    firsttext.draw(win)
##    second=Rectangle(Point(4.3,6.9),Point(4.8,7.15))
##    second.setFill("red")
##    second.draw(win)
##    secondtext=Text(Point(4.55,7.025),"second")
##    secondtext.setSize(11)
##    secondtext.draw(win)
##### Set up for Column's entry box#####
def Colentrybox(win):
    Col=Text(Point(4.3,7.2),"Column")
    Col.setFill("red")
    Col.setSize(15)
    Col.draw(win)
    
    ColEB=Entry(Point(5,7.2),5)
    ColEB.setFill("white")
    ColEB.setSize(15)
    ColEB.setText("0")
    ColEB.draw(win)
    
    
    return ColEB
##def ButtonBoxes(win):
##    b1=Rectangle(Point(0.35,0.35),Point(1.25,0.1))
##    b1.setFill("red")
##    b1.draw(win)
##    b1text=Text(Point(0.8,0.2),"1")
##    b1text.setSize(16)
##    b1text.draw(win)
##    
##    b2=Rectangle(Point(1.35,0.35),Point(2.25,.1))
##    b2.setFill("red")
##    b2.draw(win)
##    b2text=Text(Point(1.8,0.2),"2")
##    b2text.setSize(16)
##    b2text.draw(win)
##    
##    b3=Rectangle(Point(2.35,0.35),Point(3.25,.1))
##    b3.setFill("red")
##    b3.draw(win)
##    b3text=Text(Point(2.8,0.2),"3")
##    b3text.setSize(16)
##    b3text.draw(win)
##    
##    b4=Rectangle(Point(3.35,0.35),Point(4.25,.1))
##    b4.setFill("red")
##    b4.draw(win)
##    b4=Text(Point(3.8,0.2),"4")
##    b4.setSize(16)
##    b4.draw(win)
##    
##    b5=Rectangle(Point(4.35,0.35),Point(5.25,.1))
##    b5.setFill("red")
##    b5.draw(win)
##    b5=Text(Point(4.8,0.2),"5")
##    b5.setSize(16)
##    b5.draw(win)
##    
##    b6=Rectangle(Point(5.35,0.35),Point(6.25,.1))
##    b6.setFill("red")
##    b6.draw(win)
##    b6=Text(Point(5.8,0.2),"6")
##    b6.setSize(16)
##    b6.draw(win)
##    
##    b7=Rectangle(Point(6.35,0.35),Point(7.25,.1))
##    b7.setFill("red")
##    b7.draw(win)
##    b7=Text(Point(6.8,0.2),"7")
##    b7.setSize(16)
##    b7.draw(win)
    
##    return b1,b2,b3,b4,b5,b6,b7
#################Drawing Section END###################

##def Turn(win,name1,name2,count):
##    
##    Turn=Text(Point(3.8,6.5),"")
##    Turn.setFill("white")
##    Turn.draw(win)
##    
##    if count%2==1:
##        Turn.setText(name1+"'s turn")
##        return name1
##    elif count%2==0:
##        Turn.setText(name2+"'s turn")
##        return name2

#read the choice of namebox when click mouse    
def Readchoice(win,nameBox,nameBox2):
    clickPoint=win.getMouse()
##    x=clickPoint.getX()
##    y=clickPoint.getY()
##    NameCheck=None
##    
##    if 2.5<=x<=2.7 and 7.35<=y<=7.65:
    name1=str(nameBox.getText())
    #there are two boxes
    win.getMouse()
    name2=str(nameBox2.getText())
##        NameCheck=True
##    while checkMouse!=None    
    return name1,name2#,NameCheck
###get the record from the record.txt file
def inputrecord(win,name1):
    input=open("record.txt","r")
    output=open("record.txt","a")
    
    nameValid=None
    #find if the name is in the list
    for line in input:
        line1=line.split(",")
        #if find the name then nameValid is true
        if line1[0]==name1:
            nameValid=True
            #break after find the name
            break
        #if find the name
    if nameValid==True:
        record=Text(Point(1.3,7.15),line1[1]+line1[2].rstrip())
        record.setFill("white")
        record.setSize(15)
        record.draw(win)
        #if not find the name then it will create one
    elif nameValid==None:
        print(name1+",win",0,",lose",0,file=output)
        record=Text(Point(1.3,7.15),"win0,lose0")
        record.setFill("white")
        record.setSize(15)
        record.draw(win)
    #close file    
    input.close()
    output.close()
# repeat action with second name    
def inputrecord2(win,name2):
    input=open("record.txt","r")
    output=open("record.txt","a")
    nameValid=None
    for line in input:
        line1=line.split(",")
        if line1[0]==name2:
            nameValid=True
            break
    if nameValid==True:
        record=Text(Point(1.3,6.35),line1[1]+line1[2].rstrip())
        record.setFill("white")
        record.setSize(15)
        record.draw(win)
    elif nameValid==None:
        print(name2+",win",0,",lose",0,file=output)
        record=Text(Point(1.3,6.35),"win0,lose0")
        record.setFill("white")
        record.setSize(15)
        record.draw(win)
        
    input.close()
    output.close()
    ##############
# read the choice of Column entry box and return that value in int    
def ReadColchoice(win,ColEB):
    win.getMouse()
    Col=int(ColEB.getText())
    return Col
# find if it's valid to be on the board
def checkValid(Col,w):
    onBoard=None
    Full=False
    valid=False
    
    if 1 <=Col<=7:
        onBoard=True
    #check if the column is full    
    for i in range(len(w[Col])):
        if w[Col][5]!=0:
            Full=True
    #if not full and onBoard then it's valid
    if onBoard==True and Full==False:
        valid=True
        
    return valid
# function to clear box when not valid
def clearBoxes(ColEB,win):
       ColEB.setText("0")
#function to check if there is any empty place
def checkFill(w,Col):
    
    for i in range(len(w[Col])):
        if w[Col][i]==0:
            return i
            
#win conditions
#to check win which spent me lots of time
def checkwin(w):
    Win=False
    if (w[0][0]!=0 and w[0][0]==w[1][0] and w[1][0]==w[2][0] and w[2][0]==w[3][0])  or (w[1][0]!=0 and w[1][0]==w[2][0] and w[2][0]==w[3][0] and w[3][0]==w[4][0]) or (w[2][0]!=0 and w[2][0]==w[3][0]and w[3][0]==w[4][0] and w[4][0]==w[5][0] )or (w[3][0]!=0 and w[3][0]==w[4][0] and w[4][0]==w[5][0] and w[5][0]==w[6][0])or (w[0][1]!=0 and w[0][1]==w[1][1] and w[1][1]==w[2][1] and w[2][1]==w[3][1])or (w[1][1]!=0 and w[1][1]==w[2][1] and w[2][1]==w[3][1] and w[3][1]==w[4][1]) or (w[2][1]!=0 and w[2][1]==w[3][1]and w[3][1]==w[4][1] and w[4][1]==w[5][1] )or (w[3][1]!=0 and w[3][1]==w[4][1] and w[4][1]==w[5][1] and w[5][1]==w[6][1])or (w[0][2]!=0 and w[0][2]==w[1][2] and w[1][2]==w[2][2] and w[2][2]==w[3][2] )or (w[1][2]!=0 and w[1][2]==w[2][2] and w[2][2]==w[3][2] and w[3][2]==w[4][2]) or (w[2][2]!=0 and w[2][2]==w[3][2] and w[3][2]==w[4][2] and w[4][2]==w[5][2]) or (w[3][2]!=0 and w[3][2]==w[4][2] and w[4][2]==w[5][2] and w[5][2]==w[6][2])or (w[0][3]!=0 and w[0][3]==w[1][3] and w[1][3]==w[2][3] and w[2][3]==w[3][3])or (w[1][3]!=0 and w[1][3]==w[2][3]and w[2][3]==w[3][3] and w[3][3]==w[4][3]) or (w[2][3]!=0 and w[2][3]==w[3][3] and w[3][3]==w[4][3] and w[4][3]==w[5][3] )or (w[3][3]!=0 and w[3][3]==w[4][3] and w[4][3]==w[5][3] and w[5][3]==w[6][3])or (w[0][4]!=0 and w[0][4]==w[1][4] and w[1][4]==w[2][4] and w[2][4]==w[3][4] )or (w[1][4]!=0 and w[1][4]==w[2][4] and w[2][4]==w[3][4] and w[3][4]==w[4][4])or (w[2][4]!=0 and w[2][4]==w[3][4] and w[3][4]==w[4][4] and w[4][4]==w[5][4]) or (w[3][4]!=0 and w[3][4]==w[4][4] and w[4][4]==w[5][4] and w[5][4]==w[6][4])or (w[0][5]!=0 and w[0][5]==w[1][5] and w[1][5]==w[2][5] and w[2][5]==w[3][5] )or (w[1][5]!=0 and w[1][5]==w[2][5] and w[2][5]==w[3][5] and w[3][5]==w[4][5] )or (w[2][5]!=0 and w[2][5]==w[3][5] and w[3][5]==w[4][5] and w[4][5]==w[5][5])or (w[3][5]!=0 and w[3][5]==w[4][5] and w[4][5]==w[5][5] and w[5][5]==w[6][5])or (w[0][0]!=0 and w[0][0]==w[0][1] and w[0][1]==w[0][2] and w[0][2]==w[0][3] )or (w[0][1]!=0 and w[0][1]==w[0][2] and w[0][2]==w[0][3] and w[0][3]==w[0][4] )or (w[0][2]!=0 and w[0][2]==w[0][3] and w[0][3]==w[0][4] and w[0][4]==w[0][5])or (w[1][0]!=0 and w[1][0]==w[1][1] and w[1][1]==w[1][2] and w[1][2]==w[0][3])or (w[1][1]!=0 and w[1][1]==w[1][2] and w[1][2]==w[1][3] and w[1][3]==w[1][4]) or (w[1][2]!=0 and w[1][2]==w[1][3] and w[1][3]==w[1][4] and w[1][4]==w[1][5])or (w[2][0]!=0 and w[2][0]==w[2][1] and w[2][1]==w[2][2] and w[2][2]==w[2][3] )or (w[2][1]!=0 and w[2][1]==w[2][2] and w[2][2]==w[2][3] and w[2][3]==w[2][4]) or (w[2][2]!=0 and w[2][2]==w[2][3] and w[2][3]==w[2][4] and w[2][4]==w[2][5])or (w[3][0]!=0 and w[3][0]==w[3][1] and w[3][1]==w[3][2] and w[3][2]==w[3][3]) or (w[3][1]!=0 and w[3][1]==w[3][2] and w[3][2]==w[3][3] and w[3][3]==w[3][4]) or (w[3][2]!=0 and w[3][2]==w[3][3] and w[3][3]==w[3][4] and w[3][4]==w[3][5])or (w[4][0]!=0 and w[4][0]==w[4][1] and w[4][1]==w[4][2] and w[4][2]==w[4][3] )or (w[4][1]!=0 and w[4][1]==w[4][2] and w[4][2]==w[4][3] and w[4][3]==w[4][4])or (w[4][2]!=0 and w[4][2]==w[4][3] and w[4][3]==w[4][4] and w[4][4]==w[4][5])or (w[5][0]!=0 and w[5][0]==w[5][1] and w[5][1]==w[5][2] and w[5][2]==w[5][3]) or (w[5][1]!=0 and w[5][1]==w[5][2] and w[5][2]==w[5][3] and w[5][3]==w[5][4] )or (w[5][2]!=0 and w[5][2]==w[5][3] and w[5][3]==w[5][4] and w[5][4]==w[5][5])or (w[6][0]!=0 and w[6][0]==w[6][1] and w[6][1]==w[6][2] and w[6][2]==w[6][3])or (w[6][1]!=0 and w[6][1]==w[6][2] and w[6][2]==w[6][3] and w[6][3]==w[6][4]) or (w[6][2]!=0 and w[6][2]==w[6][3] and w[6][3]==w[6][4] and w[6][4]==w[6][5])or (w[0][0]!=0 and w[0][0]==w[1][1] and w[1][1]==w[2][2] and w[2][2]==w[3][3] )or (w[1][0]!=0 and w[1][0]==w[2][1] and w[2][1]==w[3][2] and w[3][2]==w[4][3] )or (w[2][0]!=0 and w[2][0]==w[3][1] and w[3][1]==w[4][2] and w[4][2]==w[5][3])or (w[3][0]!=0 and w[3][0]==w[4][1] and w[4][1]==w[5][2] and w[5][2]==w[6][3])or (w[0][1]!=0 and w[0][1]==w[1][2] and w[1][2]==w[2][3] and w[2][3]==w[3][4]) or (w[1][1]!=0 and w[1][1]==w[2][2] and w[2][2]==w[3][3] and w[3][3]==w[4][4] )or (w[2][1]!=0 and w[2][1]==w[3][2] and w[3][2]==w[4][3] and w[4][3]==w[5][4] )or (w[3][1]!=0 and w[3][1]==w[4][2] and w[4][2]==w[5][3] and w[5][3]==w[6][4])or (w[0][2]!=0 and w[0][2]==w[1][3] and w[1][3]==w[2][4] and w[2][4]==w[3][5]) or (w[1][2]!=0 and w[1][2]==w[2][3] and w[2][3]==w[3][4] and w[3][4]==w[4][5] )or (w[2][2]!=0 and w[2][2]==w[3][3] and w[3][3]==w[4][4] and w[4][4]==w[5][5]) or (w[3][2]!=0 and w[3][2]==w[4][3] and w[4][3]==w[5][4] and w[5][4]==w[6][5])or (w[0][3]!=0 and w[0][3]==w[1][2] and w[1][2]==w[2][1] and w[2][1]==w[3][0])or (w[1][3]!=0 and w[1][3]==w[2][2] and w[2][2]==w[3][1] and w[3][1]==w[4][0]) or (w[2][3]!=0 and w[2][3]==w[3][2] and w[3][2]==w[4][1] and w[4][1]==w[5][0]) or (w[3][3]!=0 and w[3][3]==w[4][2] and w[4][2]==w[5][1] and w[5][1]==w[6][0])or (w[0][4]!=0 and w[0][4]==w[1][3] and w[1][3]==w[2][2] and w[2][2]==w[3][1]) or (w[1][4]!=0 and w[1][4]==w[2][3] and w[2][3]==w[3][2] and w[3][2]==w[4][1])or (w[2][4]!=0 and w[2][4]==w[3][3] and w[3][3]==w[4][2] and w[4][2]==w[5][1]) or (w[3][4]!=0 and w[3][4]==w[4][3] and w[4][3]==w[5][2] and w[5][2]==w[6][1])or (w[0][5]!=0 and w[0][5]==w[1][4] and w[1][4]==w[2][3] and w[2][3]==w[3][2] )or (w[1][5]!=0 and w[1][5]==w[2][4] and w[2][4]==w[3][3] and w[3][3]==w[4][2]) or (w[2][5]!=0 and w[2][5]==w[3][4] and w[3][4]==w[4][3] and w[4][3]==w[5][2])or (w[3][5]!=0 and w[3][5]==w[4][4] and w[4][4]==w[5][3] and w[5][3]==w[6][2]) :
        Win=True

    return Win
    
    
##def PlayersChoice(win,point,rectangle):
##        ll = rectangle.getP1()  # assume p1 is ll (lower left)
##        ur = rectangle.getP2()  # assume p2 is ur (upper right)
##
##        return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()
##def ClickButton():
##    pass
def main():
#####Set up########
    win=setUpWindow()
    GameLabels(win)
    nameBox,nameBox2=drawNameBoxes(win)
    DrawTitles(win)
    ColEB=Colentrybox(win)
################set up #################
    
#########read name############
    name1,name2=Readchoice(win,nameBox,nameBox2)
    inputrecord(win,name1)
    inputrecord2(win,name2)
    
###########name and input output##########
#####list for connect 4#####
    w=[]
    for i in range(7):
        row=[]
        for j in range(6):
            row.append(0)
        w.append(row)
#########List for connect 4##########
    count=1
    Turn=Text(Point(3.8,6.5),"")
    Turn.setFill("white")
    Turn.draw(win)
    
    a=""
######while loop for the game######
    Win=checkwin(w)
    while Win==False:
        #if and elif is to find out who is the winner and the loser
        #variable to store their name
        if count%2==1:
            Turn.setText(name1+"'s turn")
            a=name1
        elif count%2==0:
            Turn.setText(name2+"'s turn")
            a=name2
            
        if a ==name1:
            loser=name2
        elif a ==name2:
            loser=name1
        #this count is to count the turns
        count+=1
        Col=ReadColchoice(win,ColEB)
        # when not valid it will clear the box
        while not checkValid(Col,w):
            clearBoxes(ColEB,win)
            Col=ReadColchoice(win,ColEB)
        #find if there is an empty place first
        x=checkFill(w,Col)
        # a is the spot that is empty
        w[Col][x]=a
        if count%2==1:
            color="yellow"
        elif count%2==0:
            color="red"
        #draw the circle on that empty spot
        Fill=Circle(Point(Col-.2,x+.8),0.45)
        Fill.setFill(color)
        Fill.draw(win)
        print(w)
        #check win in every turn
        Win=checkwin(w)
    Turn.setText(a+" is the winner.")
    #change the win and lose
    input=open("record.txt","a+")
    for line in input:
        line1=line.split(",")
        if line1[0]==a:
           b=line1[1].split()
           c=int(b[1])
           b[1]=c+1
        
        if line1[0]==loser:
            d=line[2].split()
            e=int(d[1])
            d[1]=e+1
            
    
        
    
##    Player1=player(name1,1,"yellow",win)
##    Player1.move()
main()