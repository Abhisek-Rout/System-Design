"""
This class represents a Sales Report, gathering and processing sales data from user input.
"""
from report_template import ReportTemplate

class SalesReport(ReportTemplate):
    def gather_data(self):
        gather_data = input("Enter the data for sales: ")
        print(f"Sales data: {gather_data}")
    
    def process_data(self):
        proces_data = input("Enter the process data of sales: ")
        print(f"Processed sales data: {proces_data}")
