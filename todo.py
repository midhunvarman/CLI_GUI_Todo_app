import time
import os
import argparse
from datetime import date
import sys


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Clear screen.
# os.system('cls')

###Functions###
def add(todo_item):
    f = open("todo.txt","at")
    fitem = todo_item + "\n"
    f.write(fitem)
    f.close()
    print("Added todo: \"%s\"" %todo_item)


def ls():
    try:
        f = open("todo.txt","rt")
        data = f.read().split("\n")
        data = data[:-1]
        if(len(data) == 0):
            print("There are no pending todos!")
            exit()
        data.reverse()
        x = len(data)
        for i in data:
            xstr = str(x)
            sys.stdout.buffer.write("[".encode('utf8'))
            sys.stdout.buffer.write(xstr.encode('utf8'))
            sys.stdout.buffer.write("] ".encode('utf8'))
            sys.stdout.buffer.write(i.encode('utf8'))
            sys.stdout.buffer.write(u"\n".encode('utf8'))
            x = x-1
        f.close()
    except FileNotFoundError:
        print("There are no pending todos!")


def delone(todo_item):
    try:
        f = open("todo.txt","rt")
        data = f.read().split("\n")
        data = data[:-1]
        x = len(data)
        f.close()

        todo_item = int(todo_item)

        if(todo_item > x or todo_item <= 0):
            print("Error: todo #%d does not exist. Nothing deleted." %todo_item)
            sys.exit()

        x = 1

        f = open("todo.txt","wt")
        for i in data:
            if(x == todo_item):
                x = x+1
            else:
                fitem = i + "\n"
                f.write(fitem)
            x = x+1
        f.close()
        print("Deleted todo #%d" %todo_item)
    except FileNotFoundError:
        print("Error: No todos to delete")

def doneone(todo_item):
    try:
        f = open("todo.txt","rt")
        data = f.read().split("\n")
        data = data[:-1]
        x = len(data)
        f.close()

        today = date.today()

        todo_item = int(todo_item)

        if(todo_item > x or todo_item == 0):
            print("Error: todo #%d does not exist." %todo_item)
            sys.exit()

        x = 1

        f = open("todo.txt","wt")
        fdone = open("done.txt","at")
        for i in data:
            if(x == todo_item):
                # YYYY-MM-DD
                d1 = today.strftime("%Y-%m-%d")
                # print("d1 =", d1)
                i = "x " + d1 + " " + i + "\n"
                fdone.write(i)
                x = x+1
            else:
                fitem = i + "\n"
                f.write(fitem)
            x = x+1
        fdone.close()
        f.close()

        print("Marked todo #%d as done." %todo_item)
    except FileNotFoundError:
        print("Error: No todos added")

def Help():
    # print("Usage :-")
    sys.stdout.buffer.write("Usage :-".encode('utf8'))
    sys.stdout.buffer.write(u"\n".encode('utf8'))
    sys.stdout.buffer.write("$ ./todo add \"todo item\"  # Add a new todo".encode('utf8'))
    sys.stdout.buffer.write(u"\n".encode('utf8'))
    sys.stdout.buffer.write("$ ./todo ls               # Show remaining todos".encode('utf8'))
    sys.stdout.buffer.write(u"\n".encode('utf8'))
    sys.stdout.buffer.write("$ ./todo del NUMBER       # Delete a todo".encode('utf8'))
    sys.stdout.buffer.write(u"\n".encode('utf8'))
    sys.stdout.buffer.write("$ ./todo done NUMBER      # Complete a todo".encode('utf8'))
    sys.stdout.buffer.write(u"\n".encode('utf8'))
    sys.stdout.buffer.write("$ ./todo help             # Show usage".encode('utf8'))
    sys.stdout.buffer.write(u"\n".encode('utf8'))
    sys.stdout.buffer.write("$ ./todo report           # Statistics".encode('utf8'))

def report():
    try:
        f = open("todo.txt","rt")
        todo_data = f.read().split("\n")
        todo_data = todo_data[:-1]
        fdone = open("done.txt","rt")
        done_data = fdone.read().split("\n")
        done_data = done_data[:-1]
        todolen = len(todo_data)
        donelen = len(done_data)
        f.close()
        fdone.close()

        today = date.today()
        todoSTR = str(todolen)
        doneSTR = str(donelen)
        # YYYY-MM-DD
        d1 = today.strftime("%Y-%m-%d")

        sys.stdout.buffer.write(d1.encode('utf8'))
        sys.stdout.buffer.write(" Pending : ".encode('utf8'))
        sys.stdout.buffer.write(todoSTR.encode('utf8'))
        sys.stdout.buffer.write(" Completed : ".encode('utf8'))
        sys.stdout.buffer.write(doneSTR.encode('utf8'))
        sys.stdout.buffer.write("\n".encode('utf8'))
    except FileNotFoundError:
        print("Error: No todos added")

