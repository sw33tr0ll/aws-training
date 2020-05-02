#!/usr/bin/env python3
import boto3
s3_client = boto3.client('s3')

# retrieve list of buckets
raw_response = s3_client.list_buckets()

# for each bucket in your list....
for bucket in raw_response['Buckets']:
    bucketName = bucket['Name']
    
    # grab (raw) information about the objects in that bucket
    raw_response = s3_client.list_objects_v2(Bucket=bucketName)
    
    # if the bucket has any objects, print the name of each object
    if raw_response['KeyCount']>0:
        print("Files for bucket: {}".format(bucketName))
        # for each object in the bucket
        for bucket_object in raw_response['Contents']:
            # print the name of the object
            print(bucket_object['Key'])
    else:
        print("No files found in bucket: {}".format(bucketName))
