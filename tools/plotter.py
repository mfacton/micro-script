"""Simple Line Plotter for streaming high bandwidth data"""

from enum import Enum

import cv2
import numpy as np


class PlotColors(Enum):
    """Colors for each data segment"""

    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    RED = (255, 0, 0)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)
    WHITE = (255, 255, 255)
    MAROON = (128, 0, 0)
    LIME = (0, 128, 0)
    PURPLE = (128, 0, 128)
    NAVY = (0, 0, 128)
    OLIVE = (128, 128, 0)
    TEAL = (0, 128, 128)
    SILVER = (192, 192, 192)
    ORANGE = (255, 165, 0)
    BROWN = (128, 0, 0)
    DARK_CYAN = (0, 128, 128)
    BLACK = (0, 0, 0)


class Plot:
    """Line Plot class"""

    def __init__(
        self,
        data_length,
        min,
        max,
        width=1600,
        height=800,
        pixel_shift=2,
        frame_skip=1,
        line_thickness=2,
        background=PlotColors.BLACK,
        data_colors=list(PlotColors),
        title="Plot",
    ):
        self.data_length = data_length
        self.min = min
        self.max = max
        self.width = width
        self.height = height
        self.pixel_shift = pixel_shift
        self.frame_skip = frame_skip
        self.line_thickness = line_thickness
        self.background = background
        self.data_colors = data_colors
        self.title = title

        self.canvas = np.full(
            (self.height, self.width + 1, 3), self.background.value, dtype=np.uint8
        )
        self.last_points = np.zeros((data_length,))
        self.first_plot = True
        self.frame_count = 0

    def push(self, new_data):
        """Add next point to plot"""
        self.canvas[:, : -self.pixel_shift, :] = self.canvas[:, self.pixel_shift :, :]
        self.canvas[:, -self.pixel_shift :] = self.background.value
        for i in range(self.data_length):
            plot_y = (new_data[i]-self.min)*self.height/(self.max-self.min)
            if not self.first_plot:
                cv2.line(
                    self.canvas,
                    (self.width, int(self.height - plot_y)),
                    (
                        self.width - self.pixel_shift,
                        self.height - int(self.last_points[i]),
                    ),
                    self.data_colors[i % len(self.data_colors)].value,
                    self.line_thickness,
                )
            self.last_points[i] = plot_y

        if self.first_plot:
            self.first_plot = False

        if self.frame_count == 0:
            cv2.imshow(self.title, self.canvas)
            cv2.waitKey(1)
        
        self.frame_count += 1

        if self.frame_count > self.frame_skip:
            self.frame_count = 0


    def reset(self):
        """Resets the plot"""
        self.canvas = np.full(
            (self.height, self.width + 1, 3), self.background.value, dtype=np.uint8
        )
        self.canvas = np.zeros((self.height, self.width + 1, 3), dtype=np.uint8)
        self.first_plot = True

    def close(self):
        """Close plot window"""
        cv2.destroyAllWindows()
