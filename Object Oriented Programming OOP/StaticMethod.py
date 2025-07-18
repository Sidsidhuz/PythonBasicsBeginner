class Employee:
    def __init__(self,name,salary,project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name
    @staticmethod
    def gather_requirment(project_name):
        if project_name == 'ABC Project':
            requirment = ['task1','task2','task3']
        else:
            requirment = ['task1']
        return requirment

    def work(self):
        requirment = self.gather_requirment(self.project_name)
        for task in requirment:
            print('Completed',task)
emp = Employee('Kelly',20000,'ABC Project')
emp.work()