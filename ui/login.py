from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("InfoSousa Frota")
        self.setFixedSize(450, 650)

        self.montar_tela()

    def montar_tela(self):

        # Layout principal
        layout = QVBoxLayout()
        layout.setSpacing(12)

        # ==========================
        # LOGO
        # ==========================

        logo = QLabel()

        pixmap = QPixmap("assets/IsIcone.png")

        pixmap = pixmap.scaled(
            180,
            180,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)

        # ==========================
        # TÍTULO
        # ==========================

        titulo = QLabel("InfoSousa")
        titulo.setAlignment(Qt.AlignCenter)

        titulo.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:#1565C0;
        """)

        # ==========================
        # SUBTÍTULO
        # ==========================

        subtitulo = QLabel("Sistema de Gestão")
        subtitulo.setAlignment(Qt.AlignCenter)

        subtitulo.setStyleSheet("""
            font-size:15px;
            color:gray;
        """)

        # ==========================
        # VERSÃO
        # ==========================

        versao = QLabel("Versão 0.1.0 ROMENSON C DE SOUSA LTDA")
        versao.setAlignment(Qt.AlignCenter)

        versao.setStyleSheet("""
            color:gray;
            font-size:12px;
        """)

        # ==========================
        # USUÁRIO
        # ==========================

        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuário")
        self.usuario.setMinimumHeight(40)

        # ==========================
        # SENHA
        # ==========================

        self.senha = QLineEdit()
        self.senha.setPlaceholderText("Senha")
        self.senha.setEchoMode(QLineEdit.Password)
        self.senha.setMinimumHeight(40)

        # ==========================
        # BOTÃO
        # ==========================

        botao = QPushButton("Entrar")
        botao.setMinimumHeight(45)

        botao.clicked.connect(self.entrar)

        botao.setStyleSheet("""
            QPushButton{
                background:#1565C0;
                color:white;
                border-radius:8px;
                font-size:16px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#1976D2;
            }
        """)

        # ==========================
        # LAYOUT
        # ==========================

        layout.addStretch()

        layout.addWidget(logo)

        layout.addWidget(titulo)

        layout.addWidget(subtitulo)

        layout.addWidget(versao)

        layout.addSpacing(30)

        layout.addWidget(self.usuario)

        layout.addWidget(self.senha)

        layout.addSpacing(20)

        layout.addWidget(botao)

        layout.addStretch()

        self.setLayout(layout)

    def entrar(self):

        usuario = self.usuario.text()
        senha = self.senha.text()

        if usuario == "admin" and senha == "123":

            QMessageBox.information(
                self,
                "InfoSousa",
                "Login realizado com sucesso!"
            )

        else:

            QMessageBox.warning(
                self,
                "Erro",
                "Usuário ou senha inválidos."
            )