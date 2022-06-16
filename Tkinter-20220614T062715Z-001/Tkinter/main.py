from tkinter import *
import tkinter.font as tkFont
import random
from PIL import ImageTk, Image
import customtkinter
import sqlite3

root = Tk()
root.title("Graphical Password")
root.geometry("600x675")

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# create a database or connect to one
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# create table
'''c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)""")'''

# # Create Submit function for Database
# def submit():
#     # create a database or connect to one
#     conn = sqlite3.connect('customer.db')
#     # create cursor
#     c = conn.cursor()
#     # Insert into Table
#     c.execute("INSERT INTO customers VALUES (:userID, :email, :password)",
#               {
#                   'userID': username,
#                   'email': email,
#                   # 'password': password,
#               })
#     # commit changes
#     conn.commit()
#     # close connection
#     conn.close()
#     # Clear The Text Boxes
#     # f_name.delete(0, END)
#     # l_name.delete(0, END)
#     # address.delete(0, END)
#     # city.delete(0, END)
#     # state.delete(0, END)
#     # zipcode.delete(0, END)
#
#
# # Create query function
# def query():
#     # create a database or connect to one
#     conn = sqlite3.connect('customer.db')
#     # create cursor
#     c = conn.cursor()
#
#     # Query the Database
#     c.execute("SELECT *, oid FROM customers")
#     records = c.fetchall()
#     # print(records)
#
#     # Loop through labels
#     print_records = ''
#     for record in records:
#         print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
#
#     query_label = Label(root, text=print_records)
#     query_label.grid(row=12, column=0, columnspan=2)
#
#     # commit changes
#     conn.commit()
#     # close connection
#     conn.close()
#
# # Create Submit Button
# submit_btn = Button(root, text="Add Record To Database", command=submit)
# submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
#
# # Create Query Button
# query_btn = Button(root, text="Show Records", command=query)
# query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

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
    graphicPass()

    userLabel = Label(frame1, text="Password")
    Button(text="submit", command=graphicPass).grid(row=3, column=1)


