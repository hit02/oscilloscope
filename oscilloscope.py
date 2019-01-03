from plot import Plot
from probe import Probe
from channel import Channel

import IPython
ipython = IPython.get_ipython()


class Oscilloscope:

    @staticmethod
    def start():
        plot = Plot()
        probe = Probe()
        channel = Channel()
        plot.add_channel(channel)

        while not plot.closed:
            samples = probe.get_samples(1024)
            # samples = integrate_samples(samples)
            channel.add_samples(samples)
            plot.update_plot()


if __name__ == "__main__":
    osc = Oscilloscope()
    osc.start()
