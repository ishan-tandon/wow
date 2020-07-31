import Tkinter
import tkMessageBox
from Tkinter import*
from PIL import ImageTk, Image
import os
doublecolor1="white"
doublecolor2="white"
#introduction
root=Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.config(background="black")
img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
panel = Label(root, image = img,bg="black")
panel.grid(row=0,column=0,rowspan=5,columnspan=18)
Label(root,fg="white",bg="black",text="The Year was 2016\nA study into Graitational Waves left 50 scientists at CERN exposed to deep space delta \
radiation which mutated the DNA of 18 top-secret Researchers.\nThese mutations, gave these humans power:-Power to alter nature accoding to their needs.\
 These men, now with 'superpowers', vowed to keep their identity hidden. They formed a society which helped shape the next 100 years of Human History.\n \
 They call themselves  the 'Wavelength Intensified Zenith Alternating Research Division', or W.I.Z.A.R.D.s  ").grid(row=6,sticky=W)
Label(root,fg="white",bg="black",text="All was peaceful until a group of W.I.Z.A.R.D.s rebelled, and killed 1.5 Billion Civillians, thus starting,:\n\
 The War of W.I.Z.A.R.D.s").grid(row=7)
Label(root,fg="white",bg="black",text="A W.I.Z.A.R.D. has 2 powers- XP and HP\nFor any W.I.Z.A.R.D. duel, each one starts with 100 XP and 100HP.\n\
W.I.Z.A.R.D.s use XP to alter nature and perform 'Spell'. This may damage their oppenents HP. Damaging HP increases ones XP. Every time a spell is executed\
\n, a W.I.Z.A.R.D is awarded 10 XP\nFinish your opponents HP to win! ").grid(row=8)
def close_window ():
    root.destroy()
