from sklearn.ensemble import RandomForestClassifier
import numpy as np
from spectral import *
from PIL import Image
import time

classes = ["epithelium", "stroma", "necrosis", "blood", "lymphocytes"]

start = time.time()
def current(): return round(time.time() - start, 2)

print(f"{current()} Loaded imports.")

masks = {}
for tissue in classes:
    for set in ["train", "test"]:
        masks[f"{tissue}_{set}"] = np.asarray(Image.open(f"/data/berisha_lab/neuwirth/annotations-1-masks/{tissue}_{set}.png"))
        masks[f"{tissue}_{set}"][masks[f"{tissue}_{set}"] > 0] = 1
        print(f"{current()} Loaded {tissue}_{set}.")

print(f"{current()} Finished loading masks.")

OV63 = '/data/berisha_lab/ftir/with-paraffin/ov-63/hd/16ca/ov-63-hd-16ca.hdr'
img = open_image(OV63)
print(f"{current()} Loaded imaging file.")
y = np.zeros_like(masks["epithelium_train"])
i = 1

for i in len(masks):
    mask = masks[i]
    y[mask == 1] = i
    i += 1

print(np.count(y))
