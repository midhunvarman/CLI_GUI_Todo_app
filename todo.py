import time
import os
import argparse
from datetime import date
import sys

# Clear screen.
# os.system('cls')

###Functions###
def add(todo_item):
    f = open("todo.txt","at")
    fitem = todo_item+ "\n"
    f.write(fitem)
    f.close()
    print("Added todo: \"%s\"" %todo_item)
    exit()

def ls():
    try:
        f = open("todo.txt","rt")
        data = f.read().split("\n")
        data = data[:-1]
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


def del1(todo_item):
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

def done(todo_item):
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

def deadline(todo_no,deadline):
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

        todo_item = int(todo_item)

        if(todo_item > x or todo_item <= 0):
            print("Error: todo #%d does not exist. Nothing deleted." %todo_item)
            sys.exit()

        x = 1

        f = open("todo.txt","wt")
        for i in data:
            if(x == todo_item):
                taks =i.split("x")
                if(len(taks)==2):
                    print("Error deadline already present")
                    exit()
                x = x+1
                fitem = i + "x" +deadline +"\n"
                f.write(fitem)
            else:
                fitem = i + "\n"
                f.write(fitem)
            x = x+1
        f.close()
        print("Deleted todo #%d" %todo_item)
    except FileNotFoundError:
        print("Error file not found")
    f = open("todo.txt","at")


if len(sys.argv) > 3:
    print("length exceeded")
    sys.exit()



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
            del1(sys.argv[2])
        except IndexError:
            print("Error: Missing NUMBER for deleting todo.")
    elif(sys.argv[1] == "done"):
        try:
            done(sys.argv[2])
        except IndexError:
            print("Error: Missing NUMBER for marking todo as done.")
    elif(sys.argv[1] == "help"):
        Help()
    elif(sys.argv[1] == "report"):
        report()
