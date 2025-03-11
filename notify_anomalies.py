 
import boto3

def send_sns_notification(topic_arn: str, message: str):
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn=topic_arn,
        Message=message
    )
    print(f"SNS notification sent: {response}")

if __name__ == "__main__":
    # Replace with your SNS topic ARN
    topic_arn = "arn:aws:sns:us-east-1:123456789012:AnomalyAlerts"
    message = "An anomaly has been detected in the dataset. Please investigate."
    send_sns_notification(topic_arn, message)
