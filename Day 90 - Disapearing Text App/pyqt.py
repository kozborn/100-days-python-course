import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QLabel,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtCore import QTimer

app = QApplication(sys.argv)  # Create the application instance


COUNTER = 10


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Disappearing text app")  # Set the window title
        self.setGeometry(100, 100, 800, 600)  # Set the window size and position

        self.secondsCounter = COUNTER

        self.label = QLabel(self)
        self.label.setText(f"Seconds left: {self.secondsCounter}")

        # Create a QTextEdit widget
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Type your text here...")
        self.text_edit.textChanged.connect(
            self.on_text_changed
        )  # Connect the textChanged signal to the slot
        # Set QTextEdit as the central widget of the main window

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        container.setLayout(layout)

        # Set the container as the central widget
        self.setCentralWidget(container)
        self.startCustomTimer()

    def on_text_changed(self):
        # Get the current text from the QTextEdit
        text = self.text_edit.toPlainText()
        # Check if the text is empty
        self.secondsCounter = COUNTER
        if not text:
            # If empty, set the placeholder text
            self.text_edit.setPlaceholderText("Type your text here...")
        else:
            # If not empty, clear the placeholder text
            self.text_edit.setPlaceholderText("")

    def startCustomTimer(self):
        self.timer = QTimer(self)  # Start a timer with a 1-second interval
        self.secondsCounter = COUNTER
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)

    def update_label(self):
        self.secondsCounter -= 1
        self.label.setText(f"Seconds left: {self.secondsCounter}")
        if self.secondsCounter <= 0:
            self.timer.stop()
            self.text_edit.setPlainText("")
            self.text_edit.setPlaceholderText("Type your text here...")
            self.startCustomTimer()


if __name__ == "__main__":
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
