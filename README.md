# Dummy dataset for Engine Fuel Injector Failure Prediction
#### Wednesday 11 Sep 2024

This repository contains a dummy dataset designed to predict the **Time Until Failure** (in hours) for fuel injectors, based on **CuNi Contamination** levels in engine fuel. The dataset can be used to train and evaluate machine learning models that estimate how long fuel injectors will last given the contamination level of copper-nickel (CuNi) particles in the fuel.

## Dataset Description

The dataset consists of 500 samples, with two columns:

1. **CuNi Content (ppm)**: The level of copper-nickel contamination in parts per million (ppm) in the engine fuel.
2. **Time Until Failure (hours)**: The time (in hours) until the fuel injectors are expected to fail, based on the contamination level. The relationship between CuNi content and time until failure is **non-linear**, with higher CuNi content generally reducing the injector's lifespan. Random noise has been added to introduce variability and make the problem less straightforward.

The dataset is stored in a CSV file: `engine_fuel_injector_failure.csv`

### Sample Data

| CuNi Content (ppm) | Time Until Failure (hours) |
|--------------------|----------------------------|
| 38.08              | 79.85                      |
| 15.45              | 208.45                     |
| 92.56              | 28.34                      |
| 74.67              | 37.12                      |
| 29.24              | 109.56                     |

## Usage

This dataset can be used to train machine learning models in platforms like **Microsoft Azure**, or other machine learning frameworks such as **scikit-learn**, **TensorFlow**, etc. The primary goal is to predict the time until failure based on CuNi contamination levels.

### Steps to Use in Microsoft Azure:

1. Upload the dataset (`engine_fuel_injector_failure.csv`) to your Azure workspace.
2. Split the data into training and test sets (e.g., 80/20 split).
3. Experiment with different models such as:
   - Linear Regression
   - Decision Trees
   - Random Forests
   - Neural Networks
4. Use evaluation metrics (such as MAE, RMSE) to measure model performance.
5. Test predictions by entering new CuNi contamination levels to get an estimate of the fuel injector's time until failure.

