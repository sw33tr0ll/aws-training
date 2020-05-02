#!/usr/bin/env python3
import boto3
ec2_client = boto3.client('ec2','us-east-2')
print(ec2_client.describe_instances())
