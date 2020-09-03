from dotenv import load_dotenv
load_dotenv()
import boto3
import botostubs
import os


class ClientFactory:
    def __init__(self,client):
        self._client = boto3.client(client,
                region_name=os.environ.get('Server_Region'),
                aws_access_key_id=os.environ.get("AWS_Access_Id"),
                aws_secret_access_key=os.environ.get("AWS_Access_Key"))
    
    def get_client(self):
        return self._client

class RDSClient(ClientFactory):
    def __init__(self):
        super().__init__('rds')

class EC2Client(ClientFactory):
    def __init__(self):
        super().__init__('ec2')