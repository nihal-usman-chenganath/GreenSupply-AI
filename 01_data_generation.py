import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

def generate_organic_decay_data(samples=2000):
    data = []
    for _ in range(samples):
        # 1. Input Features (The "Causes")
        temp = np.random.uniform(18, 48)            # Celsius (Kerala to UAE range)
        humidity = np.random.uniform(20, 95)        # Percentage
        storage_condition = np.random.choice([0, 1]) # 0: Traditional, 1: Controlled/Sealed
        transit_duration = np.random.uniform(0.5, 7) # Days from harvest to warehouse
        
        # 2. The Decay Formula (Biological Heuristics)
        # We start with a max shelf life of 30 days for ideal conditions
        base_life = 30.0
        
        # Apply penalties based on physical laws:
        # Temperature: Penalty increases exponentially as it gets hotter
        temp_penalty = 0.05 * np.exp(0.08 * (temp - 20)) 
        
        # Humidity: Extreme high (>85%) or extreme low (<30%) reduces life
        hum_penalty = 0.02 * abs(humidity - 50)
        
        # Storage: Controlled storage adds 4 days of stability
        storage_bonus = 4.0 if storage_condition == 1 else 0.0
        
        # 3. Calculate Target: Remaining Shelf Life (RSL)
        rsl = base_life - temp_penalty - hum_penalty + storage_bonus - (transit_duration * 1.5)
        
        # Add "Real-world Noise" (unpredictable biological variance)
        rsl += np.random.normal(0, 0.5)
        
        # Ensure values stay within realistic bounds
        rsl = max(0, min(30, round(rsl, 2)))
        
        data.append([temp, humidity, storage_condition, transit_duration, rsl])

    columns = ['Avg_Temp_C', 'Humidity_Pct', 'Storage_Type', 'Transit_Days', 'Remaining_Shelf_Life']
    return pd.DataFrame(data, columns=columns)

# Generate and Save
df = generate_organic_decay_data()
df.to_csv('leaf_shelf_life_data.csv', index=False)
print("Project Step 1 Complete: Dataset 'leaf_shelf_life_data.csv' created.")
print(df.head())