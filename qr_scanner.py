from tkinter import *
import os

root=Tk()
root.title(" QR codes Scanner")
root.geometry("622x400")
root.configure(bg='#91ebff')

def scanning():
    os.system('python attend.py')  
    

qr_button=Button(root,text="Mark Attendance",command=scanning).pack(pady=60)


root.mainloop()
