
# local dictionary
$ cd /Users/xiaochengliu/Downloads

# create stack
$ aws cloudformation create-stack \
   --stack-name assignment-five-bucketpolicy-mapping-CLI-updated2 \
   --template-body file://assignment-five-bucketpolicy-mapping-updated1.json
   
# create bucket   
$ aws s3 mb s3://bucket-assignment-test1

# copy/write bucket object to local
$ aws s3 cp s3://oliver-us-east-2-second-assignment-bucketpolicy-test/test1.json test2.json

# copy/write local file to bucket object
$ aws s3 cp assignment-four-s3lambda-complete2.json s3://oliver-us-east-2-assignment-four-s3bucket-read-complete/read_object_for_test.json
$ aws s3 cp second-assignment-bucketpolicy-test.json s3://oliver-us-east-2-second-assignment-bucketpolicy-test/test1.json

# copy/write bucket object to other bucket object
$ aws s3 cp s3://oliver-us-east-2-second-assignment-bucketpolicy-test/test1.json s3://oliver-us-east-2-second-assignment-bucketpolicy-updated/test3.json


# create stack（+lambda role）
$ aws cloudformation create-stack \
  --stack-name assignment-four-s3lambda-CLI-complete2 \
  --template-body file://assignment-four-s3lambda-complete2.json \
  --capabilities CAPABILITY_NAMED_IAM
