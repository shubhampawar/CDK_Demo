import boto3
import os
s3 = boto3.client('s3')
def handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    try:
        print("[LambdaListenet] New file with name {} created in bucket {}".format(key, bucket_name))
        response = {'status': 'success', 'key': key}
        return response
    except Exception as e:
        print(e)
        print("[Error] :: Error processing file {} from bucket {}.   ".format(key, bucket_name))
        raise e