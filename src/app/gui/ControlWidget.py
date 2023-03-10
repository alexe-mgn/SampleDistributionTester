from typing import Iterable
import numpy as np

from PySide6.QtCore import Qt, \
    Signal, Slot, \
    QSignalBlocker
from PySide6.QtWidgets import \
    QWidget, \
    QTableWidgetItem, \
    QHeaderView, \
    QDialog, QFileDialog, QMessageBox

from src.app.utils import PATH
from src.app.stat_math.distributions import parse_distribution, ParserError

from .UI.ControlWidget import Ui_ControlWidget


class ControlWidget(QWidget, Ui_ControlWidget):
    _NORMAL_DIST = '1 / 2 * (1 + erf((x - mean) / (std * sqrt(2))))'

    samples_changed = Signal()

    @property
    def size(self):
        return self._samples.shape[0]

    @size.setter
    def size(self, size):
        if size < 2:
            raise ValueError(f'Invalid samples size: {size}')

        if size != self.size:
            self._samples.resize(size, refcheck=False)
            self.update_table()
            self.samples_changed.emit()

    @property
    def samples(self):
        return np.copy(self._samples)

    @samples.setter
    def samples(self, samples: Iterable[float]):
        self._samples = np.array(samples)
        self.update_table()
        self.samples_changed.emit()

    @property
    def cdf(self):
        return self._cdf

    def __init__(self):
        super().__init__()
        self.setupUi()

        self._last_path = PATH.CWD
        self._samples = np.array([])
        table_widget = self.tableWidget
        samples = []
        for i in range(table_widget.rowCount()):
            samples.append(float(table_widget.item(i, 0).text()))
        self._samples = np.array(samples)

        self._input_dist_prev_index = self.inputDistribution.currentIndex()
        self._custom_dist_str = self.inputCustomDistribution.text()

        self._update_distribution_choice()

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
        self.inputCustomDistribution.editingFinished.connect(self._update_distribution)

        self.tableWidget.itemChanged.connect(self._table_item_change)

        self.buttonImport.clicked.connect(self._ui_import_samples)
        self.buttonExport.hide()

        self.samples_changed.connect(self._update_stats)

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
        dist = self._cdf(samples)
        table_widget = self.tableWidget
        sb = QSignalBlocker(table_widget)
        input_n = self.inputN
        sb_input = QSignalBlocker(input_n)

        input_n.setValue(self.size)
        table_widget.setRowCount(self.size)
        for i in range(table_widget.rowCount()):
            table_widget.setItem(i, 0, item := QTableWidgetItem(str(samples[i])))
            item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable)
            table_widget.setItem(i, 1, item := QTableWidgetItem(str(dist[i])))
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)

    @Slot()
    @Slot(int)
    def _update_distribution_choice(self, index=None):
        input_dist = self.inputDistribution
        if index is None:
            index = input_dist.currentIndex()
        else:
            sb = QSignalBlocker(input_dist)
            input_dist.setCurrentIndex(index)
            index = input_dist.currentIndex()

        input_custom_dist = self.inputCustomDistribution
        sb = QSignalBlocker(input_custom_dist)
        if self._input_dist_prev_index == 0:
            self._custom_dist_str = input_custom_dist.text()
        input_custom_dist.setEnabled(index == 0)
        input_custom_dist.setText(self._custom_dist_str if index == 0 else self._NORMAL_DIST)
        del sb

        self._input_dist_prev_index = index
        self._update_distribution()

    @Slot()
    @Slot(str)
    def _update_distribution(self, dist_str=None):
        input_custom_dist = self.inputCustomDistribution
        if dist_str is None:
            dist_str = input_custom_dist.text()
        else:
            sb = QSignalBlocker(input_custom_dist)
            input_custom_dist.setText(dist_str)

        try:
            self._cdf = parse_distribution(dist_str)
        except Exception as exception:
            self.valueError.show()
            self.valueError.setText(str(exception))
        else:
            self.valueError.hide()
            self.valueError.setText(self.tr('No errors'))
            self.update_table()
            self.samples_changed.emit()

    @Slot()
    def _update_stats(self):
        self.valueMean.setText(str(np.mean(self._samples)))
        self.valueStd.setText(str(np.std(self._samples)))

    @Slot(QTableWidgetItem)
    def _table_item_change(self, item: QTableWidgetItem):
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
            table_widget.item(row, 1).setText(str(self._cdf(samples)[row]))
            self.samples_changed.emit()

    def _parse_data(self, text: str) -> list[float]:
        lines = text.strip().split('\n')
        data = [0] * len(lines)
        n = 0
        try:
            for n, i in enumerate(lines):
                data[n] = float(i)
        except Exception as exception:
            raise ParserError(f'Error on line {n}: {str(exception)}')
        return data

    def _ui_import_samples(self):
        dialog = QFileDialog(self, self.tr('Choose file'))
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

        dialog.setNameFilters(['CSV (*.csv)', 'Text files (*.txt)', 'Any files (*)'])

        dialog.setDirectory(self._last_path)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            self._last_path = dialog.directory()
            try:
                with open(dialog.selectedFiles()[0], mode='r', encoding='utf8') as f:
                    data = self._parse_data(f.read())
            except Exception as exception:
                QMessageBox.critical(self, 'Error', str(exception))
            else:
                self.samples = data
