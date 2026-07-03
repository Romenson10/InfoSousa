from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame
)
from PySide6.QtCore import Qt


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("InfoSousa Frota")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        principal = QHBoxLayout()
        central.setLayout(principal)

        # ======================
        # MENU LATERAL
        # ======================

        menu = QFrame()
        menu.setFixedWidth(220)

        menu.setStyleSheet("""
            QFrame{
                background:#0D47A1;
            }

            QPushButton{
                background:transparent;
                color:white;
                border:none;
                text-align:left;
                padding:12px;
                font-size:14px;
            }

            QPushButton:hover{
                background:#1565C0;
            }
        """)

        menu_layout = QVBoxLayout()

        titulo = QLabel("InfoSousa")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color:white;
            font-size:22px;
            font-weight:bold;
            padding:20px;
        """)

        menu_layout.addWidget(titulo)

        botoes = [
            "🏠 Dashboard",
            "📦 Estoque",
            "🚛 Veículos",
            "🔧 Manutenção",
            "📋 Ordens de Serviço",
            "💰 Financeiro",
            "📊 Relatórios",
            "⚙ Configurações"
        ]

        for texto in botoes:
            botao = QPushButton(texto)
            menu_layout.addWidget(botao)

        menu_layout.addStretch()

        menu.setLayout(menu_layout)

        # ======================
        # CONTEÚDO
        # ======================

        conteudo = QWidget()

        conteudo_layout = QVBoxLayout()

        titulo = QLabel("Dashboard")
        titulo.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        conteudo_layout.addWidget(titulo)

        # Cards

        cards = QHBoxLayout()

        for texto in [
            "Produtos\n0",
            "Veículos\n0",
            "OS\n0",
            "Alertas\n0"
        ]:

            card = QFrame()

            card.setStyleSheet("""
                QFrame{
                    background:white;
                    border:1px solid #DDD;
                    border-radius:10px;
                }
            """)

            card_layout = QVBoxLayout()

            label = QLabel(texto)

            label.setAlignment(Qt.AlignCenter)

            label.setStyleSheet("""
                font-size:18px;
                font-weight:bold;
            """)

            card_layout.addWidget(label)

            card.setLayout(card_layout)

            cards.addWidget(card)

        conteudo_layout.addLayout(cards)

        conteudo_layout.addStretch()

        conteudo.setLayout(conteudo_layout)

        principal.addWidget(menu)

        principal.addWidget(conteudo)