"""
Abstract class defining the template for report generation, enforcing the structure while allowing specific implementations for each report type.
"""
from abc import ABC, abstractmethod

class ReportTemplate(ABC):
    @abstractmethod
    def gather_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    def format_report(self):
        print("Formatting the report with appropriate layout and style.")

    def print_report(self):
        print("Printing the report for final review and distribution.")

    # Template method defining the skeleton of the report generation
    def generate_report(self):
        self.gather_data()  # Specific to each report
        self.process_data() # Specific to each report
        self.format_report() # Common to all report
        self.print_report() # Common to all report
