import json
import boto3
import csv

s3 = boto3.client('s3')
def lambda_handler(event, context):
#        print(event)
        
     bucketname = event['Records'][0]['s3']['bucket']['name']
     csvfile = event['Records'][0]['s3']['object']['key']
     csvfilevalues = s3.get_object(Bucket=bucketname, Key=csvfile)
     lines = csvfilevalues['Body'].read().decode('utf-8').split()
        
     results=[]
        
     for row in csv.DictReader(lines):
        results.append(row.values())
        
     print(results)
        
        
     return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
   
