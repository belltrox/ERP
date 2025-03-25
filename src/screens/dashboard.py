from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class DashboardScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Primer QLabel
        label1 = QLabel("Bienvenido al Dashboard del ERP", self)
        layout.addWidget(label1)

        # Segundo QLabel
        label2 = QLabel("Últimos proyectos", self)
        layout.addWidget(label2)

        self.setLayout(layout)
