# The first four lines of code are the same. 
#!/usr/bin/env python3
import boto3
iam_client = boto3.client('iam')
raw_response = iam_client.list_users()
# Now, instead of printing the raw_response, we:
# grab the list of users from the raw response
user_list = raw_response['Users']
# then iterate through each user in the list
for user in user_list:
    # and print the user name of that user
    print(user['UserName'])
