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
        """Draw a simple and basic bar graph."""
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
        """Draw a simple and basic horizontal bar graph."""
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
        """Draw a standard scatter graph using the x and y coordinates"""
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
        """Draw a color coded pie chart"""
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
        """By using this command you can simly draw a histograph"""
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
        """Draw an area graph using this command. An example for usage is ```graph.area_graph(x=(12, 2), y=(1,12))```."""
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
        """Draw a simple step graph"""
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
        """Draw a simple stem graph."""
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
        """Draw a simple box plot graph"""
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
        """Draw a violin graph"""
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
        """Draw a heat map"""
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
        """Draw a realtime graph"""
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
        """Save the graph to a file"""
        plt.savefig(
            filename,
            dpi=dpi,
            bbox_inches="tight"
        )
    # -------------------------
    # 3D LINE GRAPH
    # -------------------------
    def line_3d_graph(
        self,
        x,
        y,
        z,
        color="blue",
        linewidth=2,
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        show=True
    ):
        """Draw a 3D line graph."""

        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection="3d")

        ax.plot(
            x,
            y,
            z,
            color=color,
            linewidth=linewidth
        )

        ax.set_title(self.title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        if show:
            plt.show()

    # -------------------------
    # 3D SCATTER GRAPH
    # -------------------------
    def scatter_3d_graph(
        self,
        x,
        y,
        z,
        color="red",
        size=50,
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        show=True
    ):
        """Draw a 3D scatter graph."""

        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection="3d")

        ax.scatter(
            x,
            y,
            z,
            c=color,
            s=size
        )

        ax.set_title(self.title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        if show:
            plt.show()

    # -------------------------
    # 3D BAR GRAPH
    # -------------------------
    def bar_3d_graph(
        self,
        x,
        y,
        z,
        dx=0.5,
        dy=0.5,
        color="skyblue",
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        show=True
    ):
        """Draw a 3D bar graph."""

        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection="3d")

        ax.bar3d(
            x,
            y,
            np.zeros(len(z)),
            dx,
            dy,
            z,
            color=color,
            shade=True
        )

        ax.set_title(self.title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        if show:
            plt.show()

    # -------------------------
    # 3D SURFACE GRAPH
    # -------------------------
    def surface_3d_graph(
        self,
        x,
        y,
        z,
        cmap="viridis",
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        show=True
    ):
        """Draw a 3D surface graph."""

        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection="3d")

        ax.plot_surface(
            x,
            y,
            z,
            cmap=cmap,
            edgecolor="none"
        )

        ax.set_title(self.title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        if show:
            plt.show()

    # -------------------------
    # 3D WIREFRAME GRAPH
    # -------------------------
    def wireframe_3d_graph(
        self,
        x,
        y,
        z,
        color="black",
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        show=True
    ):
        """Draw a 3D wireframe graph."""

        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection="3d")

        ax.plot_wireframe(
            x,
            y,
            z,
            color=color
        )

        ax.set_title(self.title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        if show:
            plt.show()

    # -------------------------
    # 3D CONTOUR GRAPH
    # -------------------------
    def contour_3d_graph(
        self,
        x,
        y,
        z,
        cmap="viridis",
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        show=True
    ):
        """Draw a 3D contour graph."""

        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection="3d")

        ax.contour3D(
            x,
            y,
            z,
            50,
            cmap=cmap
        )

        ax.set_title(self.title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        if show:
            plt.show()

    # -------------------------
    # 3D STEM GRAPH
    # -------------------------
    def stem_3d_graph(
        self,
        x,
        y,
        z,
        color="green",
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
        show=True
    ):
        """Draw a 3D stem graph."""

        fig = plt.figure(figsize=self.figsize)
        ax = fig.add_subplot(111, projection="3d")

        for xi, yi, zi in zip(x, y, z):
            ax.plot(
                [xi, xi],
                [yi, yi],
                [0, zi],
                color=color
            )

        ax.scatter(
            x,
            y,
            z,
            color=color
        )

        ax.set_title(self.title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        if show:
            plt.show()