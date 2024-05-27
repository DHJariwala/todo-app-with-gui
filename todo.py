from datetime import date
class Todo:
    def __init__(self,maxPriority = 3) -> None:
        self.task = {}
        self.lastIndex = 0
        self.priorities = [i for i in range(maxPriority,0,-1)]
        # self.priorities = [2,1,0]
        self.priority = {}
        for p in self.priorities:
            self.priority[p] = []
        pass
    def add(self,task,date=date.today(),priority=1):
        self.lastIndex += 1
        self.task[self.lastIndex] = {
            'taskName' : task,
            'completed' : 0,
            'dueDate' : date,
            'priority' : priority
        }
        self.priority[priority].append(self.lastIndex)
        pass
    def edit(self,task_no,new_task_name = None,new_task_date=None,new_task_priority=None):
        if new_task_name:
            self.task[task_no]['taskName'] = new_task_name
        if new_task_date:
            self.task[task_no]['dueDate'] = new_task_date
        if new_task_priority and self.task[task_no]['priority'] != new_task_priority:
            self.priority[self.task[task_no]['priority']].remove(task_no)
            self.priority[new_task_priority].append(task_no)
            self.task[task_no]['priority'] = new_task_priority
        pass
    def completeTask(self,task_no):
        self.task[task_no]['completed'] = 1
        pass
    def deleteTask(self,task_no):
        self.priority[self.task[task_no]['priority']].remove(task_no)
        del self.task[task_no]
        pass
    def getIncompleteTasks(self): # Return tasks in form of string
        returnArr = []
        # print("Incomplete Tasks:")
        for priority in self.priorities:
            for taskNo in self.priority[priority]:
                if self.task[taskNo]['completed'] == 0:
                    returnArr.append(f'{"!"*(priority)} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']}')
                    # print(f'{taskNo} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']} {"!"*(priority)}')
        
        # print('Completed Tasks: ')
        for priority in self.priorities:
            for taskNo in self.priority[priority]:
                if self.task[taskNo]['completed'] == 1:
                    returnArr.append(f'{"!"*(priority)} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']}')
                    # print(f'{taskNo} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']} {"!"*(priority)}')
        return '\n'.join(returnArr)
    def printCompletedTask(self): # print only completed tasks
        print('Completed Tasks: ')
        for priority in self.priorities:
            for taskNo in self.priority[priority]:
                if self.task[taskNo]['completed'] == 1:
                    print(f'{taskNo} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']} {"!"*(priority)}')
        pass
    def printTasks(self): # print incomplete task first, then completed
        print("Incomplete Tasks:")
        for priority in self.priorities:
            for taskNo in self.priority[priority]:
                if self.task[taskNo]['completed'] == 0:
                    print(f'{taskNo} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']} {"!"*(priority)}')
        print('Completed Tasks: ')
        for priority in self.priorities:
            for taskNo in self.priority[priority]:
                if self.task[taskNo]['completed'] == 1:
                    print(f'{taskNo} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']} {"!"*(priority)}')
        pass
    def printIncompleteTask(self): # print only incomplete task
        print("Incomplete Tasks:")
        for priority in self.priorities:
            for taskNo in self.priority[priority]:
                if self.task[taskNo]['completed'] == 0:
                    print(f'{taskNo} {self.task[taskNo]['taskName']} - {self.task[taskNo]['dueDate']} {"!"*(priority)}')
        pass
    def debug(self):
        print(self.task)
        print(self.priority)
        pass
    def reset(self):
        self.task = {}
        self.lastIndex = 0
        self.priority = {
            0:[],
            1:[],
            2:[]
        }
        pass