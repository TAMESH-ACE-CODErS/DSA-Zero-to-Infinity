class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
        
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setsalary(self,salary):
        self.salary=salary

    def getEmpid(self):
        return self.empid
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
    
    def showall(self):
        print(f"name of emp is: {self.name} and id is {self.empid} and salary is {self.salary}")
    
e1=Employee(239005,"USAB",20000000000000)
e1.setName("BASU")
e1.showall()

    
    