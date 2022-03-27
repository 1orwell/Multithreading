from math import prod
from tkinter import W
import hr
import employees
import productivity


salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = employees.HourlyEmployee(2, 'Fred Blogs', 50, 20)
commision_employee = employees.CommisionEmployee(3, 'Elise Ratcliffe', 1600, 600)

payroll_system = hr.PayrollSystem()
"""
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commision_employee
])
"""


manager = employees.Manager(1, 'Mary Poppins', 3000)
secretary = employees.Secretary(2, 'John Smith', 1500)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]

productivity_system = productivity.ProductivitySytstem()
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)
#payroll_system.calculate_payroll(employees)