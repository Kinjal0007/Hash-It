from tkinter import *
root=Tk()
root["bg"]="yellow"
root.title("My Calculator")
e=Entry(root,width=52,border=6)
e.grid(row=0,column=0,padx=55,pady=30,columnspan=6)

def b_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def fun_clear():
    e.delete(0, END)

def fun_add():
    first_number=e.get()
    e.delete(0, END)
    global f_num
    global math
    math="addition"
    f_num=int(first_number)

def fun_subtract():
    first_number=e.get()
    e.delete(0, END)
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)

def fun_multiply():
    first_number=e.get()
    e.delete(0, END)
    global f_num
    global math
    math="multiply"
    f_num=int(first_number)

def fun_divide():
    first_number=e.get()
    e.delete(0, END)
    global f_num
    global math
    math="divide"
    f_num=int(first_number)


def fun_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0, f_num+int(second_number))
    if math=="subtraction":
        e.insert(0, f_num-int(second_number))
    if math=="multiply":
        e.insert(0, f_num*int(second_number))
    if math=="divide":
        e.insert(0, f_num/int(second_number))

b_equal=Button(root, text="=",font=("EWERT" ,20 ,"bold"),padx=37.5,pady=40,bg="green",command=fun_equal).grid(row=4,column=2)

b_clear=Button(root, text="C",font=("EWERT" ,20 ,"bold"),padx=36,pady=40,bg="black",fg="white",command=fun_clear).grid(row=4,column=0)

b_add=Button(root, text="+",font=("EWERT" ,20 ,"bold"),padx=39.5,pady=40,bg="grey",fg="white",command=fun_add).grid(row=1,column=3)
b_minus=Button(root, text="-",font=("EWERT" ,20 ,"bold"),padx=43.5,pady=40,bg="grey",fg="white",command=fun_subtract).grid(row=2,column=3)
b_prod=Button(root, text="*",font=("EWERT" ,20 ,"bold"),padx=41.5,pady=40,bg="grey",fg="white",command=fun_multiply).grid(row=3,column=3)
b_quot=Button(root, text="/",font=("EWERT" ,20 ,"bold"),padx=43.5,pady=40,bg="grey",fg="white",command=fun_divide).grid(row=4,column=3)

b_0=Button(root, text="0",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(0)).grid(row=4,column=1)

b_1=Button(root, text="1",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(1)).grid(row=3,column=0)
b_2=Button(root, text="2",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(2)).grid(row=3,column=1)
b_3=Button(root, text="3",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(3)).grid(row=3,column=2)

b_4=Button(root, text="4",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(4)).grid(row=2,column=0)
b_5=Button(root, text="5",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(5)).grid(row=2,column=1)
b_6=Button(root, text="6",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(6)).grid(row=2,column=2)

b_7=Button(root, text="7",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(7)).grid(row=1,column=0)
b_8=Button(root, text="8",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(8)).grid(row=1,column=1)
b_9=Button(root, text="9",font=("EWERT" ,20 ,"bold"),padx=38.5,pady=40,bg="grey",fg="white",command=lambda: b_click(9)).grid(row=1,column=2)


root.mainloop()