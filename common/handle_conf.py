"""
==========================
Author:sunk123
Time:2022-07-18 19:14
Company:力石科技有限公司
==========================
"""
import configparser
import os
from common.handle_path import CONF_DIR


class Config(configparser.ConfigParser):
    """在创建对象时，直接加载配置文件中的内容"""
    def __init__(self, conf_file):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.read(conf_file, encoding='utf-8')
        self.config_path = os.path.join(CONF_DIR, 'config.ini')

    def get_config(self, title, key):
        """
        配置文件读取
        :data self:
        :data title:
        :data value:
        :return:
        """
        return self.config.get(title, key)

    def set_config(self, title, key, value):
        """
        配置文件更新
        :data self:
        :data title:
        :data value:
        :data text:
        :return:
        """
        self.config.set(title, key, value)
        with open(self.config_path, 'w') as f:
            return self.config.write(f)

    def add_config(self, title):
        """
        配置文件title添加
        :data title:
        :return:
        """
        self.config.add_section(title)
        with open(self.config_path, 'w') as f:
            return self.config.write(f)


conf = Config(os.path.join(CONF_DIR, 'config.ini'))

# if __name__ == '__main__':
#     #配置文件路径 从文件中读取配置信息
#     config = Config(os.path.join(CONF_DIR, 'config.ini'))
#     #获取所有的节点
#     print(config.sections())
#     #获取节点中的value,config[节点名][key]
#     print(config["default"]["forwardX11"])
#     print(config.get('logging', 'name'))