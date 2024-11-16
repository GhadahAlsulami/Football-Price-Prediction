# Football Price Range Prediction

This project is a Machine Learning application built using FastAPI and Streamlit to predict the price range of football players based on certain features. The purpose of the project is to deploy a KNN (K-Nearest Neighbors) model and make it accessible via a web-based interface for user-friendly predictions.

## Project Overview

The application is divided into two main components:

1. **FastAPI Backend**:
   - **Description**: The backend is implemented using FastAPI, which provides a RESTful API for making predictions. The KNN model and a scaler are loaded to preprocess the input data and return the predicted price range.
   - **Deployment**: The FastAPI application is hosted on Render. The API accepts `POST` requests to the `/predict` endpoint with the input features and returns the prediction.
   - **Link**: [FastAPI on Render](https://football-price-prediction.onrender.com/predict)

2. **Streamlit Frontend**:
   - **Description**: The frontend is created with Streamlit, which provides a simple web interface for users to input player data and get predictions from the FastAPI backend.
   - **Deployment**: The Streamlit app is hosted on Streamlit Cloud and sends requests to the FastAPI backend for predictions.
   - **Link**: [Streamlit App](https://football-price-prediction.streamlit.app/)

## Features

- **User Inputs**: Users can input features such as:
  - Appearance
  - Minutes Played
  - Highest Value
- **API**: The FastAPI backend processes these features, scales them using the pre-trained scaler, and predicts the price range using the KNN model.
- **Price Range**: The predicted price range can be one of the following:
  - 0: Cheap Price
  - 1: Good Price
  - 2: High Price

## How It Works

1. **Input Data**: Users input the player features in the Streamlit web app.
2. **Data Processing**: The input data is sent to the FastAPI backend, where it is preprocessed and scaled.
3. **Prediction**: The KNN model makes a prediction, which is returned to the Streamlit app and displayed to the user.

## Requirements

- **Backend**: FastAPI, joblib, numpy
- **Frontend**: Streamlit, requests

## Links to the Deployed Application

- **Streamlit Frontend**: [Streamlit App](https://football-price-prediction.streamlit.app/)
- **FastAPI Backend**: [FastAPI on Render](https://football-price-prediction.onrender.com/predict)

## Setup and Running Locally

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd football-price-prediction
   
2.**Install the dependencies:**
   ```bash
    pip install -r requirements.txt

3. **Run the FastAPI server:**
   ```bash
    uvicorn main:app --reload

4. **Run the Streamlit app:**
   ```bash
    streamlit run App.py

## Enjoy using the Football Price Range Prediction app!
