import drawer
from gui import Ui_Dialog_Image_Denoise
from graph import Graph
from drawer import Drawer

import numpy as np
import matplotlib

matplotlib.use('TkAgg')


# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog_Image_Denoise):

    def __init__(self, dialog):
        # Создаем окно
        Ui_Dialog_Image_Denoise.__init__(self)
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
        self.pushButton_signal.clicked.connect(self.btn_signal)

    def signal(self):
        amplitudes = [float(self.lineEdit_dome_amplitude_1.text()),
                      float(self.lineEdit_dome_amplitude_2.text()),
                      float(self.lineEdit_dome_amplitude_3.text())]
        sigmas = [float(self.lineEdit_dome_sigma_1.text()),
                 float(self.lineEdit_dome_sigma_2.text()),
                 float(self.lineEdit_dome_sigma_3.text())]
        shifts_x = [float(self.lineEdit_dome_bias_x_1.text()),
              float(self.lineEdit_dome_bias_x_2.text()),
              float(self.lineEdit_dome_bias_x_3.text())]
        shifts_y = [float(self.lineEdit_dome_bias_y_1.text()),
              float(self.lineEdit_dome_bias_y_2.text()),
              float(self.lineEdit_dome_bias_y_3.text())]
        n = int(self.lineEdit_n.text())
        m = int(self.lineEdit_m.text())
        signal = np.zeros((n, m), dtype=float)
        # Создаем композицию из гауссовых куполов
        for i in range(n):
            for j in range(m):
                for k in range(3):
                    signal[i][j] += amplitudes[k]*np.exp(-(((i-shifts_x[k])**2/(2*sigmas[k]*sigmas[k])) + ((j-shifts_y[k])**2/(2*sigmas[k]*sigmas[k]))))
        return signal

    def image_to_grayscale(self, image):
        height, width, _ = image.shape
        gray_image = np.zeros((height, width), dtype=int)
        for i in range(height):
            for j in range(width):
                pixel = image[i, j]
                gray_image[i, j] = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
        grayscale_image = gray_image*255/np.max(gray_image)
        return grayscale_image

    def btn_signal(self):
        signal = self.signal()
        Drawer.graph_2d_gray(self.graph_1, signal)
        alpha = float(self.lineEdit_noise_procent.text())

