# Fiber Optic Signal Loss Prediction (Machine Learning Project)

This project develops a **Machine Learning (ML)** model to analyze and predict **Signal Loss** in **Fiber Optic** cables. By utilizing a collected dataset, the model is trained to predict the signal attenuation based on various cable parameters and characteristics.

## 🌟 Key Features

* **Model Training:** Uses collected data to train a regression model for accurate signal loss prediction.
* **Data Generation/Preparation:** Includes a script for creating or preparing the initial project dataset.
* **Prediction:** Allows for predicting signal loss for new, unseen data using the saved, trained model (`signal_loss_model.pkl`).

## 🛠️ Project Structure

| File | Description |
| :--- | :--- |
| `fiber_optic_dataset.csv` | The dataset used for training and testing the ML model. |
| `create_dataset.py` | Script used to generate or preprocess the dataset. |
| `train_model.py` | The main script for training the Machine Learning model and saving it to disk. |
| `signal_loss_model.pkl` | The trained and saved prediction model. |
| `predict_model.py` | Script to load the trained model and perform predictions on new data. |
| `app.py` | Core file for running the full project, potentially serving as a simple application interface. |

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Installation of Dependencies

First, ensure you have all the necessary libraries installed. The primary requirements include libraries like `pandas` and `scikit-learn`.

```bash
pip install pandas scikit-learn
```

### 2.Training the Model

To train the model from scratch and save the output:

```bash
python train_model.py
```

### 3.Making Predictions

Once the model is trained and saved, you can use the following script to load it and make predictions:

```bash
python predict_model.py
```
