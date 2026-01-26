# src/preprocess.py
import os
import cv2
import numpy as np

def load_images(base_path, img_size=64):
    categories = ['Healthy', 'Unhealthy']
    X, y = [], []

    for label, category in enumerate(categories):
        path = os.path.join(base_path, category)

        for img_name in os.listdir(path):
            try:
                img_path = os.path.join(path, img_name)
                img = cv2.imread(img_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, (img_size, img_size))
                X.append(img.flatten())
                y.append(label)
            except:
                continue

    X = np.array(X) / 255.0
    y = np.array(y)

    return X, y
