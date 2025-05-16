from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import os

# Lấy đường dẫn tuyệt đối đến thư mục cha (code)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from main import run_all_game
class PUBGLoginUI(QWidget):
    def __init__(self, switch_to_signup_callback):
        super().__init__()
        self.setWindowTitle("PUBG Login Clone - PyQt5")
        self.setFixedSize(500,400)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.switch_to_signup_callback = switch_to_signup_callback
        self.run=run_all_game
        self.init_ui()
        

    def init_ui(self):
        title = QLabel("PUBG LOGIN")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #f0c420;")

        username_input = QLineEdit()
        username_input.setPlaceholderText("Enter your username")
        username_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        password_input = QLineEdit()
        password_input.setPlaceholderText("Enter your password")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        login_button = QPushButton("Login")
        login_button.setCursor(Qt.PointingHandCursor)
        login_button.clicked.connect(self.run)
        login_button.setStyleSheet("""
            background-color: #f0c420;
            color: black;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        """)

        signup_button = QPushButton("Sign Up")
        signup_button.setCursor(Qt.PointingHandCursor)
        signup_button.setStyleSheet("""
            background-color: #2a2a2a;
            color: white;
            padding: 10px;
            border-radius: 10px;
        """)
        signup_button.clicked.connect(self.switch_to_signup_callback)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.addWidget(title)
        layout.addWidget(username_input)
        layout.addWidget(password_input)
        layout.addWidget(login_button)
        layout.addWidget(signup_button)

        self.setLayout(layout)
