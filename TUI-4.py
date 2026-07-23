import sys 
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton, 
    QGridLayout, 
    QComboBox, 
    QLineEdit
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Información personal")
        self.resize(500,800)
        self.central=QWidget()
        self.setCentralWidget(self.central)

        self.crear_componentes()
        self.setStyleSheet("""
                QLabel {
                    color: white;
                    font-size: 18px;
                    font-family: Segoe UI;
                }
                QPushButton {
                    font-size: 16px;
                    font-family: Segoe UI;
                    font-weight: bold;
                }
                QLabel#titulo {        
                    font-size: 28px;
               }
            """)
    def crear_componentes(self):
        fuente_titulo=QFont("Arial", 25)
        fuente_titulo.setBold(True)
        titulo=QLabel("Información Personal")
        titulo.setObjectName("titulo")
        titulo.setFont(fuente_titulo)

        foto = QLabel("FOTO", self.central)
        foto.setAlignment(Qt.AlignCenter)
        foto.setFixedSize(180, 256)
        foto.setStyleSheet("""
                    color: white;
                    font-size: 30px;
                    font-weight: bold;
                    border: 2px solid white;
                """)
        main=QGridLayout()
        form=QVBoxLayout()
        botones=QHBoxLayout()
        main.addWidget(titulo,0,0,1,2,Qt.AlignCenter)
        main.addWidget(foto,1,0,1,1,Qt.AlignCenter)
        main.addLayout(form,1,1,1,1)
        main.addLayout(botones,2,0,1,2)

        nombre=QLineEdit()
        edad=QLineEdit()
        carrera=QComboBox()
        carrera.addItem("Ingenieria Aeronautica")
        carrera.addItem("Ingenieria en Inteligencia Artificial")
        carrera.addItem("Ingenieria en Sistemas")
        carrera.addItem("Ingenieria en Comunicaciones y Electronica")
        carrera.addItem("Ingenieria Mecatronica")
        carrera.addItem("Ingenieria Quimica")
        correo=QLineEdit()

        form.addWidget(QLabel("Nombre:"))
        form.addWidget(nombre)
        form.addWidget(QLabel("Edad:"))
        form.addWidget(edad)
        form.addWidget(QLabel("Carrera:"))
        form.addWidget(carrera)
        form.addWidget(QLabel("Correo:"))
        form.addWidget(correo)

        guardar=QPushButton("Guardar")
        cancelar=QPushButton("Cancelar")   
        botones.addStretch()
        botones.addWidget(guardar)
        botones.addWidget(cancelar)
        botones.addStretch()

        self.central.setLayout(main)

app=QApplication(sys.argv)
vent1=ventana()
vent1.show()
app.exec()