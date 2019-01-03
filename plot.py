import _tkinter
import matplotlib.pyplot as plt


class Plot:
    def __init__(self, x_size=1024, y_size=70000):
        self.channels = []
        self.x_size = x_size
        self.y_size = y_size
        self.current_max_sample = 0
        self.closed = False

    def add_channel(self, channel):
        self.channels.append(channel)

    def remove_channel(self):
        pass

    def update_plot(self):
        # pls update me https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
        if self.closed:
            return
        try:
            plt.clf()
            with plt.style.context(('dark_background')):
                plt.axis([0, self.x_size, -self.y_size, self.y_size])
                plt.plot(self.channels[0].samples, color=self.channels[0].color)
                plt.pause(0.05)
        except _tkinter.TclError:
            self.closed = True
