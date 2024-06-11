from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QFont, QFontDatabase, QColor
from PyQt5.QtCore import Qt
import sys
import os

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
            painter.drawText(self.rect(), Qt.AlignCenter, text)  # type: ignore
        else:
            print("Error: Could not load the font.")

    def open_menu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 854, 480)
        self.setStyleSheet("background-color: #2B2B2B;")  # Very dark grey background

        layout = QVBoxLayout(self)

        # Create a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        # Create a widget for the scroll area content
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        # Create a grid layout for the apps
        grid_layout = QGridLayout(scroll_content)
        scroll_content.setLayout(grid_layout)

        # Set the font for the app names
        font_id = QFontDatabase.addApplicationFont(FONT_PATH)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            app_font = QFont(font_family, 10)
        else:
            print("Error: Could not load the font.")
            app_font = QFont()

        # Add app icons and names to the grid layout
        row = 0
        col = 0
        for app_name in sorted(os.listdir(APPS_FOLDER_PATH)):
            if app_name.endswith(".png"):
                app_base_name = app_name[:-4]  # Remove the .png extension

                # Create a label for the app icon
                icon_label = QLabel()
                pixmap = QPixmap(os.path.join(APPS_FOLDER_PATH, app_name)).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon_label.setPixmap(pixmap)

                # Create a label for the app name
                name_label = QLabel(app_base_name)
                name_label.setFont(app_font)
                name_label.setStyleSheet("color: white;")
                name_label.setAlignment(Qt.AlignCenter)

                # Add the icon and name to the grid layout
                grid_layout.addWidget(icon_label, row, col, Qt.AlignCenter)
                grid_layout.addWidget(name_label, row + 1, col, Qt.AlignCenter)

                # Update row and column indices for the grid layout
                col += 1
                if col == 6:  # 6 columns per row
                    col = 0
                    row += 2  # Move to the next set of rows for icons and names

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    menu_window = MenuWindow()
    menu_window.show()
    sys.exit(app.exec_())
