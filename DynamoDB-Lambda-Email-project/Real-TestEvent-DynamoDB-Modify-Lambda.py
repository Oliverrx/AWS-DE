import json

# real event obtained from lambda function log
event = {'Records': [
        {'eventID': 'c9cf4c3a141df8ebc09ed1ab86a91745', 'eventName': 'MODIFY', 'eventVersion': '1.1', 'eventSource': 'aws:dynamodb', 'awsRegion': 'us-east-2', 'dynamodb': {'ApproximateCreationDateTime': 1699495551.0, 'Keys': {'StudentName': {'S': 'Molly'
                    }, 'StudentID': {'S': '420'
                    }
                }, 'NewImage': {'State': {'S': 'NY'
                    }, 'StudentName': {'S': 'Molly'
                    }, 'Age': {'S': '14'
                    }, 'StudentID': {'S': '420'
                    }
                }, 'OldImage': {'State': {'S': 'NY'
                    }, 'StudentName': {'S': 'Molly'
                    }, 'Age': {'S': '16'
                    }, 'StudentID': {'S': '420'
                    }
                }, 'SequenceNumber': '29948200000000020559383453', 'SizeBytes': 108, 'StreamViewType': 'NEW_AND_OLD_IMAGES'
            }, 'eventSourceARN': 'arn:aws:dynamodb:us-east-2: 823650347705:table/Student/stream/2023-11-02T17: 30: 58.123'
        }
        ]
        }

# convert python dictionary into json format for lambda test event
serialized_event = json.dumps(event)
print(serialized_event)
# paste output as real event to replace default test event
