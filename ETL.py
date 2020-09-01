from dotenv import load_dotenv
import os
import boto3
load_dotenv()

bucket_name = os.environ.get("Bucket_Name")

def build_bucket():
    s3 = boto3.client('s3',
                region_name=os.environ.get("Server_Region"),
                aws_access_key_id= os.environ.get("AWS_Access_Id"),
                aws_secret_access_key= os.environ.get("AWS_Access_Key"))

    response = s3.list_buckets()
    print(response)

    for bucket in response['Buckets']:
        if bucket_name in bucket['Name']:
            print(bucket['Name'])
        # else:
        #     response = s3.create_bucket(bucket_name)
        #     print('Bucket created')
    return s3

def transfer_file(connection):
    connection.upload_file(Bucket=bucket_name, 
               Filename='./bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', 
               Key='bitcoindata.csv')

    res = connection.head_object(Bucket='bitcoindata1', 
                       Key='bitcoindata.csv')
    # Print the size of the uploaded object
    print(res['ContentLength'])

def main():
    build_bucket()
    # transfer_file(connection)

if __name__ == "__main__":
    main()


