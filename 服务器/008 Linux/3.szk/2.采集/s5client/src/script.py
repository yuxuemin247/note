

from src.client import SSHSalt, Agent
from lib.config.settings import settings

def run():
    mode = settings.MODE

    if mode == 'agent':
        obj = Agent()
    else:
        obj = SSHSalt()

    obj.collect()