def deadline(todo_item):
    todo_no,deadline = todo_item.split(" ")
    # print(todo_no)
    # print(deadline)
    try:
        yyyy,mm,dd = deadline.split("/")
        if(int(yyyy)/10000 != 0 and int(yyyy) < 2020):
            print("Error date syntax invalid use yyyy/mm/dd")
            exit()
        elif(int(mm)/100 != 0 and int(mm) >= 13):
            print("Error date syntax invalid use yyyy/mm/dd")
            exit()
        elif(int(dd)/100!= 0 and int(mm) >= 32):
            print("Error date syntax invalid use yyyy/mm/dd")
            exit()
    except ValueError:
        print("Error date syntax invalid use yyyy/mm/dd")

    try:

        f = open("todo.txt","rt")
        data = f.read().split("\n")
        data = data[:-1]
        x = len(data)
        f.close()

        todo_no = int(todo_no)

        if(todo_no > x or todo_no <= 0):
            print("Error: todo #%d does not exist." %todo_no)
            sys.exit()

        x = 1

        f = open("todo.txt","wt")
        for i in data:
            if(x == todo_no):
                taks =i.split("|")
                taks[0] = taks[0].strip()
                if(len(taks)==2):
                    # print("Error deadline already present")
                    x = x+1
                    fitem = taks[0] + " | " +deadline +"\n"
                    f.write(fitem)
                else:
                    x = x+1
                    fitem = i + " | " +deadline +"\n"
                    f.write(fitem)
            else:
                fitem = i + "\n"
                f.write(fitem)
            x = x+1
        f.close()
        # todolistUpdate()
        print("deadline added to #%d" %todo_no)
    except FileNotFoundError:
        print("Error file not found")


if len(sys.argv) > 3:
    print("length exceeded")
    sys.exit()

### -----------gui functions --------------------

root = tk.Tk()
root.title('Todo List')
root.geometry("530x300+500+300")

task = []
doneTask = []

###Functions###
def addTask():
    global task
    word = e1.get()
    if len(word)==0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        f = open("todo.txt","at")
        fitem = word + "\n"
        f.write(fitem)
        f.close()
        task.append(word)
        todolistUpdate()
        e1.delete(0,'end')

def todolistUpdate():
    global task
    f = open("todo.txt","rt")
    data = f.read().split("\n")
    task = data[:-1]
    clearList()
    for i in task:
        t.insert('end', i)

def donelistUpdate():
    global doneTask
    f = open("done.txt","rt")
    data = f.read().split("\n")
    doneTask = data[:-1]
    clearDoneList()
    for i in doneTask:
        done1.insert('end', i)

def clearList():
    t.delete(0,'end')

def clearDoneList():
    done1.delete(0,'end')

def del1():
    global task
    try:
        val = t.get(t.curselection())
        todolistUpdate()
        if val in task:
            task.remove(val)

            f = open("todo.txt","rt")
            data = f.read().split("\n")
            data = data[:-1]
            x = len(data)
            f.close()

            x = 0

            f = open("todo.txt","wt")
            for i in data:
                if(i == val):
                    x = x+1
                else:
                    fitem = i + "\n"
                    f.write(fitem)
                x = x+1
            f.close()

            todolistUpdate()
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')

def del2():
    global doneTask
    try:

        doneVal = done1.get(done1.curselection())
        donelistUpdate()
        if doneVal in doneTask:
            doneTask.remove(doneVal)

            f = open("done.txt","rt")
            data = f.read().split("\n")
            data = data[:-1]
            x = len(data)
            f.close()

            x = 0

            f = open("done.txt","wt")
            for i in data:
                if(i == doneVal):
                    x = x+1
                else:
                    fitem = i + "\n"
                    f.write(fitem)
                x = x+1
            f.close()

            donelistUpdate()
    except:
        messagebox.showinfo('Cannot Delete', 'No done task Item Selected')

