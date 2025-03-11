
import requests

def download_nab_dataset(url: str, output_file: str):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded dataset to {output_file}")
    else:
        print("Failed to download dataset.")

if __name__ == "__main__":
    # Example NAB data file URL
    url = "https://raw.githubusercontent.com/numenta/NAB/master/data/realAWSCloudwatch/ec2_cpu_utilization_5f5533.csv"
    output_file = "ec2_cpu_utilization.csv"
    download_nab_dataset(url, output_file)
