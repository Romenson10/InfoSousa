import sys

from PySide6.QtWidgets import QApplication

from ui.login import Login

app = QApplication(sys.argv)

janela = Login()
janela.show()

sys.exit(app.exec())