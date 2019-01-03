import pyaudio
import struct


class Probe:
    def __init__(self, count=1024, resolution=16, channels=1):
        pa_resolution = {
            32: pyaudio.paInt32,
            16: pyaudio.paInt16,
            8: pyaudio.paInt8}
        self.BYTES_PER_SAMPLE = resolution // 8
        self.UNPACK_TYPE = {1: 'b', 2: 'h', 4: 'i'}[self.BYTES_PER_SAMPLE]
        record_seconds = 0.1
        if resolution in pa_resolution:
            self.RESOLUTION = pa_resolution[resolution]
        else:
            raise ValueError('Available resolutions are {}'.format(pa_resolution.keys()))
        self.CHANNELS = channels
        self.RATE = 64000
        self.CHUNK = 1024
        self.RECORD_SECONDS = record_seconds
        self.samples = []
        audio = pyaudio.PyAudio()
        self.stream = audio.open(format=self.RESOLUTION, channels=self.CHANNELS, rate=self.RATE, input=True,
                                 frames_per_buffer=self.CHUNK)

    def __read_samples(self, min_samples_to_be_in_buffer):
        # CHUNK IN STREAM INIT !!!!!!!!!!!!!!!!
        samples_available = self.stream.get_read_available()
        if samples_available + len(self.samples) < min_samples_to_be_in_buffer:
            samples_to_read = min_samples_to_be_in_buffer
        else:
            samples_to_read = samples_available
        raw_samples = self.stream.read(samples_to_read)
        self.samples.extend(
            struct.unpack(self.UNPACK_TYPE * int(len(raw_samples) // self.BYTES_PER_SAMPLE), raw_samples))

    def get_samples(self, count):
        if len(self.samples) < count:
            self.__read_samples(count - len(self.samples))
        samples = self.samples[:count]
        self.samples = self.samples[count:]
        return samples

    def counter_high_pass_filter(self):
        pass
        # Return RC high-pass filter output samples, given input samples,
        # time interval dt, and time constant RC
        # function highpass(real[0..n] x, real dt, real RC)
        # var real[0..n] y
        # var real α := RC / (RC + dt)
        # y[0] := x[0]
        # for i from 1 to n
        #   y[i] := α * y[i-1] + α * (x[i] - x[i-1])
        # return y
