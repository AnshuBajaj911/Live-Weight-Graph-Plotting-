from tkinter import *

def getvals(): 
   print("Submitting form")
   print(f"{d_value.get(), w_value.get()} ")
   lst=[]
   v1 = d_value.get()
   v2 = w_value.get()
   lst.append(v1)
   lst.append(float(v2))
   with open("test.txt", "a") as f:
       lst = map(str, lst)
       l = ",".join(lst)
       l = l+"\n"
       f.write(l)
       d_entry.delete(first=0,last=100)
       w_entry.delete(first=0,last=100)
   
       d_entry.focus()
       
    

root=Tk()
root.title("Weight-Graph")
root.geometry("270x180")

Date=Label(root,text="Date\n")
weight=Label(root,text="Weight\n")

Date.grid()
weight.grid(row=2)

d_value= StringVar()
w_value= StringVar()

d_entry = Entry(root,textvariable = d_value)
w_entry = Entry(root,textvariable = w_value)

d_entry.grid(row=0,column=1)
d_entry.focus()
w_entry.grid(row=2,column=1)

Button(text="Submit",command=getvals).grid(column=1)
root.mainloop()