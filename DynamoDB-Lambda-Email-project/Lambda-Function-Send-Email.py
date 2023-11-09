import json
import boto3


client = boto3.client('ses', region_name='us-east-2')

sender = 'oliver.xc.liu@gmail.com'
recipient = 'oliverxcl9821@gmail.com'

# body_html = """<html>
# <head></head>
# <body>
#   <h1>Amazon SES Test (SDK for Python)</h1>
#   <p>This email was sent with
#     <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
#     <a href='https://aws.amazon.com/sdk-for-python/'>
#       AWS SDK for Python (Boto)</a>.</p>
# </body>
# </html>
#             """ 


# body_html = f"<html><head></head><body><h1>Amazon SES Test (SDK for Python)</h1><p>This email was sent with using the<a href='https://aws.amazon.com/sdk-for-python/'>AWS SDK for Python (Boto)</a>.</p></body></html>"  
            
            
# body_text = f"For dynamodb table {tablename}\r\n"
#             "There is a {action} update."
#             "The change is {data}."
             
# body_text = ("For dynamodb table {tablename}\r\n"
#              "There is a {action} update."
#              "The change is {data}."
#             )


def send_email(table_name, region, action, data):
    body_html = """\
    <html>
      <head>For dynamodb table {tablename}</head>
      <body>
            <h1>Schema Change Detected in {region}</h1><br>
            <br>
            <h2>There is a {action} update. </h2><br><br>
        <p><h1>Schema Change Detected in {region}</h1><br>
            <br>
            <h2>There is a {action} update. </h2><br><br>
            The change is {data}. <br><br>
        </p>
      </body>
    </html>
    """.format(tablename= table_name, region = region, action = action, data = data)
    charset = "UTF-8"
    subject = "Test email"
    
    response = client.send_email(
        Destination={
            'ToAddresses': [
                recipient
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': charset,
                    'Data': body_html,
                },
                # 'Text': {
                #     'Charset': charset,
                #     'Data': body_text,
                # },
            },
            'Subject': {
                'Charset': charset,
                'Data': subject,
            },
        },
        Source= sender,
        )
        
    print(response)


def get_table_name(str):
    L = []
    j = 0
    for i in str:
        if i == "/":
            L.append(j)
        j+=1
    tablename = str[L[0]+1 : L[1]]
    return tablename
    

def lambda_handler(event, context):

    print(f"event: {event}")
    
    for record in event['Records']:
        eventsource_ARN = record['eventSourceARN']
        table_name = get_table_name(eventsource_ARN)
        old_image = record["dynamodb"]["OldImage"]
        event_name = record["eventName"]
        region = record["awsRegion"]
        
        if event_name == "MODIFY":
            new_image = record["dynamodb"]["NewImage"]
            data = {"new_image": new_image, "old_image": old_image}
            
        if event_name == "REMOVE":
            data = {"old_image": old_image}
            
        send_email(table_name, region, event_name, data)
