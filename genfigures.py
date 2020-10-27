import pickle

from PIL import ImageFont, ImageDraw, Image

from utils import Figure

TEXT = "0123456789."

fnt = ImageFont.truetype("FreeMonoBold", 100)

FIGURES = {}

for c in TEXT:
    bbox = fnt.getbbox(c, "1")
    shape = (bbox[0] + bbox[2], bbox[1] + bbox[3])
    im = Image.new("1", shape)
    d = ImageDraw.Draw(im)
    d.text((0, 0), c, font=fnt, fill=(1,))
    FIGURES[c] = Figure(shape, list(im.getdata()))

with open("figures.dat", "wb") as f:
    pickle.dump(FIGURES, f)
# im.show()
