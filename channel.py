from logger import Logger


class Channel:

    def __init__(self, max_samples=1024, color='#20C20E'):
        self.__samples = []
        self.__max_samples = max_samples
        self.__current_max_sample = 0
        self.__color = color

    @property
    def samples(self):
        return self.__samples

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def current_max_sample(self):
        return self.__current_max_sample

    @property
    def max_samples(self):
        return self.max_samples

    @max_samples.setter
    def max_samples(self, value):
        self.__max_samples = value
        self.__delete_unnecessary_samples()

    def __delete_unnecessary_samples(self):
        if self.__current_max_sample > self.__max_samples:
            del self.__samples[:(self.__current_max_sample - self.__max_samples)]
            self.__current_max_sample -= self.__current_max_sample - self.__max_samples

    def add_samples(self, samples):
        if len(samples) > self.__max_samples:
            Logger.warning('Too much samples to hold. Dropped {} samples.'.format(len(samples) - self.__max_samples))
        self.__current_max_sample += len(samples)
        self.__samples.extend(samples)
        self.__delete_unnecessary_samples()
