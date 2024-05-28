import tkinter
from tkinter import ttk
from mysql.connector import connect

from windows.AuthWindow import AuthWindow
from windows.RequestsWindow import RequestsWindow

connector = connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    db='techservice'
)
connector.autocommit = True
cur = connector.cursor()

user = AuthWindow(cur).show()
RequestsWindow(cur, user).show()
# print(user)