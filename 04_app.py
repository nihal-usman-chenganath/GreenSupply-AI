import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Setup the Page
st.set_page_config(page_title="Green-Supply AI Dashboard", page_icon="🍃")
st.title("🍃 Green-Supply: Leaf Shelf Life Predictor")
st.write("This AI tool predicts the remaining shelf life of sustainable packaging materials based on transit and environment data.")

# 2. Load the trained model
model = joblib.load('leaf_model.pkl')

# 3. Create Sidebar for User Inputs
st.sidebar.header("Shipment Parameters")

def user_input_features():
    # We focus on Transit Days since it's our most important feature!
    transit = st.sidebar.slider('Transit Days', 1, 10, 3)
    temp = st.sidebar.slider('Average Temperature (°C)', 15, 45, 25)
    humidity = st.sidebar.slider('Humidity (%)', 30, 90, 60)
    storage = st.sidebar.selectbox('Storage Type', options=[0, 1], format_func=lambda x: 'Traditional (0)' if x == 0 else 'Controlled (1)')
    
    data = {'Avg_Temp_C': temp,
            'Humidity_Pct': humidity,
            'Storage_Type': storage,
            'Transit_Days': transit}
    return pd.DataFrame(data, index=[0])

df_input = user_input_features()

# 4. Display Inputs and Make Prediction
st.subheader("Shipment Details")
st.write(df_input)

prediction = model.predict(df_input)

# 5. Show the Result with dynamic color
st.subheader("Prediction Result")
days_left = round(prediction[0], 1)

if days_left > 15:
    st.success(f"Estimated Remaining Shelf Life: **{days_left} Days**")
elif days_left > 7:
    st.warning(f"Estimated Remaining Shelf Life: **{days_left} Days**")
else:
    st.error(f"Estimated Remaining Shelf Life: **{days_left} Days** (High Waste Risk!)")

st.info("💡 Insight: Transit Days was identified as the strongest predictor of decay in this model.")