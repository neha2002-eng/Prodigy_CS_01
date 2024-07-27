"""Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption."""

from tkinter import *
from tkinter import messagebox


def mainscreen():
    screen = Tk()
    screen.geometry("375x398")
    screen.title("Caesar Cipher")

    def encrypt():
        text = text1.get(1.0, END)
        key = int(code.get())
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_text += chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            else:
                encrypted_text += char
        show_message("Encrypted Text", encrypted_text)           


    def decrypt():
        text = text1.get(1.0, END)
        key = int(code.get())
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            else:
                decrypted_text += char
        show_message("Decrypted Text", decrypted_text)

    def reset():
        code.set("")
        text1.delete(1.0, END)

    def show_message(title, message):
        msg_box = Toplevel(screen)
        msg_box.title(title)
        msg_box.geometry("400x200")  # Set the size of the message box
        label = Label(msg_box, text=message, wraplength=380, font=("calbri", 12))
        label.pack(padx=10, pady=10)
        button = Button(msg_box, text="OK", command=msg_box.destroy)
        button.pack(pady=10)


    Label(text = "Enter the text for encryption and decryption", fg="black", font= ("calbri",12)).place(x = 10, y = 10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text = "Enter the key to shift", fg="black", font= ("calbri",12)).place(x = 10, y = 170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 20),show="").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#E83833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()


mainscreen()  