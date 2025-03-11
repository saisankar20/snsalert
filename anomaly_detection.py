# 
import pandas as pd
import numpy as np

def detect_anomalies(input_file: str, threshold: float):
    # Load the preprocessed dataset
    df = pd.read_csv(input_file)

    # Compute the z-scores of the metric
    df['z_score'] = (df['value'] - df['value'].mean()) / df['value'].std()

    # Mark anomalies
    df['anomaly'] = df['z_score'].abs() > threshold

    # Return only the rows flagged as anomalies
    anomalies = df[df['anomaly']]
    return anomalies

if __name__ == "__main__":
    input_file = "ec2_cpu_utilization_preprocessed.csv"
    threshold = 3.0  # Adjust threshold as needed
    anomalies = detect_anomalies(input_file, threshold)
    print("Detected anomalies:")
    print(anomalies)
