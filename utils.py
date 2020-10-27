from random import uniform
from math import sqrt

BACKGROUND = 0
OUTSIDE = 1
INSIDE = 2
OVERLAY = 3


class Array:
    def __init__(self, shape, data=None):
        if shape != (0, 0):
            if data is None:
                self.matrix = bytearray(shape[0] * shape[1])
            else:
                self.matrix = data
            self.width = shape[0]
            self.height = shape[1]
        else:
            self.matrix = None
            self.width = 0
            self.height = 0

    def index(self, i, j):
        return i + j * self.width

    def set(self, i, j, v):
        if self.matrix is not None:
            idx = self.index(i, j)
            self.matrix[idx] = int(v)

    def get(self, i, j):
        return self.matrix[self.index(i, j)]


class Matrix(Array):
    def __init__(self, width=0):
        super().__init__(shape=(width, width))
        self.count = 0
        self.inside = 0

    def index_xy(self, x, y):
        i = int((x + 1.0) / 2.0 * self.width)
        j = int((y + 1.0) / 2.0 * self.height)
        return i, j

    def approx_pi(self):
        return 4.0 * self.inside / self.count

    def fill_matrix(self, points):
        for n in range(points):
            x, y = uniform(-1, 1), uniform(-1, 1)
            isinside = sqrt(x * x + y * y) <= 1
            self.inside += isinside
            self.count += 1
            i, j = self.index_xy(x, y)
            self.set(i, j, INSIDE if isinside else OUTSIDE)


class Figure(Array):
    def __init__(self, shape, data):
        super().__init__(shape=shape, data=data)

    def draw(self, m, x, y):
        for j in range(self.height):
            yc = y + j
            for i in range(self.width):
                xc = x + i
                v = self.get(i, j)
                if v != 0:
                    m.set(xc, yc, OVERLAY)


def memory_usage():
    """Memory usage of the current process in kb."""
    status = None
    result = {'peak': 0, 'rss': 0}
    try:
        # This will only work on systems with a /proc file system
        # (like Linux).
        status = open('/proc/self/status')
        for line in status:
            parts = line.split()
            key = parts[0][2:-1].lower()
            if key in result:
                result[key] = int(parts[1])
    finally:
        if status is not None:
            status.close()

    return result


def perf_stats(pi, points, delta):
    print(f"Approximation: pi = {pi} with {points:,d} points")
    print(f"Elapsed time : {delta:0.3f}s ({int(points / delta):,d} points/s)")
    peak = memory_usage()["peak"]
    print(f"Peak memory  : {peak // 1024} MB")
