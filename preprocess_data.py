# 
import pandas as pd

def preprocess_dataset(input_file: str, output_file: str):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Basic preprocessing: fill missing values, sort by timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')
    df.fillna(method='ffill', inplace=True)

    # Save the preprocessed data to a new file
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    input_file = "ec2_cpu_utilization.csv"
    output_file = "ec2_cpu_utilization_preprocessed.csv"
    preprocess_dataset(input_file, output_file)
