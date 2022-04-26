import tkinter as Tkinter
from tkinter import *
from tkinter import ttk
#hockey stick selector
global height
global age
global experience
global budget
global play
global bow
global toe
global mat

print("yooo")

def varTester(testvar):
    try:
        y = float(testvar)
    except:
        errorVar("ERROR INVALID INPUT")

   
def p1enter():
    errorVarClear("ERROR INVALID INPUT")
    errorVarClear("INVALID AGE/EXPERIENCE ")
    errorVarClear("INVALID HEIGHT")
    global height
    global age
    global experience
    global budget
    global play
    h = height_number.get()
    a = age_number.get()
    e = experience_number.get()
    b = budget_number.get()
    varTester(h)
    varTester(a)
    varTester(e)
    varTester(b)
   
    height = float(h)
    age = float(a)
    experience = float(e)
    budget = float(b)
    if experience > age:
        errorVar("INVALID AGE/EXPERIENCE ")
        return
    if height > 260 or height < 80 :
        errorVar("INVALID HEIGHT")
        return
       
    screen.destroy()
    screen2()
   

def hTest():
    global height
    global age
    global experience
    global budget
    global play
    if height < 123:
        return 28
    if height > 122 and height <131:
        return 30
    if height >= 131 and height < 138:
        return 32
    if height >= 138 and height < 153:
        return 34
    if height >= 153 and height <160:
        return 35.5
    if height >=160 and height <175:
        return 36.5
    if height >= 175:
        return 37.5

def material():
    global height
    global age
    global experience
    global budget
    global play
    global mcarbon
       
    mwood = True
    mcarbon = True
    wood = 0
    carbon = 0
    glass = 0
    if age < 13:
        wood = wood +1
        glass = glass +1
    if age > 12 and age <=18:
        glass = glass +1
        carbon = carbon +1
    if experience == 0:
        wood = wood +1
        carbon = carbon -1
        glass = glass +1
    if experience ==1:
        glass =  glass+1
        carbon = carbon +1
    if experience ==2:
        glass =  glass+1
        carbon = carbon +2
    if experience >2:
        glass =  glass+1
        carbon = carbon +2
    if budget <=50:
        carbon = carbon -3
        wood = wood +2
        glass = glass +1
    if budget >50 and budget <= 100:
        carbon = carbon +1
        glass = glass +2
        wood = wood +1
    if budget >100 and budget <= 150:
        carbon = carbon +2
        glass = glass +1
        wood = wood -2
    if budget >150:
        carbon = carbon +3
        glass = glass +1
        wood = wood -3

    if wood <=0 or glass + carbon >4:
        mwood= False
    if carbon <=0 or glass + wood >4:
        mcarbon = False
    if mwood ==  False:
        x =  carbon + glass
        c = (carbon / x) * 100
        c =round(c,1)
        g = (glass /x) *100
        g =  round(g,1)
       
    if mcarbon == False:
        material = "wood and fiberglass"
    else:
        return    
       
def shape():
    global toe
    global bow
    reg = 0
    meg = 0
    low = 0
    short =0
    mid =0
    maxi = 0
    hook = 0
    global height
    global age
    global experience
    global budget
    global play
    global mcarbon
    if var1.get() == 1:
        reg = reg +2
    if experience > 1 and experience < 4:
        reg = reg +1
        meg = meg +2
        low = low+1
    if experience < 2:
        reg = reg +2
        meg = meg +1
        low = low-1
    if experience >=4:
        low = low +2
        meg = meg +1
        reg = reg +1
    if var2.get() == 1:
        short = short +1
        meg = meg +1
        maxi = maxi +1
        mid = mid+1
    if var3.get() == 1:
        reg = reg +1
        low = low +1
        hook = hook +2
        mid = mid +1
        short = short +1
    if var4.get() == 1 or var5.get() == 1:
        meg = meg +1
        low = low +2
        maxi = maxi +2
        hook = hook +1
    if play == 1 :
           maxi = maxi +2
    if play ==2:
           mid = mid +2
    if play ==3:
           short = short+2
    var = {short:"Shorti",mid:"Midi ",maxi:"Maxi",hook:"hook"}
    toe = var.get(max(var))
    var = {reg:"Regular 20mm",meg:"Mega 24.75mm",low:"Low 25mm"}
    bow = var.get(max(var))
       
