# src/features.py
import numpy as np

def flatten_features(images):
    return images.reshape(images.shape[0], -1)
