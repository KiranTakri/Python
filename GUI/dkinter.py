from tkinter import *
root = Tk()


root.title("My first Application using Tkinter")
root.geometry("400x300")
# root.minsize(width=100,height=200)
# root.maxsize(width=300,height=500)

# Widgets - label , button, checkbox, radiobutton, etc
# def say_hello():
#     print("Hello sir")
#     print("Good Morning")

#1. Button
# btn=Button(root,text="Click",command=say_hello)
# btn.pack()
# btn.grid()
# btn.place()

#2. Label
l1=Label(root,text="Advance Python",bg="Green",width=15,fg="White")
l1.place(x=30,y=50)


#3. CheckButton
# var=IntVar()
# check_b=Checkbutton(root,text="Accept",variable=var,bg="red",fg="White")
# check_b.pack()

#4. Input field -Entry()
# def user_input():
#     print(Entry.get())
# en=Entry(root)
# en.pack()


#5. radio button
# def show():
#     print(var.get())
# var=StringVar()
# rb1=Radiobutton(root,text="Male",variable=var,value="Male")
# rb2=Radiobutton(root,text="Female",variable=var,value="Female")
# rb1.pack()
# rb2.pack()

# b=Button(root,text="Submit",command=show)
# b.pack()
# root.mainloop()

#6. ListBox
# def select():
#     print(listbox.get(listbox.curselection()))
# listbox=Listbox(root)
# listbox.insert(1,"Linux")
# listbox.insert(2,"Java")
# listbox.insert(3,"C++")
# listbox.pack()
# btn=Button(root,text="submit",command=select)
# btn.pack()
root.mainloop()