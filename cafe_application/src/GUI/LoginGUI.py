from tkinter import *
from tkinter import messagebox, ttk, Label, Tk

from BLL.AccountBLL import AccountBLL
from GUI.HomeGUI import HomeGUI
from PIL import ImageTk, Image


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
