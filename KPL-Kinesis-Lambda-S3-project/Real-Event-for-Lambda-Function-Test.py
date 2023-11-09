import json

# real event obtained from lambda function log
event = { 
    'Records': [
        { 'kinesis': { 
            'kinesisSchemaVersion': '1.0', 
            'partitionKey': 'A', 
            'sequenceNumber': '49645845095191784933439131728620421857206050072899354626', 
            'data': 'eyJJRCI6IDE2NiwgIk5hbWUiOiAiQiBIIiwgIkFnZSI6IDU4LCAiU3RhdGUiOiAiVFgifQ==', 
            'approximateArrivalTimestamp': 1698346534.069 
            }, 
        'eventSource': 'aws:kinesis', 
        'eventVersion': '1.0', 
        'eventID': 'shardId-000000000000:49645845095191784933439131728620421857206050072899354626', 
        'eventName': 'aws:kinesis:record', 
        'invokeIdentityArn': 'arn:aws:iam::823650347705:role/oliver-us-east-2-Kinesis-Lambda-Role', 
        'awsRegion': 'us-east-2', 
        'eventSourceARN': 'arn:aws:kinesis:us-east-2:823650347705:stream/Kinesis-Lambda-second-assignment' 
        }, 
        { 'kinesis': { 
            'kinesisSchemaVersion': '1.0', 
            'partitionKey': 'A', 
            'sequenceNumber': '49645845095191784933439131728621630783025664770793537538', 
            'data': 'eyJJRCI6IDgxNCwgIk5hbWUiOiAiRCBOIiwgIkFnZSI6IDExLCAiU3RhdGUiOiAiT0gifQ==', 
            'approximateArrivalTimestamp': 1698346535.155 
            }, 
        'eventSource': 'aws:kinesis', 
        'eventVersion': '1.0', 
        'eventID': 'shardId-000000000000:49645845095191784933439131728621630783025664770793537538', 
        'eventName': 'aws:kinesis:record', 
        'invokeIdentityArn': 'arn:aws:iam::823650347705:role/oliver-us-east-2-Kinesis-Lambda-Role', 
        'awsRegion': 'us-east-2', 
        'eventSourceARN': 'arn:aws:kinesis:us-east-2:823650347705:stream/Kinesis-Lambda-second-assignment' 
        }
        ] 
    }
# convert python dictionary into json format for lambda test event
# write json files to S3 bucket
serialized_event = json.dumps(event)
print(serialized_event)
# paste output as real event to replace default test event
