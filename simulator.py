import sys
import time

from utils import Matrix, perf_stats


def main(argv):
    assert len(argv) == 2, "Vous devez donner le nombre de points"
    points = int(argv[1])
    assert points > 0, "Le nombre de points doit être > 0"

    delta = time.perf_counter()
    m = Matrix()
    m.fill_matrix(points)
    delta = time.perf_counter() - delta
    perf_stats(m.approx_pi(), points, delta)


if __name__ == "__main__":
    main(sys.argv)
