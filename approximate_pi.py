import subprocess
import sys
import time

from utils import Matrix, perf_stats

PPM_FOLDER = "ppm"
FIGURES = None
PROTOCOL = "P6"
COLORS = [b'\xff\xff\xff', b'\xff\x00\xff', b'\x00\x00\xff', b'\x00\xff\x00']


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
    path = os.path.join(PPM_FOLDER, fname)

    print(f"Image {n} with {m.count:9,d} points: pi = {m.approx_pi():0.{rounding}f} saved in {fname}")

    with open(path, "wb") as f:
        mat = m.matrix.copy()
        draw_text(m, pi, rounding)
        header = f"{PROTOCOL} {m.width} {m.height} 255\n"
        f.write(header.encode("UTF-8"))
        for v in m.matrix:
            f.write(COLORS[v])
    m.matrix = mat

    return path


def main(argv):
    width = int(argv[1])
    points = int(argv[2])
    rounding = int(argv[3])

    m = Matrix(width)
    steps = points // 10

    delta = time.perf_counter()

    fnames = []
    for n, p in enumerate(range(steps, points + steps, steps)):
        m.fill_matrix(steps)
        fname = generate_ppm_file(m, rounding, n)
        fnames.append(fname)

    print("Generating GIF pi.gif")
    subprocess.call(["python", "convert.py"] + fnames + ["pi.gif"])

    delta = time.perf_counter() - delta
    perf_stats(m.approx_pi(), points, delta)


if __name__ == "__main__":
    import os
    import pickle

    with open("figures.dat", "rb") as file:
        FIGURES = pickle.load(file)

    os.makedirs(PPM_FOLDER, exist_ok=True)

    main(sys.argv)
