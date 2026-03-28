import tkinter as tk
from tkinter import messagebox, filedialog
def show_message():
    messagebox.showinfo("Message", "Hello! This is a message box")

def open_file():
    file = filedialog.askopenfilename()
    messagebox.showinfo("Selected File", file)
window = tk.Tk()
window.title("Advanced Widgets Demo")
window.geometry("400x300")
frame = tk.Frame(window)
frame.pack()
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
for i in range(1, 21):
    listbox.insert(tk.END, "Item " + str(i))
listbox.pack()
scrollbar.config(command=listbox.yview)
tk.Button(window, text="Show Message", command=show_message).pack(pady=5)
tk.Button(window, text="Open File", command=open_file).pack(pady=5)
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)
menubtn = tk.Menubutton(window, text="Options", relief=tk.RAISED)
menubtn.menu = tk.Menu(menubtn, tearoff=0)
menubtn["menu"] = menubtn.menu
menubtn.menu.add_command(label="Show Message", command=show_message)
menubtn.menu.add_command(label="Open File", command=open_file)
menubtn.pack(pady=10)
window.mainloop()