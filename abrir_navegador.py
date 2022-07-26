import webbrowser
from tkinter import *

from matplotlib.pyplot import text

root = Tk()
root.title("Abrir Navegador")
root.geometry('250x250')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir Google', command=google).pack(pady=20)
root.mainloop()