import tkinter as tk
window = tk.Tk()
window.title("Hello World App")
window.geometry("300x200")
label = tk.Label(window, text="Hello World")
label.pack(pady=50)
window.mainloop()