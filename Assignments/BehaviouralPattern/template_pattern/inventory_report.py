"""
This class represents an Inventory Report, gathering and processing sales data from user input.
"""
from report_template import ReportTemplate

class InventoryReport(ReportTemplate):
    def gather_data(self):
        gather_data = input("Enter the data for inventory: ")
        print(f"Inventory data: {gather_data}")
    
    def process_data(self):
        proces_data = input("Enter the process data of inventory: ")
        print(f"Processed inventory data: {proces_data}")
