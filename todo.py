import argparse
from functions import save_task,delete_task,add_task,load_tasks

task_list = load_tasks()

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest='command',required=True)

add_parser = subparser.add_parser('add')
add_parser.add_argument('task',type=str)

delete_parser = subparser.add_parser('delete')
delete_parser.add_argument('index',type=int)

show_parser = subparser.add_parser('list')

args = parser.parse_args()

if args.command == 'add':
    task_list=add_task(task_list,args.task)
    print(task_list)
    save_task(task_list)
elif args.command == 'delete':
    task_list=delete_task(task_list,args.index)
    print(task_list)
    save_task(task_list)
elif args.command == 'list':
    for i in range(len(task_list)):
        print(f'{i+1}.{task_list[i]}')