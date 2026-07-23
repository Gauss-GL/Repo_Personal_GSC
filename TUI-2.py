import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout,  
    QPushButton
)
from PySide6.QtCore import Qt


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Perfil")
        self.resize(540,400)
        self.central = QWidget()
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
        principal=QVBoxLayout()
        titulo=QLabel("Perfil de usuario")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 24pt;
            font-weight: bold;
        """)
        fotoDatos=QHBoxLayout()
        Botones=QHBoxLayout()

        principal.addStretch()
        principal.addWidget(titulo)
        principal.addLayout(fotoDatos)
        principal.addStretch()
        principal.addLayout(Botones)
        principal.addStretch()

        datos=QVBoxLayout()
        self.foto = QLabel("FOTO", self.central)
        self.foto.setAlignment(Qt.AlignCenter)
        self.foto.setFixedSize(120, 240)
        self.foto.setStyleSheet("""
                    
                    color: white;
                    font-size: 30px;
                    font-weight: bold;
                    border: 2px solid white;
                """)
        fotoDatos.addWidget(self.foto)
        fotoDatos.addLayout(datos)
        fotoDatos.addStretch()
        
        nombre=QLabel("Nombre: Nombre Apellido")
        carrera=QLabel("Carrera: Ingenieria en IA")
        semestre=QLabel("Semestre: 3")
        datos.addWidget(nombre)
        datos.addWidget(carrera)
        datos.addWidget(semestre)
        datos.addStretch()
        datos.addStretch()

        beditar=QPushButton("Editar")
        beliminar=QPushButton("Eliminar")
        Botones.addStretch()
        Botones.addWidget(beditar)
        Botones.addWidget(beliminar)
        Botones.addStretch()
        self.central.setLayout(principal)


app = QApplication(sys.argv)

vent1 = Ventana()
vent1.show()
app.exec()