from gui import Ui_Dialog
from graph import Graph
from drawer import Drawer

import numpy as np
import matplotlib

matplotlib.use('TkAgg')


# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        # Создаем окно
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс
        # ПОЛЯ КЛАССА
        # Параметры 1 графика
        self.graph_1 = Graph(
            layout=self.layout_plot_1,
            widget=self.widget_plot_1,
            name_graph="Сигнал"
        )

        # Параметры 2 графика
        self.graph_2 = Graph(
            layout=self.layout_plot_2,
            widget=self.widget_plot_2
        )

        # Параметры 3 графика
        self.graph_3 = Graph(
            layout=self.layout_plot_3,
            widget=self.widget_plot_3
        )

        # Параметры 4 графика
        self.graph_4 = Graph(
            layout=self.layout_plot_4,
            widget=self.widget_plot_4
        )

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        self.pushButton_signal.clicked.connect(self.signal)

    def signal(self):
        amplitudes = [int(self.lineEdit_dome_amplitude_1.text()),
                      int(self.lineEdit_dome_amplitude_2.text()),
                      int(self.lineEdit_dome_amplitude_3.text())]
        sigma = [int(self.lineEdit_dome_sigma_1.text()),
                 int(self.lineEdit_dome_sigma_2.text()),
                 int(self.lineEdit_dome_sigma_3.text())]
        x0 = [int(self.lineEdit_dome_bias_x_1.text()),
              int(self.lineEdit_dome_bias_x_2.text()),
              int(self.lineEdit_dome_bias_x_3.text())]
        y0 = [int(self.lineEdit_dome_bias_y_1.text()),
              int(self.lineEdit_dome_bias_y_2.text()),
              int(self.lineEdit_dome_bias_y_3.text())]
        n = 512
        m = 512

        x = np.arange(0, n)
        y = np.arange(0, m)
        xx, yy = np.meshgrid(x, y)

        z1 = amplitudes[0] * np.exp(-((xx - x0[0]) ** 2 + (yy - y0[0]) ** 2) / (2 * sigma[0] ** 2))
        z2 = amplitudes[1] * np.exp(-((xx - x0[1]) ** 2 + (yy - y0[1]) ** 2) / (2 * sigma[1] ** 2))
        z3 = amplitudes[2] * np.exp(-((xx - x0[2]) ** 2 + (yy - y0[2]) ** 2) / (2 * sigma[2] ** 2))

        z = z1 + z2 + z3

        Drawer.graph_2d_gray(self.graph_1, z)

        return z
