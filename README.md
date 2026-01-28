# Agricultural Plant Health Classification (Bean Crop)

## Project Overview
This project is a **proof-of-concept machine learning system** for classifying agricultural plant images into **healthy** and **unhealthy** categories. It demonstrates an end-to-end ML workflow — from data loading and preprocessing to model training, evaluation, and reflection — using a real-world image dataset.

The project intentionally progresses from **classical machine learning baselines** to an **exploratory deep learning approach**, highlighting trade-offs, limitations, and future directions relevant to AI-powered products.


## Problem Statement
Early detection of plant stress and disease is critical for improving crop yield and reducing agricultural losses. Manual inspection is time-consuming, subjective, and difficult to scale.

The goal of this project is to automatically classify **Bean plant images** into:
- **Healthy (label 0)**
- **Unhealthy (label 1)**


## Dataset
**Source:** Mendeley Data – Bangladeshi Vegetables Dataset  
**Selected Crop:** Bean  

Only the Bean crop was used in this project to:
- Reduce inter-crop variability
- Focus on binary classification
- Clearly demonstrate the ML workflow

### Class Distribution
- Healthy: 632 images  
- Unhealthy: 13 images  

The dataset is **severely imbalanced**, which significantly affects model performance and evaluation.



## Approach

### 1. Data Preprocessing
- Images loaded from directory structure (`Healthy`, `Unhealthy`)
- Converted to RGB format
- Resized to **64 × 64**
- Pixel values normalized to `[0, 1]`

Two representations were used:
- **Flattened images** for classical ML models
- **3D image tensors** for the CNN


### 2. Feature Representation
- Raw pixel intensities
- Flattened to 1D vectors for classical models
- Preserved spatial structure for CNN experiments

This design allows direct comparison between traditional ML and deep learning approaches.


### 3. Models Implemented

#### Classical Machine Learning (Baseline)
- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Random Forest Classifier**

These models were selected to:
- Build interpretable baselines
- Apply classification concepts learned from regression
- Highlight the limitations of classical models on image data

#### Deep Learning (Exploratory)
- **Simple Convolutional Neural Network (CNN)**
  - Convolution + pooling layers
  - Fully connected classification head
  - Binary output using sigmoid activation

The CNN was implemented as a proof-of-concept to assess suitability for computer vision tasks.

---

### 4. Evaluation Metrics
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix

Special attention was paid to minority class performance due to dataset imbalance.



## Results

### Classical Models
- Accuracy ranged between **94% – 98%**
- Models performed very well on the **Healthy** class
- All classical models failed to correctly identify **Unhealthy** samples

This demonstrates that:
High accuracy does not imply effective classification when classes are imbalanced.

### CNN Experiment
- The CNN learned spatial features directly from images
- Training accuracy fluctuated across epochs
- Performance was limited by:
  - Small dataset size
  - Severe class imbalance
  - Lack of data augmentation

Despite limitations, the CNN confirms the **appropriateness of deep learning for this problem domain**.

---

## Challenges Faced
- Severe class imbalance (632 vs 13 samples)
- Learning and applying image-based classification within a short timeframe
- Implementing image loading and preprocessing pipelines
- Understanding and interpreting classification metrics beyond accuracy
- Managing deep learning instability with limited data



## Limitations
- Flattened pixel features discard spatial information
- Classical ML models are not well-suited for complex visual patterns
- Minority class underrepresentation limits generalization
- CNN experiment was constrained by time and data availability


## Key Takeaway
This project establishes a **strong baseline** and demonstrates an understanding of:
- ML experimentation workflows
- Model limitations
- The transition from classical ML to modern computer vision systems

