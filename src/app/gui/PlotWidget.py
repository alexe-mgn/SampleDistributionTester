from typing import Callable

import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class PlotWidget(FigureCanvasQTAgg):

    def __init__(self):
        super().__init__(Figure(figsize=(5, 3)))
        self._ax = self.figure.subplots()

    def plot(self, samples: np.ndarray, cdf: Callable[[np.ndarray, float, float], np.ndarray]):
        samples = np.sort(samples)
        size = samples.shape[0]
        min_x, max_x = min(samples), max(samples)
        margin_x = (max_x - min_x) * 0.1

        self._ax.clear()
        xs = np.linspace(min_x - margin_x, max_x + margin_x, 1000)
        self._ax.plot(xs, cdf(xs, np.mean(samples), np.std(samples)))
        xs = np.repeat(samples, 2)
        ys = np.roll(np.repeat(np.arange(1, size + 1) / size, 2), 1)
        ys[0] = 0
        self._ax.plot(np.pad(xs, (1, 1), constant_values=(min_x - margin_x, max_x + margin_x)),
                      np.pad(ys, (1, 1), constant_values=(0, 1)))
        self.draw()
