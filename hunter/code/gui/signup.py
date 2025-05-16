from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class PUBGSignupUI(QWidget):
    def __init__(self, switch_to_login_callback):
        super().__init__()
        self.setWindowTitle("PUBG Sign Up Clone - PyQt5")
        self.setFixedSize(500,400)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.switch_to_login_callback = switch_to_login_callback
        self.init_ui()

    def init_ui(self):
        title = QLabel("PUBG SIGN UP")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #f0c420;")

        username_input = QLineEdit()
        username_input.setPlaceholderText("Choose a username")
        username_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        email_input = QLineEdit()
        email_input.setPlaceholderText("Enter your email")
        email_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        password_input = QLineEdit()
        password_input.setPlaceholderText("Create a password")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        confirm_input = QLineEdit()
        confirm_input.setPlaceholderText("Re-enter your password")
        confirm_input.setEchoMode(QLineEdit.Password)
        confirm_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        signup_button = QPushButton("Create Account")
        signup_button.setCursor(Qt.PointingHandCursor)
        signup_button.setStyleSheet("""
            background-color: #f0c420;
            color: black;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        """)

        back_login_button = QPushButton("Back to Login")
        back_login_button.setCursor(Qt.PointingHandCursor)
        back_login_button.setStyleSheet("""
            background-color: #2a2a2a;
            color: white;
            padding: 10px;
            border-radius: 10px;
        """)
        back_login_button.clicked.connect(self.switch_to_login_callback)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.addWidget(title)
        layout.addWidget(username_input)
        layout.addWidget(email_input)
        layout.addWidget(password_input)
        layout.addWidget(confirm_input)
        layout.addWidget(signup_button)
        layout.addWidget(QFrame())  # Spacer
        layout.addWidget(back_login_button)

        self.setLayout(layout)
