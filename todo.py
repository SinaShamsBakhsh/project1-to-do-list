import os
from dotenv import load_dotenv
import argparse

load_dotenv()
TASKS_FILE = os.environ.get("TASKS_FILE", "tasks.txt")

#------------------------------------------------------------------
def save_task(task):
    with open(TASKS_FILE,'w') as f:
        for t in task:
            f.write(t + "\n")
#------------------------------------------------------------------
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks=[]
            for line in f:
                tasks.append(line.strip())
            for i in range(len(task_list)):
                print(i+1, task_list[i])
            return tasks
    return []
#------------------------------------------------------------------
def add_task(list,task):
    list.append(task)
    return list
#------------------------------------------------------------------
def delete_task(list, index):
    if 1 <= index <=len(list) :
        list.pop(index-1)
        return list
    else:
        print(f"The task {index} does not exist")
#------------------------------------------------------------------
task_list = []
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command',required=True)

add_parser = subparser.add_parser('add')
add_parser.add_argument('task')

args = parser.parse_args()

if args.command == 'add':
    task_list=add_task(args.task)
    print(task_list)
    save_task(task_list)