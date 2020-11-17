from sklearn.ensemble import RandomForestClassifier
import numpy as np
from spectral import *
from PIL import Image
import time

start = time.time()
def log(t): print(f"[{round(time.time() - start, 2)}] {t}.")


log("Finished imports.")

# Data loading
classes = ["epithelium", "stroma", "necrosis", "blood", "lymphocytes"]
masks = {}
for tissue in classes:
    for set in ["train", "test"]:
        masks[f"{tissue}_{set}"] = np.asarray(Image.open(f"/data/berisha_lab/neuwirth/annotations-1-masks/ov-63-hd-16ca-{tissue}-{set}.bmp"))
        log(f"Loaded {tissue}_{set}.")
log("Finished loading masks.")

OV63 = '/data/berisha_lab/ftir/with-paraffin/ov-63/hd/16ca/ov-63-hd-16ca.hdr'
img = open_image(OV63)
log("Finished loading data.")

print(masks["epithelium_train"].shape)
print(img.shape)