button = Button (root, text = "Are you Ready to Fight?", command = close_window).grid(row=9)
root.mainloop()
choice=1
Player1="Login and Play!"
Player2="Login and Play!"
chno1=0
chno2=0
chlist=[["","",""],["Azimuth",100,100],["Vega",160,70],["Troll",50,175],["Wenger",0,200]]
while True:
    if choice==1:
        import Tkinter
        import tkMessageBox
        from Tkinter import*
        from PIL import ImageTk, Image
        import os
        root=Tk()
        root.overrideredirect(True)
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.config(background="black")
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Label(root, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        Label(root,text=Player1,fg="white",bg="black",font=25).grid(row=5,column=0,columnspan=2)
        Label(root,text=Player2,fg="white",bg="black",font=25).grid(row=5,column=17,columnspan=2)
        def close_window (x):
            global choice
            root.destroy()
            choice=x
        state=DISABLED
        if Player1!="Login and Play!" and Player2!="Login and Play!":
            if chno1>0 and chno2>0:
                state=ACTIVE
        button9 = Button (root, text = "Enter the War",bg="black",fg="white",state=state,width=52,height=2, command = lambda: close_window(9)).grid(row=11,column=6,columnspan=6)
        button8 = Button (root, text = "Create your Free Account Here!",bg="black",fg="white",width=52,height=2, command = lambda: close_window(8)).grid(row=10,column=6,columnspan=6)
        Nch1=chlist[chno1][0]
        Xch1=chlist[chno1][1]
        Hch1=chlist[chno1][2]
        chLabel11=Label(root,text="Character:- "+Nch1,bg="black",fg="white",font=15).grid(row=7,column=0,columnspan=2)
        chLabel12=Label(root,text="Starting XP:- "+str(Xch1),bg="black",fg="white",font=15).grid(row=8,column=0,columnspan=2)
        chLabel13=Label(root,text="Max HP:- "+str(Hch1),bg="black",fg="white",font=15).grid(row=9,column=0,columnspan=2)
        Nch2=chlist[chno2][0]
        Xch2=chlist[chno2][1]
        Hch2=chlist[chno2][2]
        chLabel21=Label(root,text="Character:- "+Nch2,bg="black",fg="white",font=15).grid(row=7,column=16,columnspan=2)
        chLabel22=Label(root,text="Starting XP:- "+str(Xch2),bg="black",fg="white",font=15).grid(row=8,column=16,columnspan=2)
        chLabel23=Label(root,text="Max HP:- "+str(Hch2),bg="black",fg="white",font=15).grid(row=9,column=16,columnspan=2)
        if Player1=="Login and Play!":
            button2 = Button (root, text = "Login Player 1",bg="black",fg="white",width=21,height=2, command = lambda: close_window(2)).grid(row=7,column=6,columnspan=3)
            button4 = Button (root, text = "Choose your Character",state=DISABLED,bg="black",fg="white",width=21,height=2, command = lambda: close_window(4)).grid(row=8,column=6,columnspan=3)
            button6 = Button (root, text = "Upgrade Your Spells",state=DISABLED,bg="black",fg="white",width=21,height=2, command = lambda: close_window(6)).grid(row=9,column=6,columnspan=3)
        else:
            button2 = Button (root, text = "Change Player 1",bg="black",fg="white",width=21,height=2, command = lambda: close_window(2)).grid(row=7,column=6,columnspan=3)
            if chno1==0:
                text="Choose your Character"
            else:
                text="Change your Character"
            button4 = Button (root, text = text,bg="black",fg="white",width=21,height=2, command = lambda: close_window(4)).grid(row=8,column=6,columnspan=3)
            button6 = Button (root, text = "Upgrade Your Spells",bg="black",fg="white",width=21,height=2, command = lambda: close_window(6)).grid(row=9,column=6,columnspan=3)
        if Player2=="Login and Play!":
            button3 = Button (root, text = "Login Player 2",bg="black",fg="white",width=21,height=2, command = lambda: close_window(3)).grid(row=7,column=9,columnspan=3)
            button5 = Button (root, text = "Choose your Character",state=DISABLED,bg="black",fg="white",width=21,height=2, command = lambda: close_window(5)).grid(row=8,column=9,columnspan=3)
            button7= Button (root, text = "Upgrade Your Spells",state=DISABLED,bg="black",fg="white",width=21,height=2, command = lambda: close_window(7)).grid(row=9,column=9,columnspan=3)
        else:
            button3 = Button (root, text = "Change Player 2",bg="black",fg="white",width=21,height=2, command = lambda: close_window(3)).grid(row=7,column=9,columnspan=3)
            if chno2==0:
                text="Choose your Character"
            else:
                text="Change your Character"
            button5 = Button (root, text = text,bg="black",fg="white",width=21,height=2, command = lambda: close_window(5)).grid(row=8,column=9,columnspan=3)
            button7= Button (root, text = "Upgrade Your Spells",bg="black",fg="white",width=21,height=2, command = lambda: close_window(7)).grid(row=9,column=9,columnspan=3)
        root.mainloop()
    if choice==2:
        login=open("Login.txt","r")
        x=login.readlines()
        login.close()
        for i in range(len(x)):
            x[i]=x[i][0:-1]
            x[i]=x[i].split(" ")
        un=""
        pw=""
        from Tkinter import *
        def Login(L):
            master = Tk()
            import Tkinter
            import tkMessageBox
            from PIL import ImageTk, Image
            import os
            master.overrideredirect(True)
            master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
            Tkinter.Label(text=L,fg="white",bg="black",height=2,width=80,font=100).grid(row=7,column=5,columnspan=8)
            Tkinter.Label(text="Player 1 Login",fg="white",bg="black",height=2,width=80,font=100).grid(row=6,column=5,columnspan=8)
            Tkinter.Label(text="Username",fg="white",bg="black",height=2,width=28,font=100).grid(row=8,column=7,sticky=E)
            Tkinter.Label(text="Password",fg="white",bg="black",height=2,width=28,font=100).grid(row=9,column=7,sticky=E)
            master.config(background="black")
            img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
            panel = Tkinter.Label(master, image = img,bg="black")
            panel.grid(row=0,column=0,rowspan=5,columnspan=18)
            e = Tkinter.Entry(master,bg="black",fg="white",width=28,font=100)
            e.grid(row=8,column=9,sticky=W)
            p=Tkinter.Entry(master,show="*",fg="white",bg="black",width=28,font=100)
            p.grid(row=9,column=9,sticky=W)
            e.focus_set()

            def callback():
                global un,pw
                un=e.get()
                pw=p.get()
                master.destroy()
            def callbackq():
                master.destroy()
                un=""
                choice=1

            b = Button(master, text="Login",fg="white",bg="black",command=callback,height=2,width=56,font=100)
            b.grid(row=10,column=5,columnspan=8)
            bq = Button(master, text="Back",fg="white",bg="black",command=callbackq,height=2,width=56,font=100)
            bq.grid(row=12,column=5,columnspan=8)
            mainloop()
        Login("Welcome to War of W.I.Z.A.R.D.S")
        if un!="":
            def Checker():
                global x,un,pw
                m=-1
                for i in range(len(x)):
                    if x[i][0]==un:
                        if x[i][1]==pw:
                            if x[i][0]!=Player2:
                                m+=1
                return m
            j=Checker()
            while j<0:
                Login("Username/Password does not Match. Try again or Create new account")
                j=Checker()
            Player1=un
        choice=1
    elif choice==3:
        login=open("Login.txt","r")
        x=login.readlines()
        login.close()
        for i in range(len(x)):
            x[i]=x[i][0:-1]
            x[i]=x[i].split(" ")
        un=""
        pw=""
        from Tkinter import *
        def Login(L):
            master = Tk()
            import Tkinter
            import tkMessageBox
            from PIL import ImageTk, Image
            import os
            master.overrideredirect(True)
            master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
            Tkinter.Label(text=L,fg="white",bg="black",height=2,width=80,font=100).grid(row=7,column=5,columnspan=8)
            Tkinter.Label(text="Player 2 Login",fg="white",bg="black",height=2,width=80,font=100).grid(row=6,column=5,columnspan=8)
            Tkinter.Label(text="Username",fg="white",bg="black",height=2,width=28,font=100).grid(row=8,column=7,sticky=E)
            Tkinter.Label(text="Password",fg="white",bg="black",height=2,width=28,font=100).grid(row=9,column=7,sticky=E)
            master.config(background="black")
            img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
            panel = Tkinter.Label(master, image = img,bg="black")
            panel.grid(row=0,column=0,rowspan=5,columnspan=18)
            e = Tkinter.Entry(master,bg="black",fg="white",width=28,font=100)
            e.grid(row=8,column=9,sticky=W)
            p=Tkinter.Entry(master,show="*",fg="white",bg="black",width=28,font=100)
            p.grid(row=9,column=9,sticky=W)
            e.focus_set()

            def callback():
                global un,pw
                un=e.get()
                pw=p.get()
                master.destroy()
            def callbackq():
                master.destroy()
                un=""
                choice=1

            b = Button(master, text="Login",fg="white",bg="black",command=callback,height=2,width=56,font=100)
            b.grid(row=10,column=5,columnspan=8)
            bq = Button(master, text="Back",fg="white",bg="black",command=callbackq,height=2,width=56,font=100)
            bq.grid(row=12,column=5,columnspan=8)
            mainloop()
        Login("Welcome to War of W.I.Z.A.R.D.S")
        if un!="":
            def Checker():
                global x,un,pw
                m=-1
                for i in range(len(x)):
                    if x[i][0]==un:
                        if x[i][1]==pw:
                            if x[i][0]!=Player1:
                                m+=1
                return m
            j=Checker()
            while j<0:
                Login("Username/Password does not Match or is already logged on. Try again or Create new account")
                j=Checker()
            Player2=un
        choice=1
    elif choice==4:
        import Tkinter
        import tkMessageBox
        from PIL import ImageTk, Image
        import os
        master = Tk()
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        Tkinter.Label(text="Choose Your Character",fg="white",bg="black",height=2,width=80,font=100).grid(row=7,column=5,columnspan=8)
        master.config(background="black")
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Tkinter.Label(master, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        def callback(x):
            global chno1
            master.destroy()
            chno1=x
        Azimuth = Button(master, text="Azimuth\nType:-Warrior\nStarting XP:-100\nMax HP:-100",fg="white",bg="black",command=lambda: callback(1),height=8,width=18,font=100).grid(row=8,column=0,columnspan=2,rowspan=2,sticky=W)
        Vega = Button(master, text="Vega\nType:-Mage\nStarting XP:-160\nMax HP:-70",fg="white",bg="black",command=lambda: callback(2),height=8,width=18,font=100).grid(row=8,column=2,columnspan=2,rowspan=2,sticky=W)
        Troll = Button(master, text="Troll\nType:-Tank\nStarting XP:-50\nMax HP:-175",fg="white",bg="black",command=lambda: callback(3),height=8,width=18,font=100).grid(row=8,column=4,columnspan=2,rowspan=2,sticky=W)
        Wenger = Button(master, text="Wenger\nType:-Wall\nStarting XP:-0\nMax HP:-200",fg="white",bg="black",command=lambda: callback(4),height=8,width=18,font=100).grid(row=8,column=6,columnspan=2,rowspan=2,sticky=W)
        mainloop()
        choice=1
    elif choice==5:
        import Tkinter
        import tkMessageBox
        from PIL import ImageTk, Image
        import os
        master = Tk()
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        Tkinter.Label(text="Choose Your Character",fg="white",bg="black",height=2,width=80,font=100).grid(row=7,column=5,columnspan=8)
        master.config(background="black")
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Tkinter.Label(master, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        def callback(x):
            global chno2
            master.destroy()
            chno2=x
        Azimuth = Button(master, text="Azimuth\nType:-Warrior\nStarting XP:-100\nMax HP:-100",fg="white",bg="black",command=lambda: callback(1),height=8,width=18,font=100).grid(row=8,column=0,columnspan=2,rowspan=2,sticky=W)
        Vega = Button(master, text="Vega\nType:-Mage\nStarting XP:-160\nMax HP:-70",fg="white",bg="black",command=lambda: callback(2),height=8,width=18,font=100).grid(row=8,column=2,columnspan=2,rowspan=2,sticky=W)
        Troll = Button(master, text="Troll\nType:-Tank\nStarting XP:-50\nMax HP:-175",fg="white",bg="black",command=lambda: callback(3),height=8,width=18,font=100).grid(row=8,column=4,columnspan=2,rowspan=2,sticky=W)
        Wenger = Button(master, text="Wenger\nType:-Wall\nStarting XP:-0\nMax HP:-200",fg="white",bg="black",command=lambda: callback(4),height=8,width=18,font=100).grid(row=8,column=6,columnspan=2,rowspan=2,sticky=W)
        mainloop()
        choice=1
    elif choice==6:
        import Tkinter
        import tkMessageBox
        from PIL import ImageTk, Image
        import os
        master = Tk()
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        Tkinter.Label(text="Spell Levels and Upgrades Coming Soon!",fg="white",bg="black",height=2,width=80,font=100).grid(row=7,column=5,columnspan=8)
        master.config(background="black")
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Tkinter.Label(master, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        def callback(x):
            master.destroy()
        Return = Button(master, text="Return",fg="white",bg="black",command=lambda: callback(1),height=20,width=100,font=100).grid(row=8,column=0,columnspan=18,rowspan=5)
        mainloop()
        choice=1
    elif choice==7:
        import Tkinter
        import tkMessageBox
        from PIL import ImageTk, Image
        import os
        master = Tk()
        master.overrideredirect(True)
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        Tkinter.Label(text="Spell Levels and Upgrades Coming Soon!",fg="white",bg="black",height=2,width=80,font=100).grid(row=7,column=5,columnspan=8)
        master.config(background="black")
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Tkinter.Label(master, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        def callback(x):
            master.destroy()
        Return = Button(master, text="Return",fg="white",bg="black",command=lambda: callback(1),height=20,width=160,font=100).grid(row=8,column=0,columnspan=18,rowspan=5)
        mainloop()
        choice=1
    elif choice==8:
        login=open("Login.txt","r")
        x=login.readlines()
        login.close()
        for i in range(len(x)):
            x[i]=x[i][0:-1]
            x[i]=x[i].split(" ")
        un=""
        pw=""
        from Tkinter import *
        def MakeID(L):
            import Tkinter
            import tkMessageBox
            from PIL import ImageTk, Image
            import os
            master = Tk()
            master.overrideredirect(True)
            master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
            Tkinter.Label(text=L,fg="white",bg="black",height=2,width=80,font=100).grid(row=7,column=5,columnspan=8)
            Tkinter.Label(text="Welcome to War of W.I.Z.A.R.D.S",fg="white",bg="black",height=2,width=80,font=100).grid(row=6,column=5,columnspan=8)
            Tkinter.Label(text="Username",fg="white",bg="black",height=2,width=28,font=100).grid(row=8,column=7,sticky=E)
            Tkinter.Label(text="Password",fg="white",bg="black",height=2,width=28,font=100).grid(row=9,column=7,sticky=E)
            master.config(background="black")
            img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
            panel = Tkinter.Label(master, image = img,bg="black")
            panel.grid(row=0,column=0,rowspan=5,columnspan=18)
            e = Tkinter.Entry(master,bg="black",fg="white",width=28,font=100)
            e.grid(row=8,column=9,sticky=W)
            p=Tkinter.Entry(master,show="*",fg="white",bg="black",width=28,font=100)
            p.grid(row=9,column=9,sticky=W)
            e.focus_set()
            def callback():
                global un,pw
                un=e.get()
                pw=p.get()
                master.destroy()
            b = Button(master, text="Create your free War of W.I.Z.A.R.D.S id today!",fg="white",bg="black",command=callback,height=2,width=56,font=100)
            b.grid(row=10,column=5,columnspan=8)
            mainloop()
        MakeID("Create Your War of Wizards Account!")
        def usernamecheck():
            global un,x
            m=0
            for i in x:
                if i[0]==un:
                    m+=1
            if m==0:
                return 1
            else:
                return 0
        j=usernamecheck()
        while j!=1:
            MakeID("Username Already Taken")
            j=usernamecheck()
        m=un+" "+pw+" "+"1 0\n"
        filee=open("Login.txt","a")
        filee.write(m)
        filee.close()
        if Player1=="Login and Play!":
            Player1=un
        elif Player2=="Login and Play!":
            Player2=un
        choice=1
    elif choice==9:
        break
#game code
import Tkinter
import tkMessageBox
from Tkinter import*
from PIL import ImageTk, Image
import os
class alpha1:
    from PIL import ImageTk, Image
    import os
    def __init__(self,x,pe1,pe2,l,se1,se2):

        p1=pe1[0]
        hp1=pe1[1]
        Hp1=pe1[2]
        xp1=pe1[3]
        c1=pe1[4]
        p2=pe2[0]
        hp2=pe2[1]
        Hp2=pe2[2]
        xp2=pe2[3]
        c2=pe2[4]
        root = Tk()
        root.overrideredirect(True)
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.config(background="black")
        self.topLabel = Label(root, text = "Click the Spell Name\nyou would like information about.", font=25,fg="white",bg="black")
        self.topLabel.grid(row=7,column=7,columnspan=4)
        self.infoLine = Label(root, text = "", justify = 'left',fg="white",bg="black")
        self.infoLine.grid(row=8,column=7,columnspan=4,rowspan=5)
        color1=color2="white"
        if x==1:
            color1="red"
        elif x==2:
            color2="red"
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Label(root, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        Label(root,text=p1,bg="black",font=35,fg=color1).grid(row=5,column=0)
        Label(root,text=p2,bg="black",fg=color2,font=35).grid(row=5,column=17)
        Label(root,text=c1,bg="black",fg="white").grid(row=6,column=0)
        Label(root,text=c2,bg="black",fg="white").grid(row=6,column=17)
        Label(root,text=("HP:- "+hp1+"/"+str(Hp1)),fg="white",bg="black",font=20).grid(row=7,column=0)
        Label(root,text=("HP:- "+hp2+"/"+str(Hp2)),fg="white",bg="black",font=20).grid(row=7,column=17)
        Label(root,text=("XP:- "+xp1),fg="white",bg="black",font=20).grid(row=8,column=0)
        Label(root,text=("XP:- "+xp2),fg="white",bg="black",font=20).grid(row=8,column=17)
        Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=0)
        Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=17)
        p1,b1,t1=se1
        p2,b2,t2=se2
        p1,b1,t1,p2,b2,t2=int(p1),int(b1),int(t1),int(p2),int(b2),int(t2)
        if p1==b1==t1==0:
            Label(root,text="None",fg="white",bg="black").grid(row=10,column=0)
        if p2==b2==t2==0:
            Label(root,text="None",fg="white",bg="black").grid(row=10,column=17)
        if p1!=0:
            Label(root,text="Poison Spell:- "+str(p1)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=0,columnspan=4,sticky=W)
        if p2!=0:
            Label(root,text="Poison Spell:- "+str(p2)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=15,columnspan=4,sticky=W)
        if b1!=0:
            Label(root,text="Burn Spell:- "+str(b1)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=0,columnspan=4,sticky=W)
        if b2!=0:
            Label(root,text="Burn Spell:- "+str(b2)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=15,columnspan=4,sticky=W)
        if t1!=0:
            Label(root,text="Torture Spell:- "+str(t1)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=0,columnspan=4,sticky=W)
        if t2!=0:
            Label(root,text="Torture Spell:- "+str(t2)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=15,columnspan=4,sticky=W)
        Button(root, text = "Close",width=11,height=2, command =lambda : self.close_window(root),fg="white",bg="black").grid(row=19,column=10)
        attack = [('Fireball', 'Fireball', 'Single Turn Attack Spell\nCost:5XP\nAttack:10HP'),('Lightning Spell', 'Lightning Spell', 'Single Turn Attack Spell\nCost:10XP\nAttack:20HP'),('Tornado', 'Tornado', 'Single Turn Attack Spell\nCost:75XP\nAttack:50HP'),('Killing Curse', 'Killing Curse', 'Single Turn Attack Spell\nCost:300XP\nAttack:100HP')]
        r = 7
        c = 7
        for b in attack:
            Button(root,text=b[0],width=11,height=2, bg="black",fg="white",command=lambda text=b:self.name(text)).grid(row=r,column=c)
            print "",
            r += 1
            if r > 13:
                r = 1
                c += 1
        defense = [('Mini Shield', 'Mini Shield', 'Single Turn Defence Spell\nCost:5XP\nShield From:10HP'),('Small Shield', 'Small Shield', 'Single Turn Defence Spell\nCost:10XP\nShield From:20HP'),('Medium Shield', 'Medium Shield', 'Single Turn Defence Spell\nCost:50XP\nShield From:50HP'),('Big Shield', 'Big Shield', 'Single Turn Defence Spell\nCost:200XP\nShield From:100HP')]
        r = 7
        c = 10
        for b in defense:
            Button(root,text=b[0],width=11,height=2, bg="black",fg="white",command=lambda text=b:self.name(text)).grid(row=r,column=c)
            r += 1
            if r > 13:
                r = 1
                c += 1
        status1 = [('Poison Spell', 'Poison Spell', '5-Turn Offensive Status Effect\nCost:20XP\nDamage per Turn:5HP'),('Torture Spell', 'Torture Spell', '5-Turn Offensive Status Effect\nCost:50XP\nDamage per Turn:10HP'),('Burn Spell', 'Burn Spell', '5-Turn Offensive Status Effect\nCost:25XP\nDamage per Turn:6HP'),('Frost Spell', 'Frost Spell', 'Makes Opponent Skip 2 Turns\nCost:80XP')]
        r = 18
        c = 7
        for b in status1:
            Button(root,text=b[0],width=11,height=2, bg="black",fg="white",command=lambda text=b:self.name(text)).grid(row=r,column=c)
            c += 1
        status2 = [('Mana Refill', 'Mana Refill', 'Converts 25 HP to 50 XP'),('Heal Spell', 'Heal Spell', 'Converts 50XP to 25 HP'),('Doubler', 'Doubler', 'Doubles Attack/Defence of next turn\nCost:50XP\nDoes not work on \nMana Refill/Heal Spell/Frost/Poison/Torture/Burn')]
        r = 19
        c = 7
        for b in status2:
            Button(root,text=b[0],width=11,height=2, bg="black",fg="white",command=lambda text=b:self.name(text)).grid(row=r,column=c)
            c += 1
        r1,r2,r3,r4,r5,r6=l[0],l[1],l[2],l[3],l[4],l[5]
        for i in range(4):
            Label(root,text=r1[0],fg="white",bg="black").grid(row=21,column=0,columnspan=3)
            Label(root,text=r1[1],fg=r1[5],bg="black").grid(row=22,column=0,columnspan=3)
            Label(root,text=r1[2],fg=r1[6],bg="black").grid(row=23,column=0,columnspan=3)
            Label(root,text=r1[3],fg="white",bg="black").grid(row=24,column=0,columnspan=3)
            Label(root,text=r1[4],fg="white",bg="black").grid(row=25,column=0,columnspan=3)
            Label(root,text=r2[0],fg="white",bg="black").grid(row=21,column=3,columnspan=3)
            Label(root,text=r2[1],fg=r2[5],bg="black").grid(row=22,column=3,columnspan=3)
            Label(root,text=r2[2],fg=r2[6],bg="black").grid(row=23,column=3,columnspan=3)
            Label(root,text=r2[3],fg="white",bg="black").grid(row=24,column=3,columnspan=3)
            Label(root,text=r2[4],fg="white",bg="black").grid(row=25,column=3,columnspan=3)
            Label(root,text=r3[0],fg="white",bg="black").grid(row=21,column=6,columnspan=3)
            Label(root,text=r3[1],fg=r3[5],bg="black").grid(row=22,column=6,columnspan=3)
            Label(root,text=r3[2],fg=r3[6],bg="black").grid(row=23,column=6,columnspan=3)
            Label(root,text=r3[3],fg="white",bg="black").grid(row=24,column=6,columnspan=3)
            Label(root,text=r3[4],fg="white",bg="black").grid(row=25,column=6,columnspan=3)
            Label(root,text=r4[0],fg="white",bg="black").grid(row=21,column=9,columnspan=3)
            Label(root,text=r4[1],fg=r4[5],bg="black").grid(row=22,column=9,columnspan=3)
            Label(root,text=r4[2],fg=r4[6],bg="black").grid(row=23,column=9,columnspan=3)
            Label(root,text=r4[3],fg="white",bg="black").grid(row=24,column=9,columnspan=3)
            Label(root,text=r4[4],fg="white",bg="black").grid(row=25,column=9,columnspan=3)
            Label(root,text=r5[0],fg="white",bg="black").grid(row=21,column=12,columnspan=3)
            Label(root,text=r5[1],fg=r5[5],bg="black").grid(row=22,column=12,columnspan=3)
            Label(root,text=r5[2],fg=r5[6],bg="black").grid(row=23,column=12,columnspan=3)
            Label(root,text=r5[3],fg="white",bg="black").grid(row=24,column=12,columnspan=3)
            Label(root,text=r5[4],fg="white",bg="black").grid(row=25,column=12,columnspan=3)
            Label(root,text=r6[0],fg="white",bg="black").grid(row=21,column=15,columnspan=3)
            Label(root,text=r6[1],fg=r6[5],bg="black").grid(row=22,column=15,columnspan=3)
            Label(root,text=r6[2],fg=r6[6],bg="black").grid(row=23,column=15,columnspan=3)
            Label(root,text=r6[3],fg="white",bg="black").grid(row=24,column=15,columnspan=3)
            Label(root,text=r6[4],fg="white",bg="black").grid(row=25,column=15,columnspan=3)
        root.mainloop()
    def close_window (self,root):
        root.destroy()
    def name(self,text):
        self.topLabel.config(text=text[1],fg="white",bg="black")
        self.infoLine.config(text=text[2],fg="white",bg="black")
        return None

def Killing_Curse():
    a=-300
    b=100
    c=0
    d=0
    return a,b,c,d
def Big_Shield():
    a=-200
    b=0
    c=-100
    d=0
    return a,b,c,d
def Fireball():
    a=-5
    b=10
    c=0
    d=0
    return a,b,c,d
def Small_Shield():
    a=-10
    b=0
    c=-20
    d=0
    return a,b,c,d
def Poison():
    a=-20
    b=0
    c=0
    d=0
    return a,b,c,d
def Lightning():
    a=-10
    b=20
    c=0
    d=0
    return a,b,c,d
def Burn():
    a=-25
    b=0
    c=0
    d=0
    return a,b,c,d
def Medium_Shield():
    a=-50
    b=0
    c=-50
    d=0
    return a,b,c,d
def Torture():
    a=-50
    b=0
    c=0
    d=0
    return a,b,c,d
def Tornado():
    a=-75
    b=50
    c=0
    d=0
    return a,b,c,d
def Mini_Shield():
    a=-5
    b=0
    c=-10
    d=0
    return a,b,c,d
def Skip_that_Step():
    a=0
    b=0
    c=0
    d=0
    return a,b,c,d
def Frost():
    a=-80
    b=0
    c=0
    d=0
    return a,b,c,d
def Doubler():
    a=-50
    b=0
    c=0
    d=0
    return a,b,c,d
def Ex_Pee():
    a=50
    b=0
    c=0
    d=25
    return a,b,c,d
def Ech_Pee():
    a=-50
    b=0
    c=0
    d=-25
    return a,b,c,d
def Programmer_Overide():
    a=0
    b=1000
    c=-1000
    d=0
    return a,b,c,d
#Insert That TExt Here
XP1=Xch1
HP1=Hch1
HPT1=Hch1
HPT2=Hch2
XP2=Xch2
HP2=Hch2
i=1
Poison1=0
Poison2=0
Torture1=0
Torture2=0
Frost1=0
Frost2=0
Doubler1=0
Doubler2=0
Burn1=0
Burn2=0
turner=1
rounderlist=[["","","","","","black","black"],["","","","","","black","black"],["","","","","","black","black"],["","","","","","black","black"],["","","","","","black","black"],["","","","","","black","black"]]
while HP1>0 and HP2>0:
    turndecider=1
    gx=0
    gx1=0
    hx=0
    hx1=0
    se1=[Poison1,Burn1,Torture1]
    se2=[Poison2,Burn2,Torture2]
    if doublecolor1!="white":
        doublecolor1="white"
    if doublecolor2!="white":
        doublecolor2="white"
    if turner==1:
        if Frost1==0:
            while gx==0:
                if gx1>0:
                    print "You do not have enough XP for that Spell. Please Select Another Spell"
                l1=[Player1,str(HP1),HPT1,str(XP1),chlist[chno1][0]]
                l2=[Player2,str(HP2),HPT2,str(XP2),chlist[chno2][0]]
                fh=alpha1(1,l1,l2,rounderlist,se1,se2)
                x0=ACTIVE
                x1=DISABLED
                x2=DISABLED
                x3=DISABLED
                x4=DISABLED
                x5=DISABLED
                x6=DISABLED
                x7=DISABLED
                x8=DISABLED
                x9=DISABLED
                x10=DISABLED
                x11=DISABLED
                x12=DISABLED
                x13=DISABLED
                x14=DISABLED
                x15=DISABLED
                if XP1>=5:
                    x1=ACTIVE
                    x5=ACTIVE
                if XP1>=10:
                    x2=ACTIVE
                    x6=ACTIVE
                if XP1>=75:
                    x3=ACTIVE
                if XP1>=300:
                    x4=ACTIVE
                if XP1>=50:
                    x7=ACTIVE
                    x10=ACTIVE
                    x12=ACTIVE
                    x15=ACTIVE
                if XP1>=80:
                    x11=ACTIVE
                if XP1>=200:
                    x8=ACTIVE
                if XP1>=75:
                    x3=ACTIVE
                if XP1>=20:
                    x9=ACTIVE
                if XP1>=25:
                    x13=ACTIVE
                if HP1>=25:
                    x14=ACTIVE
                g = -1
                def callbackG(spellcode):
                    global g
                    g=spellcode
                    root.destroy()
                while g<=-1:
                    hp1=str(HP1)
                    hp2=str(HP2)
                    xp1=str(XP1)
                    xp2=str(XP2)
                    root=Tk()
                    root.overrideredirect(True)
                    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
                    root.config(background="black")
                    topLabel = Label(root, text = "Choose Spell", font=25,fg="white",bg="black")
                    topLabel.grid(row=7,column=7,columnspan=4)
                    infoLine = Label(root, text = "", justify = 'left',fg="white",bg="black")
                    infoLine.grid(row=8,column=7,columnspan=4,rowspan=5)
                    img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
                    panel = Label(root, image = img,bg="black")
                    panel.grid(row=0,column=0,rowspan=5,columnspan=18)
                    Label(root,text=Player1,fg="red",bg="black",font=25).grid(row=5,column=0)
                    Label(root,text=Player2,fg="white",bg="black",font=25).grid(row=5,column=17)

                    Label(root,text=("HP:- "+hp1+"/"+str(HPT1)),fg="white",bg="black",font=20).grid(row=7,column=0)
                    Label(root,text=("HP:- "+hp2+"/"+str(HPT2)),fg="white",bg="black",font=20).grid(row=7,column=17)
                    Label(root,text=("XP:- "+xp1),fg="white",bg="black",font=20).grid(row=8,column=0)
                    Label(root,text=("XP:- "+xp2),fg="white",bg="black",font=20).grid(row=8,column=17)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=0)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=17)
                    p1,bu1,t1=se1
                    p2,bu2,t2=se2
                    p1,bu1,t1,p2,bu2,t2=int(p1),int(bu1),int(t1),int(p2),int(bu2),int(t2)
                    if p1==bu1==t1==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=0)
                    if p2==bu2==t2==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=17)
                    if p1!=0:
                        Label(root,text="Poison Spell:- "+str(p1)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=0,columnspan=4,sticky=W)
                    if p2!=0:
                        Label(root,text="Poison Spell:- "+str(p2)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=15,columnspan=4,sticky=W)
                    if bu1!=0:
                        Label(root,text="Burn Spell:- "+str(bu1)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=0,columnspan=4,sticky=W)
                    if bu2!=0:
                        Label(root,text="Burn Spell:- "+str(bu2)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=15,columnspan=4,sticky=W)
                    if t1!=0:
                        Label(root,text="Torture Spell:- "+str(t1)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=0,columnspan=4,sticky=W)
                    if t2!=0:
                        Label(root,text="Torture Spell:- "+str(t2)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=15,columnspan=4,sticky=W)
                    Button(root,text="Skip This Turn",width=11,height=2, bg="black",fg="white",state=x0, command=lambda: callbackG(0)).grid(row=12,column=10)
                    Button(root,text="Fireball",width=11,height=2, bg="black",fg="white",state=x1,command=lambda: callbackG(1)).grid(row=7,column=7)
                    Button(root,text="Lightning Spell",width=11,height=2, bg="black",fg="white",state=x2,   command=lambda: callbackG(2)).grid(row=8,column=7)
                    Button(root,text="Tornado",width=11,height=2, bg="black",fg="white",state=x3, command=lambda: callbackG(3)).grid(row=9,column=7)
                    Button(root,text="Killing Curse",width=11,height=2, bg="black",fg="white",state=x4, command=lambda: callbackG(4)).grid(row=10,column=7)
                    Button(root,text="Mini Shield",width=11,height=2, bg="black",fg="white",state=x5, command=lambda: callbackG(5)).grid(row=7,column=10)
                    Button(root,text="Small Shield",width=11,height=2, bg="black",fg="white",state=x6, command=lambda: callbackG(6)).grid(row=8,column=10)
                    Button(root,text="Medium Shield",width=11,height=2, bg="black",fg="white",state=x7, command=lambda: callbackG(7)).grid(row=9,column=10)
                    Button(root,text="Big Shield",width=11,height=2, bg="black",fg="white",state=x8, command=lambda: callbackG(8)).grid(row=10,column=10)
                    Button(root,text="Poison Spell",width=11,height=2, bg="black",fg="white",state=x9, command=lambda: callbackG(9)).grid(row=11,column=7)
                    Button(root,text="Torture Spell",width=11,height=2, bg="black",fg="white",state=x10, command=lambda: callbackG(10)).grid(row=11,column=8)
                    Button(root,text="Frost Spell",width=11,height=2, bg="black",fg="white",state=x11, command=lambda: callbackG(11)).grid(row=11,column=10)
                    Button(root,text="Doubler",width=11,height=2, bg="black",fg="white",state=x12, command=lambda: callbackG(12)).grid(row=12,column=9)
                    Button(root,text="Burn Spell",width=11,height=2, bg="black",fg="white",state=x13, command=lambda: callbackG(13)).grid(row=11,column=9)
                    Button(root,text="Mana Refill",width=11,height=2, bg="black",fg="white",state=x14, command=lambda: callbackG(14)).grid(row=12,column=7)
                    Button(root,text="Heal Spell",width=11,height=2, bg="black",fg="white",state=x15, command=lambda: callbackG(15)).grid(row=12,column=8)
                    l=rounderlist
                    r1,r2,r3,r4,r5,r6=l[0],l[1],l[2],l[3],l[4],l[5]
                    Label(root,text=r1[0],fg="white",bg="black").grid(row=21,column=0,columnspan=3)
                    Label(root,text=r1[1],fg=r1[5],bg="black").grid(row=22,column=0,columnspan=3)
                    Label(root,text=r1[2],fg=r1[6],bg="black").grid(row=23,column=0,columnspan=3)
                    Label(root,text=r1[3],fg="white",bg="black").grid(row=24,column=0,columnspan=3)
                    Label(root,text=r1[4],fg="white",bg="black").grid(row=25,column=0,columnspan=3)
                    Label(root,text=r2[0],fg="white",bg="black").grid(row=21,column=3,columnspan=3)
                    Label(root,text=r2[1],fg=r2[5],bg="black").grid(row=22,column=3,columnspan=3)
                    Label(root,text=r2[2],fg=r2[6],bg="black").grid(row=23,column=3,columnspan=3)
                    Label(root,text=r2[3],fg="white",bg="black").grid(row=24,column=3,columnspan=3)
                    Label(root,text=r2[4],fg="white",bg="black").grid(row=25,column=3,columnspan=3)
                    Label(root,text=r3[0],fg="white",bg="black").grid(row=21,column=6,columnspan=3)
                    Label(root,text=r3[1],fg=r3[5],bg="black").grid(row=22,column=6,columnspan=3)
                    Label(root,text=r3[2],fg=r3[6],bg="black").grid(row=23,column=6,columnspan=3)
                    Label(root,text=r3[3],fg="white",bg="black").grid(row=24,column=6,columnspan=3)
                    Label(root,text=r3[4],fg="white",bg="black").grid(row=25,column=6,columnspan=3)
                    Label(root,text=r4[0],fg="white",bg="black").grid(row=21,column=9,columnspan=3)
                    Label(root,text=r4[1],fg=r4[5],bg="black").grid(row=22,column=9,columnspan=3)
                    Label(root,text=r4[2],fg=r4[6],bg="black").grid(row=23,column=9,columnspan=3)
                    Label(root,text=r4[3],fg="white",bg="black").grid(row=24,column=9,columnspan=3)
                    Label(root,text=r4[4],fg="white",bg="black").grid(row=25,column=9,columnspan=3)
                    Label(root,text=r5[0],fg="white",bg="black").grid(row=21,column=12,columnspan=3)
                    Label(root,text=r5[1],fg=r5[5],bg="black").grid(row=22,column=12,columnspan=3)
                    Label(root,text=r5[2],fg=r5[6],bg="black").grid(row=23,column=12,columnspan=3)
                    Label(root,text=r5[3],fg="white",bg="black").grid(row=24,column=12,columnspan=3)
                    Label(root,text=r5[4],fg="white",bg="black").grid(row=25,column=12,columnspan=3)
                    Label(root,text=r6[0],fg="white",bg="black").grid(row=21,column=15,columnspan=3)
                    Label(root,text=r6[1],fg=r6[5],bg="black").grid(row=22,column=15,columnspan=3)
                    Label(root,text=r6[2],fg=r6[6],bg="black").grid(row=23,column=15,columnspan=3)
                    Label(root,text=r6[3],fg="white",bg="black").grid(row=24,column=15,columnspan=3)
                    Label(root,text=r6[4],fg="white",bg="black").grid(row=25,column=15,columnspan=3)
                    root.mainloop()
                if g==0:
                    a1,b1,c1,d1=Skip_that_Step()
                elif g==1:
                    a1,b1,c1,d1=Fireball()
                elif g==2:
                    a1,b1,c1,d1=Lightning()
                elif g==3:
                    a1,b1,c1,d1=Tornado()
                elif g==4:
                    a1,b1,c1,d1=Killing_Curse()
                elif g==5:
                    a1,b1,c1,d1=Mini_Shield()
                elif g==6:
                    a1,b1,c1,d1=Small_Shield()
                elif g==7:
                    a1,b1,c1,d1=Medium_Shield()
                elif g==8:
                    a1,b1,c1,d1=Big_Shield()
                elif g==9:
                    a1,b1,c1,d1=Poison()
                elif g==10:
                    a1,b1,c1,d1=Torture()
                elif g==11:
                    a1,b1,c1,d1=Frost()
                elif g==12:
                    a1,b1,c1,d1=Doubler()
                elif g==13:
                    a1,b1,c1,d1=Burn()
                elif g==14:
                    a1,b1,c1,d1=Ex_Pee()
                elif g==15:
                    a1,b1,c1,d1=Ech_Pee()
                elif g==138:
                    a1,b1,c1,d1=Programmer_Overide()
                if XP1>=-1*a1:
                    gx=1
                elif XP1<a1:
                    gx=0
                gx1+=1
        elif Frost1>0:
            g=0
            Frost1-=1
            doublecolor1="yellow"
        if Frost2==0:
            while hx==0:
                if hx1>0:
                    print "You do not have enough XP for that Spell. Please Select Another Spell"
                l1=[Player1,str(HP1),HPT1,str(XP1),chlist[chno1][0]]
                l2=[Player2,str(HP2),HPT2,str(XP2),chlist[chno2][0]]
                fh=alpha1(2,l1,l2,rounderlist,se1,se2)
                y0=ACTIVE
                y1=DISABLED
                y2=DISABLED
                y3=DISABLED
                y4=DISABLED
                y5=DISABLED
                y6=DISABLED
                y7=DISABLED
                y8=DISABLED
                y9=DISABLED
                y10=DISABLED
                y11=DISABLED
                y12=DISABLED
                y13=DISABLED
                y14=DISABLED
                y15=DISABLED
                if XP2>=5:
                    y1=ACTIVE
                    y5=ACTIVE
                if XP2>=10:
                    y2=ACTIVE
                    y6=ACTIVE
                if XP2>=75:
                    y3=ACTIVE
                if XP2>=300:
                    y4=ACTIVE
                if XP2>=50:
                    y7=ACTIVE
                    y10=ACTIVE
                    y12=ACTIVE
                    y15=ACTIVE
                if XP2>=80:
                    y11=ACTIVE
                if XP2>=200:
                    y8=ACTIVE
                if XP2>=75:
                    y3=ACTIVE
                if XP2>=20:
                    y9=ACTIVE
                if XP2>=25:
                    y13=ACTIVE
                if HP2>=25:
                    y14=ACTIVE
                h = -1
                def callbackH(spellcode):
                    global h
                    h=spellcode
                    root.destroy()
                while h<=-1:
                    hp1=str(HP1)
                    hp2=str(HP2)
                    xp1=str(XP1)
                    xp2=str(XP2)
                    root=Tk()
                    root.overrideredirect(True)
                    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
                    root.config(background="black")
                    topLabel = Label(root, text = "Choose Spell", font=25,fg="white",bg="black")
                    topLabel.grid(row=7,column=7,columnspan=4)
                    infoLine = Label(root, text = "", justify = 'left',fg="white",bg="black")
                    infoLine.grid(row=8,column=7,columnspan=4,rowspan=5)
                    text=Player2+"'s Turn"
                    img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
                    panel = Label(root, image = img,bg="black")
                    panel.grid(row=0,column=0,rowspan=5,columnspan=18)
                    Label(root,text=chlist[chno1][0],bg="black",fg="white").grid(row=6,column=0)
                    Label(root,text=chlist[chno2][0],bg="black",fg="white").grid(row=6,column=17)
                    Label(root,text=Player1,fg="white",bg="black",font=25).grid(row=5,column=0)
                    Label(root,text=Player2,fg="red",bg="black",font=25).grid(row=5,column=17)
                    Label(root,text=("HP:- "+hp1+"/"+str(HPT1)),fg="white",bg="black",font=20).grid(row=7,column=0)
                    Label(root,text=("HP:- "+hp2+"/"+str(HPT2)),fg="white",bg="black",font=20).grid(row=7,column=17)
                    Label(root,text=("XP:- "+xp1),fg="white",bg="black",font=20).grid(row=8,column=0)
                    Label(root,text=("XP:- "+xp2),fg="white",bg="black",font=20).grid(row=8,column=17)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=0)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=17)
                    p1,bu1,t1=se1
                    p2,bu2,t2=se2
                    p1,bu1,t1,p2,bu2,t2=int(p1),int(bu1),int(t1),int(p2),int(bu2),int(t2)
                    if p1==bu1==t1==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=0)
                    if p2==bu2==t2==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=17)
                    if p1!=0:
                        Label(root,text="Poison Spell:- "+str(p1)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=0,columnspan=4,sticky=W)
                    if p2!=0:
                        Label(root,text="Poison Spell:- "+str(p2)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=15,columnspan=4,sticky=W)
                    if bu1!=0:
                        Label(root,text="Burn Spell:- "+str(bu1)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=0,columnspan=4,sticky=W)
                    if bu2!=0:
                        Label(root,text="Burn Spell:- "+str(bu2)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=15,columnspan=4,sticky=W)
                    if t1!=0:
                        Label(root,text="Torture Spell:- "+str(t1)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=0,columnspan=4,sticky=W)
                    if t2!=0:
                        Label(root,text="Torture Spell:- "+str(t2)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=15,columnspan=4,sticky=W)
                    Button(root,text="Skip This Turn",width=11,height=2, bg="black",fg="white",state=y0, command=lambda: callbackH(0)).grid(row=12,column=10)
                    Button(root,text="Fireball",width=11,height=2, bg="black",fg="white",state=y1,command=lambda: callbackH(1)).grid(row=7,column=7)
                    Button(root,text="Lightning Spell",width=11,height=2, bg="black",fg="white",state=y2,   command=lambda: callbackH(2)).grid(row=8,column=7)
                    Button(root,text="Tornado",width=11,height=2, bg="black",fg="white",state=y3, command=lambda: callbackH(3)).grid(row=9,column=7)
                    Button(root,text="Killing Curse",width=11,height=2, bg="black",fg="white",state=y4, command=lambda: callbackH(4)).grid(row=10,column=7)
                    Button(root,text="Mini Shield",width=11,height=2, bg="black",fg="white",state=y5, command=lambda: callbackH(5)).grid(row=7,column=10)
                    Button(root,text="Small Shield",width=11,height=2, bg="black",fg="white",state=y6, command=lambda: callbackH(6)).grid(row=8,column=10)
                    Button(root,text="Medium Shield",width=11,height=2, bg="black",fg="white",state=y7, command=lambda: callbackH(7)).grid(row=9,column=10)
                    Button(root,text="Big Shield",width=11,height=2, bg="black",fg="white",state=y8, command=lambda: callbackH(8)).grid(row=10,column=10)
                    Button(root,text="Poison Spell",width=11,height=2, bg="black",fg="white",state=y9, command=lambda: callbackH(9)).grid(row=11,column=7)
                    Button(root,text="Torture Spell",width=11,height=2, bg="black",fg="white",state=y10, command=lambda: callbackH(10)).grid(row=11,column=8)
                    Button(root,text="Frost Spell",width=11,height=2, bg="black",fg="white",state=y11, command=lambda: callbackH(11)).grid(row=11,column=10)
                    Button(root,text="Doubler",width=11,height=2, bg="black",fg="white",state=y12, command=lambda: callbackH(12)).grid(row=12,column=9)
                    Button(root,text="Burn Spell",width=11,height=2, bg="black",fg="white",state=y13, command=lambda: callbackH(13)).grid(row=11,column=9)
                    Button(root,text="Mana Refill",width=11,height=2, bg="black",fg="white",state=y14, command=lambda: callbackH(14)).grid(row=12,column=7)
                    Button(root,text="Heal Spell",width=11,height=2, bg="black",fg="white",state=y15, command=lambda: callbackH(15)).grid(row=12,column=8)
                    l=rounderlist
                    r1,r2,r3,r4,r5,r6=l[0],l[1],l[2],l[3],l[4],l[5]
                    Label(root,text=r1[0],fg="white",bg="black").grid(row=21,column=0,columnspan=3)
                    Label(root,text=r1[1],fg=r1[5],bg="black").grid(row=22,column=0,columnspan=3)
                    Label(root,text=r1[2],fg=r1[6],bg="black").grid(row=23,column=0,columnspan=3)
                    Label(root,text=r1[3],fg="white",bg="black").grid(row=24,column=0,columnspan=3)
                    Label(root,text=r1[4],fg="white",bg="black").grid(row=25,column=0,columnspan=3)
                    Label(root,text=r2[0],fg="white",bg="black").grid(row=21,column=3,columnspan=3)
                    Label(root,text=r2[1],fg=r2[5],bg="black").grid(row=22,column=3,columnspan=3)
                    Label(root,text=r2[2],fg=r2[6],bg="black").grid(row=23,column=3,columnspan=3)
                    Label(root,text=r2[3],fg="white",bg="black").grid(row=24,column=3,columnspan=3)
                    Label(root,text=r2[4],fg="white",bg="black").grid(row=25,column=3,columnspan=3)
                    Label(root,text=r3[0],fg="white",bg="black").grid(row=21,column=6,columnspan=3)
                    Label(root,text=r3[1],fg=r3[5],bg="black").grid(row=22,column=6,columnspan=3)
                    Label(root,text=r3[2],fg=r3[6],bg="black").grid(row=23,column=6,columnspan=3)
                    Label(root,text=r3[3],fg="white",bg="black").grid(row=24,column=6,columnspan=3)
                    Label(root,text=r3[4],fg="white",bg="black").grid(row=25,column=6,columnspan=3)
                    Label(root,text=r4[0],fg="white",bg="black").grid(row=21,column=9,columnspan=3)
                    Label(root,text=r4[1],fg=r4[5],bg="black").grid(row=22,column=9,columnspan=3)
                    Label(root,text=r4[2],fg=r4[6],bg="black").grid(row=23,column=9,columnspan=3)
                    Label(root,text=r4[3],fg="white",bg="black").grid(row=24,column=9,columnspan=3)
                    Label(root,text=r4[4],fg="white",bg="black").grid(row=25,column=9,columnspan=3)
                    Label(root,text=r5[0],fg="white",bg="black").grid(row=21,column=12,columnspan=3)
                    Label(root,text=r5[1],fg=r5[5],bg="black").grid(row=22,column=12,columnspan=3)
                    Label(root,text=r5[2],fg=r5[6],bg="black").grid(row=23,column=12,columnspan=3)
                    Label(root,text=r5[3],fg="white",bg="black").grid(row=24,column=12,columnspan=3)
                    Label(root,text=r5[4],fg="white",bg="black").grid(row=25,column=12,columnspan=3)
                    Label(root,text=r6[0],fg="white",bg="black").grid(row=21,column=15,columnspan=3)
                    Label(root,text=r6[1],fg=r6[5],bg="black").grid(row=22,column=15,columnspan=3)
                    Label(root,text=r6[2],fg=r6[6],bg="black").grid(row=23,column=15,columnspan=3)
                    Label(root,text=r6[3],fg="white",bg="black").grid(row=24,column=15,columnspan=3)
                    Label(root,text=r6[4],fg="white",bg="black").grid(row=25,column=15,columnspan=3)
                    root.mainloop()
                if h==0:
                    a2,b2,c2,d2=Skip_that_Step()
                elif h==1:
                    a2,b2,c2,d2=Fireball()
                elif h==2:
                    a2,b2,c2,d2=Lightning()
                elif h==3:
                    a2,b2,c2,d2=Tornado()
                elif h==4:
                    a2,b2,c2,d2=Killing_Curse()
                elif h==5:
                    a2,b2,c2,d2=Mini_Shield()
                elif h==6:
                    a2,b2,c2,d2=Small_Shield()
                elif h==7:
                    a2,b2,c2,d2=Medium_Shield()
                elif h==8:
                    a2,b2,c2,d2=Big_Shield()
                elif h==9:
                    a2,b2,c2,d2=Poison()
                elif h==10:
                    a2,b2,c2,d2=Torture()
                elif h==11:
                    a2,b2,c2,d2=Frost()
                elif h==12:
                    a2,b2,c2,d2=Doubler()
                elif h==13:
                    a2,b2,c2,d2=Burn()
                elif h==14:
                    a2,b2,c2,d2=Ex_Pee()
                elif h==15:
                    a2,b2,c2,d2=Ech_Pee()
                elif h==138:
                    a2,b2,c2,d2=Programmer_Overide()
                if XP2>=(-1*a2):
                        hx=1
                elif XP2<a2:
                        hx=0
                hx1+=1
        elif Frost2>0:
            h=0
            Frost2-=1
            doublecolor2="yellow"
    elif turner==2:
        if Frost2==0:
            while hx==0:
                if hx1>0:
                    print "You do not have enough XP for that Spell. Please Select Another Spell"
                l1=[Player1,str(HP1),HPT1,str(XP1),chlist[chno1][0]]
                l2=[Player2,str(HP2),HPT2,str(XP2),chlist[chno2][0]]
                fh=alpha1(2,l1,l2,rounderlist,se1,se2)
                y0=ACTIVE
                y1=DISABLED
                y2=DISABLED
                y3=DISABLED
                y4=DISABLED
                y5=DISABLED
                y6=DISABLED
                y7=DISABLED
                y8=DISABLED
                y9=DISABLED
                y10=DISABLED
                y11=DISABLED
                y12=DISABLED
                y13=DISABLED
                y14=DISABLED
                y15=DISABLED
                if XP2>=5:
                    y1=ACTIVE
                    y5=ACTIVE
                if XP2>=10:
                    y2=ACTIVE
                    y6=ACTIVE
                if XP2>=75:
                    y3=ACTIVE
                if XP2>=300:
                    y4=ACTIVE
                if XP2>=50:
                    y7=ACTIVE
                    y10=ACTIVE
                    y12=ACTIVE
                    y15=ACTIVE
                if XP2>=80:
                    y11=ACTIVE
                if XP2>=200:
                    y8=ACTIVE
                if XP2>=75:
                    y3=ACTIVE
                if XP2>=20:
                    y9=ACTIVE
                if XP2>=25:
                    y13=ACTIVE
                if HP2>=25:
                    y14=ACTIVE
                h = -1
                def callbackH(spellcode):
                    global h
                    h=spellcode
                    root.destroy()
                while h<=-1:
                    hp1=str(HP1)
                    hp2=str(HP2)
                    xp1=str(XP1)
                    xp2=str(XP2)
                    root=Tk()
                    root.overrideredirect(True)
                    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
                    root.config(background="black")
                    topLabel = Label(root, text = "Choose Spell", font=25,fg="white",bg="black")
                    topLabel.grid(row=7,column=7,columnspan=4)
                    infoLine = Label(root, text = "", justify = 'left',fg="white",bg="black")
                    infoLine.grid(row=8,column=7,columnspan=4,rowspan=5)
                    text=Player2+"'s Turn"
                    img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
                    panel = Label(root, image = img,bg="black")
                    panel.grid(row=0,column=0,rowspan=5,columnspan=18)
                    Label(root,text=chlist[chno1][0],bg="black",fg="white").grid(row=6,column=0)
                    Label(root,text=chlist[chno2][0],bg="black",fg="white").grid(row=6,column=17)
                    Label(root,text=Player1,fg="white",bg="black",font=25).grid(row=5,column=0)
                    Label(root,text=Player2,fg="red",bg="black",font=25).grid(row=5,column=17)
                    Label(root,text=("HP:- "+hp1+"/"+str(HPT1)),fg="white",bg="black",font=20).grid(row=7,column=0)
                    Label(root,text=("HP:- "+hp2+"/"+str(HPT2)),fg="white",bg="black",font=20).grid(row=7,column=17)
                    Label(root,text=("XP:- "+xp1),fg="white",bg="black",font=20).grid(row=8,column=0)
                    Label(root,text=("XP:- "+xp2),fg="white",bg="black",font=20).grid(row=8,column=17)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=0)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=17)
                    p1,bu1,t1=se1
                    p2,bu2,t2=se2
                    p1,bu1,t1,p2,bu2,t2=int(p1),int(bu1),int(t1),int(p2),int(bu2),int(t2)
                    if p1==bu1==t1==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=0)
                    if p2==bu2==t2==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=17)
                    if p1!=0:
                        Label(root,text="Poison Spell:- "+str(p1)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=0,columnspan=4,sticky=W)
                    if p2!=0:
                        Label(root,text="Poison Spell:- "+str(p2)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=15,columnspan=4,sticky=W)
                    if bu1!=0:
                        Label(root,text="Burn Spell:- "+str(bu1)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=0,columnspan=4,sticky=W)
                    if bu2!=0:
                        Label(root,text="Burn Spell:- "+str(bu2)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=15,columnspan=4,sticky=W)
                    if t1!=0:
                        Label(root,text="Torture Spell:- "+str(t1)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=0,columnspan=4,sticky=W)
                    if t2!=0:
                        Label(root,text="Torture Spell:- "+str(t2)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=15,columnspan=4,sticky=W)
                    Button(root,text="Skip This Turn",width=11,height=2, bg="black",fg="white",state=y0, command=lambda: callbackH(0)).grid(row=12,column=10)
                    Button(root,text="Fireball",width=11,height=2, bg="black",fg="white",state=y1,command=lambda: callbackH(1)).grid(row=7,column=7)
                    Button(root,text="Lightning Spell",width=11,height=2, bg="black",fg="white",state=y2,   command=lambda: callbackH(2)).grid(row=8,column=7)
                    Button(root,text="Tornado",width=11,height=2, bg="black",fg="white",state=y3, command=lambda: callbackH(3)).grid(row=9,column=7)
                    Button(root,text="Killing Curse",width=11,height=2, bg="black",fg="white",state=y4, command=lambda: callbackH(4)).grid(row=10,column=7)
                    Button(root,text="Mini Shield",width=11,height=2, bg="black",fg="white",state=y5, command=lambda: callbackH(5)).grid(row=7,column=10)
                    Button(root,text="Small Shield",width=11,height=2, bg="black",fg="white",state=y6, command=lambda: callbackH(6)).grid(row=8,column=10)
                    Button(root,text="Medium Shield",width=11,height=2, bg="black",fg="white",state=y7, command=lambda: callbackH(7)).grid(row=9,column=10)
                    Button(root,text="Big Shield",width=11,height=2, bg="black",fg="white",state=y8, command=lambda: callbackH(8)).grid(row=10,column=10)
                    Button(root,text="Poison Spell",width=11,height=2, bg="black",fg="white",state=y9, command=lambda: callbackH(9)).grid(row=11,column=7)
                    Button(root,text="Torture Spell",width=11,height=2, bg="black",fg="white",state=y10, command=lambda: callbackH(10)).grid(row=11,column=8)
                    Button(root,text="Frost Spell",width=11,height=2, bg="black",fg="white",state=y11, command=lambda: callbackH(11)).grid(row=11,column=10)
                    Button(root,text="Doubler",width=11,height=2, bg="black",fg="white",state=y12, command=lambda: callbackH(12)).grid(row=12,column=9)
                    Button(root,text="Burn Spell",width=11,height=2, bg="black",fg="white",state=y13, command=lambda: callbackH(13)).grid(row=11,column=9)
                    Button(root,text="Mana Refill",width=11,height=2, bg="black",fg="white",state=y14, command=lambda: callbackH(14)).grid(row=12,column=7)
                    Button(root,text="Heal Spell",width=11,height=2, bg="black",fg="white",state=y15, command=lambda: callbackH(15)).grid(row=12,column=8)
                    l=rounderlist
                    r1,r2,r3,r4,r5,r6=l[0],l[1],l[2],l[3],l[4],l[5]
                    Label(root,text=r1[0],fg="white",bg="black").grid(row=21,column=0,columnspan=3)
                    Label(root,text=r1[1],fg=r1[5],bg="black").grid(row=22,column=0,columnspan=3)
                    Label(root,text=r1[2],fg=r1[6],bg="black").grid(row=23,column=0,columnspan=3)
                    Label(root,text=r1[3],fg="white",bg="black").grid(row=24,column=0,columnspan=3)
                    Label(root,text=r1[4],fg="white",bg="black").grid(row=25,column=0,columnspan=3)
                    Label(root,text=r2[0],fg="white",bg="black").grid(row=21,column=3,columnspan=3)
                    Label(root,text=r2[1],fg=r2[5],bg="black").grid(row=22,column=3,columnspan=3)
                    Label(root,text=r2[2],fg=r2[6],bg="black").grid(row=23,column=3,columnspan=3)
                    Label(root,text=r2[3],fg="white",bg="black").grid(row=24,column=3,columnspan=3)
                    Label(root,text=r2[4],fg="white",bg="black").grid(row=25,column=3,columnspan=3)
                    Label(root,text=r3[0],fg="white",bg="black").grid(row=21,column=6,columnspan=3)
                    Label(root,text=r3[1],fg=r3[5],bg="black").grid(row=22,column=6,columnspan=3)
                    Label(root,text=r3[2],fg=r3[6],bg="black").grid(row=23,column=6,columnspan=3)
                    Label(root,text=r3[3],fg="white",bg="black").grid(row=24,column=6,columnspan=3)
                    Label(root,text=r3[4],fg="white",bg="black").grid(row=25,column=6,columnspan=3)
                    Label(root,text=r4[0],fg="white",bg="black").grid(row=21,column=9,columnspan=3)
                    Label(root,text=r4[1],fg=r4[5],bg="black").grid(row=22,column=9,columnspan=3)
                    Label(root,text=r4[2],fg=r4[6],bg="black").grid(row=23,column=9,columnspan=3)
                    Label(root,text=r4[3],fg="white",bg="black").grid(row=24,column=9,columnspan=3)
                    Label(root,text=r4[4],fg="white",bg="black").grid(row=25,column=9,columnspan=3)
                    Label(root,text=r5[0],fg="white",bg="black").grid(row=21,column=12,columnspan=3)
                    Label(root,text=r5[1],fg=r5[5],bg="black").grid(row=22,column=12,columnspan=3)
                    Label(root,text=r5[2],fg=r5[6],bg="black").grid(row=23,column=12,columnspan=3)
                    Label(root,text=r5[3],fg="white",bg="black").grid(row=24,column=12,columnspan=3)
                    Label(root,text=r5[4],fg="white",bg="black").grid(row=25,column=12,columnspan=3)
                    Label(root,text=r6[0],fg="white",bg="black").grid(row=21,column=15,columnspan=3)
                    Label(root,text=r6[1],fg=r6[5],bg="black").grid(row=22,column=15,columnspan=3)
                    Label(root,text=r6[2],fg=r6[6],bg="black").grid(row=23,column=15,columnspan=3)
                    Label(root,text=r6[3],fg="white",bg="black").grid(row=24,column=15,columnspan=3)
                    Label(root,text=r6[4],fg="white",bg="black").grid(row=25,column=15,columnspan=3)
                    root.mainloop()
                if h==0:
                    a2,b2,c2,d2=Skip_that_Step()
                elif h==1:
                    a2,b2,c2,d2=Fireball()
                elif h==2:
                    a2,b2,c2,d2=Lightning()
                elif h==3:
                    a2,b2,c2,d2=Tornado()
                elif h==4:
                    a2,b2,c2,d2=Killing_Curse()
                elif h==5:
                    a2,b2,c2,d2=Mini_Shield()
                elif h==6:
                    a2,b2,c2,d2=Small_Shield()
                elif h==7:
                    a2,b2,c2,d2=Medium_Shield()
                elif h==8:
                    a2,b2,c2,d2=Big_Shield()
                elif h==9:
                    a2,b2,c2,d2=Poison()
                elif h==10:
                    a2,b2,c2,d2=Torture()
                elif h==11:
                    a2,b2,c2,d2=Frost()
                elif h==12:
                    a2,b2,c2,d2=Doubler()
                elif h==13:
                    a2,b2,c2,d2=Burn()
                elif h==14:
                    a2,b2,c2,d2=Ex_Pee()
                elif h==15:
                    a2,b2,c2,d2=Ech_Pee()
                elif h==138:
                    a2,b2,c2,d2=Programmer_Overide()
                if XP2>=(-1*a2):
                        hx=1
                elif XP2<a2:
                        hx=0
                hx1+=1
        elif Frost2>0:
            h=0
            Frost2-=1
            doublecolor2="yellow"
        if Frost1==0:
            while gx==0:
                if gx1>0:
                    print "You do not have enough XP for that Spell. Please Select Another Spell"
                l1=[Player1,str(HP1),HPT1,str(XP1),chlist[chno1][0]]
                l2=[Player2,str(HP2),HPT2,str(XP2),chlist[chno2][0]]
                fh=alpha1(1,l1,l2,rounderlist,se1,se2)
                x0=ACTIVE
                x1=DISABLED
                x2=DISABLED
                x3=DISABLED
                x4=DISABLED
                x5=DISABLED
                x6=DISABLED
                x7=DISABLED
                x8=DISABLED
                x9=DISABLED
                x10=DISABLED
                x11=DISABLED
                x12=DISABLED
                x13=DISABLED
                x14=DISABLED
                x15=DISABLED
                if XP1>=5:
                    x1=ACTIVE
                    x5=ACTIVE
                if XP1>=10:
                    x2=ACTIVE
                    x6=ACTIVE
                if XP1>=75:
                    x3=ACTIVE
                if XP1>=300:
                    x4=ACTIVE
                if XP1>=50:
                    x7=ACTIVE
                    x10=ACTIVE
                    x12=ACTIVE
                    x15=ACTIVE
                if XP1>=80:
                    x11=ACTIVE
                if XP1>=200:
                    x8=ACTIVE
                if XP1>=75:
                    x3=ACTIVE
                if XP1>=20:
                    x9=ACTIVE
                if XP1>=25:
                    x13=ACTIVE
                if HP1>=25:
                    x14=ACTIVE
                g = -1
                def callbackG(spellcode):
                    global g
                    g=spellcode
                    root.destroy()
                while g<=-1:
                    hp1=str(HP1)
                    hp2=str(HP2)
                    xp1=str(XP1)
                    xp2=str(XP2)
                    root=Tk()
                    root.overrideredirect(True)
                    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
                    root.config(background="black")
                    topLabel = Label(root, text = "Choose Spell", font=25,fg="white",bg="black")
                    topLabel.grid(row=7,column=7,columnspan=4)
                    infoLine = Label(root, text = "", justify = 'left',fg="white",bg="black")
                    infoLine.grid(row=8,column=7,columnspan=4,rowspan=5)
                    img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
                    panel = Label(root, image = img,bg="black")
                    panel.grid(row=0,column=0,rowspan=5,columnspan=18)
                    Label(root,text=Player1,fg="red",bg="black",font=25).grid(row=5,column=0)
                    Label(root,text=Player2,fg="white",bg="black",font=25).grid(row=5,column=17)

                    Label(root,text=("HP:- "+hp1+"/"+str(HPT1)),fg="white",bg="black",font=20).grid(row=7,column=0)
                    Label(root,text=("HP:- "+hp2+"/"+str(HPT2)),fg="white",bg="black",font=20).grid(row=7,column=17)
                    Label(root,text=("XP:- "+xp1),fg="white",bg="black",font=20).grid(row=8,column=0)
                    Label(root,text=("XP:- "+xp2),fg="white",bg="black",font=20).grid(row=8,column=17)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=0)
                    Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=17)
                    p1,bu1,t1=se1
                    p2,bu2,t2=se2
                    p1,bu1,t1,p2,bu2,t2=int(p1),int(bu1),int(t1),int(p2),int(bu2),int(t2)
                    if p1==bu1==t1==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=0)
                    if p2==bu2==t2==0:
                        Label(root,text="None",fg="white",bg="black").grid(row=10,column=17)
                    if p1!=0:
                        Label(root,text="Poison Spell:- "+str(p1)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=0,columnspan=4,sticky=W)
                    if p2!=0:
                        Label(root,text="Poison Spell:- "+str(p2)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=15,columnspan=4,sticky=W)
                    if bu1!=0:
                        Label(root,text="Burn Spell:- "+str(bu1)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=0,columnspan=4,sticky=W)
                    if bu2!=0:
                        Label(root,text="Burn Spell:- "+str(bu2)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=15,columnspan=4,sticky=W)
                    if t1!=0:
                        Label(root,text="Torture Spell:- "+str(t1)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=0,columnspan=4,sticky=W)
                    if t2!=0:
                        Label(root,text="Torture Spell:- "+str(t2)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=15,columnspan=4,sticky=W)
                    Button(root,text="Skip This Turn",width=11,height=2, bg="black",fg="white",state=x0, command=lambda: callbackG(0)).grid(row=12,column=10)
                    Button(root,text="Fireball",width=11,height=2, bg="black",fg="white",state=x1,command=lambda: callbackG(1)).grid(row=7,column=7)
                    Button(root,text="Lightning Spell",width=11,height=2, bg="black",fg="white",state=x2,   command=lambda: callbackG(2)).grid(row=8,column=7)
                    Button(root,text="Tornado",width=11,height=2, bg="black",fg="white",state=x3, command=lambda: callbackG(3)).grid(row=9,column=7)
                    Button(root,text="Killing Curse",width=11,height=2, bg="black",fg="white",state=x4, command=lambda: callbackG(4)).grid(row=10,column=7)
                    Button(root,text="Mini Shield",width=11,height=2, bg="black",fg="white",state=x5, command=lambda: callbackG(5)).grid(row=7,column=10)
                    Button(root,text="Small Shield",width=11,height=2, bg="black",fg="white",state=x6, command=lambda: callbackG(6)).grid(row=8,column=10)
                    Button(root,text="Medium Shield",width=11,height=2, bg="black",fg="white",state=x7, command=lambda: callbackG(7)).grid(row=9,column=10)
                    Button(root,text="Big Shield",width=11,height=2, bg="black",fg="white",state=x8, command=lambda: callbackG(8)).grid(row=10,column=10)
                    Button(root,text="Poison Spell",width=11,height=2, bg="black",fg="white",state=x9, command=lambda: callbackG(9)).grid(row=11,column=7)
                    Button(root,text="Torture Spell",width=11,height=2, bg="black",fg="white",state=x10, command=lambda: callbackG(10)).grid(row=11,column=8)
                    Button(root,text="Frost Spell",width=11,height=2, bg="black",fg="white",state=x11, command=lambda: callbackG(11)).grid(row=11,column=10)
                    Button(root,text="Doubler",width=11,height=2, bg="black",fg="white",state=x12, command=lambda: callbackG(12)).grid(row=12,column=9)
                    Button(root,text="Burn Spell",width=11,height=2, bg="black",fg="white",state=x13, command=lambda: callbackG(13)).grid(row=11,column=9)
                    Button(root,text="Mana Refill",width=11,height=2, bg="black",fg="white",state=x14, command=lambda: callbackG(14)).grid(row=12,column=7)
                    Button(root,text="Heal Spell",width=11,height=2, bg="black",fg="white",state=x15, command=lambda: callbackG(15)).grid(row=12,column=8)
                    l=rounderlist
                    r1,r2,r3,r4,r5,r6=l[0],l[1],l[2],l[3],l[4],l[5]
                    Label(root,text=r1[0],fg="white",bg="black").grid(row=21,column=0,columnspan=3)
                    Label(root,text=r1[1],fg=r1[5],bg="black").grid(row=22,column=0,columnspan=3)
                    Label(root,text=r1[2],fg=r1[6],bg="black").grid(row=23,column=0,columnspan=3)
                    Label(root,text=r1[3],fg="white",bg="black").grid(row=24,column=0,columnspan=3)
                    Label(root,text=r1[4],fg="white",bg="black").grid(row=25,column=0,columnspan=3)
                    Label(root,text=r2[0],fg="white",bg="black").grid(row=21,column=3,columnspan=3)
                    Label(root,text=r2[1],fg=r2[5],bg="black").grid(row=22,column=3,columnspan=3)
                    Label(root,text=r2[2],fg=r2[6],bg="black").grid(row=23,column=3,columnspan=3)
                    Label(root,text=r2[3],fg="white",bg="black").grid(row=24,column=3,columnspan=3)
                    Label(root,text=r2[4],fg="white",bg="black").grid(row=25,column=3,columnspan=3)
                    Label(root,text=r3[0],fg="white",bg="black").grid(row=21,column=6,columnspan=3)
                    Label(root,text=r3[1],fg=r3[5],bg="black").grid(row=22,column=6,columnspan=3)
                    Label(root,text=r3[2],fg=r3[6],bg="black").grid(row=23,column=6,columnspan=3)
                    Label(root,text=r3[3],fg="white",bg="black").grid(row=24,column=6,columnspan=3)
                    Label(root,text=r3[4],fg="white",bg="black").grid(row=25,column=6,columnspan=3)
                    Label(root,text=r4[0],fg="white",bg="black").grid(row=21,column=9,columnspan=3)
                    Label(root,text=r4[1],fg=r4[5],bg="black").grid(row=22,column=9,columnspan=3)
                    Label(root,text=r4[2],fg=r4[6],bg="black").grid(row=23,column=9,columnspan=3)
                    Label(root,text=r4[3],fg="white",bg="black").grid(row=24,column=9,columnspan=3)
                    Label(root,text=r4[4],fg="white",bg="black").grid(row=25,column=9,columnspan=3)
                    Label(root,text=r5[0],fg="white",bg="black").grid(row=21,column=12,columnspan=3)
                    Label(root,text=r5[1],fg=r5[5],bg="black").grid(row=22,column=12,columnspan=3)
                    Label(root,text=r5[2],fg=r5[6],bg="black").grid(row=23,column=12,columnspan=3)
                    Label(root,text=r5[3],fg="white",bg="black").grid(row=24,column=12,columnspan=3)
                    Label(root,text=r5[4],fg="white",bg="black").grid(row=25,column=12,columnspan=3)
                    Label(root,text=r6[0],fg="white",bg="black").grid(row=21,column=15,columnspan=3)
                    Label(root,text=r6[1],fg=r6[5],bg="black").grid(row=22,column=15,columnspan=3)
                    Label(root,text=r6[2],fg=r6[6],bg="black").grid(row=23,column=15,columnspan=3)
                    Label(root,text=r6[3],fg="white",bg="black").grid(row=24,column=15,columnspan=3)
                    Label(root,text=r6[4],fg="white",bg="black").grid(row=25,column=15,columnspan=3)
                    root.mainloop()
                if g==0:
                    a1,b1,c1,d1=Skip_that_Step()
                elif g==1:
                    a1,b1,c1,d1=Fireball()
                elif g==2:
                    a1,b1,c1,d1=Lightning()
                elif g==3:
                    a1,b1,c1,d1=Tornado()
                elif g==4:
                    a1,b1,c1,d1=Killing_Curse()
                elif g==5:
                    a1,b1,c1,d1=Mini_Shield()
                elif g==6:
                    a1,b1,c1,d1=Small_Shield()
                elif g==7:
                    a1,b1,c1,d1=Medium_Shield()
                elif g==8:
                    a1,b1,c1,d1=Big_Shield()
                elif g==9:
                    a1,b1,c1,d1=Poison()
                elif g==10:
                    a1,b1,c1,d1=Torture()
                elif g==11:
                    a1,b1,c1,d1=Frost()
                elif g==12:
                    a1,b1,c1,d1=Doubler()
                elif g==13:
                    a1,b1,c1,d1=Burn()
                elif g==14:
                    a1,b1,c1,d1=Ex_Pee()
                elif g==15:
                    a1,b1,c1,d1=Ech_Pee()
                elif g==138:
                    a1,b1,c1,d1=Programmer_Overide()
                if XP1>=-1*a1:
                    gx=1
                elif XP1<a1:
                    gx=0
                gx1+=1
        elif Frost1>0:
            g=0
            Frost1-=1
            doublecolor1="yellow"

    if g==0:
        gstar=Player1+" skipped this Round"
        a1,b1,c1,d1=Skip_that_Step()
    elif g==1:
        gstar=Player1+" chose the Fireball"
    elif g==2:
        gstar=Player1+" chose the Lightning Spell"
    elif g==3:
        gstar=Player1+" chose the Tornado"
    elif g==4:
        gstar=Player1+" chose the Killing Curse"
    elif g==5:
        gstar=Player1+" chose the Mini Shield"
    elif g==6:
        gstar=Player1+" chose the Small Shield"
    elif g==7:
        gstar=Player1+" chose the Medium Shield"
    elif g==8:
        gstar=Player1+" chose the Big Shield"
    elif g==9:
        gstar=Player1+" chose the Poison Spell"
        Poison2+=5
    elif g==10:
        gstar=Player1+" chose the Torture Spell"
        Torture2+=5
    elif g==11:
        gstar=Player1+" chose the Frost Spell"
        Frost2+=2
    elif g==12:
        gstar=Player1+" chose the Doubler"
        Doubler1+=2
    elif g==13:
        gstar=Player1+" chose the Burn Spell"
        Burn2+=5
    elif g==14:
        gstar=Player1+" chose the Mana Refill"
    elif g==15:
        gstar=Player1+" chose the Healer"
    elif g==138:
        gstar="Programmer Override. No one can beat Ishan Tandon"
    if h==0:
        hstar=Player2+" skipped this Round"
        a2,b2,c2,d2=Skip_that_Step()
    elif h==1:
        hstar=Player2+" chose the Fireball"
    elif h==2:
        hstar=Player2+" chose the Lightning Spell"
    elif h==3:
        hstar=Player2+" chose the Tornado"
    elif h==4:
        hstar=Player2+" chose the Killing Curse"
    elif h==5:
        hstar=Player2+" chose the Mini Shield"
    elif h==6:
        hstar=Player2+" chose the Small Shield"
    elif h==7:
        hstar=Player2+" chose the Medium Shield"
    elif h==8:
        hstar=Player2+" chose the Big Spell"
    elif h==9:
        hstar=Player2+" chose the Poison Spell"
        Poison1+=5
    elif h==10:
        hstar=Player2+" chose the Torture Spell"
        Torture1+=5
    elif h==11:
        hstar=Player2+" chose the Frost Spell"
        Frost1+=2
    elif h==12:
        hstar=Player2+" chose the Doubler"
        Doubler2+=2
    elif h==13:
        hstar=Player2+" chose the Burn Spell"
        Burn1+=5
    elif h==14:
        hstar=Player2+" chose the Mana Refill"
    elif h==15:
        hstar=Player2+" chose the Healer"
    elif h==138:
        hstar="Programmer Override. No one can beat Ishan Tandon"
    if Doubler1==1:
        b1,c1=(b1*2),(c1*2)
        doublecolor1="cyan"
        Doubler1-=1
    elif Doubler1==2:
        Doubler1-=1
    if Doubler2==1:
        b2,c2=(b2*2),(c2*2)
        doublecolor2="cyan"
        Doubler2-=1
    elif Doubler2==2:
        Doubler2-=1
