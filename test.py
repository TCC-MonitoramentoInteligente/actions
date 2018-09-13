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
       'Content-Type: text/html\n\n' \
       '{} \n\n' \
       '--NextPart\n' \
       'Content-Type: image/jpeg; name="event.jpeg";\n' \
       'Content-Disposition: attachment;\n' \
       'Content-Transfer-Encoding: base64;\n' \
       'filename="event.jpeg"\n\n' \
       '/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFhUXGBoaFxgYGBgaFxcYGBgXFxoXGBgaHSggGBolGxUYITEhJSkrLi4uGB8zODMtNygtLisBCgoKDg0OFxAQFysdFx0tLSsrKy0tLS0rLSstKystLS0tLS0tLTctKystLS03LS0tNzM4LTg2OCswKysrKzcrLf/AABEIAKgBLAMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAABAgADBAUGB//EAD4QAAEDAgIIBAUCBAUEAwAAAAEAAhEDITFBBAUSUWFxgZEGobHwEyIywdHh8RQzQnIjUlNikgcVQ9IWJaL/xAAZAQEBAQEBAQAAAAAAAAAAAAAAAQIDBAX/xAAiEQEBAQACAwACAgMAAAAAAAAAARECIQMSMRNRQWEiMkL/2gAMAwEAAhEDEQA/AA0Xy80HHigHXSunDHt6SviuawHcPMIgnD91W1p3pmA/5u6GnaIyn3vSPrDcecT6JnPgXdZV0ySZGCEPsmQb8jYRxU2ZuSZ4YJgzO887eaDHGT+iurpnVB0GMuQ2hwUnoFHE+4w7yoKw68cVfTqEPBJiOHRUCDHLFaGbwen6qwe90ukXUCZGzsyDvBAxsvCuY2SJwxJ4cIX0CtAoG1wzoLBfPXzJJGN75rr5P4b5K7E7QkjLIG+RzSPIaCSDa4nPcFdBIgkb/dlW4Q68k8rXwXJilvGXEASBMHyRYwziY5eSsg4wp8Mid+V1EOXDjh0QfEX9Pcqo5Ta3HdwQLpzvwm0funZp9q9gb8N2/ojzOKraDgM8ZHqg3mIGXXBCrnPmIw9OCrdcmLkduiJaQScuOHZSZVhqNNsEs8ITtdkAO+66jqZPLtf7hRAItEDrii0ZyDxKV5GFupUdOP2RTOwth68VC5oyCGyMzxwhIG7wTKob4mIRYOEhPs2wA9VI5TwsipNsISfFjLt6pi4T79VACcclEFhnDclcOHMym2CM+Z4JA0yVVFw3G25M53++OEoBhHvFAsacY6hD1CZOSU2waZ33hHik2jhJ95Jppi7M2Qa+bgYJXOib9cSiTODlERxOcZezCZzREXvmCo5wggfYJKbSLgBXV00C1zHPFAkTET1Re0Zg/bgeClNnCOUZKJE2xHX3dWNG9VbV8Z7I7JtMoLXTlHv1TMYdqfcclRPe8XV1EjaAxuOCs+rK+iV2kaO4f0hoAvMiBeMv0Xz97BJgyvoWs7aO7+3PovnVY3iQOC6+X7GuVJsgds/NLTeRi6eEeymFMjd+yL9x7Ab1yY0GCcirgBI38VS+mTyEZxKIaYy77lBaWcRw95qutzVZpZlwt3ujAyIVU4ccJHK8/olc6RIAtmkMTj+Pd0+1w+2fkggOZN+SRz5kA5Zb5TioDjGGWWX3SmqNrGD/AG/dAadO4NvJW4busqsc+wUgG33UTCOqCcvz3RNQnOE72CZF8598kgA6KiNcLx3UL5433lKbxYwOkotAaMybopmCMr80wJ3hLGeHPCeKUndBKiLQDiInkfypUqWvgqW45x+PtinMCLTbNAknHI70cMemPNEEnd6oB1oIk78kNXSZi3olDt8HmgRnvwwgd1G0wi7WZpNp99laxwF5Kh4E8bJWsO8RyuqqF0+4RcOI6BR/H7JWjKY5KIZr2gREz7yTVHDfG4CeGKSq8xbzus79q+PH1WpDHX1RozKlZrXuLWEnajGAJx3le0o6JodRpaynT2SYBwdz2pk8180oaQ5nzjaJFxOEZiEmj60rCuagYQ0i7QRs9jv6hdOHT2eHj4r47eVzlHY1zoPwazqU7WzccWmIJ7rG4wMHeWayadrKrVe6o8RJwGQFgOQCSkCczv4c1mx5K1B0G9oW3QwS9lgZcFkosxvPTLqtuhtJqMGHzC557lmfR9A1xV/wXi/0jAG8' \
       '--NextPart--'.format(SENDER, SENDER, body_html)

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
