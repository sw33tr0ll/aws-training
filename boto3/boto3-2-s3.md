# So, you wanna script some S3 buckets...
This code should look pretty familiar if you read [the last part of this tutorial](./boto3-1)

```
#!/usr/bin/env python3
import boto3
s3_client = boto3.client('s3')
raw_response = s3_client.list_buckets()
for bucket in raw_response['Buckets']:
    print(bucket['Name'])
```

The code above imports the boto3 library into a python script, creates an S3 client object, calls the AWS API for a list of buckets, and prints through the list. 