#Start of Calculations
    XP1+=a1
    XP2+=a2
    if (b1+c2)>0 and b1!=0:
        HP2=HP2-(b1+c2)
        XP1=XP1+(b1+c2)
    if (b2+c1)>0 and b2!=0:
        HP1=HP1-(b2+c1)
        XP2=XP2+(b2+c1)
    HP1-=d1
    HP2-=d2
    if Poison2>0:
        HP2-=5
        Poison2-=1
    if Poison1>0:
        HP1-=5
        Poison1-=1
    if Burn2>0:
        HP2-=6
        Burn2-=1
    if Burn1>0:
        HP1-=6
        Burn1-=1
    if Torture1>0:
        HP1-=10
        Torture1-=1
    if Torture2>0:
        HP2-=10
        Torture2-=1
    if HP1>HPT1:
        HP1=HPT1
    elif HP1<0:
        HP1=0
    if HP2>HPT2:
        HP2=HPT2
    elif HP2<0:
        HP2=0
    rounder="Round "+str(i)
    Xpeter1=str(XP1)
    Hpeter1=str(HP1)
    Xpeter2=str(XP2)
    Hpeter2=str(HP2)
    XP1+=10
    XP2+=10
    gline=Player1+" has "+Xpeter1+" XP and "+Hpeter1+" HP left."
    hline=Player2+" has "+Xpeter2+" XP and "+Hpeter2+" HP left."
    rounderlist.pop(0)
    rounderlist.append([rounder,gstar,hstar,gline,hline,doublecolor1,doublecolor2])
    if HP1<=0 or HP2<=0:
        turndecider=0
    if turndecider!=0:
        root = Tk()
        root.overrideredirect(True)
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.config(background="black")
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Tkinter.Label(root, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        def callback(x):
            root.destroy()
        Return = Button(root, text="Continue Game",fg="white",bg="black",command=lambda: callback(1),height=10,width=20,font=100).grid(row=8,column=4,columnspan=10,rowspan=5)
        topLabel = Label(root, text = "After "+str(rounderlist[-1][0]), font=25,fg="white",bg="black")
        topLabel.grid(row=7,column=7,columnspan=4)
        infoLine = Label(root, text = "", justify = 'left',fg="white",bg="black")
        infoLine.grid(row=8,column=7,columnspan=4,rowspan=5)
        img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        panel = Label(root, image = img,bg="black")
        panel.grid(row=0,column=0,rowspan=5,columnspan=18)
        Label(root,text=Player1,fg="red",bg="black",font=25).grid(row=5,column=0)
        Label(root,text=Player2,fg="white",bg="black",font=25).grid(row=5,column=17)

        Label(root,text=("HP:- "+hp1+"/"+str(HPT1)),fg="white",bg="black",font=20).grid(row=7,column=0)
        Label(root,text=("HP:- "+hp2+"/"+str(HPT2)),fg="white",bg="black",font=20).grid(row=7,column=17)
        Label(root,text=("XP:- "+xp1),fg="white",bg="black",font=20).grid(row=8,column=0)
        Label(root,text=("XP:- "+xp2),fg="white",bg="black",font=20).grid(row=8,column=17)
        Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=0)
        Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=17)
        p1,bu1,t1=se1
        p2,bu2,t2=se2
        p1,bu1,t1,p2,bu2,t2=int(p1),int(bu1),int(t1),int(p2),int(bu2),int(t2)
        if p1==bu1==t1==0:
            Label(root,text="None",fg="white",bg="black").grid(row=10,column=0)
        if p2==bu2==t2==0:
            Label(root,text="None",fg="white",bg="black").grid(row=10,column=17)
        if p1!=0:
            Label(root,text="Poison Spell:- "+str(p1)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=0,columnspan=4,sticky=W)
        if p2!=0:
            Label(root,text="Poison Spell:- "+str(p2)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=15,columnspan=4,sticky=W)
        if bu1!=0:
            Label(root,text="Burn Spell:- "+str(bu1)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=0,columnspan=4,sticky=W)
        if bu2!=0:
            Label(root,text="Burn Spell:- "+str(bu2)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=15,columnspan=4,sticky=W)
        if t1!=0:
            Label(root,text="Torture Spell:- "+str(t1)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=0,columnspan=4,sticky=W)
        if t2!=0:
            Label(root,text="Torture Spell:- "+str(t2)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=15,columnspan=4,sticky=W)
        l=rounderlist
        r1,r2,r3,r4,r5,r6=l[0],l[1],l[2],l[3],l[4],l[5]
        Label(root,text=r1[0],fg="white",bg="black").grid(row=21,column=0,columnspan=3)
        Label(root,text=r1[1],fg=r1[5],bg="black").grid(row=22,column=0,columnspan=3)
        Label(root,text=r1[2],fg=r1[6],bg="black").grid(row=23,column=0,columnspan=3)
        Label(root,text=r1[3],fg="white",bg="black").grid(row=24,column=0,columnspan=3)
        Label(root,text=r1[4],fg="white",bg="black").grid(row=25,column=0,columnspan=3)
        Label(root,text=r2[0],fg="white",bg="black").grid(row=21,column=3,columnspan=3)
        Label(root,text=r2[1],fg=r2[5],bg="black").grid(row=22,column=3,columnspan=3)
        Label(root,text=r2[2],fg=r2[6],bg="black").grid(row=23,column=3,columnspan=3)
        Label(root,text=r2[3],fg="white",bg="black").grid(row=24,column=3,columnspan=3)
        Label(root,text=r2[4],fg="white",bg="black").grid(row=25,column=3,columnspan=3)
        Label(root,text=r3[0],fg="white",bg="black").grid(row=21,column=6,columnspan=3)
        Label(root,text=r3[1],fg=r3[5],bg="black").grid(row=22,column=6,columnspan=3)
        Label(root,text=r3[2],fg=r3[6],bg="black").grid(row=23,column=6,columnspan=3)
        Label(root,text=r3[3],fg="white",bg="black").grid(row=24,column=6,columnspan=3)
        Label(root,text=r3[4],fg="white",bg="black").grid(row=25,column=6,columnspan=3)
        Label(root,text=r4[0],fg="white",bg="black").grid(row=21,column=9,columnspan=3)
        Label(root,text=r4[1],fg=r4[5],bg="black").grid(row=22,column=9,columnspan=3)
        Label(root,text=r4[2],fg=r4[6],bg="black").grid(row=23,column=9,columnspan=3)
        Label(root,text=r4[3],fg="white",bg="black").grid(row=24,column=9,columnspan=3)
        Label(root,text=r4[4],fg="white",bg="black").grid(row=25,column=9,columnspan=3)
        Label(root,text=r5[0],fg="white",bg="black").grid(row=21,column=12,columnspan=3)
        Label(root,text=r5[1],fg=r5[5],bg="black").grid(row=22,column=12,columnspan=3)
        Label(root,text=r5[2],fg=r5[6],bg="black").grid(row=23,column=12,columnspan=3)
        Label(root,text=r5[3],fg="white",bg="black").grid(row=24,column=12,columnspan=3)
        Label(root,text=r5[4],fg="white",bg="black").grid(row=25,column=12,columnspan=3)
        Label(root,text=r6[0],fg="white",bg="black").grid(row=21,column=15,columnspan=3)
        Label(root,text=r6[1],fg=r6[5],bg="black").grid(row=22,column=15,columnspan=3)
        Label(root,text=r6[2],fg=r6[6],bg="black").grid(row=23,column=15,columnspan=3)
        Label(root,text=r6[3],fg="white",bg="black").grid(row=24,column=15,columnspan=3)
        Label(root,text=r6[4],fg="white",bg="black").grid(row=25,column=15,columnspan=3)
        root.mainloop()
    i+=1
    if turner==1:
        turner=2
    elif turner==2:
        turner=1

