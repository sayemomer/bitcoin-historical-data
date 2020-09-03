import boto3
import botostubs

class ClientFactory:
    def __init__(self,client):
        self._client = boto3.client(client,region_name='') # type: botostubs.rds  
    
    def get_client(self):
        return self._client

class RDSClient(ClientFactory):
    def __init__(self):
        super().__init__('rds')

class EC2Clinet(ClientFactory):
    def __init__(self):
        super().__init__('ec2')