import json

import requests

from src.plugins import PluginsManager
from lib.config.settings import settings

class Base():

    def post_data(self, info):

        ### {'content-type': 'application/json'}
        requests.post(settings.API_URL, data=json.dumps(info))
        # requests.post(settings.API_URL, json=(info))


class Agent(Base):

    def collect(self):
        info = PluginsManager().execute()

        for k, v in info.items():
            print(k, v)

        self.post_data(info)


class SSHSalt(Base):

    def get_hosts(self):
        res = requests.get(settings.API_URL)
        hostlist = json.loads(res)
        return hostlist

    def collect(self):

        host_list = self.get_hosts()
        for hostname in host_list:
            info = PluginsManager(hostname=hostname).execute()
            self.post_data(info)



