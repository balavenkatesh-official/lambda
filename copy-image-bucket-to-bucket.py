import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    print (event)
    
    for record in event['Records']:
        print (record)
        sourceBucket = record['s3']['bucket']['name']
        filename = record['s3']['object']['key']
        destinationBucket = sourceBucket + '-copied'
        copysource = {
            'Bucket' : sourceBucket , 
             'Key' : filename
    
        }
        
        s3.meta.client.copy(copysource, destinationBucket, filename)
        


    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

