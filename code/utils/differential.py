import numpy as np


def laplacian(f):
    gfx, gfy, gfz = np.gradient(f)

    ggfx, _, _ = np.gradient(gfx)
    _, ggfy, _ = np.gradient(gfy)
    _, _, ggfz = np.gradient(gfz)

    lap = ggfx + ggfy + ggfz

    return lap


def laplacian_2d(f):
    """Calculate a 2D laplacian of a given field

    Args:
        f (np.array): field

    Returns:
        np.array: laplacian of f
    """
    gfx, gfy = np.gradient(f)
    ggfx, _ = np.gradient(gfx)
    _, ggfy = np.gradient(gfy)

    return ggfx + ggfy
