import time


class Logger:
    def __init__(self, filename):
        self.log_file = open(filename, "a")

    def log(self, string):
        self.log_file.write("%.1f: %s\n" % (time.time(), string))
        self.log_file.flush()
