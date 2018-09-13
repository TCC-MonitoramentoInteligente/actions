import boto3

SENDER = "jhonata.antunes@outlook.com"
AWS_REGION = "us-west-2"
SUBJECT = "Alerta de evento"
CHARSET = "UTF-8"

body_html = """
    <html>
    <head></head>
    <body>
      <h1>Um evento foi detectado</h1>
      <p>O evento X foi detectado às pela camera.</p>
      <p>MIA</p>
    </body>
    </html>
                """

data = 'From: {}\n' \
       'To: {}\n' \
       'Subject: Test email (contains an attachment)\n' \
       'MIME-Version: 1.0\n' \
       'Content-type: Multipart/Mixed; boundary="NextPart"\n\n' \
       '--NextPart\n' \
       'Content-Type: text/plain\n\n' \
       'This is the message body.\n\n' \
       '--NextPart\n' \
       'Content-Type: text/plain;\n' \
       'Content-Disposition: attachment; ' \
       'filename="attachment.txt"\n\n' \
       'This is the text in the attachment.\n\n' \
       '--NextPart--'.format(SENDER, SENDER)

print(data)

client = boto3.client('ses', region_name=AWS_REGION)

response = client.send_raw_email(
    Destinations=[
    ],
    FromArn='',
    RawMessage={
        'Data': data,
    },
)
