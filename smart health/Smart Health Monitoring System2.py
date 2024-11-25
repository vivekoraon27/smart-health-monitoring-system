import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

Function to generate synthetic heart rate data
def generate_synthetic_heart_rate_data(num_points=100):
    # Generate timestamps
    start_time = datetime.datetime.now()
    time_stamps = [start_time + datetime.timedelta(seconds=i * 10) for i in range(num_points)]

    # Generate synthetic heart rates (normal range 60-100 bpm)
    heart_rates = np.random.randint(60, 100, size=num_points)

    # Create a DataFrame
    data = pd.DataFrame({
        'Timestamp': time_stamps,
        'Heart Rate': heart_rates
    })

    return data

Generate synthetic data
num_data_points = 200
heart_rate_data = generate_synthetic_heart_rate_data(num_data_points)

Plotting the heart rate data
plt.figure(figsize=(12, 6))
plt.plot(heart_rate_data['Timestamp'], heart_rate_data['Heart Rate'], marker='o', linestyle='-', color='b')
plt.title('Synthetic Heart Rate Monitoring')
plt.xlabel('Time')
plt.ylabel('Heart Rate (bpm)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()