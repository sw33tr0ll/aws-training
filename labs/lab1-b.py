#!/usr/bin/env python3
import boto3
iam_client = boto3.client('iam')
raw_response = iam_client.list_users()
print(raw_response)
