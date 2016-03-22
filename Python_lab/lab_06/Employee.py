class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)


class EmployeeSpecial(Employee):

    def __init__(self,name, salary, specialization):

        super().__init__(name, salary)
        self.specialization= specialization
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary, ", Specjalization: ", self.specialization)




emp1= Employee("Hubert", 3000)

emp1.displayEmployee()
emp1.displayCount()

emp2= EmployeeSpecial("Adam", 2000, "Hydrualik")
emp2.displayEmployee()