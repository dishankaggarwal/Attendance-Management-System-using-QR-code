from tkinter import *
import os



root=Tk()
root.title("Generate QR codes")
root.geometry("622x400")
root.configure(bg='#91ebff')
def click():
    os.system("python generate.py")

my_label=Label(root, text='Welcome to Online attendance System',height=2,bg="#cfcec6",font=('Comic Sans MS Bold',20),borderwidth=3).pack(pady=20)
# Label(root,text='').pack()
# Label(root,text='').pack()
# Label(root,text='').pack()
# Label(root,text='').pack()
# Label(root,text='').pack()

my_button=Button(root,text="Click here to generate QR codes!", command=click,height=2,bg='#cfcec6',borderwidth=5).pack(pady=80)






root.mainloop()
