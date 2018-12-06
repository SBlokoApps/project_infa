from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
 
 
class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self):
        # You must call the super class method
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 80))         # Set sizes 
        self.setWindowTitle("Работа с QTableWidget")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget
        X = 3
        table = QTableWidget(self)  # Create a table
        table.setColumnCount(1)     #Set 1 columns
        table.setRowCount(X)        # and X row
 
        # Set the table headers
        table.setHorizontalHeaderLabels([".........................................Name..................................."])
 
        #Set the tooltips to headings
        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
 
        # Set the alignment to the headers
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)

 
        # Fill the first line
        table.setItem(0, 0, QTableWidgetItem(" "))
        table.setItem(1, 0, QTableWidgetItem(" "))
        table.setItem(2, 0, QTableWidgetItem(" "))
 
        # Do the resize of the columns by content
        table.resizeColumnsToContents()
 
        grid_layout.addWidget(table, 0, 0)   # Adding the table to the grid
 
 
if __name__ == "__main__":
    import sys
 
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
