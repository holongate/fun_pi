import sys
import time

from utils import Matrix, perf_stats

FIGURES = None
COLORS = ["1 1 1\n", "1 0 1\n", "0 0 1\n", "0 1 0\n"]


def draw_text(m, pi, rounding):
    txt = f"{pi:.{rounding}f}"
    xo = (m.width - FIGURES['0'].width * len(txt)) // 2
    yo = (m.height - FIGURES['0'].height) // 2

    for c in txt:
        FIGURES[c].draw(m, xo, yo)
        xo += FIGURES[c].width


def generate_ppm_file(m, rounding, n):
    pi = m.approx_pi()
    fname = f"img{n}_{pi:.{rounding}f}.ppm".replace(".", "-", 1)

    print(f"Image {n} with {m.count:9,d} points: pi = {m.approx_pi():0.{rounding}f} saved in {fname}")

    with open(fname, "wt") as f:
        mat = m.matrix.copy()
        draw_text(m, pi, rounding)
        f.writelines(f"P3 {m.width} {m.height} 1\n")
        for v in m.matrix:
            f.writelines(COLORS[v])
    m.matrix = mat


def main(argv):
    width = int(argv[1])
    points = int(argv[2])
    rounding = int(argv[3])

    m = Matrix(width)
    steps = points // 10

    delta = time.perf_counter()

    for n, p in enumerate(range(steps, points + steps, steps)):
        m.fill_matrix(steps)
        generate_ppm_file(m, rounding, n)

    delta = time.perf_counter() - delta
    perf_stats(m.approx_pi(), points, delta)


if __name__ == "__main__":
    import os
    import pickle

    with open("figures.dat", "rb") as f:
        FIGURES = pickle.load(f)

    os.makedirs("ppm", exist_ok=True)
    os.chdir("ppm")

    main(sys.argv)
