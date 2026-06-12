from graphics import Graphs
g = Graphs(title="Test", theme="ggplot")
temperatures = [
    [22, 25, 28],
    [24, 27, 30],
    [26, 29, 32]
]

g.heatmap(
    matrix=temperatures,
    color="green"
)