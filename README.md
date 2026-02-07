🍃 Green-Supply AI: Predictive Shelf Life for Raw leaf

📌 Project Overview :

This project addresses the critical issue of organic waste in the sustainable packaging industry (specifically focusing on areca and banana leaves). In high-heat climates like the UAE and complex logistics routes in south India(raw materials), rapid degradation of materials leads to significant financial loss.I developed an End-to-End Machine Learning Pipeline that predicts the remaining shelf life of these materials based on environmental and logistical factors, allowing for data-driven "First-Expired, First-Out" (FEFO) inventory management.

🚀 Key Features: 





    Synthetic Data Engineering: Generated a dataset of 1,500+ shipments with scientifically grounded correlations between heat, humidity, and organic decay.
    Predictive Modeling: Implemented a Random Forest Regressor to handle non-linear relationships in biological degradation.
    Feature Importance Analysis: Identified Transit Days as the primary driver of waste, providing actionable business intelligence for logistics optimization.
    Interactive Dashboard: Built a Streamlit web application for real-time "what-if" analysis by warehouse managers.
    
📊 Technical PerformanceModel: 

    Random Forest Regressor (n_estimators=100)
    R² Score: 0.92 (The model explains 92% of the variance in decay)
    MAE (Mean Absolute Error): 0.45 days (Predictions are accurate within ~11 hours)
    
🛠️ Tech Stack

    Language: Python
    Environment: Conda
    Libraries: Pandas, Scikit-Learn, Matplotlib, Seaborn, Joblib
    Deployment: Streamlit
    
📂 Project Structure

    01_data_generation.py: Script for creating the transactional dataset.
    02_data_analysis.ipynb: Exploratory Data Analysis (EDA) and visualization.
    03_model_training.ipynb: Model selection, training, and evaluation.
    04_app.py: The code for the interactive Streamlit dashboard.
    leaf_model.pkl: The serialized (saved) AI model.

https://github.com/user-attachments/assets/d4b795a4-fd95-4f37-812e-d80ee12e99cf