HP=max(HP1,HP2)
if HP==HP1 and HP!=HP2:
    pc1="blue"
    pc2="red"
    c=1
elif HP==HP2 and HP!=HP1:
    pc1="red"
    pc2="blue"
    c=2
else:
    pc1="green"
    pc2="green"
    c=3
hp1=str(HP1)
hp2=str(HP2)
xp1=str(XP1)
xp2=str(XP2)
root=Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.config(background="black")
topLabel = Label(root, text = "Choose Spell", font=25,fg="white",bg="black")
topLabel.grid(row=7,column=7,columnspan=4)
infoLine = Label(root, text = "", justify = 'left',fg="white",bg="black")
infoLine.grid(row=8,column=7,columnspan=4,rowspan=5)
text=Player2+"'s Turn"
img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
panel = Label(root, image = img,bg="black")
panel.grid(row=0,column=0,rowspan=5,columnspan=18)
Label(root,text=chlist[chno1][0],bg="black",fg="white").grid(row=6,column=0)
Label(root,text=chlist[chno2][0],bg="black",fg="white").grid(row=6,column=17)
Label(root,text=Player1,fg=pc1,bg="black",font=25).grid(row=5,column=0)
Label(root,text=Player2,fg=pc2,bg="black",font=25).grid(row=5,column=17)
Label(root,text=("HP:- "+hp1+"/"+str(HPT1)),fg="white",bg="black",font=20).grid(row=7,column=0)
Label(root,text=("HP:- "+hp2+"/"+str(HPT2)),fg="white",bg="black",font=20).grid(row=7,column=17)
Label(root,text=("XP:- "+xp1),fg="white",bg="black",font=20).grid(row=8,column=0)
Label(root,text=("XP:- "+xp2),fg="white",bg="black",font=20).grid(row=8,column=17)
Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=0)
Label(root,text="Status Effects",font=25,fg="white",bg="black").grid(row=9,column=17)
p1,bu1,t1=se1
p2,bu2,t2=se2
p1,bu1,t1,p2,bu2,t2=int(p1),int(bu1),int(t1),int(p2),int(bu2),int(t2)
if p1==bu1==t1==0:
    Label(root,text="None",fg="white",bg="black").grid(row=10,column=0)
