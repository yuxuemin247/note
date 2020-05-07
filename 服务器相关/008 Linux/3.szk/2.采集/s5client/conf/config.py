

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER = 'root'
PWD = '123'
MODE = 'agent' # ssh / salt

# SSH_PORT = 22
# SSH_USERNAME = 'root'
# SSH_PWD = '123'

DEBUG = True

PLUGINS_DICT = {
    'basic' : 'src.plugins.basic.Basic',
    'board' : 'src.plugins.board.Board',
    'cpu' : 'src.plugins.cpu.Cpu',
    'disk' : 'src.plugins.disk.Disk',
    'nic' : 'src.plugins.nic.Nic',
}

API_URL = 'http://127.0.0.1:8000/asset/'
