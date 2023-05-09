from PyQt5.QtWidgets import *

from view4 import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    """
    Class representing details for the shopping cart and its menu
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor to initialize state of the object

        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.shop_button.clicked.connect(lambda: self.shop())
        self.exit_button.clicked.connect(lambda: self.exit())
        self.total_button.clicked.connect(lambda: self.grandtotal())
        self.exit2_button.clicked.connect(lambda: self.exit2())

        self.cookie_label.hide()
        self.sandwich_label.hide()
        self.water_label.hide()
        self.cookie_input.hide()
        self.sandwich_input.hide()
        self.water_input.hide()
        self.total_button.hide()
        self.exit2_button.hide()

        self.main_or_cart.setText('Main Menu')

    def shop(self) -> None:
        """
        Function to display details once shop button is pressed
        """
        self.shop_button.hide()
        self.exit_button.hide()
        self.main_or_cart.setText('Cart Menu')

        self.cookie_label.show()
        self.sandwich_label.show()
        self.water_label.show()
        self.cookie_input.show()
        self.sandwich_input.show()
        self.water_input.show()
        self.total_button.show()
        self.exit2_button.show()


    def exit(self) -> None:
        """
        Function to close window
        """
        self.close()

    def grandtotal(self) -> None:
        """
        Function to receive and calculate user inputs and then display total
        :return: total of all items
        """
        try:
            # Grabs user inputs and calculates total
            cookie = int(self.cookie_input.text())
            sandwich = int(self.sandwich_input.text())
            water = int(self.water_input.text())

            cookie_total = cookie * 1.50
            sandwich_total = sandwich * 4.00
            water_total = water * 1.00

            total_price = cookie_total + sandwich_total + water_total

            self.total_label.setText(
                f'\n({cookie}) - Cookie: \t\t${cookie_total:.2f}\n({sandwich}) - Sandwich: \t\t${sandwich_total:.2f}\n'
                f'({water}) - Water: \t\t${water_total:.2f}\n\tGrand Total = {total_price:.2f}')

        except ValueError:
            self.total_label.setText(f'\nCookie, sandwich, and water\nmust be whole integers\ne.g. 10, 2, 3')

        self.cookie_input.setText('')
        self.sandwich_input.setText('')
        self.water_input.setText('')

    def exit2(self) -> None:
        """
        Function to close window and displays main menu options
        """
        self.cookie_label.hide()
        self.sandwich_label.hide()
        self.water_label.hide()
        self.cookie_input.hide()
        self.sandwich_input.hide()
        self.water_input.hide()
        self.total_button.hide()
        self.exit2_button.hide()
        self.total_label.hide()

        self.shop_button.show()
        self.exit_button.show()

        self.main_or_cart.setText('Main Menu')
