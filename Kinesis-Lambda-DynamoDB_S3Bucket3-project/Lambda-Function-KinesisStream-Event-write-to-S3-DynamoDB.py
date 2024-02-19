import json
import base64
import boto3


# write to S3 bucket function
def send_to_s3(data, sequenceNumber):
    s3 = boto3.client('s3')   
    file_name = f'{sequenceNumber}.json'
    s3_path = 'kinesis_datastream_' + file_name
    # s3_path = 'kinesis_datastream/' + file_name ##建folder
    bucket = 'oliver-us-east-2-kinesislambda-assignment-dynamodb'
    response = s3.put_object(Bucket=bucket, Key=s3_path, Body=data)
    return response

# write to DynamoDB table function
def send_to_dynamodb(ID, Name, Age, State):
    dynamodb = boto3.client("dynamodb")
    response = dynamodb.put_item(
        TableName = "Student",
        Item = {
            'StudentID': {
                'S': ID
            },
            'StudentName': {
                'S': Name
            },
            'Age': {
                'S': Age
            },
            'State': {
                'S': State
            }
        }
        )
    return response
    
# lambda handler to process kinesis stream event
def lambda_handler(event, context):
    print(f"event: {event}")
    for record in event['Records']:
        encoded_data = record['kinesis']['data']
        # decode kinesis data stream event record into json format
        decoded_data = base64.b64decode(encoded_data)
        print(f"decoded_data: {decoded_data}")
        print(type(decoded_data))
        
        # view data in python dictionary format
        deserialized_data = json.loads(decoded_data)
        print(f"data: {deserialized_data}")
        print(type(deserialized_data))
        
        # write to S3 bucket
        sequence_number = record["kinesis"]["sequenceNumber"]
        result = send_to_s3(decoded_data, sequence_number)
        print(f"dump data to s3 bucket: {result}")
        
        # write to DynamoDB table
        ID = str(deserialized_data["ID"])
        Name = str(deserialized_data["Name"])
        Age = str(deserialized_data["Age"])
        State = str(deserialized_data["State"])
        response = send_to_dynamodb(ID, Name, Age, State)
        print(f"dump data to dynamoda table: {response}")
