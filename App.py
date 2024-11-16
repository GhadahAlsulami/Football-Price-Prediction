import streamlit as st
import requests

# Set up the Streamlit app
st.title("Football Price Range Prediction")

# User inputs for the features defined in main.py
appearance = st.number_input("Appearance", min_value=0, max_value=100, value=30)
minutes_played = st.number_input("Minutes Played", min_value=0, max_value=10000, value=2000)
highest_value = st.number_input("Highest Value", min_value=0, max_value=50000000, value=5000000)

# Prediction button
if st.button("Predict Price Range"):
    # API request URL
    url = "https://football-price-prediction.onrender.com/predict"  # Use your deployed URL

    # Data for the POST request
    data = {
        "appearance": appearance,
        "minutes_played": minutes_played,
        "highest_value": highest_value
    }

    # Send the POST request
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for request errors

        # Check if 'prediction' exists in the response JSON
        if "prediction" in response.json():
            prediction = response.json()["prediction"]
            # Interpret the prediction
            price_range = {0: "Cheap Price", 1: "Good Price", 2: "High Price"}
            st.write(f"Estimated Price Range: {price_range.get(prediction, 'Unknown Price Range')}")
        else:
            st.error("Prediction not found in API response.")
    except requests.exceptions.RequestException as e:
        st.error("Error requesting prediction from API. Please try again.")
        st.write(e)
    except KeyError as e:
        st.error("Unexpected response format.")
        st.write(f"Error: {e}")
