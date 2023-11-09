import json

def lambda_handler(event, context):
    num1 = 1.5
    num2 = 6.3
    sum = num1 + num2
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
    print(f"event: {event}")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
