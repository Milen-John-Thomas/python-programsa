import boto3
from config import conf

class Authentication:

    def __init__(self,profile):
        self.session = boto3.Session(profile_name=profile)
    def initializeService(self,service):
        self.client = self.session.client(service)
        return self.client

account_one = Authentication('default')
result = account_one.initializeService(conf['service']).SecurityGroup('sg-928dd2e8')
print(result)
