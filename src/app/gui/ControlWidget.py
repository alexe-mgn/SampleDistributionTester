import numpy as np

from PySide6.QtCore import Qt, \
    Signal, Slot, \
    QSignalBlocker
from PySide6.QtWidgets import \
    QWidget, \
    QTableWidgetItem, \
    QHeaderView

from .UI.ControlWidget import Ui_ControlWidget

from src.app.stat_math.distributions import parse_distribution


class ControlWidget(QWidget, Ui_ControlWidget):
    _NORMAL_DIST = '1/(1 * sqrt(2 * pi)) * exp(-0.5 * ((x - 0) / 1)^2)'

    samples_changed = Signal()

    @property
    def size(self):
        return self._samples.shape[0]

    @size.setter
    def size(self, size):
        if size < 1:
            raise ValueError(f'Invalid samples size: {size}')

        if size != self.size:
            self._samples.resize(size, refcheck=False)
            self.update_table()
            self.samples_changed.emit()

    @property
    def samples(self):
        return np.copy(self._samples)

    def __init__(self):
        super().__init__()
        self.setupUi()

        self._samples = np.array([])
        table_widget = self.tableWidget
        samples = []
        for i in range(table_widget.rowCount()):
            samples.append(float(table_widget.item(i, 0).text()))
        self._samples = np.array(samples)

        self._custom_dist_str = self.inputCustomDistribution.text()
        self._update_distribution_choice(0)
        self._update_distribution()

        self.samples_changed.emit()

    def setupUi(self, target=None):
        super().setupUi(self if target is None else target)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self._init_table()

        if not self.inputCustomDistribution.text():
            self.inputCustomDistribution.setText(self._NORMAL_DIST)

        self.valueError.hide()

        # Connections
        self.inputN.valueChanged.connect(lambda e, self=self: self.__class__.size.__set__(self, e))

        self.inputDistribution.currentIndexChanged.connect(self._update_distribution_choice)
        self.inputCustomDistribution.textChanged.connect(self._update_distribution)

        self.tableWidget.itemChanged.connect(self._table_item_changed)

    def _init_table(self):
        table_widget = self.tableWidget
        samples = []
        for i in range(table_widget.rowCount()):
            if (item := table_widget.item(i, 0)) is None:
                table_widget.setItem(i, 0, item := QTableWidgetItem('0'))
            item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)
            if (item := table_widget.item(i, 1)) is None:
                table_widget.setItem(i, 1, item := QTableWidgetItem(''))
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)

    @Slot()
    def update_table(self):
        samples = self._samples
        dist = self._dist_f(samples)
        table_widget = self.tableWidget
        sb = QSignalBlocker(table_widget)

        table_widget.setRowCount(self.size)
        for i in range(table_widget.rowCount()):
            table_widget.setItem(i, 0, item := QTableWidgetItem(str(samples[i])))
            item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)
            table_widget.setItem(i, 1, item := QTableWidgetItem(str(dist[i])))
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)

    @Slot(int)
    def _update_distribution_choice(self, index):
        input_custom_dist = self.inputCustomDistribution
        input_custom_dist.setEnabled(index == 0)
        input_custom_dist.setText(self._custom_dist_str if index == 0 else self._NORMAL_DIST)

    @Slot(str)
    def _update_distribution(self, dist_str=None):
        if dist_str is None:
            dist_str = self._NORMAL_DIST

        try:
            self._dist_f = parse_distribution(dist_str)
        except Exception as exception:
            self.valueError.show()
            self.valueError.setText(str(exception))
        else:
            self.valueError.hide()
            self.valueError.setText(self.tr('No errors'))
            self.update_table()

    @Slot(QTableWidgetItem)
    def _table_item_changed(self, item: QTableWidgetItem):
        table_widget = self.tableWidget
        sb = QSignalBlocker(table_widget)

        samples = self._samples
        row = item.row()
        try:
            value = float(item.text())
        except Exception:
            item.setText(str(samples[row]))
        else:
            samples[row] = value
            item.setText(str(value))
            table_widget.item(row, 1).setText(str(self._dist_f(value)))
            self.samples_changed.emit()