if p2==bu2==t2==0:
    Label(root,text="None",fg="white",bg="black").grid(row=10,column=17)
if p1!=0:
    Label(root,text="Poison Spell:- "+str(p1)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=0,columnspan=4,sticky=W)
if p2!=0:
    Label(root,text="Poison Spell:- "+str(p2)+" Turn(s)(reduces 5 HP every turn)",fg="white",bg="black").grid(row=10,column=15,columnspan=4,sticky=W)
if bu1!=0:
    Label(root,text="Burn Spell:- "+str(bu1)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=0,columnspan=4,sticky=W)
if bu2!=0:
    Label(root,text="Burn Spell:- "+str(bu2)+" Turn(s)(reduces 6 HP every turn)",fg="white",bg="black").grid(row=11,column=15,columnspan=4,sticky=W)
if t1!=0:
    Label(root,text="Torture Spell:- "+str(t1)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=0,columnspan=4,sticky=W)
if t2!=0:
    Label(root,text="Torture Spell:- "+str(t2)+" Turn(s)(reduces 10 HP every turn)",fg="white",bg="black").grid(row=12,column=15,columnspan=4,sticky=W)
if c==1:
    topLabel = Label(root, text = Player1+" won the game in "+str(i-1)+" rounds", font=25,fg="white",bg="black").grid(row=7,column=5,columnspan=8)
