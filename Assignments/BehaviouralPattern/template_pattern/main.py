from report_template import ReportTemplate
from employee_report import EmployeeReport
from inventory_report import InventoryReport
from sales_report import SalesReport

class Exercise:
    def main(self):
        # Initialise sales report
        print("*"*25)
        sales_report: SalesReport = SalesReport()
        print("Generating sales report")
        sales_report.generate_report()

        # Initialise employees report
        employee_report: EmployeeReport = EmployeeReport()
        print("Generating employee report")
        employee_report.generate_report()

        # Initialise inventory report
        inventory_report: InventoryReport = InventoryReport()
        print("Generating inventory report")
        inventory_report.generate_report()

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()