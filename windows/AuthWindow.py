import tkinter
from tkinter import ttk
class AuthWindow():
    def __init__(self, cur) -> None:
        self.window = tkinter.Tk(screenName="Войдите в аккаунт")
        self.user = None
        self.cur = cur
        self.build_auth()
    
    def build_auth(self):
        self.auth_frame = ttk.Frame(self.window)
        self.error_label_auth = ttk.Label(self.auth_frame)
        self.error_label_auth.grid(row=3, column=0, columnspan=2)
        
        ttk.Label(self.auth_frame, text="Имя пользователя").grid(row=1, column=0)
        username = ttk.Entry(self.auth_frame)
        username.grid(row=1, column=1)
        
        ttk.Label(self.auth_frame, text="Пароль").grid(row=2, column=0)
        password = ttk.Entry(self.auth_frame)
        password.grid(row=2, column=1)
        
        enter_button = ttk.Button(self.auth_frame, text="Войти", command=lambda: self.sign_in(username=username.get(), password=password.get()))
        enter_button.grid(row=4, column=0)

        register_button = ttk.Button(self.auth_frame, text="Зарегестрироваться", command=lambda: self.show_register())
        register_button.grid(row=4, column=1)

        self.auth_frame.grid(row=0, column=0, rowspan=6)
    
    def build_register(self):
        self.reg_frame = ttk.Frame(self.window)
        self.error_label_register = ttk.Label(self.reg_frame)
        self.error_label_register.grid(row=0, column=0, columnspan=2)
        
        ttk.Label(self.reg_frame, text="Имя пользователя").grid(row=1, column=0)
        username = ttk.Entry(self.reg_frame)
        username.grid(row=1, column=1)
        
        ttk.Label(self.reg_frame, text="Пароль").grid(row=2, column=0)
        password = ttk.Entry(self.reg_frame)
        password.grid(row=2, column=1)

        ttk.Label(self.reg_frame, text="Повторите пароль").grid(row=3, column=0)
        password_repeat = ttk.Entry(self.reg_frame)
        password_repeat.grid(row=3, column=1)

        ttk.Label(self.reg_frame, text="E-mail").grid(row=4, column=0)
        email = ttk.Entry(self.reg_frame)
        email.grid(row=4, column=1)
        
        back_button = ttk.Button(self.reg_frame, text="Назад", command=lambda: self.show_login())
        back_button.grid(row=5, column=0)
        reg_button = ttk.Button(self.reg_frame, text="Зарегестрироваться", command=lambda: self.sign_up(username.get(), email.get(), password.get(), password_repeat.get()))
        reg_button.grid(row=5, column=1)

        self.reg_frame.grid(column=0, row=0)
        
    def sign_in(self, username, password):
        self.cur.execute(f"SELECT * FROM user WHERE username='{username}' AND password='{password}'")
        result = self.cur.fetchall()
        if (len(result) > 0):
            self.user = result[0]
            self.close()
            return
        self.cur.execute(f"SELECT * FROM employers WHERE username='{username}' AND password='{password}'")
        result = self.cur.fetchall()
        if (len(result) > 0):
            self.user = result[0]
            self.close()
            return
        self.error_label_auth['text'] = 'Неверный логин или пароль'
    
    def sign_up(self, username, email, password, password_repeat):
        if (password != password_repeat):
            self.error_label_register['text'] = "Пароли не совпадают"
            return
        if (username == "" or email == "" or password== ""):
            self.error_label_register['text'] = "Поле не может быть пустым"
            return
        self.cur.execute(f"INSERT INTO user(username, email, password) VALUES ('{username}','{email}','{password}')")

    def show_register(self):
        self.auth_frame.destroy()
        self.build_register()

    def show_login(self):
        self.reg_frame.destroy()
        self.build_auth()

    def show(self):
        self.window.mainloop()
        return self.user

    def close(self):
        self.window.destroy()