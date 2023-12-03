from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# Класс для объектов графика
class Graph:
    def __init__(self, layout, widget, name_graph=""):
        # Объекты графика
        self.axis = None
        self.figure = None
        self.canvas = None
        self.toolbar = None
        self.layout = layout  # Слой - для отрисовки графика
        self.widget = widget  # Виджет - для отрисовки графика
        self.name_graph = name_graph
        # Вызываем инициализацию
        self.initialize()

    def initialize(self, draw=False):
        # Инициализирует фигуру matplotlib внутри контейнера GUI.
        # Вызываем только один раз при инициализации

        # Создание фигуры (self.fig и self.ax)
        self.figure = Figure()
        self.axis = self.figure.add_subplot(111)
        # Создание холста
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        if draw:
            self.canvas.draw()
