import json
import os

import requests

from src.plugins import PluginsManager
from lib.config.settings import settings
from concurrent.futures import ThreadPoolExecutor
class Base():

    def post_data(self, info):

        ### {'content-type': 'application/json'}
        requests.post(settings.API_URL, data=json.dumps(info))
        # requests.post(settings.API_URL, json=(info))


class Agent(Base):

    def collect(self):
        info = PluginsManager().execute()

        hostname = info['basic']['data']['hostname']

        h = open(os.path.join(settings.BASEDIR,'conf/cert'), 'r', encoding='utf-8').read()

        if not h:
            with open(os.path.join(settings.BASEDIR,'conf/cert'), 'w', encoding='utf-8') as fp:
                fp.write(hostname)
        else:
            info['basic']['data']['hostname'] = h


        for k, v in info.items():

            print(k, v)

        self.post_data(info)


class SSHSalt(Base):

    def get_hosts(self):
        res = requests.get(settings.API_URL)
        hostlist = json.loads(res)
        return hostlist


    def run(self, hostname):
        info = PluginsManager(hostname=hostname).execute()
        self.post_data(info)

    def collect(self):

        host_list = self.get_hosts()
        p = ThreadPoolExecutor(10)

        for hostname in host_list:
            p.submit(self.run, hostname)





