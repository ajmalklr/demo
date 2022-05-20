import parser
from tkinter import *

root=Tk()                                   #main window
root.title("Calculator")                    #window name
root.geometry("312x324")                    #window size

i=0
def btn_clr():
    input_field.delete(0,END)


def btn_num(num):
    global i
    input_field.insert(i,num)
    i+=1

def btn_cal():
    entire_string=input_field.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        btn_clr()
        input_field.insert(0,result)

    except:
        btn_clr()
        input_field.insert(0,"Error")



input_text=StringVar()

#create input frame
input_frame=Frame(root,width=312,height=50,bd=0)
input_frame.pack(side=TOP)

#create input field
input_field=Entry(input_frame,font=('arial',20,'bold'),width=50,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack()

#create button frame
btn_frame=Frame(root,width=312,height=272.2,bg="grey")
btn_frame.pack()

Button(btn_frame,text="C",width=32,height=3,bd=0,fg="black",bg="#eee",command=lambda:btn_clr()).grid(row=0 ,column=0,columnspan=3,pady=1,padx=1)
Button(btn_frame,text="/",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num("/")).grid(row=0 ,column=3,pady=1,padx=1)
Button(btn_frame,text="1",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(1)).grid(row=1 ,column=0,pady=1,padx=1)
Button(btn_frame,text="2",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(2)).grid(row=1 ,column=1,pady=1,padx=1)
Button(btn_frame,text="3",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(3)).grid(row=1 ,column=2,pady=1,padx=1)
Button(btn_frame,text="*",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num("*")).grid(row=1 ,column=3,pady=1,padx=1)
Button(btn_frame,text="4",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(4)).grid(row=2 ,column=0,pady=1,padx=1)
Button(btn_frame,text="5",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(5)).grid(row=2 ,column=1,pady=1,padx=1)
Button(btn_frame,text="6",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(6)).grid(row=2 ,column=2,pady=1,padx=1)
Button(btn_frame,text="-",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num("-")).grid(row=2 ,column=3,pady=1,padx=1)
Button(btn_frame,text="7",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(7)).grid(row=3 ,column=0,pady=1,padx=1)
Button(btn_frame,text="8",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(8)).grid(row=3 ,column=1,pady=1,padx=1)
Button(btn_frame,text="9",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(9)).grid(row=3 ,column=2,pady=1,padx=1)
Button(btn_frame,text="+",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num("+")).grid(row=3 ,column=3,pady=1,padx=1)
Button(btn_frame,text="0",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(0)).grid(row=4 ,column=0,pady=1,padx=1)
Button(btn_frame,text=".",width=10,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_num(".")).grid(row=4 ,column=1,pady=1,padx=1)
Button(btn_frame,text="=",width=21,height=3,bd=0,fg="black",bg="#eee",command=lambda :btn_cal()).grid(row=4 ,column=2,columnspan=2,pady=1,padx=1)

root.mainloop()