import numpy as np
import time
import random
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data Generation Functions
def generate_normal_data(mean=50, std_dev=5):
    """Generate normal data following a Gaussian distribution."""
    return np.random.normal(mean, std_dev)

def generate_anomalous_data(mean=50, std_dev=5, anomaly_factor=3):
    """Generate anomalous data by amplifying or diminishing normal values."""
    return generate_normal_data(mean, std_dev) * anomaly_factor

def generate_data_stream(mean=50, std_dev=5, anomaly_probability=0.05, interval=1):
    """
    Generator that yields real-time data (normal or anomalous).
    
    :param mean: Mean of the normal data.
    :param std_dev: Standard deviation of the normal data.
    :param anomaly_probability: Probability of generating an anomaly.
    :param interval: Time interval (in seconds) between data points.
    """
    while True:
        if random.random() < anomaly_probability:
            data = generate_anomalous_data(mean, std_dev)
        else:
            data = generate_normal_data(mean, std_dev)
        
        yield data
        time.sleep(interval)


# Anomaly Detection Functions
def z_score(value, mean, std_dev):
    """Calculate the Z-Score of a value given the mean and standard deviation."""
    if std_dev == 0:
        return 0  # Handle division by zero
    return (value - mean) / std_dev

def detect_anomalies(data_stream, window_size=50, z_threshold=3):
    """
    Detect anomalies in real-time using the Z-Score method and plot data.
    
    :param data_stream: A generator that provides real-time data.
    :param window_size: Size of the sliding window for calculating statistics.
    :param z_threshold: Z-Score threshold for detecting anomalies.
    """
    # Keep a sliding window of the last `window_size` data points
    data_window = deque(maxlen=window_size)
    data_points = []  # List to store data points for plotting
    anomaly_points = []  # List to store anomalies for plotting
    timestamps = []  # List to store time (x-axis)

    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    ax.set_title('Real-Time Data Stream and Anomaly Detection')
    ax.set_xlabel('Time')
    ax.set_ylabel('Data Value')

    # Function to update the plot
    def update(frame):
        nonlocal data_window

        # Get new data from the stream
        data = next(data_stream)
        data_window.append(data)
        data_points.append(data)
        timestamps.append(len(data_points))

        # Compute mean and standard deviation from the window
        if len(data_window) >= 2:
            window_mean = np.mean(data_window)
            window_std_dev = np.std(data_window)
            
            # Calculate the Z-Score for the current data point
            z = z_score(data, window_mean, window_std_dev)
            
            # Detect anomalies if Z-Score exceeds the threshold
            if abs(z) > z_threshold:
                print(f"Anomaly detected! Data: {data}, Z-Score: {z:.2f}, Mean: {window_mean:.2f}, Std Dev: {window_std_dev:.2f}")
                anomaly_points.append((len(data_points), data))  # Store anomaly (time, value)
            else:
                print(f"Normal data: {data}, Z-Score: {z:.2f}, Mean: {window_mean:.2f}, Std Dev: {window_std_dev:.2f}")

        # Clear the previous plot
        ax.clear()

        # Plot normal data points
        ax.plot(timestamps, data_points, label='Data Stream', color='blue')

        # Plot anomalies in red
        if anomaly_points:
            anomaly_times, anomaly_values = zip(*anomaly_points)
            ax.scatter(anomaly_times, anomaly_values, color='red', label='Anomalies')

        # Set plot labels and limits
        ax.set_xlim(max(0, len(data_points) - window_size), len(data_points) + 10)
        ax.set_ylim(min(data_points) - 5, max(data_points) + 5)
        ax.legend()

    # Create an animation that updates the plot in real time
    ani = FuncAnimation(fig, update, interval=200)

    # Show the plot
    plt.show()

# Main function to run the data generation, anomaly detection, and visualization
if __name__ == "__main__":
    # Start the data stream generator
    data_stream = generate_data_stream(mean=50, std_dev=5, anomaly_probability=0.05, interval=.2)
    
    # Start the real-time anomaly detection with visualization
    detect_anomalies(data_stream, window_size=50, z_threshold=3)
