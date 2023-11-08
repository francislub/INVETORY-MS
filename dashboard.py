from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="black")
        self.root .title("Inventory Management System | Developed by Francis")
        
        
        #====================title================
        self.icon_title = PhotoImage(file="images/logo.png")
        desired_width = 100
        desired_height = 50
        self.icon_title = self.icon_title.subsample(int(self.icon_title.width() / desired_width), int(self.icon_title.height() / desired_height)) 
        title= Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #============btn_logout=====
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #========clock================
        self.lbl_clock = Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYY\t\t Time: HH:MM:SS" ,font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #===========Left Menu==============
        self.MenuLogo= Image.open("images/menu.jpg")
        self.MenuLogo = self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=600)
        
        lbl_menuLogo = Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        self.icon_side = PhotoImage(file="images/side.png")
        new_width, new_height = 40, 40  # Set the new dimensions
        self.icon_side = self.icon_side.subsample(self.icon_side.width()// new_width, self.icon_side.height() // new_height)
        
        lbl_menu = Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee = Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu,text="Supplier",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu,text="Products",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #===============content==================
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=250,y=120,height=100,width=200)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=450,y=120,height=100,width=200)
        
        self.lbl_category=Label(self.root,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=650,y=120,height=100,width=200)
       
        self.lbl_product=Label(self.root,text="Total Product\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=850,y=120,height=100,width=200)
       
        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=1050,y=120,height=100,width=200)
       
       
        #========footer================
        lbl_footer = Label(self.root,text="IMS-Inventory Management System | Developed by Francis \nFor any Technical Issue Contact: 0741789121",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)
    #==============================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj= employeeClass(self.new_win)
if __name__=="__main__":
    root=Tk()
    ob = IMS(root)
    root.mainloop()