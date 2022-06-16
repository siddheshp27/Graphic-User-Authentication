from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import customtkinter
import sqlite3 as slt

root = Tk()
root.title("Graphical Password")
# root.geometry("1920x1080")


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("Dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")

# Database creation/connection
conn = slt.connect('userinfo.db')

# cursor creation
c = conn.cursor()
# c.execute('''CREATE TABLE user(
#     username text,
#     email text,
#     password text
#     )''')

conn.commit()

# initializing Variable
fruitPass = []
chocoPass = []
alfaPass = []
fcount = [0]
ccount = [0]
acount = [0]
priordict = {}


def Login():
    for widgets in root.winfo_children():
        widgets.destroy()
    frame1 = LabelFrame(root, text="Login", padx=40, pady=20)
    frame1.pack(padx=40, pady=40)
    userLabel = Label(frame1, text="UserID")
    userLabel.grid(row=1, column=1, padx=10, pady=(0, 4))
    userentry = Entry(frame1)
    userentry.grid(row=1, column=2)
    username = userentry.get()
    submit = Button(frame1, text="Submit",
                    command=lambda: check(userentry.get()))
    submit.grid(row=2, column=2, pady=(15, 0), padx=(0, 30))


def check(username):
    usernameLst = []
    passwordLst = []
    upasswordLst = []
    ind = None
    conn = slt.connect('userinfo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    users = c.fetchall()
    for i in users:
        usernameLst.append(i[0])
        passwordLst.append(i[2])
    if(username in usernameLst):
        ind = usernameLst.index(username)
        uPass = passwordLst[ind]
        for i in uPass:
            upasswordLst.append(i)

        graphicPass(username, upasswordLst)
    else:
        messagebox.showwarning("Warning", "Username does not exist.")
    conn.commit()
    conn.close()


def store(char, cate):
    flast = len(fcount)-1
    clast = len(ccount)-1
    alast = len(acount)-1

    if cate == 'F':
        if char not in fruitPass:
            if fcount[flast] < 3:
                fruitPass.append(char)
                # print(fruitPass)
                fcount.append(((fcount[flast])+1))
                # print(fcount[flast])
            else:
                messagebox.showwarning(
                    "Warning", "Maximum 3 items accepted for each category.")
        else:
            messagebox.showwarning("Warning", "Item is already selected.")

    if cate == 'C':
        if char not in chocoPass:
            if ccount[clast] < 3:
                chocoPass.append(char)
                # print(chocoPass)
                ccount.append(((ccount[clast])+1))
                # print(ccount[clast])
            else:
                messagebox.showwarning(
                    "Warning", "Maximum 3 items accepted for each category.")
        else:
            messagebox.showwarning("Warning", "Item is already selected.")

    if cate == 'A':
        if char not in alfaPass:
            if acount[alast] < 3:
                alfaPass.append(char)
                # print(alfaPass)
                acount.append(((acount[alast])+1))
                # print(acount[alast])
            else:
                messagebox.showwarning(
                    "Warning", "Maximum 3 items accepted for each category.")
        else:
            messagebox.showwarning("Warning", "Item is already selected.")


def signupstore(username, email, p1, p2, p3):
    fPass = ''
    sfruitPass = ''
    for i in fruitPass:
        sfruitPass += i
    schocoPass = ''
    for i in chocoPass:
        schocoPass += i
    salfaPass = ''
    for i in alfaPass:
        salfaPass += i
    priordict = {p1: sfruitPass, p2: schocoPass, p3: salfaPass}
    cpriordict = priordict.copy()
    for i in priordict:
        pmin = min(cpriordict)
        fPass += priordict[pmin]
        cpriordict.pop(pmin)
    conn = slt.connect('userinfo.db')

    # cursor creation
    c = conn.cursor()
    print(username, email, p1, p2, p3, fPass)
    c.execute("INSERT INTO  user VALUES(?,?,?)", (username, email, fPass))
    conn.commit()


def show():
    conn = slt.connect('userinfo.db')
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM user")
    users = c.fetchall()

    for i in users:
        print(i)

    conn.commit()
    conn.close


# grid for images


def graphicPass(username, password):
    frame2 = LabelFrame(root, text="Password", padx=27, pady=20)
    frame2.pack(padx=30, pady=(0, 30))
    category = ['9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    difference = []
    for i in category:
        if i not in password:
            difference.append(i)
    random.shuffle(difference)
    random.shuffle(password)
    pics = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    random.shuffle(pics)
    img1 = ImageTk.PhotoImage(Image.open(
        password[0] + "/" + pics[0]).resize((70, 70)))
    img2 = ImageTk.PhotoImage(Image.open(
        difference[1] + "/" + pics[0]).resize((70, 70)))
    img3 = ImageTk.PhotoImage(Image.open(
        password[2] + "/" + pics[0]).resize((70, 70)))
    img4 = ImageTk.PhotoImage(Image.open(
        difference[3] + "/" + pics[0]).resize((70, 70)))
    img5 = ImageTk.PhotoImage(Image.open(
        password[4] + "/" + pics[0]).resize((70, 70)))
    img6 = ImageTk.PhotoImage(Image.open(
        difference[5] + "/" + pics[0]).resize((70, 70)))
    img7 = ImageTk.PhotoImage(Image.open(
        password[6] + "/" + pics[0]).resize((70, 70)))
    img8 = ImageTk.PhotoImage(Image.open(
        difference[7] + "/" + pics[0]).resize((70, 70)))
    img9 = ImageTk.PhotoImage(Image.open(
        password[3] + "/" + pics[0]).resize((70, 70)))
    img10 = ImageTk.PhotoImage(Image.open(
        difference[9] + "/" + pics[0]).resize((70, 70)))
    img11 = ImageTk.PhotoImage(Image.open(
        password[1] + "/" + pics[0]).resize((70, 70)))
    img12 = ImageTk.PhotoImage(Image.open(
        difference[11] + "/" + pics[0]).resize((70, 70)))
    img13 = ImageTk.PhotoImage(Image.open(
        difference[12] + "/" + pics[0]).resize((70, 70)))
    img14 = ImageTk.PhotoImage(Image.open(
        difference[13] + "/" + pics[0]).resize((70, 70)))
    img15 = ImageTk.PhotoImage(Image.open(
        difference[14] + "/" + pics[0]).resize((70, 70)))
    img16 = ImageTk.PhotoImage(Image.open(
        difference[15] + "/" + pics[0]).resize((70, 70)))
    images = [img1, img2, img3, img4, img5, img6, img7, img8,
              img9, img10, img11, img12, img13, img14, img15, img16]
    random.shuffle(images)
    b1 = customtkinter.CTkButton(
        frame2, image=images[0], text="", padx=10, pady=10, height=70, width=70)
    b2 = customtkinter.CTkButton(
        frame2, image=images[1], text="", padx=10, pady=10, height=70, width=70)
    b3 = customtkinter.CTkButton(
        frame2, image=images[2], text="", padx=10, pady=10, height=70, width=70)
    b4 = customtkinter.CTkButton(
        frame2, image=images[3], text="", padx=10, pady=10, height=70, width=70)
    b5 = customtkinter.CTkButton(
        frame2, image=images[4], text="", padx=10, pady=10, height=70, width=70)
    b6 = customtkinter.CTkButton(
        frame2, image=images[5], text="", padx=10, pady=10, height=70, width=70)
    b7 = customtkinter.CTkButton(
        frame2, image=images[6], text="", padx=10, pady=10, height=70, width=70)
    b8 = customtkinter.CTkButton(
        frame2, image=images[7], text="", padx=10, pady=10, height=70, width=70)
    b9 = customtkinter.CTkButton(
        frame2, image=images[8], text="", padx=10, pady=10, height=70, width=70)
    b10 = customtkinter.CTkButton(
        frame2, image=images[9], text="", padx=10, pady=10, height=70, width=70)
    b11 = customtkinter.CTkButton(
        frame2, image=images[10], text="", padx=10, pady=10, height=70, width=70)
    b12 = customtkinter.CTkButton(
        frame2, image=images[11], text="", padx=10, pady=10, height=70, width=70)
    b13 = customtkinter.CTkButton(
        frame2, image=images[12], text="", padx=10, pady=10, height=70, width=70)
    b14 = customtkinter.CTkButton(
        frame2, image=images[13], text="", padx=10, pady=10, height=70, width=70)
    b15 = customtkinter.CTkButton(
        frame2, image=images[14], text="", padx=10, pady=10, height=70, width=70)
    b16 = customtkinter.CTkButton(
        frame2, image=images[15], text="", padx=10, pady=10, height=70, width=70)

    # List of index for randomizing buttons in grid
    ranLst = ["11", "12", "13", "14", "21", "22", "23",
              "24", "31", "32", "33", "34", "41", "42", "43", "44"]
    random.shuffle(ranLst)
    # Grid Position
    b1.grid(row=int(ranLst[0][0]), column=int(ranLst[0][1]))
    b2.grid(row=int(ranLst[1][0]), column=int(ranLst[1][1]))
    b3.grid(row=int(ranLst[2][0]), column=int(ranLst[2][1]))
    b4.grid(row=int(ranLst[3][0]), column=int(ranLst[3][1]))
    b5.grid(row=int(ranLst[4][0]), column=int(ranLst[4][1]))
    b6.grid(row=int(ranLst[5][0]), column=int(ranLst[5][1]))
    b7.grid(row=int(ranLst[6][0]), column=int(ranLst[6][1]))
    b8.grid(row=int(ranLst[7][0]), column=int(ranLst[7][1]))
    b9.grid(row=int(ranLst[8][0]), column=int(ranLst[8][1]))
    b10.grid(row=int(ranLst[9][0]), column=int(ranLst[9][1]))
    b11.grid(row=int(ranLst[10][0]), column=int(ranLst[10][1]))
    b12.grid(row=int(ranLst[11][0]), column=int(ranLst[11][1]))
    b13.grid(row=int(ranLst[12][0]), column=int(ranLst[12][1]))
    b14.grid(row=int(ranLst[13][0]), column=int(ranLst[13][1]))
    b15.grid(row=int(ranLst[14][0]), column=int(ranLst[14][1]))
    b16.grid(row=int(ranLst[15][0]), column=int(ranLst[15][1]))
    submit = Button(frame2, text="Submit")
    submit.grid(row=5, column=2, columnspan=2, pady=20)


def smallGrid():

    frame3 = LabelFrame(root, text="Fruits", padx=27, pady=20)
    frame3.grid(row=1, column=0, padx=(70, 30))
    img1 = ImageTk.PhotoImage(Image.open("A/1.jpg").resize((70, 70)))
    img2 = ImageTk.PhotoImage(Image.open("B/1.jpg").resize((70, 70)))
    img3 = ImageTk.PhotoImage(Image.open("F/1.jpg").resize((70, 70)))
    img4 = ImageTk.PhotoImage(Image.open("G/1.jpg").resize((70, 70)))
    img5 = ImageTk.PhotoImage(Image.open("M/1.jpg").resize((70, 70)))
    img6 = ImageTk.PhotoImage(Image.open("O/1.jpg").resize((70, 70)))
    img7 = ImageTk.PhotoImage(Image.open("P/1.jpg").resize((70, 70)))
    img8 = ImageTk.PhotoImage(Image.open("S/1.jpg").resize((70, 70)))
    img9 = ImageTk.PhotoImage(Image.open("W/1.jpg").resize((70, 70)))
    b1 = customtkinter.CTkButton(
        frame3, image=img1, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('A', 'F'))
    b2 = customtkinter.CTkButton(
        frame3, image=img2, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('B', 'F'))
    b3 = customtkinter.CTkButton(
        frame3, image=img3, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('F', 'F'))
    b4 = customtkinter.CTkButton(
        frame3, image=img4, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('G', 'F'))
    b5 = customtkinter.CTkButton(
        frame3, image=img5, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('M', 'F'))
    b6 = customtkinter.CTkButton(
        frame3, image=img6, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('O', 'F'))
    b7 = customtkinter.CTkButton(
        frame3, image=img7, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('P', 'F'))
    b8 = customtkinter.CTkButton(
        frame3, image=img8, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('S', 'F'))
    b9 = customtkinter.CTkButton(
        frame3, image=img9, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('W', 'F'))
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    frame4 = LabelFrame(root, text="Chocolates", padx=27, pady=20)
    frame4.grid(row=1, column=2, padx=(70, 30))
    img1 = ImageTk.PhotoImage(Image.open("9/1.jpg").resize((70, 70)))
    img2 = ImageTk.PhotoImage(Image.open("C/1.jpg").resize((70, 70)))
    img3 = ImageTk.PhotoImage(Image.open("D/1.jpg").resize((70, 70)))
    img4 = ImageTk.PhotoImage(Image.open("H/1.jpg").resize((70, 70)))
    img5 = ImageTk.PhotoImage(Image.open("I/1.jpg").resize((70, 70)))
    img6 = ImageTk.PhotoImage(Image.open("K/1.jpg").resize((70, 70)))
    img7 = ImageTk.PhotoImage(Image.open("R/1.jpg").resize((70, 70)))
    img8 = ImageTk.PhotoImage(Image.open("T/1.jpg").resize((70, 70)))
    img9 = ImageTk.PhotoImage(Image.open("N/1.jpg").resize((70, 70)))
    b1 = customtkinter.CTkButton(
        frame4, image=img1, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('9', 'C'))
    b2 = customtkinter.CTkButton(
        frame4, image=img2, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('C', 'C'))
    b3 = customtkinter.CTkButton(
        frame4, image=img3, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('D', 'C'))
    b4 = customtkinter.CTkButton(
        frame4, image=img4, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('H', 'C'))
    b5 = customtkinter.CTkButton(
        frame4, image=img5, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('I', 'C'))
    b6 = customtkinter.CTkButton(
        frame4, image=img6, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('K', 'C'))
    b7 = customtkinter.CTkButton(
        frame4, image=img7, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('R', 'C'))
    b8 = customtkinter.CTkButton(
        frame4, image=img8, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('T', 'C'))
    b9 = customtkinter.CTkButton(
        frame4, image=img9, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('N', 'C'))
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    frame5 = LabelFrame(root, text="Alphabets", padx=27, pady=20)
    frame5.grid(row=1, column=3, padx=(70, 30))
    img1 = ImageTk.PhotoImage(Image.open("E/1.jpg").resize((70, 70)))
    img2 = ImageTk.PhotoImage(Image.open("J/1.jpg").resize((70, 70)))
    img3 = ImageTk.PhotoImage(Image.open("L/1.jpg").resize((70, 70)))
    img4 = ImageTk.PhotoImage(Image.open("Y/1.jpg").resize((70, 70)))
    img5 = ImageTk.PhotoImage(Image.open("Q/1.jpg").resize((70, 70)))
    img6 = ImageTk.PhotoImage(Image.open("U/1.jpg").resize((70, 70)))
    img7 = ImageTk.PhotoImage(Image.open("V/1.jpg").resize((70, 70)))
    img8 = ImageTk.PhotoImage(Image.open("X/1.jpg").resize((70, 70)))
    img9 = ImageTk.PhotoImage(Image.open("Z/1.jpg").resize((70, 70)))
    b1 = customtkinter.CTkButton(
        frame5, image=img1, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('E', 'A'))
    b2 = customtkinter.CTkButton(
        frame5, image=img2, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('J', 'A'))
    b3 = customtkinter.CTkButton(
        frame5, image=img3, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('L', 'A'))
    b4 = customtkinter.CTkButton(
        frame5, image=img4, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('Y', 'A'))
    b5 = customtkinter.CTkButton(
        frame5, image=img5, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('Q', 'A'))
    b6 = customtkinter.CTkButton(
        frame5, image=img6, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('U', 'A'))
    b7 = customtkinter.CTkButton(
        frame5, image=img7, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('V', 'A'))
    b8 = customtkinter.CTkButton(
        frame5, image=img8, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('X', 'A'))
    b9 = customtkinter.CTkButton(
        frame5, image=img9, text="", padx=10, pady=10, height=70, width=70, command=lambda: store('Z', 'A'))
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def Signup():
    for widgets in root.winfo_children():
        widgets.destroy()
    frame1 = LabelFrame(root, text="SignUp", padx=40, pady=40)
    frame1.grid(row=0, column=0, padx=40, pady=40)
    userLabel = Label(frame1, text="UserID")
    userLabel.grid(row=0, column=0)
    userentry = Entry(frame1)
    userentry.grid(row=0, column=1)
    # global username
    username = userentry.get()

    emailLabel = Label(frame1, text="E-mail")
    emailLabel.grid(row=1, column=0, padx=10, pady=10)
    emailEntry = Entry(frame1)
    emailEntry.grid(row=1, column=1)
    # global email
    email = emailEntry.get()
    priorityLabel = Label(frame1, text="Priority Order:")
    priorityLabel.grid(row=2, column=0)
    pLabel1 = Label(frame1, text="Fruits")
    pLabel1.grid(row=2, column=1)
    pEntry1 = Entry(frame1, width=3)
    pEntry1.grid(row=2, column=1, sticky='e')
    pLabel2 = Label(frame1, text="Chocolate")
    pLabel2.grid(row=3, column=1)
    pEntry2 = Entry(frame1, width=3)
    pEntry2.grid(row=3, column=1, sticky='e')
    pLabel3 = Label(frame1, text="Alphabets")
    pLabel3.grid(row=4, column=1)
    pEntry3 = Entry(frame1, width=3)
    pEntry3.grid(row=4, column=1, sticky='e')
    smallGrid()
    submitSiup = Button(root, text='submit',
                        command=lambda: signupstore(userentry.get(), emailEntry.get(), pEntry1.get(), pEntry2.get(), pEntry3.get()))
    submitSiup.grid(row=5, column=1, columnspan=2, pady=(20, 0), padx=(30, 0))


# Home page
heading = Label(root, text="Graphical Password")
heading.config(font=('Times', 30, 'italic'))
heading.pack(pady=(90, 10))
login = Button(root, text="Login", width=20, height=2, command=Login)
login.pack(pady=20)
signup = Button(root, text="Signup", width=20, height=2, command=Signup)
signup.pack()

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
