import numpy as np

from PySide6.QtWidgets import QMainWindow

from .UI.MainWindow import Ui_MainWindow
from .ControlWidget import ControlWidget


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self, target=None):
        super().setupUi(self if target is None else target)

        self.controlWidget = ControlWidget()
        self.dockWidget.setWidget(self.controlWidget)
        self.controlWidget.samples_changed.connect(lambda self=self: self.set_samples(self.controlWidget.samples))

    def set_samples(self, samples: np.array):
        size = samples.shape[0]
        ...
