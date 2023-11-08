from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root = root
        #self.root.geometry("1350x700+0+0")
        self.root.geometry("1100x500+220+130")
        self.root.configure(bg="white")
        self.root .title("Inventory Management System | Developed by Francis")
        self.root.focus_force()
        #==============================================All Variables==============
        self.var_emp_searchby=StringVar()
        self.var_emp_searchtxt=StringVar()
        
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        
        #============================seachFrame#################################
        searchFrame = LabelFrame(self.root, text="Seach Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchFrame.place(x=250, y=20,width=600,height=70)
        
        #===============options===================
        cmb_seach = ttk.Combobox(searchFrame,textvariable=self.var_emp_searchby, values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_seach.place(x=10,y=10,width=180)
        cmb_seach.current(0)
        
        txt_seach = Entry(searchFrame,textvariable=self.var_emp_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_seach = Button(searchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        
        #======================title=========================
        title = Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)
        
        #==================content================================
        #============row1======================
        lbl_empid = Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender = Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact = Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        
        lbl_empid = Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_gender, values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        lbl_contact = Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
        #=============row2=======================
        lbl_name = Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob = Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj = Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)
        
        lbl_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        lbl_dob = Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        lbl_doj = Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        #=============row3=======================
        lbl_email = Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_pass = Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_utype = Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)
        
        lbl_email = Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        lbl_pass= Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        cmb_utype = ttk.Combobox(self.root,textvariable=self.var_utype, values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
        #=============row4=======================
        lbl_address = Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salary = Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
        
        self.txt_address = Entry(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary= Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)
        #=====================button=============================
        btn_add = Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update = Button(self.root,text="Update",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete = Button(self.root,text="Delete",font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        #===========================Employee Details========================
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        
        Scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        Scrollx = Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.EmployeeTable = ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.EmployeeTable.xview)
        Scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        
        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid",width=50)
        self.EmployeeTable.column("name",width=250)
        self.EmployeeTable.column("email",width=300)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=150)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=200)
        self.EmployeeTable.column("address",width=200)
        self.EmployeeTable.column("salary",width=200)
        
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        #================================================
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required", parent = self.root)
            else:
                cur.execute("Select * from employee where eid = ?", (self.var_emp_id(),))
                row = cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error","This Employee ID already assigned, Try different", parent = self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.var_address.get(),
                        self.var_salary.get()
                    ))
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent = self.root)
        
        
if __name__=="__main__":
    root=Tk()
    ob = employeeClass(root)
    root.mainloop()