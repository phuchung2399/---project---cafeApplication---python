from tkinter import *
from tkinter import messagebox, ttk, Label, Tk

from BLL.AccountBLL import AccountBLL
#from GUI.HomeGUI import HomeGUI
from PIL import ImageTk, Image

from BLL.DecentralizationBLL import DecentralizationBLL
from BLL.StaffBLL import StaffBLL
from GUI.AccountGUI import AccountGUI
from GUI.BillGUI import BillGUI
from GUI.CategoryGUI import CategoryGUI
from GUI.CustomerGUI import CustomerGUI
from GUI.DecentralizationGUI import DecentralizationGUI
from GUI.IngredientGUI import IngredientGUI
from GUI.ProductGUI import ProductGUI
from GUI.ReceiptGUI import ReceiptGUI
from GUI.RecipeGUI import RecipeGUI
from GUI.SaleGUI import SaleGUI
from GUI.StaffGUI import StaffGUI
from GUI.SupplierGUI import SupplierGUI




class LoginGUI(Frame):
    def __init__(self):
        self.__master = Tk()
        self.init_components()


    def init_components(self):
        self.__master.configure(bg="#135066")
        self.__master.title("Đăng Nhập")
        self.__master.resizable(False, False)
        x_cordinate = int((self.__master.winfo_screenwidth()/2) - (700/2))
        y_cordinate = int((self.__master.winfo_screenheight()/2) - (500/2))
        self.__master.geometry("{}x{}+{}+{}".format(700, 500, x_cordinate, y_cordinate))

        self.contentPane = Frame(self.__master, bg="#135066", width=700, height=500)
        self.contentPane.pack(fill="both", expand=True)

        # Brand name

        self.panel1 = Frame(self.contentPane, bg="#135066", width=700, height=80)
        self.panel1.pack(side='top', fill='x')

        style = ttk.Style()
        style.configure('TSeparator', background='#ffffff')
        separator = ttk.Separator(self.panel1, orient='horizontal', style='TSeparator')
        separator.place(relx=0, rely=1, anchor='sw', relwidth=1)

        self.brandName = Label(self.panel1, text="Dũng Bảo Hưng Coffe", font=("open sans", 45, "bold"), fg="#ffffff", bg="#135066")
        self.brandName.place(relx=0.5, rely=0, anchor="n")

        # Login Form
        self.panel2 = Frame(self.contentPane, bg="#135066", width=300, height=400)
        self.panel2.pack(side='left')

        self.logo = Image.open(r"cafe_application/img/logo_cafe.png")
        self.logo = self.logo.resize((300, 300), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)

        self.logoLabel = Label(self.panel2, image=self.logo, bg="#135066")
        self.logoLabel.image = self.logo
        self.logoLabel.pack(pady=0)

        # Login Form
        self.panel3 = Frame(self.contentPane, bg="#135066", width=400, height=400, pady =90)
        self.panel3.pack(side="right")
        self.panel3.pack(fill="both", expand=True)

        self.panel4 = Frame(self.panel3, bg="#135066", width=300, height=70, pady=30)
        self.panel4.pack(side="top")

        self.loginLabel = Label(self.panel4, text="Đăng Nhập", font=("open sans", 30, "bold"), fg="#ffffff", bg="#135066")
        self.loginLabel.pack()

        self.panel5 = Frame(self.panel3, bg="#135066", width=300, height=150)
        self.panel5.pack()

        self.usernameLabel = Label(self.panel5, text="Tên đăng nhập", font=("Times New Roman", 10), fg="#ffffff", bg="#135066")
        self.usernameInput = Entry(self.panel5, font=("Times New Roman", 12), bg="#135066", fg="#ffffff")
        self.usernameInput.focus_set()
        self.passwordLabel = Label(self.panel5, text="Mật khẩu", font=("Times New Roman", 10), fg="#ffffff", bg="#135066")
        self.passwordInput = Entry(self.panel5, font=("Times New Roman", 12), bg="#135066", fg="#ffffff", show="*")

        self.usernameLabel.grid(row=0, column=0, padx=5, pady=10)
        self.usernameInput.grid(row=0, column=1, padx=5, pady=10)
        self.passwordLabel.grid(row=1, column=0, padx=5, pady=10)
        self.passwordInput.grid(row=1, column=1, padx=5, pady=10)

        self.usernameInput.insert(0, "")
        self.passwordInput.insert(0, "")

        self.usernameInput.bind("<FocusIn>", self.onClickUsername)
        self.passwordInput.bind("<FocusIn>", self.onClickPassword)

        # Login Panel Buttons
        self.loginButton = Button(self.panel3, text="Xác Nhận", font=("open sans", 12, "bold"), bg="#135066", fg="#ffffff", command=self.login)
        self.loginButton.pack(pady=(0, 20))

        self.usernameInput.bind("<Return>", self.on_enter_press)
        self.passwordInput.bind("<Return>", self.on_enter_press)
        self.__master.mainloop()

    def onClickUsername(self, event):
        if self.usernameInput.get() == "":
            self.usernameInput.delete(0, END)
        if self.passwordInput.get() == "":
            self.passwordInput.delete(0,END)
            self.passwordInput.insert(0, "")

    def onClickPassword(self, event):
        if self.passwordInput.get() == "":
            self.passwordInput.delete(0, END)
        if self.usernameInput.get() == "":
            self.usernameInput.delete(0,END)
            self.usernameInput.insert(0, "")

    def on_enter_press(self, event):
        self.login()

    def login(self):
        username = self.usernameInput.get()
        password = self.passwordInput.get()
        list = AccountBLL().searchAccounts("USERNAME = '" + username + "'", "PASSWD = '" + password + "'")
        if len(list) == 0:
            messagebox.showinfo("Message", "Kiểm tra lại thông tin đăng nhập!")
        else:
            account = list[0]
            #messagebox.showinfo("Message", "Đăng nhập thành công!")
            self.__master.destroy()
            HomeGUI(account)



