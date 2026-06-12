from graphics import Graphs
from tkinter import colorchooser
clr = colorchooser.askcolor()
g = Graphs(title="Alpha", theme="ggplot")
temperatures = [[0, 12, 45, 23],
                [1, 12, 15, 20],
                [20, 15, 12, 1]]
g.heatmap(temperatures
          ,color=str(clr[1]))
g.histogram(temperatures)