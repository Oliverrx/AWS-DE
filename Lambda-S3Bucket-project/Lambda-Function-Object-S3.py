import json
import boto3a

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    # read object from bucket 
    response = s3_client.get_object(
        Bucket='oliver-us-east-2-assignment-four-s3bucket-read-complete',
        Key='read_object_for_test.json'
        )
    print(response["Body"].read())
 
    
    # read object from bucket
    read_bucket = "oliver-us-east-2-assignment-four-s3bucket-read-complete"
    write_bucket = "oliver-us-east-2-assignment-four-s3bucket-write-complete"

    object_key = "read_object_for_test.json"
    content = s3_client.get_object(
        Bucket = read_bucket, Key = object_key)["Body"].read()
    print(content)
  
    
    # write object to bucket-test1_s3 client？
    response0 = s3_client.put_object(
        Body = 'read_object_for_test.json',
        Bucket ='oliver-us-east-2-assignment-four-s3bucket-write-complete',
        Key ='write_object_for_test1.json'
        )
    
    response1 = s3_client.put_object(
        Body = content,
        Bucket ='oliver-us-east-2-assignment-four-s3bucket-write-complete',
        Key ='write_object_for_test8.json'
        )
        
    response2 = s3_client.put_object(
        Body = 's3://oliver-us-east-2-assignment-four-s3bucket-read-complete/read_object_for_test.json',
        Bucket ='oliver-us-east-2-assignment-four-s3bucket-write-complete',
        Key ='write_object_for_test0.json'
        )


    # write object to bucket-test2_s3 resource    
    string = "hello, world"
    encoded_string = string.encode("utf-8")
    file = "write_object_for_test2.txt"
    path = file
    
    s3_resource = boto3.resource("s3")
    s3_resource.Bucket(write_bucket).put_object(Key=path, Body=encoded_string)
    
    
    # write object to bucket-test3
    some_binary_data = b'Here we have some data'
    more_binary_data = b'Here we have some more data'

    # Method 1: Object.put()
    s3 = boto3.resource('s3')
    object = s3.Object('oliver-us-east-2-assignment-four-s3bucket-write-complete', 'write_object_for_test3.txt')
    object.put(Body=some_binary_data)

    # Method 2: Client.put_object()
    client = boto3.client('s3')
    client.put_object(
        Body=more_binary_data, 
        Bucket='oliver-us-east-2-assignment-four-s3bucket-write-complete', 
        Key='write_object_for_test4.txt'
        )



    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
