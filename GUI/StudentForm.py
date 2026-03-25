from tkinter import *
root = Tk()
root.title("Student Form")
root.geometry("400x400")

Label(root, text="Student Form", bg="green", fg="white", width=25).place(x=100, y=30)


Label(root, text="Name").place(x=15, y=80)
def user_input():
    print(Entry.get())
    
en=Entry(root)
en.place(x=150,y=80)

Label(root, text="Gender").place(x=15, y=120)

gender = StringVar()

Radiobutton(root, text="Male", variable=gender, value="Male").place(x=150, y=120)
Radiobutton(root, text="Female", variable=gender, value="Female").place(x=220, y=120)


Label(root, text="Skills").place(x=50, y=160)

python_var = StringVar()
java_var = StringVar()

Checkbutton(root, text="Python", variable=python_var).place(x=150, y=160)
Checkbutton(root, text="Java", variable=java_var).place(x=220, y=160)


Label(root, text="Course").place(x=50, y=200)

listbox = Listbox(root, height=3)
listbox.insert(1, "BCA")
listbox.insert(2, "MCA")
listbox.insert(3, "B.Tech")
listbox.place(x=150, y=200)

def std_info():
    print("Name :- ",user_input)
    print("Gender:- ",gender)
    print()


btn=Button(root,text="Click",command=std_info)
btn.place(x=170,y=270)



root.mainloop()