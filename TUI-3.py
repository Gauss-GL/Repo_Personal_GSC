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

class ventana(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Registro de alumnos")
        self.resize(300,500)
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
            """)
    def crear_componentes(self):
        main=QVBoxLayout()
        titulo=QLabel("Perfil de usuario")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 24pt;
            font-weight: bold;
        """)
        grid1=QGridLayout()
        contacto=QLabel("Datos de contacto")
        contacto.setAlignment(Qt.AlignCenter)
        contacto.setStyleSheet("""
            font-size: 20pt;
            font-weight: bold;
        """)
        grid2=QGridLayout()
        botones=QHBoxLayout()
        #Declaración del arbol principal
        main.addWidget(titulo)
        main.addLayout(grid1)
        main.addWidget(contacto)
        main.addLayout(grid2)
        main.addLayout(botones)

        #Expansión de la rama de grid1 
        #Declaración de todas las etiquetas y espacios para ingresar. 
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
        #Añadir las cosas previamente creadas con su etiqueta a la grid
        grid1.addWidget(QLabel("Nombre:"),0,0,1,1,Qt.AlignCenter)
        grid1.addWidget(QLabel("Edad:"),1,0,1,1,Qt.AlignCenter)
        grid1.addWidget(QLabel("Carrera:"),2,0,1,1,Qt.AlignCenter)
        grid1.addWidget(QLabel("Correo:"),3,0,1,1,Qt.AlignCenter)
        grid1.addWidget(nombre,0,1,1,1)
        grid1.addWidget(edad,1,1,1,1)
        grid1.addWidget(carrera,2,1,1,1)
        grid1.addWidget(correo,3,1,1,1)

        #Expasinión de la  rama de grid 2
        #"Declaracion de los espacios para ingresar"
        telefono=QLineEdit() 
        ciudad=QLineEdit()
        direccion=QLineEdit()
        #Añadir lo declarado previamente
        grid2.addWidget(QLabel("Telefono:"),0,0,1,1,Qt.AlignCenter)
        grid2.addWidget(QLabel("Ciudad:"),1,0,1,1,Qt.AlignCenter)
        grid2.addWidget(QLabel("Dirección:"),2,0,1,1,Qt.AlignCenter)
        grid2.addWidget(telefono,0,1,1,1)
        grid2.addWidget(ciudad,1,1,1,1)
        grid2.addWidget(direccion,2,1,1,1)   

        #expansión de los botones
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