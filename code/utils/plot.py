import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def set_tick(ax):
    """Set the tick of any plot to have 4 minor ticks inside major ticks

    Args:
        ax : matplotlib axis
    """
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.tick_params(which="both", direction="in", width=1)
    ax.tick_params(which="major", length=4)
    ax.tick_params(which="minor", length=2, color="black")


def plot_field(ax, x, y, f, label):
    """Make 2D colormesh plot from a given field

    Args:
        ax (matplotlib axis)
        x (2D np.array): meshgrid of the x axis
        y (2D np.array): meshgrid of the y axis
        f (2D np.array): field
        label (str): label of the field

    Returns:
        matplotlib axis: plot result
    """
    pl = ax.pcolormesh(x, y, f)
    cbar = plt.colorbar(pl, ax=ax)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    cbar.set_label(label)
    set_tick(ax)

    return pl
