import json
import base64
import boto3
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_username = "oliverxcl9821@gmail.com"
smtp_password = "umjoordgvtrapwml"
send_to = "oliver.xc.liu@gmail.com"
send_from = "oliverxcl9821@gmail.com"
send_message = "hello smtp"

def smtp_send_email(res, acc, reg, db, tb, ch):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Cross Account Same Region Schema Change Detected"
    msg["From"] = send_from
    msg["To"] = send_to
    
    body_html = """\
    <html>
      <head><h1>Cross Account Same Region Schema Change Detected</h1></head>
      <body>
        <p>
            <br>
            Resource is: {resource}. <br><br>
            Account is: {account}. <<br><br>
            Region is: {region}. <br><br>
            Database is: {database}. <br><br>
            Table is: {table}. <br><br>
            Change is: {change}. <br><br>
        </p>
      </body>
    </html>
    """.format(resource = res, account = acc, region = reg, database = db, table = tb, change = ch)
    
    bodypart = MIMEText(body_html, "html")
    msg.attach(bodypart)
    
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(smtp_username, smtp_password)
    server.sendmail(send_from, send_to, msg.as_string())
    server.quit()


def send_to_sns(msg):
    client = boto3.client("sns")
    snsArn = "arn:aws:sns:us-east-2:477953174433:send_Email_SNS_topic"
    
    response = client.publish(
        TopicArn = snsArn,
        Message = msg,
        Subject = "Cross Account Same Region Schema Change Detected"
        )


def lambda_handler(event, context):
    print(f"body: {event}")
    
    for Record in event['Records']:
        body = Record["body"]
        deserialized_body = json.loads(body)
        message = deserialized_body["Message"]
        deserialized_message = json.loads(message)
        resource = deserialized_message["resources"][0]
        account = deserialized_message["account"]
        region = deserialized_message["region"]
        detail = deserialized_message["detail"]
        database = deserialized_message["detail"]["databaseName"]
        table = deserialized_message["detail"]["tableName"]
        change = deserialized_message["detail"]["typeOfChange"]
        
        smtp_send_email(resource, account, region, database, table, change)
        send_to_sns(change)
