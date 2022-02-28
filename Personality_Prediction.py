from tkinter import *
from tkinter import messagebox
global Prerna,Butola,fl

def sumDigits(n):
    if n< 10:
        return n
    else:
        return n%10 + sumDigits(n//10)

def S():
    SoFn=0
    SoLn=0
    #Declaring variables globally so that they can be accessed easily
    global Prerna,Butola,fl
    Prerna,Butola = str(fl.get()).split()

    #Checking the alphabets of first name
    for i in range(0,len(Prerna)):
        if Prerna[i] in  "ajsAJS":SoFn+=1
        elif Prerna[i] in  "bktBKT":SoFn+=2
        elif Prerna[i] in  "cluCLU":SoFn+=3
        elif Prerna[i] in  "dmvDMV":SoFn+=4
        elif Prerna[i] in  "enwENW":SoFn+=5
        elif Prerna[i] in  "foxFOX":SoFn+=6
        elif Prerna[i] in  "gpyGPY":SoFn+=7
        elif Prerna[i] in  "hqzHQZ":SoFn+=8
        elif Prerna[i] in  "irIR":SoFn+=9

    #Checking the alphabets of second name
    for i in range(0,len(Butola)):
        if Butola[i] in  "ajsAJS":SoLn+=1
        elif Butola[i] in  "bktBKT":SoLn+=2
        elif Butola[i] in  "cluCLU":SoLn+=3
        elif Butola[i] in  "dmvDMV":SoLn+=4
        elif Butola[i] in  "enwENW":SoLn+=5
        elif Butola[i] in  "foxFOX":SoLn+=6
        elif Butola[i] in  "gpyGPY":SoLn+=7
        elif Butola[i] in  "hqzHQZ":SoLn+=8
        elif Butola[i] in  "irIR":SoLn+=9

    SoFn = sumDigits(SoFn)
    SoLn = sumDigits(SoLn)
    sum3 = SoFn + SoLn
    if sum3 not in (11,22):
        sum3 = sumDigits(sum3)

    #Messagebox is used to show a new box or window which contains the information
    if sum3 == 1:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Motivated, attentive to details, ambitious, self-confident, pioneering, independent\n\n The negative impact of yours on others is: Self-centered and Aggressive")
                
    elif sum3 == 2:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Cooperative, modest, hard-working, empathetic, diplomatic\n\n The negative impact of yours on others is: Overly sensitive, uncertain, shy")
            
    elif sum3 == 3:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Artistic, entertaining, imaginative, social, inspiring, expressive, joyful\n\n The negative impact of yours on others is: Superficial, scattered")
                
    elif sum3 == 4:
        messagebox.showinfo(Prerna +  Butola,"The positive side of your personality is: Organized, practical, technical, honest, steady-minded\n\n The negative impact of yours on others is: Stubborn, inflexible")
            
    elif sum3 == 5:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Adaptable, personable, flexible, visionary, adventurous\n\n The negative impact of yours on others is: Impatient, unorganized, overcommitted")
        
    elif sum3 == 6:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Just, considerate, giving, nurturing, protective, responsible, balanced, empathetic\n\n The negative impact of yours on others is: Self-sacrificing, interfering")

    elif sum3 == 7:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Thoughtful, contemplative, rational, analytical, aware, understanding, studious\n\n The negative impact of yours on others is: Introverted, critical")
        
    elif sum3 == 8:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Efficient, well-planned, achieving, status-oriented, practical, power-seeking\n\n The negative impact of yours on others is: Over-ambitious, materialistic")
        
    elif sum3 == 9:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Caring, sensitive, creative, giving, humanitarian, selfless, creative\n\n The negative impact of yours on others is: Withdrawn, not open with one's self or others")
        
    if sum3 == 10:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Motivated, attentive to details, ambitious, self-confident, pioneering, independent\n\n The negative impact of yours on others is: Self-centered and Aggressive")
        
    elif sum3 == 11:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Inventive, intuitive, visionary\n\n The negative impact of yours on others is: Emotional, unsatisfied")
        
    elif sum3 == 22:
        messagebox.showinfo(Prerna + Butola,"The positive side of your personality is: Successful, spiritual, controlled, powerful\n\n The negative impact of yours on others is: Controlling, insensitive")

#Building the GUI 
P = Tk()
P.geometry("1500x700")
P.resizable(0,0)
P.title('PERSONALITY PREDICTION USING FULL NAME')
se = PhotoImage(file = r"C:\Users\ASUS\Downloads\logo (1).png")
bg = PhotoImage(file = r"C:\Users\ASUS\Downloads\unnamed.png")
backg = Canvas(P)
Search = Frame(backg,bg = "GREY")

fl = StringVar()
#name = Entry(P,textvariable=fl)
Label(Search,text = "SUBMIT YOUR FULL NAME: ",bg= "GREY",fg = "WHITE",font  = ("Algerian",30)).grid(row = 0,column = 0)
Entry(Search,bg = "GREY5",textvariable= fl,fg = "#ffffff",width = 50,font = 25).grid(row=1,column = 0)
Button(Search,text = "Click Me",borderwidth=5,command = S,activebackground="GREY",height=2,width = 8).grid(row=1,column=2,padx=(20,0))

backg.create_image(0,0,image = bg,anchor = NW)
backg.create_image(150,100,image = se)
backg.create_window(800,100,window = Search)
backg.pack(fill = "both",expand = True)
#name.pack()

P.mainloop()