def done():
    global task
    try:
        val = t.get(t.curselection())
        if val in task:
            f = open("todo.txt","rt")
            data = f.read().split("\n")
            data = data[:-1]
            x = len(data)
            f.close()

            today = date.today()

            x = 1

            f = open("todo.txt","wt")
            fdone = open("done.txt","at")
            for i in data:
                if(i == val):
                    # YYYY-MM-DD
                    d1 = today.strftime("%Y-%m-%d")
                    # print("d1 =", d1)
                    i = "x " + d1 + " " + i + "\n"
                    doneTask.append(i)
                    fdone.write(i)
                    x = x+1
                else:
                    fitem = i + "\n"
                    f.write(fitem)
                x = x+1
            fdone.close()
            f.close()
            task.remove(val)
            todolistUpdate()
            donelistUpdate()
    except:
        messagebox.showinfo('Cannot update Done list', 'No Task Item Selected')

def deleteAll():
    mb = messagebox.askyesno('Delete All','Are you sure?')
    if mb==True:
        while(len(task)!=0):
            task.pop()
        while(len(doneTask)!=0):
            doneTask.pop()
        f = open("todo.txt","wt")
        fdone = open("done.txt","wt")
        f.close()
        fdone.close()
        # cur.execute('delete from tasks')
        todolistUpdate()
        donelistUpdate()

def retrieveData():
    try:
        f = open("todo.txt","rt")
        todo_data = f.read().split("\n")
        task = todo_data[:-1]
        fdone = open("done.txt","rt")
        done_data = fdone.read().split("\n")
        doneTask = done_data[:-1]
        f.close()
        fdone.close()
    except FileNotFoundError:
        f = open("todo.txt","wt")
        fdone = open("done.txt","wt")
        f.close()
        fdone.close()


def bye():

    root.destroy()


##-------------------------------gui interface----------------------------------
l1 = ttk.Label(root, text = 'To-Do List')
l2 = ttk.Label(root, text='Enter task title: ')
l3 = ttk.Label(root, text='Tasks todo')
l4 = ttk.Label(root, text='Tasks done')
e1 = ttk.Entry(root, width=21)
t = tk.Listbox(root, height=13, selectmode='SINGLE')
done1 = tk.Listbox(root, height=13, selectmode='SINGLE')
b1 = ttk.Button(root, text='Add task', width=20, command=addTask)
b2 = ttk.Button(root, text='Delete task', width=20, command=del1)
b3 = ttk.Button(root, text='Delete done', width=20, command=del2)
b4 = ttk.Button(root, text='Done', width=20, command=done)
b5 = ttk.Button(root, text='Delete all', width=20, command=deleteAll)
b6 = ttk.Button(root, text='Exit', width=20, command=bye)

retrieveData()
todolistUpdate()
donelistUpdate()

#Place geometry
l2.place(x=50, y=50)
l3.place(x=220, y=50)
l4.place(x=360, y=50)
e1.place(x=50, y=80)
b1.place(x=50, y=110)
b2.place(x=50, y=140)
b3.place(x=50, y=170)
b4.place(x=50, y=200)
b5.place(x=50, y =230)
b6.place(x=50, y =260)
l1.place(x=50, y=10)
t.place(x=220, y = 75)
done1.place(x=360, y = 75)

def gui():

    root.mainloop()




if __name__ == "__main__":
    if(len(sys.argv) == 1):
        Help()
    elif(sys.argv[1] == "add"):
        # add(sys.argv[2])
        try:
            add(sys.argv[2])
        except IndexError:
            print("Error: Missing todo string. Nothing added!")
    elif(sys.argv[1] == "ls"):
        ls()
    elif(sys.argv[1] == "del"):
        try:
            delone(sys.argv[2])
        except IndexError:
            print("Error: Missing NUMBER for deleting todo.")
    elif(sys.argv[1] == "done"):
        try:
            doneone(sys.argv[2])
        except IndexError:
            print("Error: Missing NUMBER for marking todo as done.")
    elif(sys.argv[1] == "help"):
        Help()
    elif(sys.argv[1] == "report"):
        report()
    elif(sys.argv[1] == "deadline"):
        try:
            deadline(sys.argv[2])
        except IndexError:
            print("Error: Missing NUMBER for marking todo as done.")
    elif(sys.argv[1] == "gui" or sys.argv[1] == "GUI"):
        gui()