elif c==2:
    topLabel = Label(root, text = Player2+" won the game in "+str(i-1)+" rounds", font=25,fg="white",bg="black").grid(row=7,column=5,columnspan=8)
elif c==3:
    topLabel = Label(root, text = "Game is Draw", font=25,fg="white",bg="black").grid(row=7,column=5,columnspan=8)
def close():
    root.destroy()
Button(root,text="Quit",font=35,command=close,height=4,width=56,fg="white",bg="black").grid(row=10,column=5,columnspan=8,rowspan=5)
l=rounderlist
r1,r2,r3,r4,r5,r6=l[0],l[1],l[2],l[3],l[4],l[5]
Label(root,text=r1[0],fg="white",bg="black").grid(row=21,column=0,columnspan=3,stick=W)
Label(root,text=r1[1],fg=r1[5],bg="black").grid(row=22,column=0,columnspan=3,stick=W)
Label(root,text=r1[2],fg=r1[6],bg="black").grid(row=23,column=0,columnspan=3,stick=W)
Label(root,text=r1[3],fg="white",bg="black").grid(row=24,column=0,columnspan=3,stick=W)
Label(root,text=r1[4],fg="white",bg="black").grid(row=25,column=0,columnspan=3,stick=W)
Label(root,text=r2[0],fg="white",bg="black").grid(row=21,column=3,columnspan=3,stick=W)
Label(root,text=r2[1],fg=r2[5],bg="black").grid(row=22,column=3,columnspan=3,stick=W)
Label(root,text=r2[2],fg=r2[6],bg="black").grid(row=23,column=3,columnspan=3,stick=W)
Label(root,text=r2[3],fg="white",bg="black").grid(row=24,column=3,columnspan=3,stick=W)
Label(root,text=r2[4],fg="white",bg="black").grid(row=25,column=3,columnspan=3,stick=W)
Label(root,text=r3[0],fg="white",bg="black").grid(row=21,column=6,columnspan=3,stick=W)
Label(root,text=r3[1],fg=r3[5],bg="black").grid(row=22,column=6,columnspan=3,stick=W)
Label(root,text=r3[2],fg=r3[6],bg="black").grid(row=23,column=6,columnspan=3,stick=W)
Label(root,text=r3[3],fg="white",bg="black").grid(row=24,column=6,columnspan=3,stick=W)
Label(root,text=r3[4],fg="white",bg="black").grid(row=25,column=6,columnspan=3,stick=W)
Label(root,text=r4[0],fg="white",bg="black").grid(row=21,column=9,columnspan=3,stick=W)
Label(root,text=r4[1],fg=r4[5],bg="black").grid(row=22,column=9,columnspan=3,stick=W)
Label(root,text=r4[2],fg=r4[6],bg="black").grid(row=23,column=9,columnspan=3,stick=W)
Label(root,text=r4[3],fg="white",bg="black").grid(row=24,column=9,columnspan=3,stick=W)
Label(root,text=r4[4],fg="white",bg="black").grid(row=25,column=9,columnspan=3,stick=W)
Label(root,text=r5[0],fg="white",bg="black").grid(row=21,column=12,columnspan=3,stick=W)
Label(root,text=r5[1],fg=r5[5],bg="black").grid(row=22,column=12,columnspan=3,stick=W)
Label(root,text=r5[2],fg=r5[6],bg="black").grid(row=23,column=12,columnspan=3,stick=W)
Label(root,text=r5[3],fg="white",bg="black").grid(row=24,column=12,columnspan=3,stick=W)
Label(root,text=r5[4],fg="white",bg="black").grid(row=25,column=12,columnspan=3,stick=W)
Label(root,text=r6[0],fg="white",bg="black").grid(row=21,column=15,columnspan=3,stick=W)
Label(root,text=r6[1],fg=r6[5],bg="black").grid(row=22,column=15,columnspan=3,stick=W)
Label(root,text=r6[2],fg=r6[6],bg="black").grid(row=23,column=15,columnspan=3,stick=W)
Label(root,text=r6[3],fg="white",bg="black").grid(row=24,column=15,columnspan=3,stick=W)
Label(root,text=r6[4],fg="white",bg="black").grid(row=25,column=15,columnspan=3,stick=W)
Label(root,text="Developed By:-",fg="white",bg="black").grid(row=15,column=0,columnspan=3,stick=W)
Label(root,text="Ishan Tandon",fg="white",bg="black").grid(row=16,column=0,columnspan=3,stick=W)
Label(root,text="",fg="black",bg="black").grid(row=17,column=0,columnspan=3,stick=W)
Label(root,text="",fg="black",bg="black").grid(row=18,column=0,columnspan=3,stick=W)
Label(root,text="War of W.I.Z.A.R.D.S",fg="white",bg="black").grid(row=16,column=3,columnspan=3,stick=W)
Label(root,text="Alpha Build 1.2",fg="white",bg="black").grid(row=17,column=3,columnspan=3,stick=W)
Label(root,text="29/1/2018",fg="white",bg="black").grid(row=18,column=3,columnspan=3,stick=W)
Label(root,text="",fg="white",bg="black").grid(row=19,column=15,columnspan=3,stick=W)
Label(root,text="",fg="white",bg="black").grid(row=20,column=15,columnspan=3,stick=W)
root.mainloop()