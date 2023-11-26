import boto3
from botocore.exceptions import ClientError
import json

def lambda_handler(event, context):
    ses_client = boto3.client('ses')
    sender_email = "kg2982@columbia.edu"  # Replace with your verified sender email
    json_data = json.loads(event['Records'][0]['Sns']['Message'])
    recipient_email = json_data['recipient']
    subject = json_data['subject']
    body_text = json_data['body']

    try:
        response = ses_client.send_email(
            Destination={'ToAddresses': [recipient_email]},
            Message={
                'Body': {'Text': {'Data': body_text}},
                'Subject': {'Data': subject}
            },
            Source=sender_email,
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