# grid for images
def graphicPass():
    frame2 = LabelFrame(root, text="Password", padx=27, pady=20)
    frame2.pack()
    category = ['4', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    random.shuffle(category)
    pics = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    random.shuffle(pics)
    img1 = ImageTk.PhotoImage(Image.open(category[0] + "/" + pics[0]).resize((100, 100)))
    img2 = ImageTk.PhotoImage(Image.open(category[1] + "/" + pics[0]).resize((100, 100)))
    img3 = ImageTk.PhotoImage(Image.open(category[2] + "/" + pics[0]).resize((100, 100)))
    img4 = ImageTk.PhotoImage(Image.open(category[3] + "/" + pics[0]).resize((100, 100)))
    img5 = ImageTk.PhotoImage(Image.open(category[4] + "/" + pics[0]).resize((100, 100)))
    img6 = ImageTk.PhotoImage(Image.open(category[5] + "/" + pics[0]).resize((100, 100)))
    img7 = ImageTk.PhotoImage(Image.open(category[6] + "/" + pics[0]).resize((100, 100)))
    img8 = ImageTk.PhotoImage(Image.open(category[7] + "/" + pics[0]).resize((100, 100)))
    img9 = ImageTk.PhotoImage(Image.open(category[8] + "/" + pics[0]).resize((100, 100)))
    img10 = ImageTk.PhotoImage(Image.open(category[9] + "/" + pics[0]).resize((100, 100)))
    img11 = ImageTk.PhotoImage(Image.open(category[10] + "/" + pics[0]).resize((100, 100)))
    img12 = ImageTk.PhotoImage(Image.open(category[11] + "/" + pics[0]).resize((100, 100)))
    img13 = ImageTk.PhotoImage(Image.open(category[12] + "/" + pics[0]).resize((100, 100)))
    img14 = ImageTk.PhotoImage(Image.open(category[13] + "/" + pics[0]).resize((100, 100)))
    img15 = ImageTk.PhotoImage(Image.open(category[14] + "/" + pics[0]).resize((100, 100)))
    img16 = ImageTk.PhotoImage(Image.open(category[15] + "/" + pics[0]).resize((100, 100)))
    fruits = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16]
    random.shuffle(fruits)
    b1 = customtkinter.CTkButton(frame2, image=fruits[0], text="", padx=30, pady=30)
    b2 = customtkinter.CTkButton(frame2, image=fruits[1], text="", padx=30, pady=30)
    b3 = customtkinter.CTkButton(frame2, image=fruits[2], text="", padx=30, pady=30)
    b4 = customtkinter.CTkButton(frame2, image=fruits[3], text="", padx=30, pady=30)
    b5 = customtkinter.CTkButton(frame2, image=fruits[4], text="", padx=30, pady=30)
    b6 = customtkinter.CTkButton(frame2, image=fruits[5], text="", padx=30, pady=30)
    b7 = customtkinter.CTkButton(frame2, image=fruits[6], text="", padx=30, pady=30)
    b8 = customtkinter.CTkButton(frame2, image=fruits[7], text="", padx=30, pady=30)
    b9 = customtkinter.CTkButton(frame2, image=fruits[8], text="", padx=30, pady=30)
    b10 = customtkinter.CTkButton(frame2, image=fruits[9], text="", padx=30, pady=30)
    b11 = customtkinter.CTkButton(frame2, image=fruits[10], text="", padx=30, pady=30)
    b12 = customtkinter.CTkButton(frame2, image=fruits[11], text="", padx=30, pady=30)
    b13 = customtkinter.CTkButton(frame2, image=fruits[12], text="", padx=30, pady=30)
    b14 = customtkinter.CTkButton(frame2, image=fruits[13], text="", padx=30, pady=30)
    b15 = customtkinter.CTkButton(frame2, image=fruits[14], text="", padx=30, pady=30)
    b16 = customtkinter.CTkButton(frame2, image=fruits[15], text="", padx=30, pady=30)

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
    submit = Button(frame2, text="submit")
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
    b1 = customtkinter.CTkButton(frame3, image=img1, text="", padx=10, pady=10, height=70, width=70)
    b2 = customtkinter.CTkButton(frame3, image=img2, text="", padx=10, pady=10, height=70, width=70)
    b3 = customtkinter.CTkButton(frame3, image=img3, text="", padx=10, pady=10, height=70, width=70)
    b4 = customtkinter.CTkButton(frame3, image=img4, text="", padx=10, pady=10, height=70, width=70)
    b5 = customtkinter.CTkButton(frame3, image=img5, text="", padx=10, pady=10, height=70, width=70)
    b6 = customtkinter.CTkButton(frame3, image=img6, text="", padx=10, pady=10, height=70, width=70)
    b7 = customtkinter.CTkButton(frame3, image=img7, text="", padx=10, pady=10, height=70, width=70)
    b8 = customtkinter.CTkButton(frame3, image=img8, text="", padx=10, pady=10, height=70, width=70)
    b9 = customtkinter.CTkButton(frame3, image=img9, text="", padx=10, pady=10, height=70, width=70)
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
    frame4.grid(row=1, column=2)
    img1 = ImageTk.PhotoImage(Image.open("9/1.jpg").resize((70, 70)))
    img2 = ImageTk.PhotoImage(Image.open("C/1.jpg").resize((70, 70)))
    img3 = ImageTk.PhotoImage(Image.open("D/1.jpg").resize((70, 70)))
    img4 = ImageTk.PhotoImage(Image.open("H/1.jpg").resize((70, 70)))
    img5 = ImageTk.PhotoImage(Image.open("I/1.jpg").resize((70, 70)))
    img6 = ImageTk.PhotoImage(Image.open("K/1.jpg").resize((70, 70)))
    img7 = ImageTk.PhotoImage(Image.open("R/1.jpg").resize((70, 70)))
    img8 = ImageTk.PhotoImage(Image.open("T/1.jpg").resize((70, 70)))
    img9 = ImageTk.PhotoImage(Image.open("N/1.jpg").resize((70, 70)))
    b1 = customtkinter.CTkButton(frame4, image=img1, text="", padx=10, pady=10, height=70, width=70)
    b2 = customtkinter.CTkButton(frame4, image=img2, text="", padx=10, pady=10, height=70, width=70)
    b3 = customtkinter.CTkButton(frame4, image=img3, text="", padx=10, pady=10, height=70, width=70)
    b4 = customtkinter.CTkButton(frame4, image=img4, text="", padx=10, pady=10, height=70, width=70)
    b5 = customtkinter.CTkButton(frame4, image=img5, text="", padx=10, pady=10, height=70, width=70)
    b6 = customtkinter.CTkButton(frame4, image=img6, text="", padx=10, pady=10, height=70, width=70)
    b7 = customtkinter.CTkButton(frame4, image=img7, text="", padx=10, pady=10, height=70, width=70)
    b8 = customtkinter.CTkButton(frame4, image=img8, text="", padx=10, pady=10, height=70, width=70)
    b9 = customtkinter.CTkButton(frame4, image=img9, text="", padx=10, pady=10, height=70, width=70)
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    frame5 = LabelFrame(root, text="Chocolates", padx=27, pady=20)
    frame5.grid(row=1, column=3)
    img1 = ImageTk.PhotoImage(Image.open("E/1.jpg").resize((70, 70)))
    img2 = ImageTk.PhotoImage(Image.open("J/1.jpg").resize((70, 70)))
    img3 = ImageTk.PhotoImage(Image.open("L/1.jpg").resize((70, 70)))
    img4 = ImageTk.PhotoImage(Image.open("Y/1.jpg").resize((70, 70)))
    img5 = ImageTk.PhotoImage(Image.open("Q/1.jpg").resize((70, 70)))
    img6 = ImageTk.PhotoImage(Image.open("U/1.jpg").resize((70, 70)))
    img7 = ImageTk.PhotoImage(Image.open("V/1.jpg").resize((70, 70)))
    img8 = ImageTk.PhotoImage(Image.open("X/1.jpg").resize((70, 70)))
    img9 = ImageTk.PhotoImage(Image.open("Z/1.jpg").resize((70, 70)))
    b1 = customtkinter.CTkButton(frame5, image=img1, text="", padx=10, pady=10, height=70, width=70)
    b2 = customtkinter.CTkButton(frame5, image=img2, text="", padx=10, pady=10, height=70, width=70)
    b3 = customtkinter.CTkButton(frame5, image=img3, text="", padx=10, pady=10, height=70, width=70)
    b4 = customtkinter.CTkButton(frame5, image=img4, text="", padx=10, pady=10, height=70, width=70)
    b5 = customtkinter.CTkButton(frame5, image=img5, text="", padx=10, pady=10, height=70, width=70)
    b6 = customtkinter.CTkButton(frame5, image=img6, text="", padx=10, pady=10, height=70, width=70)
    b7 = customtkinter.CTkButton(frame5, image=img7, text="", padx=10, pady=10, height=70, width=70)
    b8 = customtkinter.CTkButton(frame5, image=img8, text="", padx=10, pady=10, height=70, width=70)
    b9 = customtkinter.CTkButton(frame5, image=img9, text="", padx=10, pady=10, height=70, width=70)
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# def save():
#    print(username, email)

def Signup():
    for widgets in root.winfo_children():
        widgets.destroy()
    frame1 = LabelFrame(root, text="SignUp", padx=40, pady=40)
    frame1.grid(row=0, column=0, padx=40, pady=40)
    userLabel = Label(frame1, text="UserID")
    userLabel.grid(row=0, column=0)
    userentry = Entry(frame1)
    userentry.grid(row=0, column=1)
    global username
    username = userentry.get()
    emailLabel = Label(frame1, text="E-mail")
    emailLabel.grid(row=1, column=0, padx=10, pady=10)
    emailEntry = Entry(frame1)
    emailEntry.grid(row=1, column=1)
    global email
    email = emailEntry.get()
    priorityLabel= Label(frame1, text="Priority Order:")
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
