import sys
import os
import glob
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QTextEdit, QFileDialog, QLabel, QDialog, QLineEdit,
    QComboBox, QDialogButtonBox, QFormLayout, QSizePolicy, QSpacerItem
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class CustomInputDialog(QDialog):
    def __init__(self, title, label, is_combo=False, options=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setStyleSheet(self.styleSheet() + """
            QLabel {
                color: white;
            }

            QPushButton {
                background-color: #444;
                color: white;
                border: 1px solid #666;
                padding: 6px 12px;
                border-radius: 4px;
            }

            QPushButton:hover {
                background-color: #666;
            }

            QLineEdit {
                background-color: #222;
                color: white;
                border: 1px solid #666;
                padding: 4px;
                border-radius: 4px;
            }

            QComboBox {
                color: white;
                background-color: #444;
                border: 1px solid #666;
                padding: 5px;
                border-radius: 4px;
            }

            QComboBox QAbstractItemView {
                background-color: #333;
                color: white;
                selection-background-color: #007acc;
                selection-color: white;
            }
        """)

        self.layout = QFormLayout(self)
        self.label = QLabel(label)
        self.layout.addRow(self.label)

        if is_combo:
            self.input_field = QComboBox(self)
            self.input_field.addItems(options)
        else:
            self.input_field = QLineEdit(self)

        self.layout.addRow(self.input_field)
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addRow(self.buttons)

    def get_value(self):
        if isinstance(self.input_field, QComboBox):
            return self.input_field.currentText()
        return self.input_field.text()


class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📁 File Manager GUI")
        self.setGeometry(200, 100, 900, 600)
        self.current_path = os.getcwd()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        output_layout = QVBoxLayout()
        clear_button_layout = QHBoxLayout()

        # Directory Label
        self.dir_label = QLabel(f"📍 Current Directory: {self.current_path}")
        self.dir_label.setFont(QFont("Segoe UI", 10))
        self.dir_label.setStyleSheet("color: #dddddd; margin-bottom: 5px;")

        # Output area
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setFont(QFont("Consolas", 14))
        self.output_area.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #dcdcdc;
                padding: 15px;
                border: 1px solid #444;
                border-radius: 5px;
            }
        """)

        # Clear Button
        clear_btn = QPushButton("🧹 Clear Console")
        clear_btn.setFont(QFont("Segoe UI", 11))
        clear_btn.setCursor(Qt.PointingHandCursor)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #444;
                color: white;
                padding: 8px 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #666;
            }
        """)
        clear_btn.clicked.connect(self.clearConsole)
        clear_button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        clear_button_layout.addWidget(clear_btn)

        # Buttons
        buttons = [
            ("📁 Change Directory", self.changeDirectory),
            ("🔍 Find File Types", self.getFile),
            ("📂 Show Current Directory", self.showCurrentDirectory),
            ("📄 Show All Files", self.listFiles),
            ("✏️ Edit Text File", self.editTextFile),
            ("➕➖ Add/Remove File", self.addRemoveFile),
            ("❌ Exit", self.close)
        ]

        for text, handler in buttons:
            btn = QPushButton(text)
            btn.setFont(QFont("Segoe UI", 12))
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #007acc;
                    color: white;
                    padding: 12px 24px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #005999;
                }
            """)
            btn.clicked.connect(handler)
            button_layout.addWidget(btn)

        # Layouts assembly
        output_layout.addWidget(self.dir_label)
        output_layout.addWidget(self.output_area)
        output_layout.addLayout(clear_button_layout)

        main_layout.addLayout(button_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(output_layout)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        self.central_widget.setLayout(main_layout)
        self.setStyleSheet("background-color: #2b2b2b;")

    def showMessage(self, message):
        self.output_area.append(message + "\n")

    def clearConsole(self):
        self.output_area.clear()

    def updateDirLabel(self):
        self.dir_label.setText(f"📍 Current Directory: {self.current_path}")

    def changeDirectory(self):
        new_path = QFileDialog.getExistingDirectory(self, "Select Directory", self.current_path)
        if new_path:
            self.current_path = new_path
            self.updateDirLabel()
            self.showMessage(f"✅ Changed working directory to:\n{self.current_path}")

    def listFiles(self):
        files = os.listdir(self.current_path)
        self.showMessage(f"📁 Files and directories in '{self.current_path}':\n{files}")

    def showCurrentDirectory(self):
        self.showMessage(f"📍 Current working directory: {self.current_path}")

    def getFile(self):
        dialog = CustomInputDialog("Find File Type", "Enter file extension (e.g. .txt):", parent=self)
        if dialog.exec_():
            file_type = dialog.get_value()
            pattern = os.path.join(self.current_path, '*' + file_type)
            matched_files = glob.glob(pattern)
            if matched_files:
                for file in matched_files:
                    size = os.path.getsize(file)
                    name = os.path.basename(file)
                    self.showMessage(f"📄 {name} — {size} bytes")
                self.showMessage(f"✅ Found {len(matched_files)} file(s) with '{file_type}'")
            else:
                self.showMessage(f"❗ No files found with '{file_type}'")

    def addRemoveFile(self):
        action_dialog = CustomInputDialog("Add/Remove File", "Choose action:", is_combo=True, options=["Create", "Remove"], parent=self)
        if action_dialog.exec_():
            action = action_dialog.get_value()
            file_dialog = CustomInputDialog("File Name", "Enter file name (with extension):", parent=self)
            if file_dialog.exec_():
                file_name = file_dialog.get_value()
                full_path = os.path.join(self.current_path, file_name)

                if action == "Create":
                    try:
                        with open(full_path, 'x'):
                            pass
                        self.showMessage(f"✅ File '{file_name}' created.")
                    except FileExistsError:
                        self.showMessage(f"⚠️ File '{file_name}' already exists.")
                elif action == "Remove":
                    if os.path.exists(full_path):
                        os.remove(full_path)
                        self.showMessage(f"🗑️ File '{file_name}' removed.")
                    else:
                        self.showMessage(f"❌ File '{file_name}' does not exist.")

    def editTextFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File to Edit", self.current_path, "Text Files (*.txt);;All Files (*)")
        if file_name:
            mode_dialog = CustomInputDialog("Edit Mode", "Choose mode:", is_combo=True, options=["Append", "Write"], parent=self)
            if mode_dialog.exec_():
                mode = mode_dialog.get_value()
                text_dialog = CustomInputDialog("Edit Text", "Enter text to write/append:", parent=self)
                if text_dialog.exec_():
                    text = text_dialog.get_value()
                    with open(file_name, 'a' if mode == "Append" else 'w') as f:
                        f.write(text + '\n')
                    self.showMessage(f"✅ Successfully {mode.lower()}ed to '{os.path.basename(file_name)}'")


def main():
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
