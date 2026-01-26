# Agricultural Plant Health Classification (Bean Crop)

## Project Overview
This project is a proof-of-concept machine learning system for classifying agricultural plant images into **healthy** and **unhealthy** categories. The goal is to demonstrate an end-to-end ML workflow — from data loading and preprocessing to model training, evaluation, and reflection — using a real-world dataset.

---

## Problem Statement
Early detection of plant diseases is essential for improving crop yield and reducing losses. Manual inspection of crops is time-consuming and prone to error.

This project aims to automatically classify images of **Bean plants** into:
- **Healthy (label 0)**
- **Unhealthy (label 1)**

---

## Dataset
**Source:** Mendeley Data – Bangladeshi Vegetables Dataset  
**Focus Crop:** Bean  


Only the Bean crop was selected to:
- Reduce inter-crop variability
- Simplify the baseline model
- Clearly demonstrate the ML workflow

### Class Distribution
- Healthy: 632 images  
- Unhealthy: 13 images  

This class imbalance is noted and discussed in the evaluation.

---

## Approach

### 1. Data Preprocessing
- Images loaded from directory structure
- Resized to **64 × 64**
- Converted to RGB
- Flattened into feature vectors
- Pixel values normalized to `[0, 1]`

### 2. Feature Representation
- Raw pixel intensities (flattened)
- Chosen intentionally as a simple, interpretable baseline

### 3. Model
- **Logistic Regression**
- Selected due to:
  - Prior experience with regression-based models
  - Interpretability
  - Suitability for a baseline classifier

### 4. Evaluation Metrics
- Accuracy
- Precision, Recall, F1-score
- Confusion Matrix

---

## Results

**Accuracy:** ~94.6%

**Key Observations:**
- The model performs well on the majority (Healthy) class
- Recall for the Unhealthy class is very low due to severe class imbalance
- High accuracy is misleading in this context, highlighting the importance of class-aware metrics

---

## Challenges Faced
- Severe class imbalance in the dataset
- Learning and implementing image-based classification within a limited timeframe
- Understanding and implementing image loading and preprocessing pipelines
- Limited ability of traditional ML models to capture spatial features in images

---

## Limitations
- Flattened pixel features lose spatial information
- Logistic Regression struggles with complex visual patterns
- Minority class is underrepresented
- No data augmentation or class rebalancing applied

---

## Future Work
To improve performance and move toward production-ready AI systems, my thoughts would be to:

- Apply **class weighting or oversampling** techniques
- Use **Convolutional Neural Networks (CNNs)** for automatic feature learning
- Explore **Vision Transformers (ViT)** and other pretrained models available on **Hugging Face**
- Extend the system to multi-crop or multi-disease classification
- Investigate related applications such as document analysis using computer vision techniques

---

