import pymysql

# 连接 --> 游标 -> 操作 --> 关闭游标 --> 关闭连接
conn = pymysql.connect(host='localhost', user='root', password='123456',
                       database='test', charset='utf8mb4')  # 特别注意该字符集，标准的 mysql 字符集
cur = conn.cursor()
count = cur.execute('select * from scores where score=4;')  # 返回：Number of affected rows
print(f'查询到 {count} 条记录！')

res = cur.fetchone()
print(res)

res = cur.fetchone()
print(res)

print(cur.fetchmany())
#
# # 游标是一直往下走的， fetchall 是取到剩余的条数。
print(cur.fetchall())
# 到 fetchmany 是一条都取不到了，最多取到 count 条
print(cur.fetchmany())

res = cur.fetchone()
print(res)


cur.close()
conn.close()
