import pymysql

dbinfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'test',
}
sqls = ['select 1', 'select version()']
res = []


class ConnDB:
    def __init__(self, dbinfo, sqls):
        self.host = dbinfo['host']
        self.port = dbinfo['port']
        self.user = dbinfo['user']
        self.password = dbinfo['password']
        self.db = dbinfo['db']
        self.sqls = sqls

    def run(self):
        # 建立连接
        con = pymysql.connect(host=self.host, port=self.port, user=self.user,
                              password=self.password, db=self.db)
        # 游标建立的同时开启事务
        cur = con.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                res.append(cur.fetchone())
            # 关闭游标
            cur.close()
            # 事务提交，只涉及到查询，没有必要 commit。
            con.commit()
        except:
            # 回滚
            con.rollback()
        # 关闭数据库连接
        con.close()


if __name__ == '__main__':
    db = ConnDB(dbinfo, sqls)
    db.run()
    print(res)  # 由元组组成的列表
