"""
This class represents an Employee Report, gathering and processing sales data from user input.
"""
from report_template import ReportTemplate

class EmployeeReport(ReportTemplate):
    def gather_data(self):
        gather_data = input("Enter the data for employee: ")
        print(f"Employee data: {gather_data}")
    
    def process_data(self):
        proces_data = input("Enter the process data of employee: ")
        print(f"Processed employee data: {proces_data}")
