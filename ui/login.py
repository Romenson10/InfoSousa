from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout
)

from PySide6.QtCore import Qt


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("InfoSousa Frota")
        self.resize(450, 60)

        self.montar_tela()

    def montar_tela(self):

        layout = QVBoxLayout()

        titulo = QLabel("InfoSousa")
        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
            color:#1976D2;
        """)

        usuario = QLineEdit()
        usuario.setPlaceholderText("Usuário")

        senha = QLineEdit()
        senha.setPlaceholderText("Senha")
        senha.setEchoMode(QLineEdit.Password)

        botao = QPushButton("Entrar")

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addSpacing(25)
        layout.addWidget(usuario)
        layout.addWidget(senha)
        layout.addSpacing(20)
        layout.addWidget(botao)
        layout.addStretch()

        self.setLayout(layout)