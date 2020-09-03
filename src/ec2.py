RDS_SECURITY_GROUP = 'rds_public_sg'
RDS_VPC_ID=''

class EC2:
    def __init__(self,client):
        self._client = client
    
    def create_security_group(self):
        return self._client.create_security_group(
            GroupName=RDS_SECURITY_GROUP,
            Description='RDS security group for public access',
            VpcId=RDS_VPC_ID
        )
    def add_inbound_rule_to_sg(self,security_group_id):
        self._client.authorize_security_group_ingress(
            GroupID=security_group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 5432,
                    'ToPort':5432,
                    'IpRanges':[{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
