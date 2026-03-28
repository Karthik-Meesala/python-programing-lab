import tkinter as tk
def show_selection():
    hobbies = []
    if var1.get() == 1:
        hobbies.append("Reading")
    if var2.get() == 1:
        hobbies.append("Sports")
    if var3.get() == 1:
        hobbies.append("Music")

    gender = gender_var.get()

    result_label.config(text="Hobbies: " + ", ".join(hobbies) + "\nGender: " + gender)
window = tk.Tk()
window.title("CheckButton and Radiobutton Demo")
window.geometry("400x300")
tk.Label(window, text="Select your hobbies:").pack()
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
tk.Checkbutton(window, text="Reading", variable=var1).pack()
tk.Checkbutton(window, text="Sports", variable=var2).pack()
tk.Checkbutton(window, text="Music", variable=var3).pack()
tk.Label(window, text="Select your gender:").pack()
gender_var = tk.StringVar()
tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").pack()
tk.Button(window, text="Submit", command=show_selection).pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()