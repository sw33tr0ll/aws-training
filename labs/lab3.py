#!/usr/bin/env python3
import boto3
s3_client = boto3.client('s3')
bucketname = 'sweetroll-12942' # put your bucketname here

with open('test.txt','rb') as file_data:
	s3_client.upload_fileobj(file_data, bucketname, 'test.txt')
