class Employee:
    def __init__(self,name,job):
        self.name= name
        self.job= job
        
    def jobInfo(self):
        return self.job
    
Emp= Employee("Annareddy Rakesh Reddy","Manager")
Emp1=Employee("Kalluru Gangireddy","Assistant Manager")

print(Emp.jobInfo())
print(Emp1.jobInfo())
