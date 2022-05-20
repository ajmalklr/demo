from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()

def qrgenerate():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name + '.png'
    url=pyqrcode.create(link)
    url.png(file_name,scale=7)
    img=ImageTk.PhotoImage(Image.open(file_name))
    img_label=Label(image=img)
    img_label.image=img
    canvas.create_window(200,350,window=img_label)


canvas=Canvas(root,width=400,height=600)
canvas.pack()

app_label=Label(root,text="QR Code Genarator",fg="grey",font=("Courier New",25))
canvas.create_window(200,50,window=app_label)
new_label=Label(root,text="Link Name")
link_label=Label(root,text="Link")
canvas.create_window(200,100,window=new_label)
canvas.create_window(200,150,window=link_label)
name_entry=Entry(root)
link_entry=Entry(root)
canvas.create_window(200,120,window=name_entry)
canvas.create_window(200,170,window=link_entry)
button=Button(text="Generate",command=qrgenerate)
canvas.create_window(200,200,window=button)


root.mainloop()