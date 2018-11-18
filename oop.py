class Employee:
	raise_amount = 1.04 #General class attribute, not an attribute of a specific object
	
	def __init__(self, first, last, salary): # Self refers to an instance of the class
		self.first = first
		self.last = last
		self.salary = salary
		self.email = first[0] + last + '@company.com'
	
	def fullname(self): # Methods automatically take the instance as an argument
		return '{} {}'.format(self.first, self.last)
		
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) #Employee.raise_amount works too
		
	
emp_1 = Employee('Barbara','Miller','60000') # These two variables are two separate Employee objects
emp_2 = Employee('Jerry','Moreno','57000')

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) 		#Both of these do the same thing
print Employee.fullname(emp_2)

print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.05
print(emp_1.raise_amount)
