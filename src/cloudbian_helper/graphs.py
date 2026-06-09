"""Generate graphs using matplotlib only by entering simple commands
Example usage:

```python

from graphs import Graphs


g = Graphs(
    title="Animal Balance",

    theme="ggplot"
)

g.pie_chart(
    labels=["Humans", "Animals", "Insects"],

    values=[80, 50, 40]
)

g.bar_graph(
    labels=["Humans", "Animals", "Insects"],

    values=[80, 50, 40]
)

g.horizontal_bar_graph(
    labels=["Humans", "Animals", "Insects"],

    values=[80, 50, 40]
)

```
"""


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Graphs:
    def __init__(
        self,
        title="Graph",
        figsize=(8, 5),
        theme="default",
        grid=True
    ):
        plt.style.use(theme)
        self.figsize = figsize
        self.title = title
        self.grid = grid

    # -------------------------
    # LINE GRAPH
    # -------------------------
    def line_graph(
        self,
        x,
        y,
        color="blue",
        marker="o",
        linewidth=2,
        xlabel="X",
        ylabel="Y",
        show=True
    ):
        """Draw a line graph."""
        plt.figure(figsize=self.figsize)
        plt.plot(
            x,
            y,
            color=color,
            marker=marker,
            linewidth=linewidth
        )
        plt.title(self.title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(self.grid)

        if show:
            plt.show()

    # -------------------------
    # BAR GRAPH
    # -------------------------
    def bar_graph(
        self,
        labels,
        values,
        color="skyblue",
        xlabel="Category",
        ylabel="Value",
        show=True
    ):
        plt.figure(figsize=self.figsize)
        plt.bar(labels, values, color=color)

        plt.title(self.title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        if show:
            plt.show()

    # -------------------------
    # HORIZONTAL BAR
    # -------------------------
    def horizontal_bar_graph(
        self,
        labels,
        values,
        color="green",
        show=True
    ):
        plt.figure(figsize=self.figsize)
        plt.barh(labels, values, color=color)
        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # SCATTER PLOT
    # -------------------------
    def scatter_graph(
        self,
        x,
        y,
        color="red",
        size=50,
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.scatter(
            x,
            y,
            c=color,
            s=size
        )

        plt.title(self.title)
        plt.grid(self.grid)

        if show:
            plt.show()

    # -------------------------
    # PIE CHART
    # -------------------------
    def pie_chart(
        self,
        labels,
        values,
        autopct="%1.1f%%",
        startangle=90,
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.pie(
            values,
            labels=labels,
            autopct=autopct,
            startangle=startangle
        )

        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # HISTOGRAM
    # -------------------------
    def histogram(
        self,
        data,
        bins=10,
        color="purple",
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.hist(
            data,
            bins=bins,
            color=color
        )

        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # AREA GRAPH
    # -------------------------
    def area_graph(
        self,
        x,
        y,
        color="cyan",
        alpha=0.5,
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.fill_between(
            x,
            y,
            color=color,
            alpha=alpha
        )

        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # STEP GRAPH
    # -------------------------
    def step_graph(
        self,
        x,
        y,
        color="orange",
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.step(
            x,
            y,
            color=color
        )

        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # STEM GRAPH
    # -------------------------
    def stem_graph(
        self,
        x,
        y,
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.stem(x, y)

        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # BOX PLOT
    # -------------------------
    def box_plot(
        self,
        data,
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.boxplot(data)

        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # VIOLIN PLOT
    # -------------------------
    def violin_plot(
        self,
        data,
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.violinplot(data)

        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # HEATMAP
    # -------------------------
    def heatmap(
        self,
        matrix,
        cmap="viridis",
        show=True
    ):
        plt.figure(figsize=self.figsize)

        plt.imshow(
            matrix,
            cmap=cmap
        )

        plt.colorbar()
        plt.title(self.title)

        if show:
            plt.show()

    # -------------------------
    # REALTIME LINE GRAPH
    # -------------------------
    def realtime_graph(
        self,
        data_function,
        interval=100
    ):
        fig, ax = plt.subplots()

        x_data = []
        y_data = []

        line, = ax.plot([], [])

        def animate(frame):
            value = data_function()

            x_data.append(len(x_data))
            y_data.append(value)

            line.set_data(x_data, y_data)

            ax.relim()
            ax.autoscale_view()

            return line,

        FuncAnimation(
            fig,
            animate,
            interval=interval,
            cache_frame_data=False
        )

        plt.show()

    # -------------------------
    # SAVE FIGURE
    # -------------------------
    def save(
        self,
        filename="graph.png",
        dpi=300
    ):
        plt.savefig(
            filename,
            dpi=dpi,
            bbox_inches="tight"
        )