def p2enter():
    global height
    global age
    global experience
    global budget
    global play
    global lengtht
    p = played.get()
    if p == "Defence":
        play = 1
    elif p =="Midfield":
        play = 2
    elif p == "Attack":
        play = 3
    else:
        play =4

    shape()
    material()
    lengtht = hTest()
    text()


def text():
    global mcarbon
    global toe
    global bow
    global lengtht
    tlength = ("Length :" + str(lengtht))
    ttoe = ("Toe: " + toe)
    tbow = ("Bow: " + bow)
    if mcarbon == True:
        tmaterial = ("\n" + """Material list:
1. Carbon fibre and fibre glass length about 10M of surface area for the
        materials in total
2. Resin for carbon fibre and fibre glass
3. Gelcoat colour any choice for the outside of the hockey stick
4. Spray foam for the inside of the hockey stick 1 (can)
5. Epoxy block for the mould
6. Cnc machine to be able to be used which is big enough for hockey stick
        shape
7. Vacuum bag and vacuum tape as well as a vacuum pump
8. Sandpaper of different grits
9. Fusion 360 (software)
10. S120 bord sealer
11. Curing oven for carbon fibre
12. Pre preg carbon fibre
13. 13 nuts and bolts and washers
14. Grip tape for hockey stick

Instructions

1. Make a 3d model of the hockey stick in fusion 360 and save the file as
        a stl file
2. Position the epoxy block in the cnc machine and then put it out using
        the one side of the hockey stick file to give you half a mould
3. Repeat step 2 for the other half of the mould
4. Now sand down the two halves that were cut by the cnc machine
5. Now you will need to use the board sealer to spray on the epoxy 3-5
        coats will be needed until the epoxy mould is all level
6. Easy composites have a good guide on how to do this if you are unsure
        https://www.easycomposites.co.uk/learning/cnc-machining-epoxy-tooling-
        board
7. Now we will begin to make the mould for the hockey stick
8. Start by taking the carbon fibre pre preg and laying it out on the
        epoxy resin board building it up layer by layer you want two layers
        realistically or enough till it feels strong enough including making
        sure you have the bolts in so there will be holes for them later
        on now but this in a vacuum bag and attach the vacuum pump to remove
        all the air and then place in the curing oven.
9. Remove from the curing oven and remove the vacuum bag
10. Apply grip tape to the handle
""")
    else:
        tmaterial = ("\n" + """Material list :
1. Wood
2. Fibre glass
3. Epoxy for fibre glass
4. Sand paper
5. Saw
6. plane
Instruction on how to build it
1. Take your wood and sand it down to the dimension s recommended above
2. Cover the wooden hockey stick in wood varnish
3. When dry layer on the fibre glass add epoxy to the fibre glass and add the next layer aim for 5-10 layers
4. When the fibre glass has finished apply the grip tape to the handle
5. Your hockey stick is finished
""")
    texti = (tlength + "\n" + ttoe +"\n"+ tbow + "\n" +tmaterial)
    print(texti)


       
def screen1():
    global screen
    global height_number
    global age_number
    global experience_number
    global budget_number
    print(1)

    screen = Tk()

    print(screen)
    screen.geometry("360x350")
    screen.title("Hockey Stick Guide")
    Label(text = "Basic Information", bg = "#ed890e", width = "40", height = "2", font = ("Calibri", 13)).grid(row = 1, columnspan = 3)
    screen.configure(bg ="#2e2f3b")
    Label(text = "", bg = "#2e2f3b").grid(row =2, column= 0)
    screen.resizable(False, False)

    height = StringVar()
    Label(text = "Height (cm): ", bg = "#ed890e" , font = ("Calibri", 13)).grid(row =3, column= 0)
    height_number = Entry(screen, textvariable=height)
    height_number.grid(row = 3, column = 1)

    Label(text = "", bg = "#2e2f3b",  font = ("Calibri", 2)).grid(row =4, column= 0)

    age = StringVar()
    Label(text = "Age (Years): ", bg = "#ed890e" , font = ("Calibri", 13)).grid(row =5, column= 0)
    age_number = Entry(screen, textvariable=age)
    age_number.grid(row = 5, column = 1)

    Label(text = "", bg = "#2e2f3b", font = ("Calibri", 2)).grid(row =6, column= 0)

    experience= StringVar()
    Label(text = "Experience (years) :", bg = "#ed890e" , font = ("Calibri", 13)).grid(row =7, column= 0)
    experience_number = Entry(screen, textvariable=experience)
    experience_number.grid(row = 7, column = 1)

    Label(text = "", bg = "#2e2f3b" , font = ("Calibri", 2)).grid(row =8, column= 0)
   

    budget = StringVar()
    Label(text = "Budget (£) :", bg = "#ed890e" , font = ("Calibri", 13)).grid(row =9, column= 0)
    budget_number = Entry(screen, textvariable=budget)
    budget_number.grid(row = 9, column = 1)


    Label(text = "", bg = "#2e2f3b" , font = ("Calibri", 2)).grid(row =10, column= 0)

    enter = Button(text = "Next -->",height = "2", width = "18", command  = p1enter)
    enter.grid(row = 11, columnspan = 3)
    screen.mainloop()


