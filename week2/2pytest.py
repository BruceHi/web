import pymysql

# 连接 --> 游标 -> 操作 (提交)--> 关闭游标 --> 关闭连接
conn = pymysql.connect(host='localhost', user='root', password='123456',
                       database='test', charset='utf8mb4')  # 特别注意该字符集，标准的 mysql 字符集
cur = conn.cursor()

# sql = 'select * from scores where Score = %s'
# cur.execute(sql, 4)  # execute 第二个参数列表（元组），还可以作为值来拼接 sql，必须是字符串类型。
#
# # print(cur)  # pymysql.cursors.Cursor 对象
# print(cur.fetchall())

# # # 插入一条数据
sql = 'insert into scores values (%s, %s)'
count = cur.execute(sql, ['50', '2.3'])
conn.commit()
print(cur.fetchall())
# print(count)
#
# # 插入多条数据
# sql = 'insert into scores values (%s, %s)'
# data = [
#     [11, 5],
#     [12, 3.6],
#     [13, 4.5]
# ]
# # (str, list) -> int
# count = cur.executemany(sql, data)
# print(count)
# sql = 'insert into scores values (4);'
# try:
#     cur.execute(sql)
#     conn.commit()
# except:
#     conn.rollback()


# # 在游标关闭之前提交
# conn.commit()

# # 获取最新的那一条数据的ID，这里返回0。
# last = cur.lastrowid
# print(last)

cur.close()
conn.close()
