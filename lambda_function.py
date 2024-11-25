import json
import boto3
import datetime

def lambda_handler(event, context):
    data = json.loads(event.get("body", {}))
    print("############-Body")
    print(data)
    time = datetime.datetime.utcnow()
    name = data.get("name", '')
    email = data.get("email", '')
    phoneNumber = data.get("phoneNumber", '')
    interest = data.get("interest", '')
    message = data.get("message", '')
    subject = 'Contact Us Event from ' + email
    
    # print(context)
    # TODO implement
    client = boto3.client("ses")
    body = """
    <br>
    This is a notification from marchcroft.com contact us from.
    Contact Us From Received {} <br>
    Name: {} <br>
    Email: {} <br>
    Phone Number: {} <br>
    Interest: {} <br>
    Message: {} 
    """.format(time, name, email, phoneNumber, interest, message)
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(Source = "contactus@marchcroft.com", Destination = {"ToAddresses": ["contactus@marchcroft.com"]}, Message = message)
    return {
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

