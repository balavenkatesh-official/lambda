import json
import boto3
import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

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
        
     mydb = mysql.connector.connect(host="database-1-instance-1.cx6lbzv1spei.us-east-1.rds.amazonaws.com",user="admin",password="mysql123",database="employeedb")
     mycursor = mydb.cursor()
     sql = "INSERT INTO employee (empid, empname, empaddress) VALUES (%s, %s, %s)"
     
     mycursor.executemany(sql, results)
     mydb.commit()
    
     print(mycursor.rowcount, "record inserted.")
        
     return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
   
