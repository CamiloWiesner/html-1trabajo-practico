import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configurar la ventana
        self.setWindowTitle('QLineEdit y QLabel')
        self.setGeometry(100, 100, 300, 100)

        # Crear y configurar QLineEdit
        self.line_edit = QLineEdit(self)
        self.line_edit.setMaxLength(5)  # Máximo de 5 caracteres
        self.line_edit.setFixedSize(50, 30)
        self.line_edit.move(20, 20)
        
        # Crear y configurar QLabel
        self.label = QLabel(self)
        self.label.setFixedSize(50, 30)
        self.label.move(100, 20)  # Mover QLabel 50px a la derecha del QLineEdit

        # Conectar la señal de cambio de texto
        self.line_edit.textChanged.connect(self.on_text_changed)

        # Mostrar la ventana
        self.show()

    def on_text_changed(self, text):
        self.label.setText(text)

# Inicializar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
