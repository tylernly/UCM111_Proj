from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow,
QLabel, QLineEdit, QVBoxLayout, QWidget)
from PyQt6.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("advertisement database")

        #creates the objects
        self.text = QLabel("1)insert 2)remove 3)update 4)run preset SQLs")
        self.button = QPushButton("Press Me!")
        self.input = QLineEdit()
        self.menu = QLabel("0")
        self.query = QLabel("")
        self.button.clicked.connect(self.the_button_was_clicked)

        #places all the objects into one layout
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.query)

        #container now is in the layout format
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        if(self.menu.text() == "0"):
            if(self.input.text() == "1"):
                #insert
                print("Clicked!")
                self.text.setText("inserting screen")
                print("Clicked!")
            elif(self.input.text() == "2"):
                #remove
                self.text.setText("removing screen")
            elif(self.input.text() == "3"):
                #update
                self.text.setText("updating screen")
            elif(self.input.text() == "4"):
                #run presetSQL
                self.text.setText("""1)
2)
3)
4)
5)
e) back to main screen""")
                self.menu.setText("4");
        elif(self.menu.text() == "1"):
            self.text.setText("type the table you would like to insert into")
        elif(self.menu.text() == "2"):
            self.text.setText("type the table you would like to remove from")
        elif(self.menu.text() == "3"):
            self.text.setText("type the table you would like to update from")
        elif(self.menu.text() == "4"):
            if(self.input.text() == "1"):
                #run query
                self.query.setText("test")
            if(self.input.text() == "2"):
                #run query
                self.query.setText("test")
            if(self.input.text() == "3"):
                #run query
                self.query.setText("test")
            if(self.input.text() == "4"):
                #run query
                self.query.setText("test")
            if(self.input.text() == "5"):
                #run query
                self.query.setText("test")
            
            if(self.input.text() == "e"):
                self.menu.setText("0");
                self.query.setText("")
                self.text.setText("1)insert 2)remove 3)update 4)run preset SQLs")
          

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
