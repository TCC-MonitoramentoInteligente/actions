import boto3
from botocore.exceptions import ClientError

SENDER = "Monitoramento Inteligente de Ambientes <jhonata.antunes@outlook.com>"
AWS_REGION = "us-west-2"
SUBJECT = "Alerta de evento"
CHARSET = "UTF-8"


def send_email(recipient, event, date, camera, frame64):
    body_html = """
    <html>
    <head></head>
    <body>
      <h1>Um evento foi detectado</h1>
      <p>O evento '{}' foi detectado às {} pela camera {}.</p>
      <p>MIA</p>
    </body>
    </html>
                """.format(event, date, camera)

    data = 'From: {}\n' \
           'To: {}\n' \
           'Subject: {}\n' \
           'MIME-Version: 1.0\n' \
           'Content-type: Multipart/Mixed;boundary="NextPart"\n\n' \
           '--NextPart\n' \
           'Content-Type: text/plain\n\n' \
           '{}\n\n' \
           '--NextPart\n' \
           'Content-Type: image/jpeg; name="photo.jpeg;\n' \
           'Content-Disposition: attachment;' \
           'filename="print.jpeg"\n\n' \
           '{}\n\n' \
           '--NextPart--'.format(SENDER, recipient, SUBJECT, body_html, frame64)

    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_raw_email(
            Destinations=[
            ],
            FromArn='',
            RawMessage={
                'Data': data
            },
            ReturnPathArn='',
            Source='',
            SourceArn='',
        )

    except ClientError as e:
        return e.response['Error']['Message']
    else:
        return "Email sent! Message ID: {}".format(response['ResponseMetadata']['RequestId'])
