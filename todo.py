# Must have commands:
# add "todo item"
# ls
# del NUMBER
# done NUMBER
# help
# report

# importing the required modules
import sys
from datetime import date

# help information
def info():
    l1 = "Usage :-"
    l2 = "$ ./todo add \"todo item\"  # Add a new todo" 
    l3 = "$ ./todo ls               # Show remaining todos" 
    l4 = "$ ./todo del NUMBER       # Delete a todo" 
    l5 = "$ ./todo done NUMBER      # Complete a todo" 
    l6 = "$ ./todo help             # Show usage" 
    l7 = "$ ./todo report           # Statistics" 
    print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(l1, l2, l3, l4, l5, l6, l7)) #Trying to combine to single string but not passing the test

# function to add todo with the todo string stored in args
def add(args):
    task = args
    f = open("todo.txt", "a+")
    f.write("{}\n".format(task))
    f.close()
    print("Added todo: \"{}\"".format(task))

# function to list the todo list
def ls():
    try:
        with open("todo.txt", "r") as f:
            todo_list = []
            for x in f:
                todo_list.append(x)
    except FileNotFoundError:
        print("There are no pending todos!")
        return
    
    if not todo_list:
        print("Nothing in the todo list. Please add some task.")
    else:
        while len(todo_list) > 0:
            print("[{}] {}".format(str(len(todo_list)),todo_list[-1].strip('\n')))
            todo_list.pop()                                                         # Implementation of stack to display latest as first

# function to delete todo items with number stored in args
def dele(args):
    try:
        with open("todo.txt", "r") as f:
            de_list = []
            for x in f:
                de_list.append(x)
    except FileNotFoundError:
        print("There are no pending todos!")
        return

    num = int(args)

    if num not in range(1,len(de_list)+1):
        print("Error: todo #{} does not exist. Nothing deleted.".format(num))
    else:
        de_list.pop(num-1)
        f = open("todo.txt", "w+")
        for x in de_list:
            f.write(x)
        f.close()
        print("Deleted todo #{}.".format(num))

# function to mark todo done with number stored in args
def done(args):
    try:
        with open("todo.txt", "r") as f:
            todo_list = []
            for x in f:
                todo_list.append(x)
    except FileNotFoundError:
        print("Add some tasks first!")
        return

    task_no = int(args)

    if task_no not in range(1, len(todo_list)+1):
        print("Error: todo #{} does not exist.".format(task_no))
    else:
        f = open("done.txt", "a+")
        entry = "x {} {}".format(date.today(), todo_list[task_no-1].strip('\n'))
        f.write("{}\n".format(entry))
        todo_list.pop(task_no-1)
        print("Marked todo #{} as done.".format(task_no))
        f.close()
        f = open("todo.txt", "w+")
        for x in todo_list:
            f.write(x)
        f.close()

# function to display report
def report():
    pend_count = 0
    compl_count = 0
    try:
        with open("todo.txt", "r") as f:
            for x in f:
                pend_count += 1
    except FileNotFoundError:
        print("Todo list doesnt exist. Please start one")

    try:
        with open("done.txt", "r") as f:
            for y in f:
                compl_count += 1
    except FileNotFoundError:
        print("Nothing done so far")
    print("{} Pending : {} Completed : {}".format(date.today(), pend_count, compl_count))

# function to decide with functions above to be called based on para1 and para2 values
def assign(para1, para2):
    no_args = ['ls', 'help', 'report']
    yes_arg = ['add', 'del', 'done']
    if (para1 is None) & (para2 is None):
        info()
    elif para2 is None:
        if para1 not in no_args:
            print("Invalid command.")
        else:
            if para1 == 'ls':
                ls()
            elif para1 == 'help':
                info()
            else:
                report()
    else:
        if para1 not in yes_arg:
            print("Invalid command.")
        else:
            if para1 == 'add':
                add(para2)
            elif para1 == 'del':
                dele(para2)
            else:
                done(para2)

    
# Here takes in arguments from command line and produces correct parameters for the correct function to be executed
def para_create():
    n = len(sys.argv) -1
    yes_arg = ['add', 'del', 'done']

    if sys.argv[0] != 'todo.py':
        print("Error: Start with ./todo")
    else:
        if n == 2:
            assign(sys.argv[1], sys.argv[2])
        elif n == 1:
            if sys.argv[1] not in yes_arg:
                    assign(sys.argv[1], None)
            else:
                if sys.argv[1] == 'add':
                    print("Error: Missing todo string. Nothing added!")
                elif sys.argv[1] == 'del':
                    print("Error: Missing NUMBER for deleting todo.")
                else:
                    print("Error: Missing NUMBER for marking todo as done.")
        elif n == 0:
            assign(None, None)

def main():
    #calling the parameter creating function
    para_create()

if __name__ == "__main__":
    # calling the main function
    main()
