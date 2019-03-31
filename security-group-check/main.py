import boto3,pprint
from config import conf

class Authentication:

    def __init__(self,profile):
        self.session = boto3.Session(profile_name=profile,region_name='us-west-1')
    def initializeService(self,service):
        self.client = self.session.client(service)
        return self.client

account_one = Authentication('default')
result = account_one.initializeService(conf['service']).describe_security_groups(GroupIds=['sg-928dd2e8'])
pprint.pprint(result)
