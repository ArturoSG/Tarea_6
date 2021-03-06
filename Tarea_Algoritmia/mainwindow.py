from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
    @Slot()
    def click_agregar_inicio(self):
        ID = self.ui.ID_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        print(ID, origen_x, origen_y, destino_x, destino_y, velocidad,red, green, blue)
        self.ui.salida.insertPlainText(str(ID) + str(origen_x) + str(origen_y) + str(destino_x) + str(destino_y) +str(velocidad) + str(red) + str(green) + str(blue))