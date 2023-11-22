import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    ses_client = boto3.client('ses')
    sender_email = "mh4039@columbia.edu"  # Replace with your verified sender email
    recipient_email = event['recipient']
    subject = event['subject']
    body_text = event['body']

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