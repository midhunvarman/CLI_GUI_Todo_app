import time
import os
import argparse
from datetime import date
import sys

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

def gui():
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
    root.mainloop()
