from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QFont, QFontDatabase, QColor
from PyQt5.QtCore import Qt
import sys

# Assuming the icon path is correct (adjust if needed)
ICON_PATH = "folder.png"
BACKGROUND_IMAGE_PATH = "Next.jpg"
BUTTON_BACKGROUND_IMAGE_PATH = "menu.png"  # Path to the button background image
FONT_PATH = "Hurtmold_.ttf"  # Make sure the font file is in the same directory or provide the correct path

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(854, 480)
        self.setWindowTitle("Yonder GUI")

        # Try loading the icon using a try-except block
        try:
            self.setWindowIcon(QIcon(ICON_PATH))
            print(f"Icon loaded successfully: {ICON_PATH}")  # Informative message
        except FileNotFoundError:
            print(f"Error: Icon file not found: {ICON_PATH}")  # Handle error

        # Create a button to open the new window
        self.button = QPushButton("", self)
        self.button.setFixedSize(71, 55)  # Set the button size
        self.button.setStyleSheet(f"""
            QPushButton {{
                border: none;
                background-image: url({BUTTON_BACKGROUND_IMAGE_PATH});
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 50);  # Optional: Add a pressed effect
            }}
        """)
        self.button.clicked.connect(self.open_menu)
        self.button.setGeometry(375, 400, 71, 55)  # Adjust the position of the button

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(BACKGROUND_IMAGE_PATH)
        painter.drawPixmap(self.rect(), pixmap)

        # Set the font and color for the text
        font_id = QFontDatabase.addApplicationFont(FONT_PATH)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family, 40, QFont.Bold)
            painter.setFont(font)
            painter.setPen(QColor(255, 255, 255))  # White color

            # Draw the text
            text = "YONDER OS"
            painter.drawText(self.rect(), Qt.AlignCenter, text) # type: ignore
        else:
            print("Error: Could not load the font.")

    def open_menu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 400, 300)

        # Load and display the contents of menu.py
        try:
            with open("menu.py", "r") as file:
                contents = file.read()
        except FileNotFoundError:
            contents = "Error: menu.py file not found."

        self.setFixedSize(400, 300)

        self.contents_label = QLabel(contents, self)
        self.contents_label.setGeometry(10, 10, 380, 280)
        self.contents_label.setWordWrap(True)  # Enable word wrapping if the text is long

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    print("It's showtime!")
    sys.exit(app.exec_())
