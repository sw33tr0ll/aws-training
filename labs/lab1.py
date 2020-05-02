#!/usr/bin/env python3
import boto3
print(boto3.client('iam').list_users())
