from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Softwarica College of IT and E-Commerce",bd=10,relief=GROOVE,
                    font=("arial",40,"bold"), bg="lightblue",fg='darkblue')
        title.pack(side=TOP,fill=X)

        #variables==========
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()
        self.contact_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()


        #manage frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",bg="lightblue",fg="black",font=("arial",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No",bg="lightblue",fg="black",font=("arial",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var, font=("arial",13,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="lightblue", fg="black", font=("arial", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.name_var, font=("arial", 13, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="lightblue", fg="black", font=("arial", 20, "bold"))
        lbl_gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame, textvariable=self.gender_var,font=("arial",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=3,column=1,padx=20,pady=10)

        lbl_email = Label(Manage_Frame, text="Email", bg="lightblue", fg="black", font=("arial", 20, "bold"))
        lbl_email.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("arial", 13, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="lightblue", fg="black", font=("arial", 20, "bold"))
        lbl_address.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Address = Entry(Manage_Frame, textvariable=self.address_var, font=("arial", 13, "bold"), bd=5, relief=GROOVE)
        txt_Address.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Contact NO.", bg="lightblue", fg="black", font=("arial", 20, "bold"))
        lbl_contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("arial", 13, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        #button frame
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="lightgray")
        btn_Frame.place(x=10, y=500, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)


        #detail frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightblue")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_search=Label(Detail_Frame, text="Search By", bg="lightblue", fg="black", font=("arial", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10, font=("arial", 13, "bold"), state='readonly')
        combo_search['values'] = ("roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt,font=("arial", 13, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)


        #table frame=====

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="lightblue")
        Table_Frame.place(x=10, y=70, width=770, height=485)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","gender","email","address","contact"),
                                   xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll_no")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("address", text="Address")
        self.Student_table.heading("contact", text="Contact No.")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=200)
        self.Student_table.column("gender", width=200)
        self.Student_table.column("email", width=200)
        self.Student_table.column("address", width=200)
        self.Student_table.column("contact", width=200)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    #add button====
    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                          self.name_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.email_var.get(),
                                                                          self.address_var.get(),
                                                                          self.contact_var.get()

            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Sucess","Record has been imported")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    #clear button ========
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.contact_var.set("")


    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.gender_var.set(row[2])
        self.email_var.set(row[3])
        self.address_var.set(row[4])
        self.contact_var.set(row[5])

#update button===
    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s, gender=%s, email=%s, address=%s, contact=%s where roll_no=%s", (
                                                                       self.name_var.get(),
                                                                       self.gender_var.get(),
                                                                       self.email_var.get(),
                                                                       self.address_var.get(),
                                                                       self.contact_var.get(),
                                                                       self.Roll_No_var.get()
                                                                       ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

     #delete data =====
    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    #search data=====
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()
