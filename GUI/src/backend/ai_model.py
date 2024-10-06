from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(data):
    clf = IsolationForest(random_state=42)
    data_reshaped = np.array(data).reshape(-1, 1)
    clf.fit(data_reshaped)
    predictions = clf.predict(data_reshaped)
    return predictions

if __name__ == "__main__":
    # Simulating CPU, Memory, and Disk usage values
    system_data = [15, 30, 45, 60, 90, 85, 80, 75]
    anomalies = detect_anomalies(system_data)
    print(f"Anomaly Detection: {anomalies}")
