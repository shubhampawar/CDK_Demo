import boto3
import os
import uuid
import json
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    # print(json.dump(event))
    id = str(uuid.uuid4())[:8]
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    try:
        print( "New file with name {} created in bucket {}".format(file_name, bucket_name))
        # response = {'status': 'success', 'key': key}
        table = dynamodb.Table('sample')
        response = table.put_item(Item={'id': 'bhagi','BucketName':bucket_name,'FileName':file_name})
        print(response)
        return response
    except Exception as e:
        print(e)
        print("Error processing file {} from bucket {}.   ".format(key, bucket_name))
        raise e
    return response