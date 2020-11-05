from sklearn.ensemble import RandomForestClassifier
import numpy as np
from spectral import *
from PIL import Image
import time

start = time.time()
def current(): round(time.time() - start, 2)

print(f"{current()} Loaded imports.")

OV63 = '/data/berisha_lab/ftir/with-paraffin/ov-63/hd/16ca/ov-63-hd-16ca.hdr'
img = open_image(OV63)
img[:, 1:2, :]

print(f"{current()} Loaded imaging file.")

im = Image.open("/data/berisha_lab/neuwirth/annotations-1-masks/ov-63-hd-16ca-epithelium-train.bmp")

print(f"{current()} Loaded tissue mask.")

p = np.array(im)

print(f"{current()} Cast issue mask to array.")