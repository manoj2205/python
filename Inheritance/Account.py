'''
Method overriding - redefine a method that was already defined in the parent (base class), using the same method name and parameters, but with new behavior
- often used to customize or extend behavior in subclasses — without rewriting the entire parent class.
-Method names must be the same.
-The number and type of parameters should match.
-Only works inside class inheritance.
'''
class Employee:
    def get_role(self):
        return "General Employee"

class Manager(Employee):
    def get_role(self):  # Overriding the parent method
        return "Manager of the department"

# Test
emp = Employee()
mgr = Manager()

print(emp.get_role())  # Output: General Employee
print(mgr.get_role())  # Output: Manager of the department
