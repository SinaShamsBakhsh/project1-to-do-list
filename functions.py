import os
from dotenv import load_dotenv

load_dotenv()
TASKS_FILE = os.environ.get("TASKS_FILE", "tasks.txt")
#------------------------------------------------------------------
def save_task(list:list):
    with open(TASKS_FILE,'w') as f:
        for t in list:
            f.write(t + "\n")
#------------------------------------------------------------------
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks=[]
            for line in f:
                tasks.append(line.strip())
            return tasks
    return []
#------------------------------------------------------------------
def add_task(list:list,task:str):
    list.append(task)
    return list
#------------------------------------------------------------------
def delete_task(list:str, index:int):
    if 1 <= index <=len(list) :
        list.pop(index-1)
        return list
    else:
        print(f"The task {index} does not exist")
    return list
#------------------------------------------------------------------