import pymysql


class DB:
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor()

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with DB(user='root', passwd='123456', db='test') as db:
        try:
            db.execute('insert scores into values (55, 3);')
            print(type(db.conn))
            # # 提交数据库并执行
            # db.conn.commit()
        except:
            db.conn.rollback()
            # print('错误')
            # print(db.fetchall())

        # 正常执行可以这样写，若错误执行，还是要写异常执行。


        # cursor 对象也可以直接循环
        # for i in db:
        #     print(i)

