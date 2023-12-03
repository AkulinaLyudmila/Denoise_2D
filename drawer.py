from graph import Graph


# ШАБЛОНЫ ОТРИСОВКИ ГРАФИКОВ
# Очистка и подпись графика (вызывается в начале)
def cleaning_and_chart_graph(graph: Graph, title):
    # graph.toolbar.home()  # Возвращаем зум в домашнюю позицию
    # graph.toolbar.update()  # Очищаем стек осей (от старых x, y lim)
    # Очищаем график
    graph.axis.clear()
    # Скрыть значения по осям
    graph.axis.get_xaxis().set_visible(False)
    graph.axis.get_yaxis().set_visible(False)
    # Задаем название графика
    graph.axis.set_title(title)


# Отрисовка (вызывается в конце)
def draw_graph(graph: Graph):
    # Убеждаемся, что все помещается внутри холста
    graph.figure.tight_layout()
    # Показываем новую фигуру в интерфейсе
    graph.canvas.draw()


# Отрисовка при отсутствии данных
def no_data(graph: Graph):
    graph.axis.text(0.5, 0.5, "Нет данных",
                    fontsize=14,
                    horizontalalignment='center',
                    verticalalignment='center')
    # Отрисовка, без подписи данных графиков
    draw_graph(graph)


# Класс художник. Имя холст (graph), рисует на нем данные
class Drawer:
    # ОТРИСОВКИ
    @staticmethod
    def graph_2d_color(
            graph: Graph,
            data
    ):

        # Очистка, подпись графика и осей (вызывается в начале)
        cleaning_and_chart_graph(
            # Объект графика
            graph=graph,
            # Название графика
            title=graph.name_graph
        )

        # Рисуем график
        graph.axis.imshow(data)

        # Отрисовка (вызывается в конце)
        draw_graph(graph)

    @staticmethod
    def graph_2d_gray(
            graph: Graph,
            data
    ):
        # Очистка, подпись графика и осей (вызывается в начале)
        cleaning_and_chart_graph(
            # Объект графика
            graph=graph,
            # Название графика
            title=graph.name_graph
        )

        # Рисуем график
        graph.axis.imshow(data, cmap='gray')

        # Отрисовка (вызывается в конце)
        draw_graph(graph)
