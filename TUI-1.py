import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLineEdit, 
    QPushButton
)
from PySide6.QtCore import Qt


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.resize(540,400)
        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.crear_componentes()

    def crear_componentes(self):
        principal=QVBoxLayout()
        titulo=QLabel("Inicio de sesión")
        titulo.setAlignment(Qt.AlignCenter)
        fuente=titulo.font()
        fuente.setPointSize(24)
        fuente.setBold(True)
        titulo.setFont(fuente)

        usuario=QHBoxLayout()
        contra=QHBoxLayout()
        boton=QHBoxLayout()
        olvidado=QHBoxLayout()

        principal.addStretch()
        principal.addWidget(titulo)
        principal.addLayout(usuario)
        principal.addLayout(contra)
        principal.addStretch()
        principal.addLayout(boton)
        principal.addStretch()
        principal.addLayout(olvidado)
        principal.addStretch()

        gusuario=QLineEdit()
        usuario.addWidget(QLabel("Usuario:"))
        usuario.addWidget(gusuario)

        gcontra=QLineEdit()
        contra.addWidget(QLabel("Contraseña"))
        contra.addWidget(gcontra)

        boton.addStretch()
        bot=QPushButton("Iniciar")
        boton.addWidget(bot)
        boton.addStretch()

        olvidado.addStretch()
        olv=QPushButton("¿Olvidaste tu contraseña?")
        olvidado.addWidget(olv)
        olvidado.addStretch()

        self.central.setLayout(principal)


app = QApplication(sys.argv)

vent1 = Ventana()
vent1.show()
app.exec()