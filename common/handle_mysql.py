"""
==========================
Author:sunk123
Time:2022-07-21 18:48
Company:力石科技有限公司
==========================
"""
import pymysql
from common.handle_conf import conf


class HandleDB(object):

    def __init__(self):
        # 1 连接数据库
        self.con = pymysql.connect(
            host=conf.get("mysql", 'host'),
            port=conf.getint("mysql", 'port'),
            user=conf.get("mysql", 'user'),
            database=conf.get("mysql", 'database'),
            password=conf.get("mysql", 'password'),
            # autocommit=True,  # 自动二次确认
            charset='utf8'
        )
        #创建字段型游标（返回的数据是字典类型）
        self.dbcur = self.con.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        return self.dbcur

    def __exit__(self, exc_type, exc_val, exc_tb):
        #提交事务
        self.con.commit()
        #关闭游标
        self.dbcur.close()
        #关闭数据库连接
        self.con.close()

class MysqlCurd(object):
    def find_one(self, sql):
        with HandleDB() as db:
            db.execute(sql)
            res = db.fetchone()
            print(res)
            return res

    def find_all(self, sql):
        with HandleDB() as db:
            db.execute(sql)
            res = db.fetchall()
            print(res)
            return res

    def find_count(self, sql):
        with HandleDB() as db:
            res = db.execute(sql)
            print(res)
            return res

    def __del__(self):
        pass


if __name__ == '__main__':
    sql = "SELECT * from member limit 5;"
    db = MysqlCurd()
    res = db.find_one(sql)
    print(res)
