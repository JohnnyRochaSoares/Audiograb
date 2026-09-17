# ==== Imports ==== #
import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication(sys.argv)
window = QWidget()

download_button = QPushButton("Download")
url_input = QLineEdit()


# ==== Start Download function ==== #
def start_download():
    link = url_input.text()


layout = QVBoxLayout()
layout.addWidget(url_input)
layout.addWidget(download_button)

window.setLayout(layout)

window.show()
sys.exit(app.exec())
