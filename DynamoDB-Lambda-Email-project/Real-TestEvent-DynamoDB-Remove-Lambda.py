import json

# real event obtained from lambda function log
event = {'Records': [
        {'eventID': '9ccb96e7da01f78a1a8fede64678907d', 'eventName': 'REMOVE', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-2', 'dynamodb': {'ApproximateCreationDateTime': 1699495203.0, 'Keys': {'StudentName': {'S': 'E L'
                    }, 'StudentID': {'S': '420'
                    }
                }, 'OldImage': {'State': {'S': 'NY'
                    }, 'StudentName': {'S': 'E L'
                    }, 'Age': {'S': '42'
                    }, 'StudentID': {'S': '420'
                    }
                }, 'SequenceNumber': '29948000000000020559246250', 'SizeBytes': 64, 'StreamViewType': 'NEW_AND_OLD_IMAGES'
            }, 'eventSourceARN': 'arn:aws:dynamodb:us-east-2: 823650347705:table/Student/stream/2023-11-02T17: 30: 58.123'
        }
        ]
        }

# convert python dictionary into json format for lambda test event
serialized_event = json.dumps(event)
print(serialized_event)
# paste output as real event to replace default test event
