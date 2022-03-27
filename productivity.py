class ProductivitySytstem:
    def track(self, employees, hours):
        print("Tracking employee productivity.")
        for employee in employees:
            employee.work(hours) 