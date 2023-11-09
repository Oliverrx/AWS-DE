# create kinesis stream
$ aws kinesis create-stream \
    --stream-name samplestream-test \
    --shard-count 1 

# delete kinesis stream
$ aws kinesis delete-stream \
    --stream-name samplestream-test
