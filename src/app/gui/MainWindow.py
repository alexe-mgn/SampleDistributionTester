import numpy as np
from scipy.stats import cramervonmises

from matplotlib import pyplot as plt

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from src.app.stat_math import distributions

from .UI.MainWindow import Ui_MainWindow
from .ControlWidget import ControlWidget
from .PlotWidget import PlotWidget


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()

        self._statistic = 0
        self._p_value = 0

        self.set_samples(self.controlWidget.samples)

    def setupUi(self, target=None):
        super().setupUi(self if target is None else target)
        self.controlWidget = ControlWidget()
        self.plotWidget = PlotWidget()

        self.dockWidget.setWidget(self.controlWidget)
        # TODO
        self.widgetPlotContainer.layout().removeWidget(self.valuePlot)
        self.valuePlot.deleteLater()
        self.widgetPlotContainer.layout().addWidget(self.plotWidget)

        # Connections
        self.controlWidget.samples_changed.connect(lambda self=self: self.set_samples(self.controlWidget.samples))

        self.inputSignificance.currentTextChanged.connect(self._update_results)

    def set_samples(self, samples: np.ndarray):
        pdf = self.controlWidget.pdf
        self._statistic = distributions.cramervonmises(samples, pdf)
        scipy_results = cramervonmises(samples, pdf)
        self._p_value = scipy_results.pvalue
        self._update_results()

        self._update_results()
        self._update_plot()

    @Slot()
    def _update_results(self):
        statistic = self._statistic
        p_value = self._p_value

        self.valueStatistic.setText(str(statistic))
        self.valuePValue.setText(str(p_value))
        self.valueHypothesis.setText(
            self.tr('Samples DO NOT match distribution')
            if statistic > p_value else
            self.tr('Samples MATCH distribution')
        )

    @Slot()
    def _update_plot(self):
        self.plotWidget.plot(self.controlWidget.samples, self.controlWidget.pdf)
