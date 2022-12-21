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

        self._set_samples(self.controlWidget.samples)

        self.dockWidget.adjustSize()

    def setupUi(self, target=None):
        super().setupUi(self if target is None else target)
        self.controlWidget = ControlWidget()
        self.plotWidget = PlotWidget()

        self.dockWidget.setWidget(self.controlWidget)
        # TODO
        self.widgetPlotContainer.layout().removeWidget(self.valuePlot)
        self.valuePlot.deleteLater()
        self.widgetPlotContainer.layout().addWidget(self.plotWidget)

        self.inputSignificance.clear()
        self.inputSignificance.addItems(list(map(str, sorted(
            distributions.CRAMERVONMISES_TABLE.keys(), reverse=True))))
        self.inputSignificance.setCurrentText(str(0.01))

        # Connections
        self.controlWidget.samples_changed.connect(lambda self=self: self._set_samples(self.controlWidget.samples))

        self.inputSignificance.currentTextChanged.connect(self._update_results)

    def _set_samples(self, samples: np.ndarray):
        cdf = self.controlWidget.cdf
        self._statistic = distributions.cramervonmises(samples, cdf)
        # scipy_results = cramervonmises(samples, cdf)
        # print(self._statistic, scipy_results.statistic)
        # self._p_value = scipy_results.pvalue

        self._update_results()
        self._update_plot()

    @Slot()
    def _update_results(self):
        statistic = self._statistic
        p_value = distributions.CRAMERVONMISES_TABLE[float(self.inputSignificance.currentText())]

        self.valueStatistic.setText(str(statistic))
        self.valuePValue.setText(str(p_value))
        self.valueHypothesis.setText(
            self.tr('Samples DO NOT match distribution')
            if statistic > p_value else
            self.tr('Samples MATCH distribution')
        )

    @Slot()
    def _update_plot(self):
        control_widget = self.controlWidget
        self.plotWidget.plot(control_widget.samples, control_widget.cdf)
