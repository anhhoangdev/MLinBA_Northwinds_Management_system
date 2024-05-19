from Controller.Base.BaseController import BaseController
from View.MainWindow import Ui_MainWindow


class MainWindowController(Ui_MainWindow, BaseController):
    def __init__(self):
        super().__init__()
        BaseController.__init__(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.stackedWidget.setCurrentIndex(1)
        self.setup_navigation_bar()

    def setup_navigation_bar(self):
        self.sales_dropdown_buttons = {
            "Customers": self.process_customers,
            "Orders": self.process_orders
        }
        self.pushButton_sales.setup_actions(self.sales_dropdown_buttons)

        self.operation_dropdown_buttons = {
            "Employees": self.process_employees,
            "Suppliers": self.process_suppliers,
            "Shippers": self.process_shippers
        }
        self.pushButton_operation.setup_actions(self.operation_dropdown_buttons)

        self.catalog_dropdown_buttons = {
            "Products": self.process_products,
            "Categories": self.process_categories
        }
        self.pushButton_catalog.setup_actions(self.catalog_dropdown_buttons)

    def process_customers(self):
        self.stackedWidget.setCurrentIndex(1)
        self.management_page_controller.connect_table("Customer")

    def process_orders(self):
        self.stackedWidget.setCurrentIndex(2)
        self.sales_page_controller.connect_table("SalesOrder")

    def process_employees(self):
        self.stackedWidget.setCurrentIndex(1)
        self.management_page_controller.connect_table("Employee")

    def process_suppliers(self):
        self.stackedWidget.setCurrentIndex(1)
        self.management_page_controller.connect_table("Supplier")


    def process_shippers(self):
        self.stackedWidget.setCurrentIndex(1)
        self.management_page_controller.connect_table("Shipper")

    def process_products(self):
        print("Products Pressed")
        self.stackedWidget.setCurrentIndex(1)
        self.management_page_controller.connect_table("Product")

    def process_categories(self):
        print("Categories Pressed")
        self.stackedWidget.setCurrentIndex(1)
        self.management_page_controller.connect_table("Category")

    def show(self):
        self.MainWindow.show()