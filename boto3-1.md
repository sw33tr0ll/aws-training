---
layout: default
---

# Prerequisites
This article makes a few assumptions. First, that you understand the basics of Amazon Web Services (AWS) and have hands-on experience with some key services. Second, that you have some basic experience developing scripts in Python or another language. Last, you will need to install python3 and pip. 

# What is Boto3?
[Boto3](https://aws.amazon.com/sdk-for-python/) is an extensive python library for AWS. It allows you to script the management of an AWS cloud environment and has some incredible documentation [here](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). You will need to reference these documents often, so keep them handy!

# Getting started
There are multiple ways to install the boto3 library. Let's use pip!
```
pip3 install --user boto3
```
Boto3 also requires valid API keys to get started. If you've already set up the AWS CLI with _aws configure_ then you should be good to go. Otherwise, check out the guide [here](./cli-1.md)

Here is an example of how you might use boto3 to list [IAM](./iam-1.md) users.
```
#!/usr/bin/env python3
import boto3
print(boto3.client('iam').list_users())
```

##Yadda yadda github link to lab 1, next lab, next page, iam page, cli page

![Example](./images/aws-logo.png)

