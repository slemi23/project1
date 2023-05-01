from PyQt5.QtWidgets import *

from view import *
from view2 import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    Class for main menu window, shop and exit buttons

    """
    def __init__(self, *args, **kwargs):
        """"
        Constructor to create shop and exit object buttons
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.shop_button.clicked.connect(lambda: self.shop())
        self.exit_button.clicked.connect(lambda: self.exit())

    def shop(self):
        """
        Function for button when clicked, takes user to cart menu window

        """
        self.windows = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.windows)
        self.windows.show()

    def exit(self):
        """
        Function that exits main menu window

        """
        self.close()


class Controller2(QMainWindow, Ui_SecondWindow):
    """"
    Class for cart menu window that takes users input and calculates grand total
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for total and exit buttons
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.grandtotal_button.clicked.connect(self.grandtotal)
        self.exit2_button.clicked.connect(self.exit2)

    def grandtotal(self):
        """
        Function that calculates total amount for cookies, sandwich, and water, outputs total
        :return: Grand total amount
        """
        try:
            cookie = int(self.cookie_input.text())
            sandwich = int(self.sandwich_input.text())
            water = int(self.water_input.text())

            cookie_total = cookie * 1.50
            sandwich_total = sandwich * 4.00
            water_total = water * 1.00

            total_price = cookie_total + sandwich_total + water_total

            self.total_label.setText(
                f'\n({cookie}) - Cookie: \t\t${cookie_total:.2f}\n({sandwich}) - Sandwich: \t${sandwich_total:.2f}\n'
                f'({water}) - Water: \t\t${water_total:.2f}\n\tGrand Total = {total_price:.2f}')

        except ValueError:
            self.total_label.setText(f'\nCookie, sandwich, and water\nmust be whole integers\ne.g. 10, 2, 3')

        self.cookie_input.setText('')
        self.sandwich_input.setText('')
        self.water_input.setText('')

    def exit2(self):
        """"
        Function that exits cart menu window
        """
        self.close()
