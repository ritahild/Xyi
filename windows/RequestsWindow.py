import tkinter
from tkinter import ttk

class RequestsWindow():
    def __init__(self, cur: CursorBase, user) -> None:
        self.cur = cur
        self.user = user
        self.window = tkinter.Tk(screenName="Список заявок")
        self.build_list()
    
    def build_list(self):
        list_frame = ttk.Frame(self.window)
        self.list_view = ttk.Treeview(list_frame, columns=['id', 'start_date', 'problem_title', 'problem_description', 'tech', 'status'])
        self.list_view.heading('id', text='Номер')
        self.list_view.heading('start_date', text='Дата')
        self.list_view.heading('problem_title', text='Тип неисправности')
        self.list_view.heading('problem_description', text='Описание')
        self.list_view.heading('tech', text='Оборудование')
        self.list_view.heading('status', text='Статус')
        
        
        self.list_view.grid(column=0, row=0, columnspan=3)
        add_button = ttk.Button(list_frame, text="Добавить", command=lambda: self.show_add_window())
        add_button.grid(column=0, row=1)
        edit_button = ttk.Button(list_frame, text="Изменить")
        edit_button.grid(column=1, row=1)
        del_button = ttk.Button(list_frame, text="Удалить")
        del_button.grid(column=2, row=1)
        list_frame.grid(column=0, row=0)
    
    def show_add_window(self):
        add_window = tkinter.Tk(screenName="Создать заявку")
        ttk.Label(add_window, text='Проблема').pack()
        problem_title = ttk.Entry(add_window)
        problem_title.pack()
        ttk.Label(add_window, text='Описание').pack()
        description = ttk.Entry(add_window)
        description.pack()
        ttk.Label(add_window, text='Оборудование').pack()
        tech = ttk.Entry(add_window)
        tech.pack()
        add_btn = ttk.Button(add_window, text="Добавить", command=lambda: self.add_request(
            problem_title.get(), description.get(), tech.get()
        ))
        add_btn.pack()
        add_window.mainloop()
    
    def add_request(self, title, description, tech,):
        self.cur.execute(f"INSERT INTO request(start_date, problem_title, problem_description, tech, status, user_id, employers_id) VALUES (CURRENT_TIMESTAMP, '{title}', '{description}', '{tech}', 'CREATED', {self.user[4]}, 1)")
    
    def update_list(self):
        self.list_view.delete(*self.list_view.get_children())
        for request in self.fetch_requests():
            self.list_view.insert('', ttk.END, values=request)

    def fetch_requests(self):
        self.cur.execute('SELECT * FROM request')
        return self.cur.fetchall()

    def show(self):
        self.window.mainloop()
