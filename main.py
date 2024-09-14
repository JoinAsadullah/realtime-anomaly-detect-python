import numpy as np
import time
import random
from collections import deque

# Data Generation Functions
def generate_normal_data(mean=50, standard_deviation=5):
    """Generate normal data following a Gaussian distribution."""
    return np.random.normal(mean, standard_deviation)

def generate_anomalous_data(mean=50, standard_deviation=5, anomaly_factor=3):
    """Generate anomalous data by amplifying or diminishing normal values."""
    return generate_normal_data(mean, standard_deviation) * anomaly_factor

def generate_data_stream(mean=50, standard_deviation=5, anomaly_probability=0.05, interval=1):
    """
    Generator that yields realtime data (normal or anomalous).
    
    mean= Mean of the normal data.
    standard_deviation= Standard deviation of the normal data.
    anomaly_probability= Probability of generating an anomaly.
    interval= Time interval (in seconds) between data points.

    """
    while True:
        if random.random() < anomaly_probability:
            data = generate_anomalous_data(mean, standard_deviation)
        else:
            data = generate_normal_data(mean, standard_deviation)
        
        yield data
        time.sleep(interval)


# Anomaly Detection Functions
def z_score(value, mean, standard_deviation):
    #Calculate the Z-Score of a value given the mean and standard deviation.

    if standard_deviation == 0:
        return 0  # Handle division by zero
    return (value - mean) / standard_deviation

def detect_anomalies(data_stream, window_size=50, z_threshold=3):
    """
    Detect anomalies in real-time using the Z-Score method.
    
    data_stream = A generator that provides real-time data.
    window_size = Size of the sliding window for calculating statistics.
    z_threshold = Z-Score threshold for detecting anomalies.

    """
    # Keep a sliding window of the last `window_size` data points
    data_window = deque(maxlen=window_size)
    
    for data in data_stream:
        # Add the data to the sliding window
        data_window.append(data)
        
        # Compute mean and standard deviation from the window
        if len(data_window) >= 2:  # Ensure we have enough data for meaningful statistics
            window_mean = np.mean(data_window)
            window_standard_deviation = np.std(data_window)
            
            # Calculate the Z-Score for the current data point
            z = z_score(data, window_mean, window_standard_deviation)
            
            # Detect anomalies if Z-Score exceeds the threshold
            if abs(z) > z_threshold:
                print(f"Anomaly detected! Data: {data}")
            else:
                print(f"Normal data: {data}")
        else:
            print(f"Collecting data: {data}")


# Main function to run the data generation and anomaly detection
if __name__ == "__main__":
    # Start the datastream generator
    data_stream = generate_data_stream(mean=50, standard_deviation=5, anomaly_probability=0.05, interval=2)
    
    # Start the realtime anomaly detection
    detect_anomalies(data_stream, window_size=50, z_threshold=3)
