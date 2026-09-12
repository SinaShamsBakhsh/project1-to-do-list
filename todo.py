import argparse

task_list = []
def add_task(task):
    task_list.append(task)
    return
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command',required=True)

add_parser = subparser.add_parser('add')
add_parser.add_argument('task')

args = parser.parse_args()

if args.command == 'add':
    task_list=add_task(args.task)