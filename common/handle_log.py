"""
==========================
Author:sunk123
Time:2022-07-18 19:53
Company:力石科技有限公司
==========================
"""
import os
import logging
import datetime
from common.handle_conf import conf
from common.handle_path import LOG_DIR
def create_log(name='mylog', level='DEBUG', filename='log.log', sh_level='DEBUG', fh_level='DEBUG', format="%(asctime)s %(levelname)s %(message)s"):
    print('-------zzzz-----')
    # 第一步：创建日志收集器
    log = logging.getLogger(name)
    # 第二步： 设置日志的打印级别
    log.setLevel(level)
    # 第三步： 设置日志输出渠道
    #3.1 输出到文件的配置
    now = datetime.datetime.now()
    filename = os.path.join(LOG_DIR, now.strftime("%Y-%m-%d") + filename)
    print(filename+ '-------------------------')
    fh = logging.FileHandler(filename, encoding='utf-8')
    fh.setLevel(fh_level)
    log.addHandler(fh)

    #3.2 输出到控制台
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    log.addHandler(sh)

    # 第四步： 设置日志输出的格式
    # 4 设置日志输出的等级
    #创建格式对象
    formats = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_format = logging.Formatter(formats)
    # 为输出渠道设置输出格式
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    #返回一个日志收集器
    return log

my_log = create_log(
    name=conf.get('logging', 'name'),
    level=conf.get('logging', 'level'),
    filename=conf.get('logging', 'filename'),
    sh_level=conf.get('logging', 'sh_level'),
    fh_level=conf.get('logging', 'fh_level')
)