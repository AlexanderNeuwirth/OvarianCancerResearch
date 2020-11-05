from sklearn.ensemble import RandomForestClassifier
import numpy as np
from spectral import *
from PIL import Image

OV63 = '/data/berisha_lab/ftir/with-paraffin/ov-63/hd/16ca/ov-63-hd-16ca.hdr'
img = open_image(OV63)
img[:, 1:2, :]
im = Image.open("/data/berisha_lab/neuwirth/annotations-1-masks/ov-63-hd-16ca-epithelium-train.bmp")
p = np.array(im)