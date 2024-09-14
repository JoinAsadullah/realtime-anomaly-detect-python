# Anomaly Detection Project Documentation

## Project Overview

This project implements a real-time anomaly detection system. The key objectives were to simulate a data stream with seasonal patterns and noise, detect anomalies as the data is streamed, optimize the algorithm for efficiency, and visualize the data and anomalies in real time.

### Objectives

1. **Algorithm Selection**: We implemented the **Z-Score** method for anomaly detection. The Z-Score allows us to detect anomalies by comparing each new data point to the statistical properties (mean, standard deviation) of the data stream. The algorithm adapts to changes in data distribution and can handle seasonal variations and random noise.
    
2. **Data Stream Simulation**: A function was designed to simulate real-time data with regular patterns, seasonal elements, and random noise. The simulation generates both normal and anomalous data points, ensuring that the detection algorithm has a realistic stream to process.
    
3. **Anomaly Detection**: The Z-Score method was employed for real-time anomaly detection. A sliding window mechanism was used to calculate the mean and standard deviation dynamically. Data points with Z-Scores above a certain threshold were flagged as anomalies.
    
4. **Optimization**: The algorithm was optimized for speed and efficiency by using a sliding window (`deque`) to store recent data points. This approach ensures that the calculations for mean and standard deviation remain computationally light.
    
5. **Visualization**: A real-time visualization tool was developed using `matplotlib`. The tool dynamically updates the plot with the data stream and highlights anomalies in a different color, providing clear feedback on the system’s performance.
    

## Requirements

- **Python Version**: The project was implemented using Python 3.x.
- **External Libraries**:
    - `numpy`: For mathematical operations like mean and standard deviation.
    - `matplotlib`: For real-time visualization of the data stream and detected anomalies.
    - `collections.deque`: For implementing the sliding window.

A `requirements.txt` file is provided to easily install necessary dependencies.

## Key Sections

### Algorithm Selection

We chose the **Z-Score** method for its simplicity and effectiveness in real-time anomaly detection. Z-Scores allow us to detect how many standard deviations a data point is from the mean, making it a reliable way to identify anomalies.

### Data Stream Simulation

The data stream simulation generates normal data points based on a Gaussian distribution. Anomalous data points are introduced with a small probability to test the detection mechanism. This ensures a balanced mix of regular and anomalous data for effective anomaly detection.

### Real-Time Anomaly Detection

- A sliding window stores the most recent data points.
- For each new data point, the mean and standard deviation of the sliding window are calculated.
- The Z-Score for the new data point is computed. If the Z-Score exceeds a pre-defined threshold (e.g., `|z| > 3`), the point is flagged as an anomaly.

### Optimization

The sliding window (`deque`) approach ensures that the algorithm only needs to store a fixed number of recent data points, optimizing both memory and CPU usage. This prevents the system from becoming sluggish over time, even with a large data stream.

### Visualization

We used `matplotlib` to visualize the data stream and anomalies. Normal data points are plotted in blue, while anomalies are highlighted in red. The plot is updated dynamically using `FuncAnimation` to simulate real-time feedback.

## Error Handling and Validation

The system includes robust error handling for edge cases, such as division by zero when calculating the Z-Score and handling cases where the sliding window has insufficient data points.

## Conclusion

This project successfully implements a real-time anomaly detection system that is both efficient and easy to understand. The Z-Score method, combined with sliding window optimizations and real-time visualization, provides a powerful tool for detecting anomalies in continuous data streams.

## Files Included

- `main.py`: The main script that includes data stream generation, anomaly detection, and visualization.
- `requirements.txt`: A file containing the necessary dependencies.

## How to Run

1. Install the required libraries:

    `pip install -r requirements.txt`
    
2. Run the script:
    
    `python main.py`
    

The system will start streaming data and detecting anomalies in real-time, with a live plot displaying the results.