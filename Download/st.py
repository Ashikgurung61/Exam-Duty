from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from Report_Page import *
root = Tk()
con = mysql.connector.connect(host = "localhost", user = "root",passwd = "2020Bca01",database = "t_detail")
cursor = con.cursor()
def put():
    label1.configure(text=Exa.get())
    label4.configure(text=Etimes.get())
    label6.configure(text=shiftVs.get())
    label8.configure(text=showdate.get())
    label2.configure(text = showyear.get())

def finale():
    global root33, label1, label2,choice, label4, label4, label8, Etimes, Exa,shiftVs,showdate, showyear, label6,tree, data
    root33= Tk()
    root33.geometry("1250x680+30+15")
    root33.title("Duty Chart")
    root33.configure(bg = "#326273")
    root33.resizable(0,0)
    try:
        # windows only (remove the minimize/maximize button)
        root33.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')
    
    frame = Frame(root33, bd = 10, width = 1230, height= 120, bg = "White")
    frame.place(x = 10, y = 20)

    Headinglines = Frame (root33,  height = 121,width=3, background="violet")
    Headinglines.place(x = 500, y = 20)

    bodyline = Frame(root33, height = 600,width=3, background="Black")
    bodyline.place(x = 500, y = 140)


    data = Frame(root33,border = 3, background= "#326273")
    data.place( x = 33, y = 200)

    E = Label(root33,text="Exam",fg = "Navy BLue", font="ar 24 bold").place(x = 190, y = 30)
    D = Label(root33,text = "Duty", font = "ar 24 bold", fg = "RED").place(x = 285, y = 30)
    A = Label(root33,text = "Allotment", font = "ar 24 bold", fg = "green").place(x = 190, y = 80)
    S = Label(root33,text = "System", font = "ar 24 bold", fg = "orange").place(x = 350, y = 80)

    CollegeName = Label(root33, text = "Don Bosco College, Maram",font=("Times New Roman",26))
    CollegeName.place(x = 660, y = 35)

    subheading = Frame(root33, bg = "White")
    subheading.place(x = 720,  y = 95)

    label0 = Label(subheading,text = "Examination,",font=("Times New Roman",16))
    label0.grid(row = 0, column = 1,padx = 6)

    label1 = Label(subheading,text = "       ",font=("Times New Roman",16))
    label1.grid(row = 0, column = 0,padx = 6)

    label2 = Label(subheading,text = "Year",font=("Times New Roman",16))
    label2.grid(row = 0, column = 2, padx = 6)

    frame = Frame(root33, bd = 5, width = 800, height= 90, bg = "#326273")
    frame.place(x = 600, y = 150)

    label3 = Label(frame,text = "Duration:",font = ("Gabriola",14), bg = "#326273", fg = "Red")
    label3.grid(row = 0, column=0)

    label4 = Label(frame, text = "             ",font = ("Times New Roman",14), bg = "#326273")
    label4.grid(row = 0, column=1, padx= 20)

    label5 = Label(frame,text = "Shift:",font = ("Gabriola",14), fg = "Red",bg = "#326273")
    label5.grid(row = 0, column=2, padx = 20)

    label6 = Label(frame, text = "            ",font = ("Times New Roman",14), bg = "#326273")
    label6.grid(row = 0, column=3)

    label7 = Label(frame,text = "Date:",font = ("Gabriola",14), fg = "Red",bg = "#326273")
    label7.grid(row = 0, column=4, padx = 20)

    label8 = Label(frame, text = "             ",font = ("Times New Roman",14), bg = "#326273")
    label8.grid(row = 0, column=5)    

    shift = Label(data,text="Shift:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    shift.grid(row = 5, column = 0,padx = 10, pady = 10)
        
    time = Label(data,text ="Duration",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    time.grid(row = 4, column= 0, padx = 10, pady = 10)
        
    Etimes = ttk.Combobox(data,values = ["","1 hour","2 hour","3 hour"],width = 28)
    Etimes.grid(row = 4, column = 1, padx = 10, pady=10)

    shiftVs = ttk.Combobox(data,values = ["","M o r n i n g","E v e n i n g"],width = 28)
    shiftVs.grid(row = 5, column = 1, padx = 10, pady=10)

    choicelab = Label(data, text = "Confimr Shift",font = ("Times New Roman",14),fg = "White", bg = "#326273")
    choicelab.grid(row = 6, column = 0)

    choice = StringVar()
    t = Radiobutton(data, text = "Morning",value = "0", variable = choice, bg = "#326273")
    t.grid(row = 6, column = 1, padx = 10, pady = 10)
    t1 = Radiobutton(data, text = "Evening",value = "1", variable= choice, bg = "#326273")
    t1.grid(row = 6, column = 2, padx = 10, pady = 10)
#------------------------------------------------Menu----------------------------------------------------------------
    back1 = Button(root33, bd = 0, width = 10,bg = "white", text = "Home", fg = "Black", command= root33.destroy)
    back1.place(x = 10, y = 141)
    
    def rep():
        report()

    check = Button(root33, bd = 0, width = 10,bg = "white", text = "Status", fg = "Black", command= rep)
    check.place(x = 88, y = 141)

    close = Button(root33, bd = 0, width = 10,bg = "white", text = "Quit", fg = "Black", command= True)
    close.place(x = 166, y = 141)
#-----------------------------------------------is here--------------------------------------------------------------
    exam = Label(data,text = "Examination:", fg = "White", bg = "#326273",font = ("Times New Roman",14))
    exam.grid(row = 7, column = 0, padx = 10, pady = 10)
        
    Exa = Entry(data, border = 5,width = 30)
    Exa.grid( row = 7, column = 1, padx = 10, pady = 10)

    date = Label(data, text = "Date:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    date.grid(row = 8, column = 0, padx = 10, pady = 10)
        
    showdate = Entry(data, bd = 5,width = 30)
    showdate.grid(row = 8, column = 1, padx = 10, pady = 10)

    year = Label(data, text = "Year:",fg = "White", bg = "#326273",font = ("Times New Roman",14))
    year.grid(row = 9, column = 0, padx = 10, pady = 10)

    showyear = ttk.Combobox(data, values=["","2022","2023","2024","2025","2026"] ,width = 28)
    showyear.grid(row = 9, column = 1, padx = 10, pady = 10)

    generate = Button(root33, text = "Insert",bg = "pink", border = 3,width = 25, command = put)
    generate.place(x = 167, y = 485)

    def contin():
        global enter, w1, w2, w3, w4, w5
        w1 = Exa.get()
        w2 = Etimes.get()
        w3 = shiftVs.get()
        w4 = showdate.get()
        w5 = showyear.get()
        #if w1 == "" or w2 == ""or w3 == "" or w4 == "" or w5 == "":
            #info11 = Label(root33, text="Please enter the given above fills for the exam",bg = "#326273", font = ("Times new roman",14), fg = "Red")
            #info11.place(x = 80, y = 530 )
        #else:
        data.destroy()
        generate.destroy()
        cont.destroy()

        teach = Frame(root33,bg = "#326273")
        teach.place(x = 150, y = 300)
            
        label9 = Label(teach, text = "Enter the number \n of teacher:",bg = "#326273",font = ("Times New Roman",14))
        label9.grid( row = 0, column = 0, padx = 10, pady = 10)

        enter = Entry(teach, bd = 4, width = 15)
        enter.grid(row = 1, column = 0, padx = 10, pady = 10)

        ran = Button(root33, text = "Go",width = 15,bg = "pink",command = go)
        ran.place(x = 170, y = 450)

        clear = Button(root33, text = "Clear", width = 15, command = True, bg = "Blue")
        clear.place(x = 170, y = 500)
        
    cont = Button(root33, text = "Continue",bg = "Green", border = 3,width = 25, command = contin)
    cont.place(x = 167, y = 585)
    #----------------------------------The Tree is here----------------------------------------
    #tree = ttk.Treeview(root33, columns = (1),show = "headings", height = "21")
    #tree.place(x = 850, y = 200)
    #s= ttk.Style(root33)  

    #s.theme_use("winnative")
    #tree.heading(1, text = "Invigilator's")

    trees = ttk.Treeview(root33, columns = (1,2),show = "headings", height = "21")
    trees.place(x = 647, y = 200)

    s= ttk.Style(root33)  
    s.theme_use("winnative")

    sql = "Select hNo from ehall"
    cursor.execute(sql)

    sol = cursor.fetchall()
    trees.heading(1, text = "Hall Number")
    trees.heading(2, text = "Invigilator")
    for rows in sol:
        trees.insert('', 'end', values=rows)
    
    image = Image.open("C:\\Users\\user\\py\\Examples\\logo.png")
    resize = image.resize((90,90),Image.Resampling.LANCZOS)
    new1 = ImageTk.PhotoImage(resize)
    showima = ttk.Label(root33,image=new1)
    showima.place(x = 80, y = 30)

    root33.mainloop()

#-------------------------------Random Name---------------------------------------

def go():
    global results
    try:    
        global tree
        e1 = enter.get()
        e2 = choice.get()
        lancelot = e2
        query = "SELECT t_name FROM t_register where status = %s ORDER BY RAND() LIMIT "+e1
        cursor.execute(query,(lancelot,))
    # get the results
        results = cursor.fetchall()
        for rows in results:
            trees.insert('', 'end', values = rows)
    except: 
        print("error")

Button(root, text = "SHow me ur game bro!",command=finale).pack()
root.mainloop()
#------------------------------------------------------------------------------------------------------------------