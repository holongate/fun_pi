import sys
from PIL import Image

if __name__ == "__main__":
    ppm = sys.argv[1:-2]
    gif = sys.argv[-1]

    frames = []
    for fname in ppm:
        frames.append(Image.open(fname))

    frames[0].save(gif, save_all=True, append_images=frames[1:], optimize=False, duration=1000, loop=0)
