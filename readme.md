nab_downloader.py:
This script fetches the NAB dataset from a specified URL and saves it locally. It can be used to download the data programmatically rather than manually obtaining it. Once downloaded, the dataset can be moved to your storage solution (e.g., an S3 bucket) for further processing.

preprocess_data.py:
A preprocessing utility designed to clean and organize the NAB data. It handles basic tasks like sorting the data by timestamp, filling in missing values, and outputting a cleaned version of the dataset. The goal is to ensure that the data is in a consistent and usable format before applying any anomaly detection logic.

anomaly_detection.py:
This script provides a simple anomaly detection mechanism using z-scores. It calculates how much a data point deviates from the mean and flags values that exceed a set threshold. It then returns a subset of the data containing the detected anomalies. It serves as a basic starting point for experimenting with detection logic.

notify_anomalies.py:
A notification script that sends alerts to an Amazon SNS topic when anomalies are identified. Using AWS’s boto3 library, it publishes a message to the SNS topic, ensuring that interested parties (e.g., team members, monitoring tools) are notified of any detected anomalies in real time.

CloudFormation Template:
This isn’t a Python script, but rather an infrastructure-as-code template in YAML format. It sets up the foundational AWS resources (S3 bucket, SNS topic, Lambda function, and IAM roles) required to run the above Python scripts. It enables the project to be deployed and managed in a standardized way on AWS.
