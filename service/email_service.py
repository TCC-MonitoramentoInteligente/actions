import datetime

import boto3
from botocore.exceptions import ClientError

SENDER = "eventos.mia@outlook.com"
AWS_REGION = "us-east-1"
SUBJECT = "Alerta de evento"
CHARSET = "UTF-8"


def send_email(recipient, event, cam_id, cam_name, cam_address, frame64):
    body_html = """
    <html>
    <head></head>
    <body>
      <h1>Um evento foi detectado</h1>
      <p>O evento '{}' foi detectado em {}.</p>
      <table>
          <tr>
            <th colspan="2">Camera</th>
          </tr>
          <tr>
            <td>Identificação</td>
            <td>{}</td>
          </tr>
          <tr>
            <td>Nome</td>
            <td>{}</td>
          </tr>
          <tr>
            <td>Endereço</td>
            <td>{}</td>
          </tr>
    </table>
      <p>MIA</p>
    </body>
    </html>
                """.format(event,
                           datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
                           cam_id,
                           cam_name,
                           cam_address)

    data = 'From: {}\n' \
           'To: {}\n' \
           'Subject: {}\n' \
           'MIME-Version: 1.0\n' \
           'Content-type: Multipart/Mixed; boundary="NextPart"\n\n' \
           '--NextPart\n' \
           'Content-Type: text/html;charset=utf-8\n\n' \
           '{}\n\n' \
           '--NextPart\n' \
           'Content-Type: image/jpeg; name="event.jpeg";\n' \
           'Content-Disposition: attachment;\n' \
           'Content-Transfer-Encoding: base64;\n' \
           'filename="event.jpeg"\n\n' \
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
        )

    except ClientError as e:
        return e.response['Error']['Message']
    else:
        return "Email sent! Message ID: {}".format(response['ResponseMetadata']['RequestId'])
