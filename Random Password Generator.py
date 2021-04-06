from tkinter import *
import random
import pyperclip
import string


# Setting Up the window
root=Tk()
root.title("Random Password Generator")
root.geometry("350x350+520+150")
root.resizable(0,0)

# Screen Title
label_title=Label(root,text="RANDOM PASSWORD GENERATOR",font=("tahoma","11","bold"),bg="black",fg="cyan")
label_title.pack(expand=True,fill="both")


# Length of the password
label_length=Label(root,text="Enter the length of the password:",font=("tahoma","9","bold"),fg="light green",bg="black")
label_length.pack(side="top",expand=True,fill="both")

frame_1=Frame(root,bg="black")
frame_1.pack(expand=True,fill="both")

pass_len_input=IntVar()
pass_len=Spinbox(frame_1,from_= 4, to_= 50,font=("tahoma","8","bold"),textvariable=pass_len_input,width=6)
pass_len.pack()


# Password Generator Function
pass_str=StringVar()
def generate_pass():
    password=""
    for i in range(0,4):
        password=random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for j in range(pass_len_input.get()-4):
        password=password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

    
# Button for generating Password
frame_2=Frame(root,bg="black")
frame_2.pack(expand=True,fill="both")
gen_pass_button=Button(frame_2,text="Generate Password",font=("tahoma","9","bold"),relief="ridge",fg="deep pink",command=generate_pass)
gen_pass_button.pack(expand=True)


# Displaying the Password
frame_3=Frame(root,bg="black")
frame_3.pack(expand=True,fill="both")
label_display=Label(frame_3,text="",textvariable=pass_str,font=("tahoma","11","bold"),bg="black",fg="yellow",anchor=CENTER)
label_display.pack(expand=True,fill="both")


# Copy Password
def Copy_pass():
    pyperclip.copy(pass_str.get())
frame_4=Frame(root,bg="black")
frame_4.pack(expand=True,fill="both")
Button(frame_4,text="Copy to Clipboard",font=("tahoma","9","bold"),relief="ridge",command=Copy_pass).pack()


root.mainloop()

















