from gui import Ui_Dialog
from graph import Graph
from drawer import Drawer as drawer

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
        self.draw()

    def draw(self):
        x = 10 * np.random.rand(5, 3)

        drawer.graph_2d_gray(self.graph_1, x)