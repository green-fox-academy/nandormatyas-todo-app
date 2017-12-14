import sys
import os 

class FileController():

    def __init__(self):
        if len(sys.argv) >= 2 and sys.argv[1] == "help":
            self.control_help()
        elif len(sys.argv) >= 2 and sys.argv[1] == '-l':
            self.list_tasks()
        elif len(sys.argv) >= 2 and sys.argv[1] == '-a':
            self.add_new_task()
        elif len(sys.argv) >= 2 and sys.argv[1] == '-r':
            self.remove_task()
        elif len(sys.argv) >= 2 and sys.argv[1] == '-c':
            self.complete_task()

    def control_help(self):
        print('Command Line Todo application\n''=============================')
        print('\n')
        print('Command line arguments:')
        print('-l   Lists all the tasks')
        print('-a   Adds a new task')
        print('-r   Removes a task')
        print('-c   Completes a task')

    def list_tasks(self):
        try:
            list_file = open('todos.txt')
       
        except:
            list_file = open('todos.txt', 'w')
            list_file.write('List of tasks: ')
        if os.stat("todos.txt").st_size == 0:
            print('No todos for today! :)')
        else:
            index = 1
            list_file = list_file.readlines()
            for i in list_file:
                print(str(index) + str(i))
                index += 1

    def add_new_task(self):
        list_file = open('todos.txt', 'a+')
        if sys.argv[2:] == []:
            print('No task provided')
        else:
            new_task = sys.argv[2]
            list_file.write(' [ ]')
            list_file.write(new_task)
            list_file.write('\n')
            list_file.close()

    def remove_task(self):
        list_file = open('todos.txt', 'r')
        lines = list_file.readlines()
        try:
            remove = int(sys.argv[2])
            list_file.close()
            list_file = open('todos.txt', 'w')
            del lines[remove - 1]
            list_file.seek(0)
            list_file.truncate()
            list_file.writelines(lines)
        except:
            print('Unable to remove: no index provided')
        list_file.close()

    def complete_task(self):
        list_file = open('todos.txt', 'r')
        make_complete = int(sys.argv[2])
        lines = list_file.readlines()
        list_file.close()
        list_file = open('todos.txt', 'w')
        lines[make_complete - 1] = ' [x]' + lines[make_complete - 1][3:]
        list_file.seek(0)
        list_file.truncate()
        list_file.writelines(lines)

control = FileController()