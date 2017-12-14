from sys import *
import os 

class FileController():

    def __init__(self):
        if len(argv) >= 2 and argv[1] == "help":
            self.control_help()
        elif len(argv) >= 2 and argv[1] == '-l':
            self.list_tasks()
        elif len(argv) >= 2 and argv[1] == '-a':
            self.add_new_task()
        elif len(argv) >= 2 and argv[1] == '-r':
            self.remove_task()
        elif len(argv) >= 2 and argv[1] == '-c':
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
        new_task = input('What new task would you like to add?: ')
        if len(new_task) < 1:
            print('Unable to add: no task provided')
        else:
            list_file.write(' [ ]')
            list_file.write(new_task)
            list_file.write('\n')
            list_file.close()

    def remove_task(self):
        list_file = open('todos.txt', 'r')
        lines = list_file.readlines()
        remove = str(input('Which task do you want to delete?: '))
        if len(remove) < 1:
            print('Unable to remove: no index provided')
        else:
            list_file.close()
            list_file = open('todos.txt', 'w')
            for line in lines:
                if line != ' [ ]' + remove + '\n' and line != ' [x]' + remove + '\n':
                    list_file.write(line)
        list_file.close()

    def complete_task(self):
        list_file = open('todos.txt', 'r')
        make_complete = str(input('Which task is complete?: '))
        lines = list_file.readlines()
        list_file.close()
        list_file = open('todos.txt', 'w')
        for line in lines:
            if line != ' [ ]' + make_complete + '\n':
                list_file.write(line)
            else:
                list_file.write(' [x]' + make_complete + '\n')



control = FileController()