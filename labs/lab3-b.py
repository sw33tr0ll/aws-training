#!/usr/bin/env python3
import boto3,argparse
s3_client = boto3.client('s3')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bucket", help="destination bucket name")
    parser.add_argument("-f", "--filename", help="file to upload")
    return parser.parse_args()

args = parse_args()
filename = args.filename
bucketname = args.bucket

with open(filename,'rb') as file_data:
	s3_client.upload_fileobj(file_data, bucketname, filename)
