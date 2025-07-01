from utils.passwordmgr import Hash
import tkinter as tk

def main():
    file_name = 'passwords'
    user_name = entry1.get()
    user_password = entry2.get().encode()
    password_hash = Hash.create_hash(user_password)
    data = ({user_name:password_hash})
    Hash.save(file_name, data)
    result_label.config(text="hash generated")

root = tk.Tk()
root.geometry("500x300")
root.title("Password Maneger")

label1 = tk.Label(root, text="Enter your username")
label1.pack()

entry1 = tk.Entry()
entry1.pack(pady=10)

label2 = tk.Label(root, text="Enter your password")
label2.pack()

entry2 = tk.Entry()
entry2.pack(pady=10)

button = tk.Button(text="submit",command=main)
button.pack(padx=10,pady=10)

result_label = tk.Label(root, text="", wraplength=380)
result_label.pack()

tk.mainloop()
