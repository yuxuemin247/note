import importlib
import traceback

from lib.config.settings import settings

## 插件管理类
class PluginsManager():

    def __init__(self, hostname=None):

        self.pluginSettings = settings.PLUGINS_DICT
        self.mode = settings.MODE
        self.hostname = hostname
        self.debug = settings.DEBUG

        if self.mode == 'ssh':
            self.ssh_port = settings.SSH_PORT
            self.ssh_username = settings.SSH_USERNAME
            self.ssh_pwd = settings.SSH_PWD


    def execute(self):
        # 1. 获取配置
        # 2. 循环执行
        response = {}

        for k, v in self.pluginSettings.items():
            ret = {'code': 10000, 'data': None}
            try:
                # k: basic  v: src.plugins.basic.Basic
                module_name, class_name = v.rsplit('.', 1)
                ## 将字符串路径导入
                m = importlib.import_module(module_name)
                cls = getattr(m, class_name)

                res = cls().process(self.command, self.debug)

                ret['data'] = res

                response[k] = ret

            except Exception as e:
                ret['code'] = 10001
                ret['data'] = "[%s] 模式下的主机 [%s] 采集[%s]出错,出错信息是:[%s]" % (self.mode, self.hostname if self.hostname else 'agent', k, traceback.format_exc())
                response[k] = ret

        return response


    def command(self, cmd):

        if self.mode == 'agent':

            return self.__agent(cmd)
        elif self.mode == 'ssh':

            return self.__ssh(cmd)
        elif self.mode == 'salt':

            return self.__salt(cmd)
        else:
            return '只支持采集的模式为: agent/ssh/salt 模式'


    def __agent(self, cmd):
        import subprocess
        res = subprocess.getoutput(cmd)
        return res

    def __ssh(self, cmd):

        import paramiko

        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.hostname, port=self.ssh_port, username=self.ssh_username, password=self.ssh_pwd)
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()
        return result

    def __salt(self, cmd):

        import subprocess
        res_cmd = "salt '%s' cmd.run '%s'" % (self.hostname,cmd)
        res = subprocess.getoutput(res_cmd)
        return res



