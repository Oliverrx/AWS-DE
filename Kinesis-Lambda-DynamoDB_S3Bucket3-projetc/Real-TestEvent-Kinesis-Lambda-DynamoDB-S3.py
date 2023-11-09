import json

# real event obtained from lambda function log
event = {'Records': [
        {'kinesis': {
            'kinesisSchemaVersion': '1.0', 
            'partitionKey': 'A', 
            'sequenceNumber': '49646223481747896289875448346948126371606592563844218882', 
            'data': 'eyJJRCI6IDgwNCwgIk5hbWUiOiAiQyBMIiwgIkFnZSI6IDYsICJTdGF0ZSI6ICJNQSJ9', 
            'approximateArrivalTimestamp': 1699402991.875
            }, 
        'eventSource': 'aws:kinesis', 
        'eventVersion': '1.0', 
        'eventID': 'shardId-000000000000: 49646223481747896289875448346948126371606592563844218882', 
        'eventName': 'aws:kinesis:record', 
        'invokeIdentityArn': 'arn:aws:iam: : 823650347705:role/oliver-us-east-2-Kinesis-Lambda-DynamoDB-Role', 
        'awsRegion': 'us-east-2', 
        'eventSourceARN': 'arn:aws:kinesis:us-east-2: 823650347705:stream/Kinesis-Lambda-third-assignment'
        },
        {'kinesis': {
            'kinesisSchemaVersion': '1.0', 
            'partitionKey': 'A', 
            'sequenceNumber': '49646223481747896289875448346949335297426207261738401794', 
            'data': 'eyJJRCI6IDYxMSwgIk5hbWUiOiAiRCBKIiwgIkFnZSI6IDEsICJTdGF0ZSI6ICJOWSJ9', 
            'approximateArrivalTimestamp': 1699402992.946
            }, 
        'eventSource': 'aws:kinesis', 
        'eventVersion': '1.0', 
        'eventID': 'shardId-000000000000: 49646223481747896289875448346949335297426207261738401794', 
        'eventName': 'aws:kinesis:record', 
        'invokeIdentityArn': 'arn:aws:iam: : 823650347705:role/oliver-us-east-2-Kinesis-Lambda-DynamoDB-Role', 
        'awsRegion': 'us-east-2', 
        'eventSourceARN': 'arn:aws:kinesis:us-east-2: 823650347705:stream/Kinesis-Lambda-third-assignment'
        }
    ]
}

# convert python dictionary into json format for lambda test event
# write json files to dynamodb and s3
serialized_event = json.dumps(event)
print(serialized_event)
# paste output as real event to replace default test event
