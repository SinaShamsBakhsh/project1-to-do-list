import os
from dotenv import load_dotenv
import argparse

load_dotenv()
TASKS_FILE = os.environ.get("TASKS_FILE", "tasks.txt")

#------------------------------------------------------------------
def save_task(task):
    with open(TASKS_FILE,'w') as task_file:
        for t in task:
            task_file.write(t + "\n")
#------------------------------------------------------------------


    
#------------------------------------------------------------------
task_list = []
def add_task(task):
    task_list.append(task)
    return task_list
#------------------------------------------------------------------
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command',required=True)

add_parser = subparser.add_parser('add')
add_parser.add_argument('task')

args = parser.parse_args()

if args.command == 'add':
    task_list=add_task(args.task)
    print(task_list)
    save_task(task_list)