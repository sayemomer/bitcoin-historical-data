from src.client_factory import EC2Clinet
from src.ec2 import EC2

RDS_DB_SUBNET_NAME='my-rds-subnet-group'

class RDS:
    def __init__(self,client):
        self._client = client
        """ :type : pyboto3.rds """
    
    def create_postgresql_instance(self):

        security_group_id = self.create_db_security_group_and_add_rules()
        self.create_db_subnet_group()
        print("Creating Amazon RDS instance...")
        self._client.create_db_instance(
            DBName='MyPostgreSQLDB',
            DBInstanceIdentifier='mypostgresdb',
            DBInstanceClass='db.t2.micro',
            Engine='postgres',
            EngineVersion='9.6.6',
            Port=5432,
            MasterUserName='postgres',
            MasterPassword='mypostgres',
            AllocatedStorage=20,
            MultiAZ=False,
            StorageType='gp2',
            PubliclyAccessible=True,
            VpcSecurityGroupIds=[security_group_id],
            DBSubnetGroupName=RDS_DB_SUBNET_NAME,
            TAGS=[
                {
                    'key':'Name',
                    'Value':'Omer_postgre_SQL_instance'
                }
            ]
        )

    def create_db_security_group_and_add_rules(self):
        ec2_client = EC2Clinet().get_client()
        ec2 = EC2(ec2_client)
        security_group = ec2.create_security_group()
        security_group_id = security_group['GroupId']
        ec2.add_inbound_rule_to_sg(security_group_id)

        return security_group_id

    def create_db_subnet_group(self):
        self._client.create_db_subnet_group(
            DBSubnetGroupName=RDS_DB_SUBNET_NAME,
            SubnetIds=['subnet1','subnet2']
        )