class HomeGUI(Frame):
    def __init__(self, account):
        self.__account = account
        self.__staff = StaffBLL().searchStaffs("STAFF_ID = '" + self.__account.getStaffID() + "'")[0]
        self.__decentralization = DecentralizationBLL().searchDecentralizations("DECENTRALIZATION_ID = '" + self.__account.getDecentralizationID() + "'")[0]
        self.__arr = []
        self.__arr.append(0)
        self.__arr.append(self.__decentralization.getIsSale())
        self.__arr.append(self.__decentralization.getIsProduct())
        self.__arr.append(self.__decentralization.getIsCategory())
        self.__arr.append(self.__decentralization.getIsRecipe())
        self.__arr.append(self.__decentralization.getIsImport())
        self.__arr.append(self.__decentralization.getIsBill())
        self.__arr.append(self.__decentralization.getIsWarehouses())
        self.__arr.append(self.__decentralization.getIsDecentralize())
        self.__arr.append(self.__decentralization.getIsAccount())
        self.__arr.append(self.__decentralization.getIsStaff())
        self.__arr.append(self.__decentralization.getIsCustomer())
        self.__arr.append(self.__decentralization.getIsDiscount())
        self.__arr.append(self.__decentralization.getIsDecentralize())
        self.__arr.append(1)

        self.__master = Tk()
        self.init_components()


    def init_components(self):
        self.__master.configure(bg="#135066")
        self.__master.title("Home")
        self.__master.resizable(False, False)
        x_cordinate = int((self.__master.winfo_screenwidth()/2) - (1350/2))
        y_cordinate = int((self.__master.winfo_screenheight()/2) - (1000/2))
        self.__master.geometry("{}x{}+{}+{}".format(1350, 760, x_cordinate, y_cordinate))

        self.contentPane = Frame( bg="#ffffff", width=1350, height=1000)
        self.contentPane.master = self.__master
        self.contentPane.pack(fill="both", expand=True)

        self.west = Frame(self.contentPane, bg="#135066", width=300, height=1000)
        self.west.pack(side="left")
        self.west.pack(fill="both", expand=True)

        self.info = Frame(self.west, bg="#4D9EE0", width=280, height=80)
        self.info.place(x=10, y=10)

        self.imgAvartar = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/bell-boy.png").resize((60, 60), Image.ANTIALIAS))

        self.avatar = Label(self.info, image=self.imgAvartar, bg="#4D9EE0")
        self.avatar.place(x=10, y=10)

        self.name = Label(self.info, text="Tên: " + self.__staff.getName(), font=("Tahoma", 10), fg="#ffffff", bg="#4D9EE0")
        self.name.place(x=80, y=5)
        self.rule = Label(self.info, text="Vai trò: " + self.__decentralization.getDecentralizationName(), font=("Tahoma", 10), fg="#ffffff", bg="#4D9EE0")
        self.rule.place(x=80, y=30)
        self.logout = Button(self.info, text="Đăng xuất", font=("Tahoma", 10), fg="#FF0000", bg="#4D9EE0",borderwidth=0, command=self.Logout_btn)
        self.logout.place(x=80, y=55)

        self.imgMode = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/sun.png").resize((30, 30), Image.ANTIALIAS))
        self.mode = Label(self.info, image=self.imgMode, bg="#4D9EE0")
        self.mode.bind('<Button-1>', self.changeMode)
        self.mode.place(x=230, y=40)
        self.darkMode = True

        self.fram_cate = Frame(self.west, bg="#4D9EE0", width=280, height=650)
        self.fram_cate.place(x=10, y=100)

        self.cate = Frame(self.fram_cate, bg="#ffffff", width=260, height=545)
        self.cate.place(x=10, y=50)

        self.panel = []
        self.panel.append(None)
        for i in range(1, 13):
            self.panel.append(Frame(self.cate, bg="#4D9EE0", width=250, height=40))
            self.panel[i].bind('<Button-1>', self.on_panel_click)

        self.label = []
        self.label.append(None)
        self.label.append(Label(self.panel[1], text="Bán hàng", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[2], text="Sản phẩm", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[3], text="Loại sản phẩm", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[4], text="Công Thức", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[5], text="Nhập hàng", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[6], text="Hóa đơn", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[7], text="Nhà kho", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        #self.label.append(Label(self.panel[8], text="Thống kê", font=("Times New Roman", 15), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[8], text="Tài khoản", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[9], text="Nhân viên", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[10], text="Khách hàng", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        #self.label.append(Label(self.panel[12], text="Giảm giá", font=("Times New Roman", 15), fg="#ffffff", bg="#4D9EE0"))

        self.label.append(Label(self.panel[11], text="Phân quyền", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))
        self.label.append(Label(self.panel[12], text="Nhà cung cấp", font=("Times New Roman", 16), fg="#ffffff", bg="#4D9EE0"))

        self.icon = []
        self.image = []
        self.icon.append(None)
        self.image.append(None)
        for i in range(1, 12):
            url = fr"cafe_application/img/icons/{i:02}.png"
            self.icon.append(ImageTk.PhotoImage(Image.open(url).resize((30, 30), Image.ANTIALIAS)))
            self.image.append(Label(self.panel[i], image=self.icon[i], bg="#4D9EE0"))
        self.icon.append(ImageTk.PhotoImage(Image.open(url).resize((30, 30), Image.ANTIALIAS)))
        self.image.append(Label(self.panel[len(self.label)-1], image=self.icon[len(self.icon)-1], bg="#4D9EE0"))
        self.x = 5
        self.y = 5
        for i in range(1, 13):
            if self.__arr[i] != 0:
                self.panel[i].place(x=self.x, y=self.y)
                self.image[i].place(x=20, y=4)
                self.label[i].place(x=70, y=5)
                self.y = self.y + 45

        for i in range(1, 13):
            for child in self.panel[i].winfo_children():

                child.bind('<Button-1>', self.on_childPanel_click)

        self.east = Frame(self.contentPane, bg="#4D9EE0", width=1040, height=740)
        self.east.place(x=300, y=10)

        self.function = Frame(self.east, bg="#4D9EE0", width=1040, height=740)
        self.function.pack()


        self.__master.mainloop()

    def changeMode(self, event):
        if self.darkMode:
            self.imgMode = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/moon.png").resize((30, 30), Image.ANTIALIAS))
            self.mode.configure(image=self.imgMode, bg="#135066")

            self.__master.configure(bg="#4D9EE0")
            self.west.configure(bg="#4D9EE0")
            self.logout.configure(bg="#135066")
            self.function.configure(bg="#135066")

            self.info.configure(bg="#135066")
            self.avatar.configure(bg="#135066")
            self.name.configure(bg="#135066")
            self.rule.configure(bg="#135066")
            self.fram_cate.configure(bg="#135066")
            self.cate.configure(bg="#135066")

            for i in range(1, 13):
                self.panel[i].configure(bg="#f0f0f0")
                self.image[i].configure(bg="#f0f0f0")
                self.label[i].configure(bg="#f0f0f0", fg="#000000")

            self.darkMode = False
        else:
            self.imgMode = ImageTk.PhotoImage(Image.open(r"cafe_application/img/icons/sun.png").resize((30, 30), Image.ANTIALIAS))
            self.mode.configure(image=self.imgMode, bg="#4D9EE0")
            self.function.configure(bg="#4D9EE0")

            self.__master.configure(bg="#135066")
            self.west.configure(bg="#135066")
            self.logout.configure(bg="#4D9EE0")

            self.info.configure(bg="#4D9EE0")
            self.avatar.configure(bg="#4D9EE0")
            self.name.configure(bg="#4D9EE0")
            self.rule.configure(bg="#4D9EE0")
            self.fram_cate.configure(bg="#4D9EE0")
            self.cate.configure(bg="#ffffff")

            for i in range(1, 13):
                self.panel[i].configure(bg="#4D9EE0")
                self.image[i].configure(bg="#4D9EE0")
                self.label[i].configure(bg="#4D9EE0", fg="#FFFFFF")

            self.darkMode = True

    def on_panel_click(self, event):
        self.disable()
        if self.darkMode:
            for child in event.widget.winfo_children():
                child.configure(background='#135066')
            event.widget.configure(background='#135066')
            self.callChildFrom(event.widget)
        else:
            for child in event.widget.winfo_children():
                child.configure(background='#4D9EE0')
            event.widget.configure(background='#4D9EE0')
            self.callChildFrom(event.widget)

    def on_childPanel_click(self, event):
        self.disable()
        if self.darkMode:
            parent_frame = event.widget.master
            for child in parent_frame.winfo_children():
                child.configure(background='#135066')
            parent_frame.configure(background='#135066')
            self.callChildFrom(parent_frame)
        else:
            parent_frame = event.widget.master
            for child in parent_frame.winfo_children():
                child.configure(background='#4D9EE0')
            parent_frame.configure(background='#4D9EE0')
            self.callChildFrom(parent_frame)

    def disable(self):
        frame = self.cate
        if self.darkMode:
            for child1 in frame.winfo_children():
                child1.configure(background='#4D9EE0')
                for child2 in child1.winfo_children():
                    child2.configure(background='#4D9EE0')
        else:
            for child1 in frame.winfo_children():
                child1.configure(background='#f0f0f0')
                for child2 in child1.winfo_children():
                    child2.configure(background='#f0f0f0')

    def callChildFrom(self, frame):
        if frame == self.panel[1]:
            self.openChildForm(SaleGUI(self.function))
        elif frame == self.panel[2]:
            self.openChildForm(ProductGUI(self.function))
        elif frame == self.panel[3]:
            self.openChildForm(CategoryGUI(self.function))
        elif frame == self.panel[4]:
            self.openChildForm(RecipeGUI(self.function))
        elif frame == self.panel[5]:
            self.openChildForm(ReceiptGUI(self.function))
        elif frame == self.panel[6]:
            self.openChildForm(BillGUI(self.function))
        elif frame == self.panel[7]:
            self.openChildForm(IngredientGUI(self.function))
        elif frame == self.panel[8]:
            self.openChildForm(AccountGUI(self.function))
        elif frame == self.panel[9]:
            self.openChildForm(StaffGUI(self.function))
        elif frame == self.panel[10]:
            self.openChildForm(CustomerGUI(self.function))
        elif frame == self.panel[11]:
            self.openChildForm(DecentralizationGUI(self.function))
        elif frame == self.panel[12]:
            self.openChildForm(SupplierGUI(self.function))


    def openChildForm(self, frame):
        for child in self.function.winfo_children():
            if child != frame:
                child.destroy()
        frame.pack()
        self.function.update()

    def Logout_btn(self):
        self.__master.destroy()
        LoginGUI()