def screen2():
    global screen2
    global played
    global var1
    global var2
    global var3
    global var4
    global var5
    global var6


    screen2 = Tk()
    screen2.geometry("360x350")
    screen2.title("Hockey Stick Guide")
    Label(text = "Extra Information", bg = "#ed890e", width = "40", height = "2", font = ("Calibri", 13)).grid(row = 1, columnspan = 2)
    screen2.configure(bg ="#2e2f3b")
    Label(text = "", bg = "#2e2f3b").grid(row =2, column= 0)
    screen2.resizable(False, False)
   

    Label(text = "Position :", bg = "#ed890e", font = ("Calibri", 13)).grid(row =4, column= 0)
    played = StringVar()
    main_menu = OptionMenu(screen2, played,"Defence","Midfield","Attack")
    main_menu.config(bg = "#ed890e")
    main_menu.grid(row = 4, column = 1)

    Label(text = "", bg = "#2e2f3b", font = ("Calibri", 2)).grid(row =5, column= 0)
   
    var1 = Tkinter.IntVar()#nothing
    var2 = Tkinter.IntVar()#power
    var3 = Tkinter.IntVar()#control
    var4 = Tkinter.IntVar()#flicking
    var5 = Tkinter.IntVar()#ariels
    var6 = Tkinter.IntVar()#keeper
    c1 = Tkinter.Checkbutton(screen2, text='Nothing',variable=var1, onvalue=1, offvalue=0, bg = "#ed890e", font = ("Calibri", 13))
    c1.grid(row = 6, column = 0)
    c2 = Tkinter.Checkbutton(screen2, text='Power',variable=var2, onvalue=1, offvalue=0, bg = "#ed890e", font = ("Calibri", 13))
    c2.grid(row = 6, column = 1)
    Label(text = "", bg = "#2e2f3b", font = ("Calibri", 2)).grid(row =7, column= 0)
    c3 = Tkinter.Checkbutton(screen2, text='Control',variable=var3, onvalue=1, offvalue=0, bg = "#ed890e", font = ("Calibri", 13))
    c3.grid(row = 8, column = 0)
    c4 = Tkinter.Checkbutton(screen2, text='Flicking',variable=var4, onvalue=1, offvalue=0, bg = "#ed890e", font = ("Calibri", 13))
    c4.grid(row = 8, column = 1)
    Label(text = "", bg = "#2e2f3b", font = ("Calibri", 2)).grid(row =9, column= 0)
    c5 = Tkinter.Checkbutton(screen2, text='Aerials',variable=var5, onvalue=1, offvalue=0, bg = "#ed890e", font = ("Calibri", 13))
    c5.grid(row = 10, column = 0)
    c6 = Tkinter.Checkbutton(screen2, text='Keeper',variable=var6, onvalue=1, offvalue=0, bg = "#ed890e", font = ("Calibri", 13))
    c6.grid(row = 10, column = 1)

    Label(text = "", bg = "#2e2f3b", font = ("Calibri", 2)).grid(row =11, column= 0)

    enter = Button(text = "Finish",height = "2", width = "18", command  = p2enter)
    enter.grid(row = 12, columnspan = 2)
def errorVar(output):
    Label(text = output, fg ="red", bg = "#2e2f3b", font = ("Calibri",16 )).grid(row =12, columnspan = 2)
def errorVarClear(output):
    Label(text = output, fg ="#2e2f3b", bg = "#2e2f3b", font = ("Calibri",16 )).grid(row =12, columnspan = 2)

print(2)

screen1()
print("after open")