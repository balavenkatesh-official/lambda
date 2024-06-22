import boto3

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("FriendsDDB")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    Friends = data.split("\n")
    
    for friend in Friends:
        if friend.strip() == "":  # Skip empty lines
            continue
        
        print(friend)
        friend_data = friend.split(",")
        # add to dynamodb
        try:
            table.put_item(
                Item = {
                    "Id": friend_data[0],
                    "name": friend_data[1],
                    "Subject": friend_data[2]
                }
            )
        except Exception as e:
            print(f"Error adding item to DynamoDB: {e}")

    return {
        'statusCode': 200,
        'body': 'Data processed successfully'
    }
