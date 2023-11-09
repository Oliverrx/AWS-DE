import time
from datetime import datetime
import json
import boto3

stream_name = "Kinesis-Lambda-second-assignment"

kinesis_client = boto3.client("kinesis", region_name = "us-east-2")

response = kinesis_client.describe_stream(StreamName = stream_name)

shard_id = response['StreamDescription']["Shards"][0]["ShardId"]

shard_iterator = kinesis_client.get_shard_iterator(
    StreamName = stream_name,
    ShardId = shard_id,
    ShardIteratorType = "LATEST"
)

kinesis_shard_iterator = shard_iterator["ShardIterator"]

record_response = kinesis_client.get_records(
    ShardIterator = kinesis_shard_iterator,
    Limit = 2 
)

while "NextShardIterator" in record_response:
    record_response = kinesis_client.get_records(
        ShardIterator = record_response["NextShardIterator"],
        Limit = 2)
        
    print(record_response)

    # wait for 1 seconds
    time.sleep(1)
