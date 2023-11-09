import time
import random
import json
import boto3

client = boto3.client("kinesis", region_name = "us-east-2")
stream_name = "Kinesis-Lambda-second-assignment"

try:
    while True:
        time.sleep(1)
        id = random.randint(1,1000)
        first_name = ("A","B","C","D","E","F","G")
        last_name = ("H","I","J","K","L","M","N")
        full_name = random.choice(first_name) + " " + random.choice(last_name)
        age = random.randint(1,100)
        state_list = ("OH","PA","NY","MA","GA","TX")
        state = random.choice(state_list)
        data = {
            "ID": id,
            "Name": full_name,
            "Age": age,
            "State": state
        }
        encode_data = bytes(json.dumps(data).encode("utf-8"))
        print(f"Sending: {data}")
        response = client.put_record(StreamName = stream_name, Data = encode_data, PartitionKey = "A")
        print(f"SequenceNumber is: {response['SequenceNumber']}")

except KeyboardInterrupt:
    print("Finished")
