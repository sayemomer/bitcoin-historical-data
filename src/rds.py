

class RDS:
    def __init__(self,client):
        self._client = client
        """ :type : pyboto3.rds """
    def create_postgresql_instance(self):
        print("Creating Amazon RDS instance...")
        self._client.create_db_instance()
