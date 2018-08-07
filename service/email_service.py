import boto3
from botocore.exceptions import ClientError


SENDER = "Monitoramento Inteligente de Ambientes <sender@example.com>"
AWS_REGION = "us-west-2"
SUBJECT = "Alerta de evento"
CHARSET = "UTF-8"


def send_email(recipient, event, date, camera):
    body_text = "Um evento foi detectado\r\n" \
                "O evento {} foi detectado às {} pela camera {}.\r\n" \
                "MIA.".format(event, date, camera)

    body_html = """
    <html>
    <head></head>
    <body>
      <h1>Um evento foi detectado</h1>
      <p>O evento {} foi detectado às {} pela camera {}.</p>
      <p>MIA</p>
    </body>
    </html>
                """.format(event, date, camera)

    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        return e.response['Error']['Message']
    else:
        return "Email sent! Message ID: {}".format(response['ResponseMetadata']['RequestId'])
